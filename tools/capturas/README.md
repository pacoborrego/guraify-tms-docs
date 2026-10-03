# Capturas automáticas de Odoo

Script de Playwright que abre cada pantalla de la lista de capturas y guarda el PNG con el nombre
exacto que espera la documentación. Sustituye el trabajo manual de navegar y recortar; la
anonimización sigue siendo un paso aparte, porque las capturas salen de producción.

## Flujo

1. **Sesión** (una vez por instancia): `python tools/capturas/capturas.py --instance etransport --login`
   abre un Chrome; inicias sesión con un usuario que tenga la interfaz **en inglés**; al ver el
   menú de Odoo la sesión se guarda en `tools/capturas/.auth/` (no se sube al repo).
2. **Capturar**: `python tools/capturas/capturas.py --instance etransport` recorre las pendientes
   de esa instancia y deja los PNG en `tools/capturas/raw/<carpeta>/` (no se sube: llevan datos
   reales). `--only 5_3_01 7_5_01` para unas concretas, `--chapter 4_` para un capítulo,
   `--headed` para ver el navegador, `--include-deferred` para las antiguas aplazadas.
   Al final imprime cuáles han fallado y por qué, y lo anota en `raw/INDEX.md`.
3. **Revisar** `raw/`: las entradas marcadas «⚠ revisar a mano» en `--list` tienen pasos frágiles
   (menús desplegados, desplegables, filtros). Si una no muestra lo que debe, se ajusta su entrada
   en `manifest.json` (dominio, pasos) y se repite solo esa.
4. **Anonimizar**: María pasa las de `raw/` por el agente de anonimización y deja el resultado, con
   el mismo nombre, en `source/_static/img/<carpeta>/`.
5. **Activar**: `/capturas` en Claude Code activa las figuras cuya imagen ya existe, comprueba
   nombre, tamaño y peso, y actualiza `CAPTURAS_PENDIENTES.md`.

## Ficheros

- `manifest.json`: una entrada por captura. `action` es el xmlid de la acción de ventana;
  `model` + `view` + `domain` eligen el registro (en `form`, el primero que cumpla el dominio,
  por id descendente; `record` fija un id concreto); `steps` son clics guionizados (`tab`,
  `button`, `smart`, `click`, `hover`, `scroll`, `fill`, `wait`); `clip: modal` recorta el
  diálogo; `map: true` espera a las teselas; `deferred: true` marca las antiguas aplazadas;
  `manual` avisa de que hay que revisar el resultado.
- `instances.json` (copiar de `instances.example.json`, no se sube): dirección de cada Odoo.
  `etransport` es la producción de e-transport (caps. 3, 4, 5, 7 y 8); `ludamany` es donde están
  `tms_resources` y `tms_maintenance` (cap. 6): la copia local `ludamany_260904` en
  `http://localhost:8017` con Odoo arrancado, o la producción de Ludamany.
- Tamaño: ventana de 1600 × 1000 px, que es lo que pide la guía; las capturas son de la ventana
  de Odoo, sin navegador ni barra de tareas.

## Instalación

```bash
source .venv/bin/activate
pip install playwright
python -m playwright install chromium   # opcional: el script usa el Chrome del equipo y solo recurre a este si aquel no arranca
cp tools/capturas/instances.example.json tools/capturas/instances.json   # y poner las direcciones
```

Las consultas a Odoo (resolver acciones, buscar el registro) las hace el propio Chrome desde la
página, con la sesión guardada: el motor de Playwright no necesita salir a la red.

## Si se queda parado al abrir el navegador

El script espera 60 s a que arranque el Chrome del equipo y, si no, pasa al Chromium de Playwright.
Si Chrome se está actualizando (aviso «Reinicia para actualizar»), termina la actualización o cierra
Chrome del todo antes de lanzar el script. Con `--bundled` se usa directamente el de Playwright.

## Lo que no hace

- Las 6 capturas de la app del conductor (cap. 10): se hacen en el teléfono con una ruta de
  prueba.
- El PDF de la orden de trabajo impresa (6.6): se imprime desde la ficha del vehículo y se captura
  el visor de PDF a mano.
- Anonimizar: las capturas de `raw/` no se publican tal cual.
