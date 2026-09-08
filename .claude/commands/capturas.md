---
description: Activar las capturas que María haya subido y actualizar su lista de trabajo
---

María ha subido capturas nuevas a source/_static/img/. Lee CLAUDE.md (apartado Capturas) y
CAPTURAS_PENDIENTES.md.

1. Recorre los marcadores `.. CAPTURA: <id>` de source/17.0/**/*.rst. Para cada uno cuya
   imagen ya exista en la ruta que indica su `.. figure::` comentado, activa el figure:
   quita la línea del marcador y desindenta el bloque tres espacios. No toques los que siguen
   sin imagen.
2. Comprueba los nombres de fichero de source/_static/img contra los que esperan los .rst:
   espacios, mayúsculas, numeración vieja. Si un fichero está mal nombrado, renómbralo con
   `git mv` al nombre que espera el .rst y dímelo.
3. Revisa visualmente cada imagen nueva (léela) y comprueba los requisitos de la guía:
   recortada a Odoo (sin barra del Mac, dock ni pestañas del navegador), Odoo en español,
   sin nombres, teléfonos ni direcciones reales, ancho 1400–1600 px. Si alguna no cumple,
   NO la actives: déjala en la lista como "rehacer" con el motivo.
4. Actualiza CAPTURAS_PENDIENTES.md: ✅ las activadas, motivo en las que hay que rehacer, y
   añade filas para marcadores nuevos que no estén en la lista.
5. Compila con -W y enséñame el resumen: activadas, rechazadas y motivo, pendientes.
6. Prepara el commit (no lo ejecutes) con /cerrar-tarea.
