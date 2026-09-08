# Guraify TMS Docs

Documentación de Guraify TMS (Sphinx). Publicada en https://guraify.com/docs/.

## Setup local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html
open build/html/index.html
```

## Publicar

```bash
ssh epartner "sudo -u pborrego -H /opt/tms-docs/guraify-tms-docs/deploy.sh"
```

Ver `CLAUDE.md` (convenciones y publicación), `PLAN.md` (tareas) y
`CAPTURAS_PENDIENTES.md` (capturas).
