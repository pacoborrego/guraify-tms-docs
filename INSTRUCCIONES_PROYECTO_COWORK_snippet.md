# Snippet para las instrucciones del proyecto Cowork

Texto listo para pegar/integrar en las instrucciones del proyecto "Documentación Guraify
TMS" (Cowork). Resume el estándar v2; el detalle operativo vive en
`/Users/paco/tms-docs/CLAUDE.md`.

---

**Estándar de redacción de capítulos (v2).** Al portar o revisar un capítulo de la doc
Sphinx (`/Users/paco/tms-docs`):

- **Fuente de verdad: el código.** Todo modelo, campo, método, opción de selección o ruta
  de menú citado debe existir en `custom_addons/tms_suite/`. Si el Google Doc y el código
  discrepan, manda el código y se anota la discrepancia. (Recordatorio: los modelos de
  integración son `tms_int.*`, no `tms.int.*`.)
- **Estructura:** carpeta `source/17.0/N_slug/` con `index.rst` (intro + toctree, y nota de
  frontera con el gateway si toca la API REST). Subsecciones `N_M_slug.rst`; si tienen
  partes, anidarlas como `N_M_K_slug.rst` con sub-toctree. Enseñar el esqueleto antes de
  redactar la prosa.
- **Estilo:** prosa descriptiva técnico-funcional (consultor/integrador), en español. Sin
  bloques de código salvo campos generativos (p. ej. `Parcel_Array`). Catálogos de
  campos/opciones extraídos del código en `list-table`. Diagramas de flujo con `.. mermaid::`.
- **Ruta de UI:** al inicio de cada sección, un aviso `.. admonition:: Ruta en Odoo`
  (`:class: tip`) con el breadcrumb en español, tomado de los menús reales y los `.po`
  (`tms*/i18n/es.po`). "TMS" y "EDI" no se traducen.
- **Capturas:** marcador `.. CAPTURA: <id>` + `.. figure::` comentado en cada punto que lo
  requiera; imágenes en `source/_static/img/<slug-capítulo>/`; cada captura registrada en
  `CAPTURAS_PENDIENTES.md` (responsable de captura: María).
- **Cierre:** `make html` sin warnings nuevos, y actualizar `MIGRACION.md` y `CHANGELOG.md`.
  Ver la *Definición de Hecho* en `CLAUDE.md`.

**Prioridad de trabajo:** terminar los capítulos que faltan (6 App Móvil → 8 Admin
económico → 3.2 ampliado) aplicando este estándar, y después revisar los capítulos 1–5 y
10 con el checklist de `REVISION_ESTANDAR.md` (empezando por los warnings históricos de
los caps. 4 y 5).
