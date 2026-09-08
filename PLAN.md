# Plan de cierre de la documentación Guraify TMS

Objetivo: que `guraify.com/docs` sirva para que **clientes y distribuidores** entiendan qué
es Guraify TMS y qué hace, y para que **consultores e integradores** lo implanten. Hoy sólo
cubre lo segundo, y a medias.

Este plan sustituye a `MIGRACION.md` y `REVISION_ESTANDAR.md` (borrados el 2026-09-08).
El diagnóstico completo del que sale está resumido en el apartado "Diagnóstico".

**Fuera de alcance, por decisión de Paco (2026-09-08):**
- Versiones 18.0/19.0: no se toca `versions.json` ni se crea `source/19.0/`. El selector de
  versión está oculto.
- Traducciones: se hacen cuando el contenido en español esté terminado. El selector de
  idioma está oculto y los `.po` de `source/locale/` se dejan como están.

## Cómo se trabaja

- **Una tarea por sesión.** Cada tarea tiene su comando `/dN` en `.claude/commands/`, que
  contiene el prompt completo. La sesión arranca con `/estado`, hace la tarea y cierra con
  `/cerrar-tarea`.
- **Esqueleto antes que prosa.** En las tareas de redacción, enseñar a Paco la estructura
  (ficheros, títulos, toctree) y esperar el OK antes de escribir el texto.
- **Manda el código.** Todo lo que se afirme del sistema se verifica en
  `/Users/paco/odoo17/custom_addons/tms_suite/`. Ver `CLAUDE.md`.
- **Publicar** es `/publicar` (script `deploy.sh` en epartner). No hay servicio que reiniciar.
- María hace las capturas en paralelo siguiendo `CAPTURAS_PENDIENTES.md`; cuando suba un
  lote, `/capturas` las activa.

## Tareas

Estados: ⬜ pendiente · 🔶 en curso · ✅ hecha.

| # | Estado | Tarea | Resultado esperado |
|---|---|---|---|
| D1 | ✅ | **Infraestructura** | `PLAN.md`, `CLAUDE.md` v3, comandos, `deploy.sh`, CI, repo limpio, selectores ocultos, capturas existentes activadas. Hecha el 2026-09-08 |
| D2 | 🔶 | **Capturas (María)** | Rehacer las 55 existentes (recortadas, anonimizadas, Odoo en español) y hacer las 26 que faltan. Lista en `CAPTURAS_PENDIENTES.md`. Corre en paralelo con todo lo demás |
| D3 | ✅ | **Glosario** | `source/17.0/glossary.rst` con 40 términos (definición, sinónimos descartados, modelo) y el texto de los 56 `.rst` alineado. Hecha el 2026-09-08. Deja una lista de correcciones para Odoo y la app (ver apartado al final) |
| D4 | ⬜ | **Capa de producto** | Carpeta `0_product-overview/` y portada nueva: qué es Guraify TMS, qué resuelve, para quién, módulos, app del conductor, integraciones, casos de uso, preguntas frecuentes. Sin modelos Odoo. Es lo que hoy falta por completo |
| D5 | ⬜ | **Cap. 1 Introducción** | Reorientar 1.1 y 1.3 al nuevo público. Recortar 1.4 (533 líneas de PTV y Scandit) a lo que está implementado, verificado en el código |
| D6 | ⬜ | **Cap. 3 Arquitectura** | Sacar campos y métodos de la prosa (quedan en el aviso "Ruta en Odoo" o en anexo). Corregir las referencias a los caps. 6 y 8 |
| D7 | ⬜ | **Cap. 4 Parametrización** | Reescribir 4.2 a 4.5 en prosa (hoy son apuntes). Arreglar las dos tablas rotas de 4.5.10. Quitar notas de desarrollador (4.2, 4.3, 4.5). Traducir 4.5.10. Catálogos de campos a anexo. Unificar Orden/Expedición y desambiguar "Reglas de Tarifa" |
| D8 | ⬜ | **Cap. 5 Flujos** | Cerrar la frase cortada del index. Redactar 5.3 a 5.7 al nivel de 5.1/5.2. Decidir qué tema vive en el cap. 3 y cuál en el 5 (manifiestos, optimizador, cierre por estados) y quitar la duplicidad. Traducir códigos internos de evento |
| D9 | ⬜ | **Cap. 7 Integraciones** | Etiquetarlo como *Guía del integrador* en portada y toctree. Numerar los títulos internos. Mover el catálogo de campos de mapeo (280 líneas) a anexo |
| D10 | ⬜ | **Caps. 6 y 8** | Escribir **Administración y Control Económico** (costes, división de ventas y costes, OC automáticas, liquidación, analítica, reporting) desde el código. El cap. 6 técnico de la app **no se escribe**: se fusiona con el cap. 10 más una sección corta en el 3. Renumerar según se decida con Paco al empezar la tarea |
| D11 | ⬜ | **Cap. 10 Manual del conductor** | Limpiar restos de Word, unificar el tono (tú), glosario inicial (POD, Reserva, KO, Dominio), dividir `10_3_report.rst` en 4 ficheros, escribir el flujo de **carga**, el **cierre de ruta** y el **modo sin cobertura**. Sustituir las 4 `list-table` con imágenes por figuras |
| D12 | ⬜ | **Cierre editorial** | Lectura completa de principio a fin como lector externo. `CHANGELOG`, tag de release, `/publicar` |
| D13 | ⬜ | **Historial git** | Al final de todo: `git filter-repo` para borrar de todos los commits las imágenes con datos reales (`source/_static/images/`, capturas de la app antiguas). María vuelve a clonar. Decisión de Paco 2026-09-08 |

Orden: D3 y D4 primero (lo demás las usa). D5 a D11 en cualquier orden. D12 y D13 al final.
D2 corre en paralelo todo el tiempo.

## Estructura objetivo del índice

Portada con cuatro recorridos, cada uno una tarjeta y un `toctree` con `:caption:`:

| Recorrido | Público | Contenido |
|---|---|---|
| **Conocer Guraify TMS** | Cliente, distribuidor | `0_product-overview/` (D4) + glosario (D3) |
| **Manual de implantación** | Consultor, cliente avanzado | Caps. 1 a 6 (Introducción, Modelo, Arquitectura, Parametrización, Flujos, Administración económica) |
| **Guía del integrador** | Técnico de integración | Cap. 7 + anexos de catálogos de campos |
| **Manual del conductor** | Conductor | Cap. 10 (ya aislado visualmente) |

## Correcciones en Odoo y en la app derivadas del glosario

Decididas por Paco el 2026-09-08 al aprobar el glosario (D3). Son cambios de código en
`tms_suite` (`tms/i18n/es.po`, menús) y en `tms_odoo_app`; **no** se hacen desde este repo.
Mientras no se apliquen, la doc sigue al glosario y no a la pantalla.

| Dónde | Hoy dice | Debe decir | Motivo |
|---|---|---|---|
| `tms/i18n/es.po`, entidad `tms.planning` | Planificación / Planificaciones | Planning / Plannings | Se confunde con el menú y la actividad "Planificación" |
| `tms/i18n/es.po`, estado `reserves` de la Parada | Reservista | Con reservas | Traducción errónea |
| `tms/i18n/es.po`, estado `failed` de la Parada | Fallo | Fallida | Coherencia con el resto de estados |
| `tms/i18n/es.po`, estado `completed` de la Parada | Hecho | Completada | Coherencia |
| `tms/i18n/es.po`, `tms.pricelist.item.zone.detail` | Detalle de regla de tarifa | Detalle de línea de tarifa | "Regla de tarifa" es `tms.pricelist.rule` |
| `tms/i18n/es.po`, `tms.pricelist.item.zone` | Linea Tarifa | Línea de tarifa | Tilde y preposición |
| Menú TMS › Configuración | Zonas Geográficas | Áreas Geográficas | Dos "zonas" distintas confunden con Zonas de Tarifa |
| `tms_odoo_app`, `es_ES.json` `buttons.stateLabel.failed` | Cancelado | Fallido | En `results.failed` ya dice Fallido; el mismo estado con dos nombres |
| `tms_odoo_app`, `es_ES.json` `company_domain` | sucompañina.com | tuempresa.com | Errata en el placeholder del Dominio |

## Diagnóstico (2026-09-08)

Resumen de lo encontrado en la auditoría que da origen a este plan.

- **Público equivocado.** 1.1 dice literalmente que no es un manual de usuario final. No hay
  ninguna página que explique qué es el producto. La portada son dos tarjetas.
- **Dos calidades de texto.** Caps. 1, 2, 3 y 7 en prosa trabajada; 4 y 5 (salvo 5.1, 5.2,
  5.8) en estilo telegráfico con notas de desarrollador dentro. Cap. 10 mezcla tres tonos.
- **Terminología sin fijar.** Orden/Expedición, Viaje/Ruta, "API Inbox"/"Bandeja de Entrada
  API"; "Reglas de Tarifa" significa dos cosas (4.2.3 y 4.4.3).
- **Duplicidades cap. 3 ↔ cap. 5.** Manifiestos, optimizador, cierre por estados, frontera
  con el gateway.
- **Huecos.** El menú salta 5 → 7 → 10; el texto cita los caps. 6 y 8 como existentes.
- **Capturas.** Las 17 de septiembre no estaban activadas (figures comentados). 12 marcadas
  como hechas sin fichero. Nombres con espacios y numeración vieja. Son capturas a pantalla
  completa (barra del Mac, dock, hora, 1–2,5 MB) con Odoo en inglés mientras el texto da las
  rutas en español.
- **Datos personales.** Las capturas de la app muestran nombres, teléfonos y direcciones
  reales; el repo es público. Se rehacen todas (D2) y se limpia el historial (D13).
- **Herramienta.** Selectores de idioma y versión que prometían lo que no existe (ocultos en
  D1). No había nada de despliegue en el repo; la web servía el build del 21 de mayo.
