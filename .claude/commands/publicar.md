---
description: Publicar la documentación en guraify.com/docs (build + copia en epartner)
---

Publica la documentación. Lee primero el apartado "Publicación" de CLAUDE.md.

1. Comprueba que no hay cambios locales sin commitear ni commits sin push
   (`git status --short`, `git log origin/17.0..HEAD` o la rama que toque). Si los hay, para
   y dímelo: no se publica nada que no esté en GitHub.
2. Ejecuta en el servidor:
   `ssh epartner "sudo -u pborrego -H /opt/tms-docs/guraify-tms-docs/deploy.sh"`
   El script hace pull, compila con -W y copia a /var/www/tms-docs. No hay servicio que
   reiniciar.
3. Verifica con curl que https://guraify.com/docs/ y una página cambiada en esta publicación
   devuelven 200, y que el HTML servido contiene algún texto nuevo de la publicación.
4. Si CHANGELOG.md tiene una sección "Sin publicar" con contenido, propónme moverla a una
   sección con el nombre del tag (AAMMDD_VNN) y crear el tag git. No lo ejecutes sin mi OK.
