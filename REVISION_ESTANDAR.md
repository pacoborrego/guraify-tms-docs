# Revisión de capítulos contra el estándar v2

Auditoría de los capítulos ya redactados (1–5 y 10) para alinearlos con el estándar
consolidado en el cap. 7. El estándar completo y la *Definición de Hecho* están en
`CLAUDE.md` (sección "Migración Drive → Sphinx").

## Qué se revisa en cada capítulo

Para cada capítulo/subsección se comprueba que cumple los puntos del estándar:

1. **Modelos verificados** — cada modelo/campo/método citado existe en `tms_suite`
   (ojo a `tms_int.*` vs `tms.int.*`); discrepancias anotadas.
2. **Catálogos desde el código** — listas de campos/opciones en `list-table`, no a mano.
3. **Diagramas** — `.. mermaid::` del flujo donde aporte, coherente con el código.
4. **Ruta de UI** — aviso `.. admonition:: Ruta en Odoo` (`:class: tip`) en español al
   inicio de cada sección.
5. **Capturas** — marcadores `.. CAPTURA:` + figure comentado y filas en
   `CAPTURAS_PENDIENTES.md`.
6. **Estilo** — prosa descriptiva consultor/integrador, sin bloques de código (salvo
   campos generativos).
7. **Build limpio** — `make html` sin warnings nuevos (revisar los warnings históricos
   del cap. 4 y 5: tablas mal formadas, títulos cortos, etiquetas duplicadas).

## Estado por capítulo

| Cap. | Modelos | Catálogos | Diagramas | Ruta UI | Capturas | Estilo | Build | Notas |
|---|---|---|---|---|---|---|---|---|
| 1 Introducción | ✅ | n/a | ✅ | n/a | n/a | ✅ | ✅ | **Revisado 2026-06-04.** Títulos ES numerados, fix 1.1/1.5, modelos citados, mermaid de arquitectura en 1.4, anclas pandoc limpiadas y subsecciones PTV restauradas. Capturas: la app (Scandit) se documenta en caps. 6/10, no aquí. |
| 2 Modelo Conceptual | ✅ | n/a | ✅ | ✅ | ✅ | ✅ | ✅ | **Revisado 2026-06-04.** Títulos ES numerados 2.1–2.7, modelos citados, anclas pandoc limpiadas, diagramas 2.5 y 2.6 a mermaid, conclusión 2.7 redactada. Rutas en Odoo (2.1, 2.3) y 3 marcadores de captura (Orden, Viaje, Trazabilidad) en `CAPTURAS_PENDIENTES.md`. |
| 3 Arquitectura Funcional | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Revisado 2026-06-04.** Títulos ES numerados, fix "Maestros operativos", modelos citados, rutas UI + capturas, mermaid del árbol funcional. **3.2 ampliado** creado (3.2.1–3.2.4 desde código). 3.3/3.4/3.5 ampliados. |
| 4 Parametrización | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⚠️ | **Warnings históricos**: tablas mal formadas (4_3) y etiqueta duplicada (4_2). Candidato a rutas UI por ser muy de configuración. |
| 5 Flujo Operativo | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⚠️ | **Warnings históricos**: tablas mal formadas (5_2, 5_5, 5_6, 5_9) y títulos cortos (5_5). |
| 10 Manual App Conductor | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ✅ | Es guía de usuario final: aquí sí caben capturas de la app y un tono más cercano. |

Leyenda: ⬜ pendiente de revisar · ✅ conforme · ⚠️ requiere arreglo.

## Orden sugerido

Primero **terminar los capítulos que faltan** (6 → 8 → 3.2 ampliado) aplicando el
estándar v2 desde el inicio; después **revisar 1–5 y 10**, priorizando:

1. Arreglar los **warnings históricos** de los caps. 4 y 5 (tablas y títulos), para dejar
   el build totalmente limpio.
2. Añadir **rutas de UI** a los capítulos de configuración/operativa (4 y 5), que son los
   que más lo necesitan.
3. Sembrar **marcadores de captura** y volcar sus filas a `CAPTURAS_PENDIENTES.md`.

---

*Generado: 2026-06-04. Marca cada celda al revisarla; al terminar un capítulo, refleja el
cierre en `CHANGELOG.md`.*
