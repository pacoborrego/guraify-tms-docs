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
| D9 | ✅ | **Cap. 7 Guía del integrador** | Index reescrito como Guía del integrador (qué necesitas saber antes, contratos de API en la pasarela). Todos los títulos numerados (7.1.1 … 7.2.2.2.15); las secciones internas de 7.2 van de 7.2.3 a 7.2.7 porque 7.2.1 y 7.2.2 son las páginas hijas. Catálogo de campos de mapeo (280 líneas) movido al **anexo A.22** con tabla corta de entidades y ejemplos en 7.2.1. Funciones de 7.2.2 con el nombre en monoespaciado y descripción en español. «ruta» (URL) → «dirección». Hecha el 2026-09-10 |
| D10 | ✅ | **Cap. 8 Administración y Control Económico** | Capítulo nuevo (`source/17.0/8_economic-administration/`, 8 páginas + index con mermaid): activo, pasivo y margen en los cuatro niveles, división de ventas (modo del Proyecto y porcentajes carga/descarga del tipo de orden), división de costes (modo del Planning, hubs y cargas de reparto sin coste), la orden de compra automática, la liquidación al transportista, los reembolsos y su ciclo, la cuenta analítica y el control (Transacciones, diagnósticos, motor de indicadores, tableros). Verificado en `tms`, `tms_kpi` y `tms_dashboard`. Anexo A.21, siete términos de glosario, cinco capturas, referencias del cap. 3. El antiguo cap. 6 técnico de la app no se escribe: lo técnico de la app que no quepa en el cap. 10 se anota para D11. Hecha el 2026-09-10 |
| D11 | ✅ | **Cap. 10 Manual del conductor** | Reescrito entero para el conductor: tono de tú, pasos numerados, glosario de seis palabras en el index, un solo nombre («Manual del conductor»). Dividido en ocho páginas (Entrar en la app, Tu ruta, La parada, Entregar, Cargar, Cobrar un reembolso, Cuando algo no va bien, Fin de la jornada y sin cobertura). Flujos nuevos verificados en `tms_odoo_app`: carga, pestañas, Reiniciar, sin cobertura y pantalla Cuenta (Sincronizar ahora, Actualizar mi ruta, Limpiar errores). Las cuatro list-tables con imágenes pasan a figuras seguidas. Los nombres de las imágenes existentes no cambian (lote de María en curso); seis capturas nuevas. Títulos numerados 10.N. Hecha el 2026-09-10 |
| D12 | ✅ | **Cierre editorial** | Lectura completa por cinco lectores (distribuidor, consultor ×3, integrador y conductor): unos 350 hallazgos corregidos por bloques (Conocer, 1–2, 3, 4–5, 6–8–anexos, 7–10). Cap. 2 fundido en cuatro páginas; 3.2.6 Tramos y Paradas (nueva); 4.1 al patrón D7 con anexos A.23–A.28; 1.4.6 actualizada (P3 pasa a 1.4.2); cada cosa explicada una vez; glosario ampliado (24 términos nuevos); «solo», comillas latinas, español de España; etiquetas de Odoo corregidas en `es.po`. Release `260910_V07`. Hecha el 2026-09-10 |
| D13 | ⬜ | **Historial git** | Al final de todo: `git filter-repo` para borrar de todos los commits las imágenes con datos reales (`source/_static/images/`, capturas de la app antiguas). María vuelve a clonar. Decisión de Paco 2026-09-08 |
| D14 | ✅ | **Cap. 6 Gestión de Recursos** | Capítulo nuevo del Manual de implantación para `tms_resources` y `tms_maintenance` (`source/17.0/6_resources/`, 8 páginas + index con mermaid): el área y su menú, el odómetro único (fuentes, anomalías, validación, resumen y estimación), el vehículo mantenible y la orden de trabajo, las reglas de preventivo y el control de service, los flujos del taller, las salidas de taller, los indicadores y la configuración. Verificado contra el código y los handoffs (M1 a M7). Siete términos nuevos en el glosario, anexos A.19 y A.20, trece capturas para María. Hecha el 2026-09-10 |

| D15 | ✅ | **Navegación por recorridos** | `guraify.com/docs` abre directamente la portada de las cuatro tarjetas (la raíz redirige; el documento maestro es `17.0/index`). Cada tarjeta lleva al inicio de su recorrido y la barra lateral enseña solo ese recorrido: página raíz nueva `implementation-manual.rst` para el Manual de implantación; el glosario cuelga de Conocer; el manual del conductor deja de ser `:orphan:` y su cabecera lleva el logo para volver a la portada. Plantilla de barra lateral única con el nombre del recorrido enlazado. Decisión de Paco tras ver producción (2026-09-11). Hecha el 2026-09-11 |

Orden: D3 y D4 primero (lo demás las usa). D5 a D11 y D14 en cualquier orden. D12 y D13 al final.
Numeración cerrada el 2026-09-10: el cap. 6 es Gestión de Recursos (D14) y Administración y Control Económico será el cap. 8 (D10).
D2 corre en paralelo todo el tiempo.

## Pendientes sueltos

- **Aviso al destinatario** (`tms_notify`, `tms_notify_whatsapp`, P5 de la torre de control): hecho en el código y pendiente de despliegue. No aparece en «Conocer» ni en 1.4 más que como «pendiente de despliegue» (1.4.6). Cuando Paco termine la torre de control, entra en 0.4 «Qué incluye», 0.6 y en el Manual de implantación (decisión de Paco, 2026-09-10: la torre queda fuera hasta terminarla).
- **Capturas del cap. 1**: no tiene ninguna. Candidatas: ajuste del token PTV, asistente de importación de OSM, editor de áreas, pestaña «ETA y ruta» del Viaje. Se añadirán cuando la interfaz esté traducida (ver correcciones).
- **Portal del cliente**: hoy los clientes no tienen acceso (decisión de Paco, 2026-09-10). Existe `tms_portal` (Bandejas de entrada API en el portal). Si algún día se habilita, la frase de 0.6 es la que hay que ampliar.
- **App, posible fallo funcional** (visto en D12): con **Hecho** + **No Cobrado**, la app pide el motivo y vuelve a la ruta sin cerrar el tramo ni enviar el motivo (`StopInfoPage.vue`, `RefundLeg.vue`). 10.7.3 documenta lo que hace hoy. Si lo esperado es que la app cierre el tramo como fallido, es un arreglo de la app y después se simplifica el texto.
- **6.8 / A.20**: el umbral «sin lectura reciente» es un parámetro del sistema sin pantalla (`tms_maintenance.odometer_stale_days`); si debe tocarlo el administrador, hay que llevarlo a la compañía (código).
- **8.2**: cambiar el modo de división del Proyecto no recalcula las Órdenes abiertas por sí solo (verificado en D12); si se quiere, es código.

## Estructura objetivo del índice

Portada con cuatro recorridos, cada uno una tarjeta y un `toctree` con `:caption:`:

| Recorrido | Público | Contenido |
|---|---|---|
| **Conocer Guraify TMS** | Cliente, distribuidor | `0_product-overview/` (D4) + glosario (D3) |
| **Manual de implantación** | Consultor, cliente avanzado | Página raíz `implementation-manual` + caps. 1 a 6 y 8 (Introducción, Modelo, Arquitectura, Parametrización, Flujos, Gestión de Recursos, Administración económica) + anexo A |
| **Guía del integrador** | Técnico de integración | Cap. 7 + anexos de catálogos de campos |
| **Manual del conductor** | Conductor | Cap. 10 (cabecera y barra lateral propias, con logo para volver a la portada) |

## Correcciones en Odoo y en la app derivadas del glosario

Decididas por Paco al aprobar el glosario (D3, 2026-09-08) y ampliadas en el cierre editorial (D12, 2026-09-10). Son cambios en `tms_suite` (rama 17.0) y en `tms_odoo_app`; **no** se hacen desde este repo. Mientras no estén desplegadas, la doc sigue al glosario y cita entre comillas la etiqueta que hoy ve el usuario.

### Aplicadas en el código el 2026-09-10 (pendientes de commit y despliegue por Paco)

En `tms/i18n/es.po` (validado con `msgfmt -c`): Planning / Plannings (antes Planificación / Planificaciones); estados de la Parada Con reservas / Fallida / Completada (antes Reservista / Fallo / Hecho; ojo: el mismo texto sirve para Tramo y Viaje, que quedan en femenino); Línea de tarifa, Detalle de línea de tarifa y Líneas de tarifa (antes Linea Tarifa, Detalle de regla de tarifa, Reglas Tarifa, Reglas de zona); Áreas Geográficas (menú, antes Zonas Geográficas); Importar fichero (antes Fichero de Importación); Tipos de Orden, Tipos de Destinatario, Tipos de Reembolso (Ajustes, antes Tipos de expediciones, de receptor, de valores de caja; también el campo «Tipo Órden»); Franja horaria (antes Zona Horaria); Portes (antes Costes de Envío); Diagnóstico de tarifa y toda su familia (antes Diagnosis); Correcto (antes OK, en el diagnóstico); Cobrado (antes Recopilado, en el Reembolso); Punto de inicio / Punto de fin (antes Localización Inicio / Punto Fin); Palés (antes Pallets); Definiciones de fichero (antes Ficheros EDI); Lista de facturas (menú «Invoices List», nuevo); kanban y filtros de proyectos (Ingresos, Coste, Ayuda, Enviar por API, Proyectos de Órdenes / de Viajes, Órdenes (abiertas / total)…, nuevos); pestaña «ETA y ruta» del Viaje con sus grupos y el botón «Recalcular ETA ahora» (nuevos); Política operativa y sus selecciones (nuevos).
En `tms_int/i18n/es.po`: Definición de fichero (antes Fichero EDI / Definición de Fichero), pestaña Endpoints (antes traducida como «Variables»), Endpoints API.
En `tms_odoo_app` (rama `fix/app-diagnostics-and-auth`, sin commit): `es_ES.json` failed = Fallido, company_domain = tuempresa.com, find-parcels = Encontrar bultos, título del Panel sin ruta = «No tienes ninguna ruta asignada»; títulos «Mapa» y «Bultos»; «ELIGE UNA OPCIÓN»; textos de confirmación de cancelación en español y sin «expedición».

Para que se vean en Odoo: actualizar `tms` y `tms_int` con `--i18n-overwrite` (o cargar el `.po` desde Ajustes › Traducciones). La doc ya usa estas etiquetas.

### Etiquetas de `tms_resources` y `tms_maintenance` para su futuro `es.po` (levantadas en D12)

Los dos módulos no tienen traducción; toda su interfaz sale en inglés y el cap. 6 la cita entre comillas.
Cuando se cree el `es.po`, estas son las etiquetas y los textos propuestos:

| Dónde | Texto actual | Propuesto |
|---|---|---|
| `tms_resources/views/fleet_vehicle_views.xml` pestaña | Odometer (TMS) | Odómetro (TMS) |
| ídem, botón inteligente y `fleet_vehicle_odometer_views.xml` (acción, lista, menú) | Odometer Anomalies | Anomalías de odómetro |
| `tms_resources/views/fleet_vehicle_odometer_views.xml` filtros | Draft / Valid / Rejected, Regression, Implausible Jump, Duplicate, Future Date, Driver App, Fuel Import… | Borrador / Válida / Rechazada, Retroceso, Salto inverosímil, Duplicada, Fecha futura… |
| `tms_resources/models/fleet_vehicle.py` | Last Odometer (TMS), Km per Day, Meter Type (Odometer / Engine Hours), Telemetry Device Reference | Último odómetro (TMS), Km por día, Tipo de contador (Odómetro / Horas de motor), Referencia del dispositivo de telemetría |
| `tms_resources/models/res_company.py` | Max Km per Day | Máximo de km por día |
| `tms_maintenance/views/fleet_vehicle_views.xml` pestaña | Maintenance (TMS) | Mantenimiento (TMS) |
| ídem, botones | Bulk Preventive Service · Copy Workshop Status · Print Work Order · Open Orders | Carga masiva de revisiones · Copiar estado para el taller · Imprimir orden de trabajo · Órdenes abiertas |
| ídem, grupos | Service Control · Reliability · Unit · Preventive Rules · Work Orders | Control de revisiones · Fiabilidad · Vehículo · Reglas de preventivo · Órdenes de trabajo |
| ídem, acción | Service Control (menú «Control de service») | Control de revisiones |
| `tms_maintenance/views/maintenance_request_views.xml` botón | Close Order | Cerrar orden |
| `tms_maintenance/wizard/*_views.xml` | Close Work Order, Bulk Preventive Service, Register Services, Objective Ranking, Workshop Status, Close, Cancel | Cerrar orden de trabajo, Carga masiva de revisiones, Registrar revisiones, Ranking de objetivos, Estado para el taller, Cerrar, Cancelar |
| `tms_maintenance/models/tms_maintenance_rule.py` selecciones | OK / Due Soon / Overdue / Not Evaluated; High / Medium; Kilometres / Days / Not Applicable; Does not apply to this unit, No history: load it as a pending job, Odometer capture missing, Odometer series too thin to estimate, Inconsistent data; register the real km | Al día / Por vencer / Vencido / No evaluada; Alta / Media; Kilómetros / Días / No aplica; No aplica a este vehículo, Sin historial (cargar como pendiente), Falta captura de odómetro, Serie insuficiente para estimar, Dato incoherente: registrar el km real |
| `tms_maintenance/models/fleet_vehicle.py` | Last Service Km, Fuel Service Status/Remaining, Full Service Status/Remaining, Unit Configuration, No Data | Km de la última revisión, Estado/Restante revisión de combustible, … completa, Configuración del vehículo, Sin datos |
| `tms_maintenance/models/res_company.py` | Fuel Service Interval, Full Service Interval, Service Warning Margin, Workshop Texts Signature | Intervalo revisión de combustible, Intervalo revisión completa, Margen de aviso, Firma de los textos de taller |
| Menús `tms_maintenance/views/menu.xml` (ya en español) | Control de service · Carga masiva de service | Control de revisiones · Carga masiva de revisiones |
| KPI de serie `tms_maintenance/data/tms_maintenance_kpi_data.xml` y `tms_kpi_maintenance.py` | Service de combustible vencido · Service completo vencido · Unidades con órdenes abiertas · Unidades sin odómetro · Unidades sin lectura reciente · Reglas con km estimado % | Revisión de combustible vencida · Revisión completa vencida · Vehículos con órdenes abiertas · Vehículos sin odómetro · Vehículos sin lectura reciente · Reglas con km estimado |
| Datos de serie `tms_maintenance_task_data.xml` | Gomeria · Auxilio · MO · M. Preventivo · Labor | Neumáticos · Asistencia en carretera · Mano de obra · Preventivo · (¿Labor = Mano de obra? aclarar con el cliente) |
| Datos de serie `tms_objective_service_type_data.xml` | Calibración de cubiertas · Relevamiento de cubiertas | Calibración de neumáticos · Revisión de neumáticos (ojo: `TMS_OBJECTIVES` en `fleet_service_type.py` los fija por xmlid, el nombre se puede cambiar) |
| Textos de WhatsApp y orden impresa (`fleet_vehicle.py`, literales en español a propósito) | «Chofer:», «GOMERÍA / OBJETIVOS», «SERVICE», «Próximo» | Decisión de Paco: son un contrato con el taller del cliente argentino; la doc los cita tal cual. Si se generaliza el módulo, «Conductor», «NEUMÁTICOS / OBJETIVOS», «REVISIONES», «Por vencer» |
| `tms_maintenance/tools/import_ludamany.py` | Script de migración específico de un cliente | La doc lo describe como «script de importación de la implantación». Decidir si se generaliza (nombre, CSV genéricos) o se deja fuera del producto |

### Pendientes (código, no solo traducción)

| Dónde | Hoy dice | Debe decir | Motivo |
|---|---|---|---|
| `tms_resources` y `tms_maintenance` | **Sin `i18n/es.po`**: toda su interfaz sale en inglés (Odometer (TMS), Odometer Anomalies, Maintenance (TMS), Close Order, Bulk Preventive Service, Print Work Order, Copy Workshop Status, Service Control, filtros y selecciones de la regla…) | Crear el `es.po` de los dos módulos con la tabla de etiquetas de más arriba | El cap. 6 cita las etiquetas inglesas entre comillas; las capturas del cap. 6 esperan a esto |
| `tms_maintenance/data/*.xml` (datos de serie) | Gomeria · Auxilio · MO · Labor · Calibración de cubiertas · Relevamiento de cubiertas · Control de service · Carga masiva de service · KPIs «Service … vencido», «Unidades …» | Neumáticos · Asistencia en carretera · Mano de obra · Calibración de neumáticos · Revisión de neumáticos · Control de revisiones · Carga masiva de revisiones · «Revisión … vencida», «Vehículos …» | Español de España (decisión de Paco, 2026-09-10). Los textos de WhatsApp y de la orden impresa («Chofer», «GOMERÍA», «SERVICE») son un contrato con el taller del cliente: decidir si se generalizan |
| `tms_maintenance/tools/import_ludamany.py` | Script de migración de un cliente | Generalizarlo o dejarlo fuera del producto | 6.8 lo describe como script de consola de la implantación |
| Menús `tms.operations_master_data_submenu` y `tms.administration_md_submenu` | «Maestros» dos veces (Operaciones y Administración) | Distinguirlos («Maestros operativos» / «Maestros de administración») | Un solo `msgid` («Master Data») para los dos: hace falta un texto fuente distinto |
| `tms_dashboard/data/dashboards.xml` y los JSON de las hojas | Operations KPI · Stops Operations · Pending Invoicing (y títulos de pivots en inglés) | Indicadores de operaciones · Paradas · Facturación pendiente | Sin traducción en `i18n` |
| `tms/i18n/es.po` «Trayecto», «Crear trayecto faltante» | trayecto | El glosario no tiene «trayecto»: definirlo o renombrar («precio entre zonas») | Visto en D12 (8.5, A.21) |
| `tms.pricelist.item.zone.follow_up_pass` («Seguimiento pasivo») | Campo declarado y sin uso en el cálculo | Ocultarlo o implementarlo | Visto en D12 (A.15) |
| `tms_int.integration` | Sin menú (solo acción) | Decidir si va bajo EDI | Visto en D12 (7.3) |
| `tms_int_api_get_attachment.py` | La descarga de adjuntos no registra en `tms.api.log` | Registrar si se quiere traza | Visto en D12 (7.7) |
| Informe «Transport Manifest» | Título del PDF en mayúsculas fijas «MANIFIESTO DE TRANSPORTE» (`msgid` = `msgstr`) | Cadena traducible | Cosmético (visto en D12) |
| `tms/i18n/es.po` (visto en D12, bloque C) | «Id» como nombre de los Tipos de Transportista y de Reembolso; «Arrival Geofence (m)» sin traducir (Tipo de Parada, conector de telemática) | «Nombre»; «Radio de llegada (m)» | Etiquetas de campo |
| Menú TMS › Operaciones › Planning (`tms.operations_planning_submenu`) | «Planning» (mismo `msgid` que la entidad) | «Planificación» | Choca con la entidad Planning; hace falta un texto fuente distinto |
| `tms/models/tms_stop.py` `state_group` | Hecho · Fallido · Sin Realizar (tarjetas de los tableros) | Completadas · Fallidas · Pendientes | Contra el glosario; cadenas en código |
| `tms_int/views/tms_int_menu.xml` | Menú **Patrones** comentado y campo `pattern_id` oculto | Decidir si se reactiva | Los patrones (`tms_int.pattern`) no se alcanzan desde la interfaz (visto en D12) |
| `tms/i18n/es.po` estados compartidos | Completada / Fallida / Con reservas / Reprogramada / Devuelta / Cargada / Procesada sirven para Parada, Tramo, Orden y Viaje | Separar los `msgid` por modelo si se quiere el género correcto en Tramo y Viaje | Decisión de D12: manda el femenino de la Parada |
| `tms_odoo_app` `StopInfoPage.vue`, `RefundLeg.vue` | Hecho + No Cobrado no cierra el tramo ni envía el motivo | Cerrar el tramo como fallido con el motivo (si es lo esperado) | Posible fallo (visto en D12, ver Pendientes sueltos) |

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
