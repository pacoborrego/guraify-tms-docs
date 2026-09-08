---
description: Cerrar la tarea actual — plan, changelog y commit
---

Cierra la tarea en la que acabamos de trabajar. En este orden:

1. Compila con `./.venv/bin/python -m sphinx -b html -W source build/html`. Si hay un solo
   warning, arréglalo antes de seguir: el CI y el servidor compilan con -W.
2. Actualiza PLAN.md: estado de la tarea (✅ o 🔶 con una línea de qué falta) y cualquier
   decisión tomada durante la sesión que cambie el plan.
3. Si la tarea ha creado capítulos, ficheros o marcadores de captura nuevos, refleja las
   capturas en CAPTURAS_PENDIENTES.md (fila por captura, con nombre de fichero y pie).
4. Registra el cambio en CHANGELOG.md, sección "Sin publicar": capítulo afectado y resumen.
   Si la tarea ha revelado una discrepancia entre la doc antigua y el código, anótala ahí.
5. Si has cambiado algo estructural (carpeta nueva, convención nueva, decisión de estilo),
   actualiza CLAUDE.md y su línea de fecha del pie.
6. Prepárame el commit, pero NO lo ejecutes: enséñame `git status --short`, `git diff --stat`
   y el mensaje que propones con la convención AAMMDD_VNN (mira los últimos commits para
   saber qué número toca hoy). Yo lo confirmo.
