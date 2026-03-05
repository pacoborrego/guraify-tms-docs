# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'TMS GURAIFY'
copyright = '2026, Guraify'
author = 'Guraify'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.mermaid",
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'
locale_dirs = ["locale"]
gettext_compact = False
autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    # Header
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["search-field.html"],
    "navbar_end": ["button-more-info"],
    "navbar_persistent": [],
    "content_footer_items": [],
    "footer_start": [],
    "footer_center": ["copyright"],
    "footer_end": [],
    

    # Sidebars
    "primary_sidebar_end": [],
    "secondary_sidebar_items": ["page-toc"],

    # Navigation
    "show_nav_level": 2,
    "navigation_depth": 2,
    "collapse_navigation": True,
    "header_links_before_dropdown": 6,
    "search_bar_text": "Busca en docs...",
    "article_header_start": [],
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pacoborrego/guraify-tms-docs",
            "icon": "fa-brands fa-github",
        }
    ],
    "switcher": {
        "json_url": "versions.json",
        "version_match": "17.0",
    },
}

# Static files
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_extra_path = ["../versions.json"]
html_js_files = ["language-switcher.js"]

# Logo / favicon
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"
