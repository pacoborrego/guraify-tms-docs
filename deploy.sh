#!/usr/bin/env bash
# Publica la documentación en guraify.com/docs.
#
# Se ejecuta EN EL SERVIDOR epartner, como el usuario pborrego (dueño del repo
# y de /var/www/tms-docs):
#
#     ssh epartner "sudo -u pborrego -H /opt/tms-docs/guraify-tms-docs/deploy.sh"
#
# No hay ningún servicio que reiniciar: nginx sirve /var/www/tms-docs como
# estático (vhost /etc/nginx/sites-enabled/guraify.com, location /docs/).
# Publicar = traer el repo, compilar y copiar el HTML.
set -euo pipefail

REPO=/opt/tms-docs/guraify-tms-docs
WWW=/var/www/tms-docs

cd "$REPO"
echo "== git pull"
git pull --ff-only

echo "== sphinx build completo (los warnings son errores)"
# -E -a: reconstruir TODO, no incremental. Una compilación incremental solo reescribe las
# páginas cuyo fuente cambió, y deja obsoleta la barra lateral del resto cuando se añade un
# capítulo (pasó el 2026-09-10 con el cap. 6: la portada lo tenía y el cap. 5 no).
python3 -m sphinx -b html -W --keep-going -E -a source build/html

echo "== rsync -> $WWW"
rsync -a --delete build/html/ "$WWW"/

echo "== publicado: $(git log -1 --format='%h %s') -> https://guraify.com/docs/"
