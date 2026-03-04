# Guraify TMS Docs

Documentación técnica del TMS (Sphinx).

## Requisitos
- Python 3.x
- venv recomendado

## Setup local
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html
open build/html/index.html