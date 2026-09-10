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
  La tabla de referencia se titula **"N.N.N Referencia técnica"** y va al final de la sección
  (patrón fijado en D6: 3.2.1.6, 3.2.2.5, 3.2.5.4; también 5.4.4 y 5.8.3).
  Los **catálogos de campos completos** de los maestros van al **anexo A** (`source/17.0/annexes/`,
  una página `A_NN_slug.rst` por maestro, títulos «A.N Nombre», tabla Campo / Tipo / Qué es con la
  etiqueta de la interfaz en español). El cuerpo del cap. 4 sólo lleva la tabla corta
  «Decisión / Efecto» y enlaza al anexo (patrón fijado en D7).
  Excepción de numeración en el cap. 7: las páginas hijas 7.2.1 y 7.2.2 conservan sus ficheros
  `7_2_1_*`/`7_2_2_*`, y las secciones internas de 7.2 se numeran a partir de 7.2.3 (D9).
- En la Guía del integrador sí caben campos, cabeceras y ejemplos de código.

**Terminología**: manda el glosario, `source/17.0/glossary.rst` (tarea D3, 2026-09-08). Cada
término lleva su definición, los sinónimos que **no** se usan y el modelo Odoo. Resumen de las
decisiones que más se incumplen:

| Se dice | No se dice |
|---|---|
| Orden | Expedición, Pedido (salvo "pedido de venta" para el estado nativo de Odoo), Envío |
| Viaje | Ruta (salvo "tu ruta" en el manual del conductor), Trip |
| Manifiesto / Definición de fichero | Fichero EDI (son dos cosas distintas) |
| Bandeja de entrada API | API Inbox, Inbox, Bandeja de Entrada |
| Planning (sin traducir) | Planificación, cuando es la entidad `tms.planning` |
| Regla de tarifa (qué se mide) / Línea de tarifa (el precio) | "Reglas de tarifa" para las dos |
| Área geográfica / Zona de tarifa | Zona geográfica, Zona tarifaria |
| Cálculo de ruta / Secuenciación / Optimización completa | Routing (salvo como nombre del servicio de PTV en tablas), Sequence |
| Franja (del Plan de disponibilidad) / Botones inteligentes | Slot, Smart buttons, Botones mágicos |
| Completada, Con reservas, Fallida, Reprogramada, Devuelta, Cancelada | Hecho, Reservista, Fallo, OK, KO |
| Transportista, Conductor, Cliente, Remitente, Destinatario, Bulto | Carrier, Driver, Shipper, Cargador, Receiver, Paquete |

Al añadir un término nuevo, entra primero en el glosario. Donde la interfaz de Odoo o la app
discrepen del glosario, la corrección va a Odoo o a la app (lista en `PLAN.md`, apartado
"Correcciones en Odoo y en la app"), no a la doc.

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
python -m sphinx -b html -W -E -a source build/html  # lo mismo que CI y servidor: completo, no incremental
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
`6_resources`, `7_edi-integrations`, `8_economic-administration`, `10_manual_app` y el anexo `annexes/`. El cap. 10 es `:orphan:` a propósito: no cuelga del
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
  Única excepción, por decisión de Paco (2026-09-08): **1.4.6 Evolución prevista** recoge lo
  que está en desarrollo, etiquetado como tal. Nada futuro se cuela en el resto del texto.
- **Nada de notas de desarrollador** ("conviene revisar", "el onchange reconstruye…"). Si algo
  del código parece un bug, se anota en `CHANGELOG.md` o se le dice a Paco, no al lector.
- Prosa redactada, no apuntes: párrafos completos, nada de listas de una palabra.

### Capturas

- Ruta: `source/_static/img/<slug-capítulo>/<sección>_<slug>_<NN>_<slug-captura>.png`, en
  minúsculas, sin espacios ni acentos. En el `.rst`, ruta absoluta `/_static/img/...` dentro
  de un `.. figure::` con `:alt:` y pie.
- Cuando falta la imagen se deja el marcador `.. CAPTURA: <id>` con el `figure` comentado
  (indentado bajo el marcador) y una fila en `CAPTURAS_PENDIENTES.md`. El comando `/capturas`
  activa los figures cuya imagen ya existe. Un `figure` sin imagen rompe el build con `-W`, así
  que nunca se deja activo (decisión de Paco, 2026-09-10).
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

*Actualizado el 2026-09-10 (v3, D9). Si algo de aquí queda desactualizado, actualízalo en el
mismo cambio que lo desactualiza.*
