---
description: Dónde estamos en la documentación (rama, cambios, tareas del plan, capturas)
---

Dame el estado del proyecto de documentación, sin tocar nada:

1. Lee CLAUDE.md y PLAN.md.
2. `git status --short`, rama y últimos 5 commits. Si hay cambios sin commitear, dime de qué tarea parecen.
3. Tabla de tareas de PLAN.md: cuáles están ✅, cuál está 🔶 y cuál toca ahora según el orden del plan.
4. Capturas: cuenta los marcadores `.. CAPTURA:` que quedan en source/17.0 y compáralo con
   CAPTURAS_PENDIENTES.md. Si hay imágenes nuevas en source/_static/img sin activar, dímelo
   (eso es trabajo de /capturas).
5. Compila con `./.venv/bin/python -m sphinx -b html -W source build/html` y dime si está limpio.
6. Si ves algo a medias o inconsistente entre PLAN.md, CHANGELOG.md y el contenido, dímelo.

Solo lectura: no modifiques ni crees nada.
