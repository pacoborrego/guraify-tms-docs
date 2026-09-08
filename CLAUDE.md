# Guraify TMS Docs — Contexto para Claude

Documentación de Guraify TMS (el TMS de Guraify / E-Transport sobre Odoo 17), construida
con **Sphinx** y publicada en **https://guraify.com/docs/**.

> **Autor**: Guraify — https://www.guraify.com · **Idioma** de la doc y de los commits:
> español. Interacción con Paco en español.
>
> **Estado (2026-09-08):** en fase de cierre. El plan de tareas, su estado y el diagnóstico
> del que sale están en **`PLAN.md`**. Léelo siempre después de este fichero.

---

## 1. Para quién es esta documentación

Tiene **cuatro públicos** y la portada los separa en cuatro recorridos (ver `PLAN.md`):

| Recorrido | Público | Qué espera |
|---|---|---|
| Conocer Guraify TMS | Cliente, distribuidor | Qué es, qué resuelve, para quién, sin tecnicismos |
| Manual de implantación | Consultor, cliente avanzado | Cómo funciona y cómo se configura |
| Guía del integrador | Técnico de integración | Cómo entran y salen datos |
| Manual del conductor | Conductor | Cómo usar la app, paso a paso |

**Política de nombres técnicos** (decisión 2026-09-08):

- En "Conocer Guraify TMS" y en el Manual del conductor: **ningún** modelo, campo ni método
  de Odoo.
- En el Manual de implantación: el modelo Odoo se cita entre paréntesis **sólo la primera vez**
  que aparece la entidad en cada página (p. ej. "la Parada (`tms.stop`)"). Campos, métodos y
  códigos internos **no van en la prosa**: van en el aviso "Ruta en Odoo", en una tabla de
  referencia o en un anexo.
- En la Guía del integrador sí caben campos, cabeceras y ejemplos de código.

**Terminología**: hay un glosario (tarea D3 del plan; hasta que exista, esta tabla manda):

| Se dice | No se dice | Modelo |
|---|---|---|
| Orden | Expedición, Pedido, Envío | `sale.order` |
| Tramo | Leg, Envío | `tms.shipment.leg` |
| Parada | Stop | `tms.stop` |
| Viaje | Ruta, Trip | `tms.trip` |
| Manifiesto | Fichero EDI | `tms.edi.manifest` |
| Bandeja de Entrada API | API Inbox | `tms_int.api.inbox` |
| Proyecto | — | `project.project` |
| Planning (sin traducir) | Planificación (cuando es la entidad) | `planning.*` |
| Tarifa | Pricelist | `tms.pricelist` |
| Regla de medida | Regla de tarifa (para lo que hoy es 4.2.3) | `tms.pricelist.rule` |
| Ítem de tarifa | Regla de tarifa (para lo que hoy es 4.4.3) | `tms.pricelist.item.zone` + `.detail` |

Los dos últimos son provisionales: D3 decide el nombre definitivo mirando cómo los llama la
UI en español.

"TMS" y "EDI" no se traducen.

---

## 2. El ecosistema

Esta documentación es una de las cuatro piezas del sistema:

| Carpeta | Rol | Stack |
|---|---|---|
| `/Users/paco/odoo17` | Backend Odoo con `custom_addons/tms_suite/` | Odoo 17, Python |
| `/Users/paco/tms-docs` | **Documentación** (estás aquí) | Sphinx + pydata-sphinx-theme |
| `/Users/paco/tms_odoo_app` | App móvil del conductor | Ionic Vue 3 + Capacitor |
| `/Users/paco/fastapi-odoo-gateway` | API Gateway externo ↔ Odoo | FastAPI |

Cada proyecto tiene su propio `CLAUDE.md`. El mapa de módulos y modelos de la suite está en
`/Users/paco/odoo17/custom_addons/tms_suite/CLAUDE.md`.

**Manda el código.** Todo nombre de modelo, campo, método, opción de selección o ruta de menú
que se cite debe existir en `tms_suite`. Las rutas de menú se sacan de `views/*_menu.xml` y se
traducen con `tms*/i18n/es.po`. Si una fuente antigua (Google Doc, Word) discrepa del
código, manda el código y se anota en `CHANGELOG.md`. Lección aprendida: los modelos de
integración son `tms_int.*` (guion bajo), no `tms.int.*`.

**Qué NO se documenta aquí**: los contratos de la API REST pública (payloads, ejemplos,
códigos de error) viven en el gateway (`/api/docs`). Aquí se explica la arquitectura de las
integraciones y se enlaza.

---

## 3. Herramienta

- **Sphinx 7.4.7**, tema `pydata-sphinx-theme 0.15.4`, `sphinx-design`, `sphinxcontrib-mermaid`,
  `sphinx-intl` (traducciones, aparcadas). Python del proyecto: `.venv/`.
- **Build limpio obligatorio**: el CI (`.github/workflows/build.yml`) y `deploy.sh` compilan
  con `-W`, así que **cualquier warning rompe la publicación**.

```bash
source .venv/bin/activate
make html && open build/html/index.html          # build local
python -m sphinx -b html -W source build/html     # lo mismo que CI y servidor
```

### Estructura

```
tms-docs/
├── source/
│   ├── conf.py            # idioma es, autosectionlabel con prefijo de documento
│   ├── index.rst          # raíz → 17.0/index
│   ├── 17.0/              # el contenido
│   │   ├── index.rst      # portada con tarjetas + toctrees
│   │   └── N_slug/        # un capítulo por carpeta, index.rst + N_M_slug.rst
│   ├── _static/
│   │   ├── custom.css     # marca Guraify (paleta, Mulish/Open Sans)
│   │   ├── img/<slug-capítulo>/   # capturas, una carpeta por capítulo
│   │   └── design/        # notas de diseño (no se referencian)
│   ├── _templates/        # layout.html (cabecera; aísla el manual del conductor)
│   └── locale/            # .po en/it, vacíos, aparcados
├── .claude/commands/      # /estado, /d3…/d13, /capturas, /publicar, /cerrar-tarea
├── .github/workflows/     # CI de build
├── deploy.sh              # publicación (se ejecuta en el servidor)
├── PLAN.md                # tareas y estado
├── CAPTURAS_PENDIENTES.md # lista de trabajo de María
├── CHANGELOG.md
└── versions.json          # aparcado (una sola versión)
```

Capítulos actuales en `source/17.0/`: `1_introduction`, `2_conceptual-model`,
`3_functional-architecture`, `4_parametrization`, `5_operational-flows`,
`7_edi-integrations`, `10_manual_app`. El cap. 10 es `:orphan:` a propósito: no cuelga del
toctree, se llega por la tarjeta de portada y `layout.html` le pone cabecera propia.

### Convenciones de RST

- Carpeta `N_slug-en-ingles/`, ficheros `N_M_slug.rst`; subsecciones anidadas `N_M_K_slug.rst`
  con sub-toctree en el padre. **Títulos numerados jerárquicamente** en todos los niveles
  (`3.2.1 Órdenes`, `3.2.1.1 Papel estructural`). Jerarquía de subrayados: `=`, `-`, `~`, `^`.
- Al inicio de cada sección con pantalla propia: `.. admonition:: Ruta en Odoo` con
  `:class: tip` y el breadcrumb en español (`TMS › Operaciones › Tráfico › Órdenes`).
- Tablas siempre `list-table` (las grid rompen el build con facilidad).
- Diagramas con `.. mermaid::`, validados contra el flujo real del código.
- Sin bloques de código fuera de la Guía del integrador, salvo campos generativos
  (`Parcel_Array`).
- **Nada de notas de versión** en el contenido (`versionadded`, "antes/ahora"). El texto
  describe el comportamiento actual; el historial vive en `CHANGELOG.md`.
- **Nada de notas de desarrollador** ("conviene revisar", "el onchange reconstruye…"). Si algo
  del código parece un bug, se anota en `CHANGELOG.md` o se le dice a Paco, no al lector.
- Prosa redactada, no apuntes: párrafos completos, nada de listas de una palabra.

### Capturas

- Ruta: `source/_static/img/<slug-capítulo>/<sección>_<slug>_<NN>_<slug-captura>.png`, en
  minúsculas, sin espacios ni acentos. En el `.rst`, ruta absoluta `/_static/img/...` dentro
  de un `.. figure::` con `:alt:` y pie.
- Cuando falta la imagen se deja el marcador `.. CAPTURA: <id>` con el `figure` comentado
  (indentado bajo el marcador) y una fila en `CAPTURAS_PENDIENTES.md`. El comando `/capturas`
  activa los figures cuya imagen ya existe.
- **Requisitos de una captura válida** (guía completa en `CAPTURAS_PENDIENTES.md`): recortada
  a la ventana de Odoo o a la zona relevante (sin barra del Mac, dock ni pestañas), Odoo en
  **español**, **sin datos reales** de clientes ni personas, ancho 1400–1600 px, PNG,
  idealmente < 400 KB.

---

## 4. Publicación

La web es estática. nginx en **epartner** sirve `/var/www/tms-docs` bajo `guraify.com/docs/`
(vhost `/etc/nginx/sites-enabled/guraify.com`). El repo está clonado en
`/opt/tms-docs/guraify-tms-docs`, propiedad de `pborrego`, que tiene Sphinx instalado en su
`~/.local`. **No hay servicio que reiniciar**: publicar es hacer pull, compilar y copiar.

```bash
ssh epartner "sudo -u pborrego -H /opt/tms-docs/guraify-tms-docs/deploy.sh"
```

Eso es lo que hace `/publicar`. Antes de publicar: build local limpio, `CHANGELOG.md` al día,
commit y push.

**Commits**: mensaje en español con la convención `AAMMDD_VNN` (`260908_V01`), y tag git
con el mismo nombre en cada publicación. Claude prepara el commit y lo enseña; **Paco lo
confirma**.

---

## 5. Fuera de alcance ahora

- **Versiones 18.0/19.0**: no se toca hasta que se implante la 19. `versions.json` y el
  selector quedan como están (oculto).
- **Traducciones**: después del contenido en español. Selector de idioma oculto.
- **Reescritura del historial git** (datos personales en capturas antiguas): es la última
  tarea del plan (D13), no antes.

---

*Actualizado el 2026-09-08 (v3). Si algo de aquí queda desactualizado, actualízalo en el
mismo cambio que lo desactualiza.*
