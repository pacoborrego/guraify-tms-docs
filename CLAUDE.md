# Guraify TMS Docs — Contexto para Claude

Documentación técnica del TMS de Guraify / E-Transport, construida con **Sphinx**.

> **Estado del proyecto (2026-06):** Sphinx es la **fuente de verdad única**. El Google Doc
> `2026_02_Manual Tecnico Guraify TMS_V01` queda como **archivo histórico de redacción**: su
> contenido se está migrando a `source/17.0/` capítulo a capítulo. Una vez migrado un capítulo,
> Sphinx manda; no se vuelve a editar en Drive. Ver "Migración Drive → Sphinx" más abajo.

---

## El ecosistema E-Transport / Guraify TMS

Esta documentación es **una de las cuatro piezas** del sistema. El proyecto completo vive en 4 carpetas hermanas:

| Carpeta | Rol | Stack |
|---|---|---|
| `/Users/paco/odoo17` | Backend Odoo con `custom_addons/tms_suite/` (5 módulos) | Odoo 17, Python |
| `/Users/paco/tms-docs` | **Documentación técnica** (estás aquí) | Sphinx + pydata-sphinx-theme |
| `/Users/paco/tms_odoo_app` | App móvil del conductor (Android + iOS) | Ionic Vue 3 + Capacitor 6 + Vite |
| `/Users/paco/fastapi-odoo-gateway` | API Gateway entre sistemas externos y Odoo | FastAPI + PostgreSQL propio |

Cada proyecto tiene su propio `CLAUDE.md` con detalles internos.

### El producto que documentamos: `tms_suite` (5 módulos Odoo 17)

| Módulo | Rol | Depende de |
|---|---|---|
| `tms` | Núcleo (~100 modelos): órdenes, tramos, paradas, viajes, planificación, tarificación, trazabilidad, EDI, optimización PTV/OSM | account, sale, crm, fleet, stock, mrp, project, planning, purchase, helpdesk, delivery |
| `tms_app` | Backend de la app móvil del conductor (perfiles, roles, tokens, POD, incidencias) | `tms` |
| `tms_int` | Integraciones / EDI (endpoints API, inbox, import de pedidos, mapeo, presets) | `tms` |
| `tms_map` | Vista de mapa de registros geográficos | `tms`, `web` |
| `tms_portal` | Acceso portal a los inboxes de integración | `portal`, `website`, `tms`, `tms_int` |

### Entidades clave del modelo (nombre de negocio → modelo Odoo)

- **Orden / Expedición** → `sale.order`
- **Tramo** → `tms.shipment.leg`
- **Parada** → `tms.stop`
- **Viaje / Ruta** → `tms.trip`

Separan, respectivamente: la venta al cliente · la estructura logística · la planificación · la liquidación al transportista.

---

## Stack

- **Sphinx 7.4.7** con tema `pydata-sphinx-theme 0.15.4`.
- **i18n**: `sphinx-intl 2.1.0` para traducciones (carpeta `source/locale/`).
- **Diagramas**: `sphinxcontrib-mermaid`.
- **UI components**: `sphinx-design`.
- **Python 3.x** + `venv` (existen dos: `.venv/` y `venv/`).

## Estructura

```
tms-docs/
├── source/
│   ├── conf.py            # Configuración Sphinx
│   ├── index.rst          # Página raíz
│   ├── 17.0/              # Documentación versión 17 (la actual)
│   ├── _static/           # Recursos estáticos (CSS, imágenes)
│   ├── _templates/        # Overrides de plantillas del tema
│   └── locale/            # Traducciones (sphinx-intl)
├── build/                 # Salida (no commitear html generado)
├── manual.rst             # Manual largo en RST (105 KB) en raíz
├── versions.json          # Definición de versiones para el selector
├── Makefile               # `make html`, `make gettext`, etc.
├── requirements.txt
└── README.md
```

### Mapa de capítulos en `source/17.0/`

```
1_introduction/          2_conceptual-model/      3_functional-architecture/
4_parametrization/       5_operational-flows/     10_manual_app/
```

Cada carpeta es `N_slug-en-ingles/` y contiene un `index.rst` con su `.. toctree::` más
archivos `N_M_slug.rst`. Respetar SIEMPRE esa convención de nombres y numeración.

---

## Migración Drive → Sphinx (trabajo principal en curso)

El Google Doc tiene capítulos que aún **no existen** en Sphinx. Estado:

| Cap. (Doc) | Título | En Sphinx | Acción |
|---|---|---|---|
| 1 | Introducción | ✅ | mantener |
| 2 | Modelo Conceptual | ✅ | mantener |
| 3 | Arquitectura Funcional | ✅ | hecho (revisado + 3.2 ampliado: 3.2.1–3.2.4 desde código) |
| 4 | Parametrización | ✅ | mantener |
| 5 | Flujo Operativo End-to-End | ✅ | mantener |
| 6 | Aplicación Móvil (técnica) | ❌ | **portar (PRIORIDAD 1)** → `6_mobile-app/` |
| 7 | EDI e Integraciones | ✅ | hecho (estándar v2; faltan capturas de María) |
| 8 | Administración y Control Económico | ❌ | **portar** → `8_administration/` |
| 10 | Manual App Conductor | ✅ | mantener (`10_manual_app/`) |

**Procedimiento para portar un capítulo (estándar v2, consolidado en el cap. 7):**

*Fase 1 — Esqueleto (enseñar al propietario antes de rellenar):*

1. Leer la fuente de redacción: la sección del Google Doc si existe. Si está vacía (como
   el cap. 7, que solo traía títulos), **redactar desde el código** de `tms_suite`.
2. Crear `source/17.0/N_slug/` con su `index.rst`: intro + `.. toctree::` + nota de
   frontera con el *gateway* (`.. admonition:: ... :class: important`) cuando el capítulo
   roce la API REST pública.
3. Un `.rst` por subsección (`N_M_slug.rst`). Si una subsección tiene partes propias,
   anidarlas como `N_M_K_slug.rst` con su **sub-`toctree`** en el `.rst` padre (patrón
   7.2 → 7.2.1 / 7.2.2).
4. Añadir el capítulo al `.. toctree::` de `source/17.0/index.rst`.
5. Mostrar el esqueleto al propietario (carpeta + index + toctree) antes de redactar la
   prosa, y confirmar decisiones de estilo (profundidad, diagramas, etc.).

*Fase 2 — Contenido:*

6. **Estilo**: prosa descriptiva técnico-funcional para consultor/integrador. **Sin
   bloques de código**, salvo cuando el contenido sea inherentemente generativo (p. ej.
   el campo computado `Parcel_Array`), donde un ejemplo breve en `.. code-block:: python`
   está justificado.
7. Citar el modelo Odoo entre paréntesis la primera vez (p. ej. "la Parada (`tms.stop`)").
8. **Catálogos desde el código**: campos, opciones de selección, funciones, etc. se
   extraen del código (no se inventan) y se presentan con `list-table` agrupadas por
   entidad (patrón de la tabla de campos destino en 7.2.1).
9. **Diagramas** de flujo con `.. mermaid::`, validados contra el flujo real del código.
   Si se necesita un diagrama compartible (p. ej. Lucid en Drive), exportarlo aparte y
   mantener el `.. mermaid::` como fuente en la doc.

*Fase 3 — UI y capturas (para el lector funcional):*

10. **Ruta de UI**: al inicio de cada sección, un aviso
    `.. admonition:: Ruta en Odoo` con `:class: tip` y el breadcrumb **en español**,
    tomado de los menús reales del módulo (`views/*_menu.xml`) y traducido con los
    ficheros `tms*/i18n/es.po`. "TMS" y "EDI" se quedan sin traducir.
11. **Capturas**: en cada punto que lo requiera, un marcador `.. CAPTURA: <id>` con un
    `.. figure::` **comentado** (indentado bajo el marcador, para que no rompa el build)
    apuntando a `source/_static/img/<slug-capítulo>/<sección>_<slug>_<NN>_<slug>.png`.
    Cada captura se registra en `CAPTURAS_PENDIENTES.md` (responsable de captura: María),
    que se descomenta al añadir la imagen.

*Fase 4 — Cierre:*

12. `make html` **sin warnings nuevos** (referencia: 13 warnings preexistentes). En el
    sandbox el `venv` del repo no sirve (es de macOS): instalar `requirements.txt` con
    pip y compilar con `python3 -m sphinx -b html source build/html`.
13. Marcar las subsecciones migradas en `MIGRACION.md`.
14. Registrar el cambio en `CHANGELOG.md` (sección "Sin publicar").

**Verificación obligatoria al portar:** todo nombre de modelo, campo, método, opción de
selección o **ruta de menú** citado debe existir realmente en `tms_suite`. Si el Doc y el
código discrepan, **manda el código** y se anota la discrepancia en `CHANGELOG.md` /
`MIGRACION.md`. *Lección del cap. 7:* los modelos de integración usan prefijo `tms_int.*`
(guion bajo), no `tms.int.*`; los dotted reales son `tms.edi.*`, `tms.api.log`,
`tms.agency.transfer.snapshot`.

**Definición de Hecho de un capítulo/subsección:**

- [ ] Esqueleto en su carpeta `N_slug/` y en el `toctree` de `17.0/index.rst`.
- [ ] Prosa descriptiva con modelos citados y verificados contra el código.
- [ ] Catálogos (campos/opciones) en `list-table` extraídos del código.
- [ ] Diagrama `.. mermaid::` del flujo cuando aporte.
- [ ] Aviso `Ruta en Odoo` (español) en cada sección.
- [ ] Marcadores `.. CAPTURA:` + figure comentado y filas en `CAPTURAS_PENDIENTES.md`.
- [ ] `make html` sin warnings nuevos.
- [ ] `MIGRACION.md` y `CHANGELOG.md` actualizados; discrepancias anotadas.

---

## Versionado y releases

`versions.json` declara tres versiones (17.0, 18.0, 19.0) — actualmente las tres apuntan a
`/docs/17.0/`. La doc real solo está hecha para 17.0.

```json
[
  { "name": "17.0", "version": "17.0", "url": "/docs/17.0/" },
  { "name": "18.0", "version": "18.0", "url": "/docs/17.0/" },
  { "name": "19.0", "version": "19.0", "url": "/docs/17.0/" }
]
```

**Proceso de release (definitivo — Opción A "Completo"):**

1. Cerrar los cambios y dejar `make html` sin warnings nuevos.
2. Anotar lo publicado en `CHANGELOG.md`: mover lo de "Sin publicar" a una sección con el
   número de versión y la fecha (capítulo afectado + resumen).
3. Commit en español y etiquetar con tag git `AAMMDD_VNN` (p. ej. `260603_V01`). Incrementar
   `VNN` si hay varias publicaciones el mismo día. *(Nota: los `AAMMDD_VNN` del historial eran
   mensajes de commit, no tags; a partir de ahora se crean como tags reales: `git tag AAMMDD_VNN`.)*
4. Cuando se publique 18.0/19.0: montar `source/18.0/` y ajustar las URLs de `versions.json`
   (hoy las tres versiones apuntan a `/docs/17.0/`).

Cuando se añada/cambie funcionalidad en `tms_suite` que afecte al usuario o al integrador,
**actualizar también esta doc** en el mismo cambio y reflejarlo en el `CHANGELOG.md`.

## Comandos habituales

```bash
# Activar entorno
source .venv/bin/activate   # o: source venv/bin/activate

# Build HTML
make html
open build/html/index.html

# Extraer cadenas traducibles
make gettext
sphinx-intl update -p build/gettext -l es -l en
```

## Convenciones

- **Idioma principal**: español. Algunas secciones en inglés según el público destino.
- Comentarios y commit messages: español.
- **No** committear `build/`, `.venv/`, `venv/`, `__pycache__/`.
- Usar `.. mermaid::` para diagramas, `.. grid::` (de sphinx-design) para layouts con tarjetas.
- Imágenes en `source/_static/img/<slug-capítulo>/` (una carpeta por capítulo, p. ej.
  `7_edi-integrations/`). En el `.rst` se referencian con ruta absoluta desde `source/`:
  `/_static/img/<slug-capítulo>/...`. Nombre de fichero:
  `<sección>_<slug>_<NN>_<slug-captura>.png` (minúsculas, sin espacios ni acentos).
- Las capturas pendientes se gestionan en `CAPTURAS_PENDIENTES.md` (ver Fase 3 del
  procedimiento de portado). Responsable de captura: María.
- Ruta de UI al inicio de cada sección con `.. admonition:: Ruta en Odoo` (`:class: tip`),
  breadcrumb en español tomado de los menús reales y los `.po` (`tms*/i18n/es.po`).
- Respetar la jerarquía de títulos RST (=, -, ~, ^); subsecciones anidadas `N_M_K`.
- **Numerar todos los títulos de forma jerárquica**, incluidos los subtítulos internos
  (p. ej. 3.1.1 Operaciones, 3.1.1.1 Tráfico, 3.2.2.3 Estados…). Decisión del propietario
  (2026-06-04). *Pendiente:* alinear el cap. 7, cuyos subtítulos internos aún no llevan
  número.
- Tono del manual técnico: descriptivo, orientado a consultor/integrador, sin instrucciones de
  usuario final (eso vive en el Manual App Conductor, cap. 10). Sin bloques de código salvo
  campos generativos (p. ej. `Parcel_Array`).

## Qué se documenta aquí (vs. dónde más)

- **Aquí (`tms-docs`)**: arquitectura, modelos de negocio, flujos operativos, guía de usuario, configuración de Odoo, instalación.
- **En el gateway (`/api/docs`)**: contratos de API REST públicos (payloads, ejemplos, códigos de error). **No duplicar aquí**.
- **En el código Odoo**: docstrings y comentarios técnicos finos.

Cuando se añada/cambie funcionalidad en `tms_suite` que afecte al usuario o al integrador,
**actualizar también esta doc** en el mismo cambio.

---

*Última actualización: 2026-06-04. Estándar de portado v2 consolidado a partir del cap. 7
(rutas de UI en español, capturas delegadas, catálogos desde el código, Definición de Hecho).*
