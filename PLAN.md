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
| D4 | ✅ | **Capa de producto** | `0_product-overview/` con 8 páginas (qué es, para quién, cómo funciona, qué incluye, app, integraciones, 4 casos de uso sin nombres, FAQ) y portada nueva con los cuatro recorridos y sus toctrees. Títulos sin numerar por decisión de Paco. Preguntas comerciales en "consulta con Guraify". `tms_crm` fuera del producto. Hecha el 2026-09-08 |
| D5 | ✅ | **Cap. 1 Introducción** | 1.1 y 1.3 reorientados al Manual de implantación con enlaces a los otros tres recorridos. 1.4 reescrito desde el código (3.577 → 2.300 palabras): servicios PTV reales (routing, secuenciación, optimización con `routeoptimization/v1`, no OptiFlow), cascada de geocodificación de cuatro pasos, mapa PTV con respaldo OSM, áreas, tres modos de escaneo Scandit. Lo en desarrollo va en **1.4.6 Evolución prevista**, por decisión de Paco. 1.2 sin modelos; 1.5 sin repetir ingreso/coste (enlaza a 2.1). Hecha el 2026-09-08 |
| D6 | ✅ | **Cap. 3 Arquitectura** | Campos, métodos y códigos fuera de la prosa: los estados se nombran como en pantalla, los botones por su etiqueta (Bloquear, Desbloquear, Validar e importar, Importar Fichero Ahora) y los campos van a una tabla "Referencia técnica" al final de 3.2.1, 3.2.2 y 3.2.5. Mermaid de 3.2.5 sin campos. 3.1 alineado con el menú real (Trazabilidad en Tráfico, Líneas en Maestros operativos, Administración = Opciones de tarifa/Maestros/Reembolsos/Transacciones, EDI en Configuración). Referencias a los caps. 6 y 8 sustituidas por 5.4, 5.6 y 5.7 hasta que exista D10. 3.3 ya no dice que el planificador elige el objetivo. Anglicismos: *slot* → franja, *smart buttons* → botones inteligentes, *routing* → cálculo de ruta (término nuevo en el glosario, aplicado también en 1.4 y 5.2). Hecha el 2026-09-08 |
| D7 | ✅ | **Cap. 4 Parametrización** | 4.2 a 4.5 reescritas en prosa desde los modelos (qué es el maestro, qué decide el cliente, qué efecto tiene), con una tabla corta «Decisión / Efecto» por maestro. Las 25 tablas «Campos principales» salen a un **anexo A** (`source/17.0/annexes/`, 18 páginas, una por maestro, con la etiqueta de la interfaz en español, el tipo y el significado). Fuera las notas de desarrollador, las dos tablas rotas de 4.5.10 y los códigos técnicos en prosa; «Reglas de tarifa» sólo para la unidad de medida (4.2.3) y «Líneas de tarifa» para el precio (4.4.3); kanban de proyectos en español. Nueve capturas nuevas para María. Hecha el 2026-09-10 |
| D8 | ✅ | **Cap. 5 Flujos** | Index reescrito con el mermaid del ciclo completo. 5.2 a 5.7 redactados como flujo paso a paso y verificados en el código (asistentes Asignar a viaje y Acciones operativas, Enviar a la app, trazabilidad, cadena de cierre, tarificación por tarea programada cada 5 min, Modo de facturación TMS). Reparto con el cap. 3 aplicado (entidad en el 3, flujo en el 5). Códigos de la app en una tabla de referencia técnica (5.4.4). Sin peajes en 5.2, sin *slot*, sin cap. 6. Hecha el 2026-09-08 |
| D9 | ⬜ | **Cap. 7 Integraciones** | Etiquetarlo como *Guía del integrador* en portada y toctree. Numerar los títulos internos. Mover el catálogo de campos de mapeo (280 líneas) a anexo |
| D10 | ⬜ | **Cap. 8** | Escribir **Administración y Control Económico** (costes, división de ventas y costes, OC automáticas, liquidación, analítica, reporting) desde el código. El cap. 6 técnico de la app **no se escribe**: se fusiona con el cap. 10 más una sección corta en el 3. Renumerar según se decida con Paco al empezar la tarea |
| D11 | ⬜ | **Cap. 10 Manual del conductor** | Limpiar restos de Word, unificar el tono (tú), glosario inicial (POD, Reserva, KO, Dominio), dividir `10_3_report.rst` en 4 ficheros, escribir el flujo de **carga**, el **cierre de ruta** y el **modo sin cobertura**. Sustituir las 4 `list-table` con imágenes por figuras |
| D12 | ⬜ | **Cierre editorial** | Lectura completa de principio a fin como lector externo. `CHANGELOG`, tag de release, `/publicar` |
| D13 | ⬜ | **Historial git** | Al final de todo: `git filter-repo` para borrar de todos los commits las imágenes con datos reales (`source/_static/images/`, capturas de la app antiguas). María vuelve a clonar. Decisión de Paco 2026-09-08 |
| D14 | ✅ | **Cap. 6 Gestión de Recursos** | Capítulo nuevo del Manual de implantación para `tms_resources` y `tms_maintenance` (`source/17.0/6_resources/`, 8 páginas + index con mermaid): el área y su menú, el odómetro único (fuentes, anomalías, validación, resumen y estimación), el vehículo mantenible y la orden de trabajo, las reglas de preventivo y el control de service, los flujos del taller, las salidas de taller, los indicadores y la configuración. Verificado contra el código y los handoffs (M1 a M7). Siete términos nuevos en el glosario, anexos A.19 y A.20, trece capturas para María. Hecha el 2026-09-10 |

Orden: D3 y D4 primero (lo demás las usa). D5 a D11 y D14 en cualquier orden. D12 y D13 al final.
Numeración cerrada el 2026-09-10: el cap. 6 es Gestión de Recursos (D14) y Administración y Control Económico será el cap. 8 (D10).
D2 corre en paralelo todo el tiempo.

## Pendientes sueltos

- **1.4.6 Evolución prevista está desfasada** (detectado en D8, 2026-09-08): la tarea P3 de la torre de control (ETA incremental con historial, peajes y CO₂ en el cálculo de ruta) se terminó ese mismo día en `tms_suite`. Hay que mover esos dos puntos de 1.4.6 a 1.4.2 verificándolos en `handoff/control_tower_P3.md`, y añadir la corrección al glosario si hace falta (ETA prometido / ETA vigente). Sitio natural: D12, o una sesión corta antes.

## Estructura objetivo del índice

Portada con cuatro recorridos, cada uno una tarjeta y un `toctree` con `:caption:`:

| Recorrido | Público | Contenido |
|---|---|---|
| **Conocer Guraify TMS** | Cliente, distribuidor | `0_product-overview/` (D4) + glosario (D3) |
| **Manual de implantación** | Consultor, cliente avanzado | Caps. 1 a 6 y 8 (Introducción, Modelo, Arquitectura, Parametrización, Flujos, Gestión de Recursos, Administración económica) + anexo A |
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
| `tms/i18n/es.po`, botón `Import File` del Manifiesto | Fichero de Importación | Importar fichero | Es una acción, no un campo (visto en D6) |
| `tms/i18n/es.po`, Ajustes › Datos auxiliares | Tipos de expediciones · Tipos de receptor · Tipos de valores de caja · Planificaciones | Tipos de Orden · Tipos de Destinatario · Tipos de Reembolso · Plannings | Glosario (visto en D7) |
| `tms/i18n/es.po`, `tms.time.zone` | Zona Horaria | Franja horaria | Es una franja de servicio, no un huso horario (visto en D7) |
| `tms/views/project_project_views.xml` (kanban de proyectos) | Orders, Trips, Revenue, Cost, Help, HUB/AUTO/API, filtros «Orders projects» | Órdenes, Viajes, Ingresos, Coste, Ayuda… | Cadenas sin entrada en `es.po`; la doc las da en español (visto en D7) |
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
