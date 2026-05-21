# Guraify TMS Docs — Contexto para Claude

Documentación técnica del TMS de Guraify / E-Transport, construida con **Sphinx**.

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

## Versionado

`versions.json` declara tres versiones (17.0, 18.0, 19.0) — actualmente las tres apuntan a `/docs/17.0/`. La doc real solo está hecha para 17.0 por ahora.

```json
[
  { "name": "17.0", "version": "17.0", "url": "/docs/17.0/" },
  { "name": "18.0", "version": "18.0", "url": "/docs/17.0/" },
  { "name": "19.0", "version": "19.0", "url": "/docs/17.0/" }
]
```

> Cuando se publique la versión 18 o 19, hay que ajustar las URLs y montar `source/18.0/` etc. Los apuntes "todos a 17.0" son temporales.

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
- Imágenes en `source/_static/img/` referenciadas con rutas relativas.
- Respetar la jerarquía de títulos RST (=, -, ~, ^).

## Qué se documenta aquí (vs. dónde más)

- **Aquí (`tms-docs`)**: arquitectura, modelos de negocio, flujos operativos, guía de usuario, configuración de Odoo, instalación.
- **En el gateway (`/api/docs`)**: contratos de API REST públicos (payloads, ejemplos, códigos de error). **No duplicar aquí**.
- **En el código Odoo**: docstrings y comentarios técnicos finos.

Cuando se añada/cambie funcionalidad en `tms_suite` que afecte al usuario o al integrador, **actualizar también esta doc** en el mismo cambio.

---

*Última actualización: 2026-05-19.*
