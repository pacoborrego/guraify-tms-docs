#!/usr/bin/env python3
"""Capturas de pantalla de Odoo para la documentación, con Playwright.

Lee `manifest.json` (una entrada por captura: pantalla, vista, registro, pasos) y genera los PNG en
`raw/<carpeta>/<fichero>.png` al tamaño de la guía (1600 px de ancho), recortados a la ventana de
Odoo. Las capturas salen con datos reales: `raw/` no se sube al repo. María las anonimiza y deja
el resultado en `source/_static/img/<carpeta>/`; después `/capturas` las activa en el texto.

Uso (desde la raíz del repo, con el venv activado):

    python tools/capturas/capturas.py --instance etransport --login       # una vez: abre Chrome, tú inicias sesión
    python tools/capturas/capturas.py --instance etransport               # todas las pendientes de esa instancia
    python tools/capturas/capturas.py --instance etransport --only 5_3_01 7_5_01
    python tools/capturas/capturas.py --list                              # qué hay en el manifiesto
    python tools/capturas/capturas.py --instance ludamany --include-deferred   # también las antiguas 🔁

Las instancias y sus direcciones están en `instances.json` (no se sube: lleva direcciones internas).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
import pathlib

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest.json"
INSTANCES = HERE / "instances.json"
AUTH_DIR = HERE / ".auth"
RAW_DIR = HERE / "raw"

WIDTH, HEIGHT = 1600, 1000
IDLE_MS = 1200          # espera tras cargar, para que Odoo termine de pintar
MAP_MS = 5000           # las pantallas con mapa tardan en traer las teselas


# --------------------------------------------------------------------------- utilidades

def load_json(path: Path, what: str):
    if not path.exists():
        sys.exit(f"Falta {path.name} ({what}).")
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def entries(manifest, only, instance, chapter, include_deferred):
    for e in manifest["capturas"]:
        if only and e["id"] not in only:
            continue
        if instance and e.get("instance", manifest.get("default_instance")) != instance:
            continue
        if chapter and not e["file"].startswith(chapter):
            continue
        if e.get("deferred") and not include_deferred and not only:
            continue
        yield e

FIND_JS = r"""(spec) => {
  // Busca un elemento sin depender del motor de selectores de Playwright.
  // Admite: 'css', 'css:has-text(\'txt\')', 'text=txt' (o text=/regex/i) y el sufijo ' >> nth=N'.
  const norm = s => (s || '').replace(/\s+/g, ' ').trim().toLowerCase();
  let sel = spec, nth = 0;
  const m = sel.match(/^(.*?)\s*>>\s*nth=(\d+)$/); if (m) { sel = m[1]; nth = parseInt(m[2]); }
  let els = [];
  if (sel.startsWith('text=')) {
    let pat = sel.slice(5), re = null;
    const rm = pat.match(/^\/(.*)\/([a-z]*)$/); if (rm) re = new RegExp(rm[1], rm[2]);
    const all = Array.from(document.querySelectorAll('body *')).filter(e => e.offsetParent !== null || e.tagName === 'A');
    els = all.filter(e => { const tx = e.innerText || e.textContent || ''; return re ? re.test(tx) : norm(tx).includes(norm(pat)); });
    els.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);   // el más pequeño que contiene el texto
  } else {
    const hm = sel.match(/^(.*?):has-text\(['"](.*)['"]\)(.*)$/);
    if (hm) {
      els = Array.from(document.querySelectorAll(hm[1] + (hm[3] || ''))).filter(e => norm(e.innerText || e.textContent).includes(norm(hm[2])));
    } else {
      els = Array.from(document.querySelectorAll(sel));
    }
  }
  return els.length > nth ? els[nth] : null;
}"""


def js_find(page, spec):
    return page.evaluate_handle(FIND_JS, spec).as_element()


def wait_present(page, spec, timeout_ms=30000):
    deadline = time.time() + timeout_ms / 1000
    while time.time() < deadline:
        try:
            if js_find(page, spec):
                return True
        except Exception:
            pass
        page.wait_for_timeout(300)
    raise RuntimeError(f"no aparece {spec} en {page.url}")


def js_click(page, spec, timeout_ms=15000):
    wait_present(page, spec, timeout_ms)
    el = js_find(page, spec)
    el.evaluate("e => { e.scrollIntoView({block: 'center'}); e.focus && e.focus(); e.click(); }")


def js_fill(page, spec, value):
    wait_present(page, spec)
    el = js_find(page, spec)
    el.evaluate("(e, v) => { e.focus(); e.value = v; e.dispatchEvent(new Event('input', {bubbles: true})); e.dispatchEvent(new Event('change', {bubbles: true})); }", value)


class Odoo:
    """Llamadas JSON-RPC con la sesión del navegador (para resolver acciones y buscar registros)."""

    def __init__(self, page, base_url):
        self.page = page
        self.base = base_url.rstrip("/")

    def call(self, model, method, args, kwargs=None):
        """La petición la hace el propio Chrome desde la página de Odoo (misma sesión, mismas cookies).
        Así no depende de la red de Node, que en algunos equipos está bloqueada."""
        payload = {"jsonrpc": "2.0", "method": "call",
                   "params": {"model": model, "method": method, "args": args, "kwargs": kwargs or {}}}
        if not self.page.url.startswith(self.base):
            self.page.goto(f"{self.base}/web")
            wait_present(self.page, ".o_main_navbar")
        body = self.page.evaluate(
            """async (p) => {
                 const r = await fetch('/web/dataset/call_kw/' + p.model + '/' + p.method, {
                   method: 'POST', credentials: 'same-origin',
                   headers: {'Content-Type': 'application/json'}, body: JSON.stringify(p.payload)});
                 return await r.json();
               }""",
            {"model": model, "method": method, "payload": payload})
        if "error" in body:
            raise RuntimeError(body["error"].get("data", {}).get("message") or body["error"].get("message"))
        return body["result"]

    def action_id(self, xmlid):
        module, name = xmlid.split(".", 1)
        rows = self.call("ir.model.data", "search_read",
                         [[["module", "=", module], ["name", "=", name]]],
                         {"fields": ["res_id", "model"], "limit": 1})
        if not rows:
            raise RuntimeError(f"la acción {xmlid} no existe en esta instancia")
        return rows[0]["res_id"]

    def first_id(self, model, domain, order):
        rows = self.call(model, "search_read", [domain or []],
                         {"fields": ["id"], "limit": 1, "order": order or "id desc"})
        if not rows:
            raise RuntimeError(f"ningún registro de {model} cumple {domain}")
        return rows[0]["id"]


def build_url(odoo, base, e):
    """Compone la URL de Odoo 17 (/web#...) para la entrada."""
    parts = []
    if e.get("action"):
        parts.append(f"action={odoo.action_id(e['action'])}")
    if e.get("model"):
        parts.append(f"model={e['model']}")
    view = e.get("view", "list")
    if view == "form" and e.get("record", "first") not in (0, None):
        rec = e.get("record", "first")
        rec_id = rec if isinstance(rec, int) else odoo.first_id(e["model"], e.get("domain"), e.get("order"))
        parts.append(f"id={rec_id}")
    parts.append(f"view_type={view}")
    if e.get("menu"):
        parts.append(f"menu_id={odoo.action_id(e['menu'])}")
    return f"{base}/web#" + "&".join(parts)


def run_steps(page, steps, log):
    for step in steps or []:
        kind, arg = next(iter(step.items()))
        log(f"    paso {kind}: {arg}")
        if kind == "click":
            js_click(page, arg)
        elif kind == "tab":
            js_click(page, f".o_notebook .nav-link:has-text('{arg}')")
        elif kind == "button":
            js_click(page, f"button:has-text('{arg}')")
        elif kind == "smart":
            js_click(page, f".o_stat_button:has-text('{arg}')")
        elif kind == "hover":
            js_find(page, arg).hover()
        elif kind == "scroll":
            wait_present(page, arg)
            js_find(page, arg).evaluate("e => e.scrollIntoView({block: 'center'})")
        elif kind == "fill":
            sel, value = arg
            js_fill(page, sel, value)
        elif kind == "key":
            page.keyboard.press(arg)
        elif kind == "wait":
            page.wait_for_timeout(int(arg))
        elif kind == "goto":
            page.goto(arg)
        else:
            raise RuntimeError(f"paso desconocido: {kind}")
        page.wait_for_timeout(700)


def capture(page, e, out_path, log):
    wait_present(page, ".o_action_manager, .o_web_client")
    try:
        page.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        pass
    page.wait_for_timeout(MAP_MS if e.get("map") else IDLE_MS)
    run_steps(page, e.get("steps"), log)
    if e.get("clip") == "modal":
        wait_present(page, ".modal-dialog", 15000)
        page.wait_for_timeout(700)
        box = page.evaluate("""() => { const m = Array.from(document.querySelectorAll('.modal-dialog')).pop();
                                       const r = m.getBoundingClientRect(); return {x: r.x, y: r.y, width: r.width, height: r.height}; }""")
        shot(page, out_path, clip=box)
    else:
        shot(page, out_path)


def shot(page, out_path, clip=None):
    """Captura con Playwright y, si se queda esperando (mapas WebGL, hojas de cálculo), por CDP."""
    import base64
    try:
        page.screenshot(path=str(out_path), full_page=False, clip=clip, timeout=45000, animations="disabled")
        return
    except Exception as exc:
        print(f"    (captura normal agotada: {str(exc).splitlines()[0][:60]}; uso CDP)")
    cdp = page.context.new_cdp_session(page)
    params = {"format": "png", "captureBeyondViewport": False}
    if clip:
        params["clip"] = {"x": clip["x"], "y": clip["y"], "width": clip["width"], "height": clip["height"], "scale": 1}
    data = cdp.send("Page.captureScreenshot", params)["data"]
    pathlib.Path(out_path).write_bytes(base64.b64decode(data))
    cdp.detach()


# --------------------------------------------------------------------------- comandos

def launch(pw, headless, bundled):
    """Abre el navegador. Primero el Chrome instalado en el equipo (no hay que descargar nada); si no
    arranca en 30 s (por ejemplo, Chrome actualizándose), prueba con el Chromium de Playwright.
    --bundled va directo al de Playwright."""
    args = ["--no-first-run", "--no-default-browser-check"]
    if not bundled:
        print("Abriendo el Chrome del equipo…", flush=True)
        try:
            return pw.chromium.launch(headless=headless, channel="chrome", args=args, timeout=60000)
        except Exception as exc:
            print(f"  no ha arrancado ({str(exc).splitlines()[0][:90]}); pruebo con el Chromium de Playwright.", flush=True)
    try:
        return pw.chromium.launch(headless=headless, args=args, timeout=30000)
    except Exception as exc:
        sys.exit("No hay navegador con el que capturar. Instala el de Playwright con\n"
                 "    python -m playwright install chromium\n"
                 "o cierra Chrome del todo (si se está actualizando, termina primero) y repite.\n"
                 f"Detalle: {str(exc).splitlines()[0][:120]}")


def do_login(instance_name, base, bundled=False):
    from playwright.sync_api import sync_playwright
    AUTH_DIR.mkdir(exist_ok=True)
    state = AUTH_DIR / f"{instance_name}.json"
    with sync_playwright() as pw:
        browser = launch(pw, False, bundled)
        ctx = browser.new_context(viewport={"width": WIDTH, "height": HEIGHT})
        page = ctx.new_page()
        print("Navegador abierto.", flush=True)
        page.goto(f"{base}/web/login")
        print("Inicia sesión en la ventana de Chrome (usuario con la interfaz en inglés).")
        print("Cuando veas el menú de Odoo, la sesión se guarda sola. Tienes 10 minutos.")
        wait_present(page, ".o_main_navbar", 600000)
        page.wait_for_timeout(1500)
        ctx.storage_state(path=str(state))
        browser.close()
    print(f"Sesión guardada en {state.relative_to(HERE.parent.parent)} (no se sube al repo).")


def do_run(args, manifest, instances):
    from playwright.sync_api import sync_playwright
    inst = instances.get(args.instance)
    if not inst:
        sys.exit(f"Instancia desconocida: {args.instance}. Hay: {', '.join(instances)}")
    base = inst["url"].rstrip("/")
    state = AUTH_DIR / f"{args.instance}.json"
    if not state.exists():
        sys.exit(f"No hay sesión guardada para {args.instance}: ejecuta primero --login.")
    todo = list(entries(manifest, args.only, args.instance, args.chapter, args.include_deferred))
    if not todo:
        sys.exit("Nada que capturar con esos filtros.")
    results = []
    with sync_playwright() as pw:
        browser = launch(pw, not args.headed, args.bundled)
        ctx = browser.new_context(storage_state=str(state), viewport={"width": WIDTH, "height": HEIGHT},
                                  device_scale_factor=1, locale="en-GB")
        page = ctx.new_page()
        page.goto(f"{base}/web")
        if "/web/login" in page.url:
            browser.close()
            sys.exit("La sesión guardada ha caducado: repite --login.")
        wait_present(page, ".o_main_navbar")
        print("Sesión de Odoo válida.", flush=True)
        odoo = Odoo(page, base)
        for e in todo:
            out = RAW_DIR / e["folder"] / e["file"]
            out.parent.mkdir(parents=True, exist_ok=True)
            print(f"[{e['id']}] {e['file']}")
            try:
                url = build_url(odoo, base, e)
                print(f"    {url}")
                page.goto(url)
                capture(page, e, out, lambda m: print(m))
                results.append((e["id"], "ok", str(out.relative_to(HERE))))
                print(f"    -> {out.relative_to(HERE)}")
            except Exception as exc:  # una captura que falla no para las demás
                results.append((e["id"], "ERROR", str(exc).splitlines()[0][:160]))
                print(f"    ERROR: {str(exc).splitlines()[0][:160]}")
            if page.evaluate("() => !!document.querySelector('.modal-dialog')"):
                page.keyboard.press("Escape")
                page.wait_for_timeout(400)
        browser.close()
    index = RAW_DIR / "INDEX.md"
    with index.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {time.strftime('%Y-%m-%d %H:%M')} · {args.instance}\n\n")
        for cid, st, info in results:
            fh.write(f"- {cid} · {st} · {info}\n")
    ok = sum(1 for r in results if r[1] == "ok")
    print(f"\n{ok}/{len(results)} capturas. Resumen añadido a {index.relative_to(HERE.parent.parent)}.")
    for cid, st, info in results:
        if st != "ok":
            print(f"  {cid}: {info}")


def do_list(manifest, args):
    for e in entries(manifest, args.only, args.instance, args.chapter, True):
        flag = " (aplazada)" if e.get("deferred") else ""
        manual = "  ⚠ revisar a mano: " + e["manual"] if e.get("manual") else ""
        print(f"{e['id']:10s} {e.get('instance', manifest.get('default_instance')):10s} {e['file']}{flag}{manual}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--instance", help="nombre de la instancia en instances.json")
    ap.add_argument("--login", action="store_true", help="abre Chrome para iniciar sesión y guarda la sesión")
    ap.add_argument("--only", nargs="*", help="ids de captura (p. ej. 5_3_01)")
    ap.add_argument("--chapter", help="prefijo de fichero (p. ej. 6_ o 4_3)")
    ap.add_argument("--include-deferred", action="store_true", help="incluye las antiguas aplazadas")
    ap.add_argument("--headed", action="store_true", help="con ventana visible, para ver qué pasa")
    ap.add_argument("--list", action="store_true", help="lista el manifiesto y sale")
    ap.add_argument("--bundled", action="store_true", help="usa el Chromium de Playwright en vez del Chrome instalado")
    args = ap.parse_args()

    manifest = load_json(MANIFEST, "el manifiesto de capturas")
    if args.list:
        do_list(manifest, args)
        return
    instances = load_json(INSTANCES, "las direcciones de las instancias; copia instances.example.json")
    if not args.instance:
        sys.exit("Indica --instance (" + ", ".join(instances) + ").")
    if args.login:
        do_login(args.instance, instances[args.instance]["url"], args.bundled)
        return
    do_run(args, manifest, instances)


if __name__ == "__main__":
    main()
