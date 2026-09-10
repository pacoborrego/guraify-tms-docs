# Capturas — lista de trabajo para María

Todas las capturas de la documentación hay que **rehacerlas** (las que existen) o **hacerlas**
(las que faltan). Motivo: las actuales son capturas a pantalla completa, con Odoo en inglés y,
en el caso de la app, con nombres, teléfonos y direcciones reales de destinatarios en un repo
público. Decisión de Paco, 2026-09-08.

## Requisitos de una captura válida

1. **Recorte**: solo la ventana de Odoo (o la zona relevante: un formulario, una lista, un
   menú). Sin barra de menús del Mac, sin dock, sin hora, sin pestañas ni barra de direcciones
   del navegador. En Chrome, `Cmd+Shift+4` y arrastrar sobre la zona, o usar el modo
   "Capturar área" de las herramientas de desarrollador.
2. **Odoo en español**: la interfaz debe estar en español (Preferencias del usuario › Idioma),
   porque el texto de la doc da las rutas de menú en español (TMS › Operaciones › Tráfico…).
3. **Sin datos reales**: ningún nombre de cliente, destinatario, conductor, teléfono,
   dirección, matrícula ni email real. Opciones, en este orden: usar una base de datos de
   demo; crear registros de prueba con nombres inventados; como último recurso, difuminar
   (pero el difuminado a mano se nota y deja rastros, mejor evitarlo). Las capturas de la app
   se hacen con una ruta de prueba, nunca con una ruta real.
4. **Tamaño**: ancho entre 1400 y 1600 px para pantallas de Odoo; para la app, la captura
   nativa del teléfono. Formato PNG. Idealmente por debajo de 400 KB (si pesa más, pasarla por
   https://tinypng.com o similar).
5. **Nombre de fichero**: exactamente el de la columna "Fichero" de las tablas de abajo, en la
   carpeta indicada. Si el nombre no coincide, la imagen no se muestra.

## Cómo entregar

1. Guardar el PNG en `source/_static/img/<carpeta>/` con el nombre exacto.
2. Commit y push a la rama de trabajo acordada con Paco.
3. Avisar a Paco: él ejecuta `/capturas`, que activa las imágenes en el texto, comprueba los
   requisitos y actualiza esta lista. No hace falta tocar los `.rst`.

Estados: 🔁 existe pero hay que rehacerla · ⬜ no existe · ✅ hecha y validada.


## Conocer Guraify TMS (capa de producto)

> Carpeta: `source/_static/img/0_product-overview/`
>
> Estas páginas reutilizan además cuatro capturas de otros capítulos (Orden, Optimizador,
> pantalla principal de la app), que se actualizan solas cuando se rehagan las originales.

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| ⬜ | `0_4_what-it-includes.rst` | `0_4_what-it-includes_01_tablero.png` | Tablero de operaciones: volumen, puntualidad y estado de las paradas del día. | TMS › Operaciones › Tableros (tablero de operaciones, con datos de demo) |
| ⬜ | `0_6_integrations.rst` | `0_6_integrations_01_portal.png` | El portal del cliente: envíos recibidos, rechazados y su manifiesto. | Portal del cliente, entrando con un usuario de portal: Mi cuenta › Bandejas API |

## Capítulo 2 — Modelo conceptual

> Carpeta: `source/_static/img/2_conceptual-model/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `2_1_structural-logic.rst` | `2_1_structural-logic_01_orden.png` | Formulario de una Orden (sale.order) en Odoo. | Las cuatro entidades del modelo se consultan en TMS › Operaciones › Tráfico: |
| 🔁 | `2_1_structural-logic.rst` | `2_1_structural-logic_02_viaje.png` | Formulario de un Viaje (tms.trip) en Odoo. | Las cuatro entidades del modelo se consultan en TMS › Operaciones › Tráfico: |
| 🔁 | `2_3_traceability-model.rst` | `2_3_traceability-model_01_trazabilidad.png` | Vista de Trazabilidad (tms.traceability) en Odoo. | TMS › Operaciones › Tráfico › Trazabilidad |

## Capítulo 3 — Arquitectura funcional

> Carpeta: `source/_static/img/3_functional-architecture/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `3_1_functional-organization.rst` | `3_1_functional-organization_01_menu-raiz.png` | Áreas funcionales del menú raíz de Guraify TMS. | Menú raíz: TMS, con las áreas TMS › **Operaciones**, TMS › **Administración**, |
| 🔁 | `3_2_1_orders.rst` | `3_2_1_orders_01_orden.png` | Formulario de una Orden (sale.order) con su estado operativo. | TMS › Operaciones › Tráfico › Órdenes |
| 🔁 | `3_2_1_orders.rst` | `3_2_1_orders_02_orden-bloqueada.png` | Orden bloqueada: candado cerrado tras confirmarse la ejecución. | TMS › Operaciones › Tráfico › Órdenes |
| 🔁 | `3_2_2_trips.rst` | `3_2_2_trips_01_viaje.png` | Formulario de un Viaje (tms.trip) con sus estados operativo, de compra y de facturación. | TMS › Operaciones › Tráfico › Viajes |
| 🔁 | `3_2_3_manifests.rst` | `3_2_3_manifests_01_manifiesto.png` | Formulario de un Manifiesto EDI (tms.edi.manifest) con sus estados y botones. | TMS › Operaciones › Tráfico › Manifiestos |
| ⬜ | `3_2_3_manifests.rst` | `3_2_3_manifests_02_botones-magicos.png` | Botones mágicos del Manifiesto: **Stops** y **Normalizar** (contactos pendientes). | TMS › Operaciones › Tráfico › Manifiestos |
| 🔁 | `3_2_4_api-inbox.rst` | `3_2_4_api-inbox_01_inbox.png` | Bandeja de entrada API (tms_int.api.inbox) con sus líneas y estados. | TMS › Operaciones › Tráfico › Bandeja de entrada API |
| 🔁 | `3_2_5_active-leg.rst` | `3_2_5_active-leg_01_tramo-activo.png` | Cabecera de una Orden multitramo mostrando los datos del tramo activo. | TMS › Operaciones › Tráfico › Órdenes (la cabecera de la Orden muestra los datos del |
| ⬜ | `3_3_planning-model.rst` | `3_3_planning-model_02_plan-disponibilidad.png` | Plan de Disponibilidad de Conductores: vista Gantt de *slots* (planning.slot). | TMS › Operaciones › Planificación (Plan Disponibilidad Conductores, Optimizador de Paradas) |
| 🔁 | `3_3_planning-model.rst` | `3_3_planning-model_01_optimizador.png` | Optimizador de Paradas (tms.optimizator) en Odoo. | TMS › Operaciones › Planificación (Plan Disponibilidad Conductores, Optimizador de Paradas) |
| 🔁 | `3_4_pricing-model.rst` | `3_4_pricing-model_01_tarifa.png` | Configuración de una Tarifa (tms.pricelist) en Odoo. | TMS › Configuración (Tarifas, Reglas, Productos) |

## Capítulo 4 — Parametrización

> Carpeta: `source/_static/img/4_parametrization/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_01_datos-auxiliares.png` | Panel "Datos auxiliares" en TMS › Configuración › Ajustes. | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_02_tipos-servicio-lista.png` | Lista de Tipos de Servicio (tms.service.type). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_03_tipos-servicio-form.png` | Formulario de un Tipo de Servicio con sus variables logísticas. | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_04_tipos-orden.png` | Lista de Tipos de Orden (tms.shipment.type). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_05_tipos-parada.png` | Lista de Tipos de Parada (tms.stop.type). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_06_tipos-destinatario.png` | Lista de Tipos de Destinatario (tms.receiper.type). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_07_tipos-transportista.png` | Lista de Tipos de Transportista (tms.carrier.type). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_08_tipos-reembolso.png` | Lista de Tipos de Reembolso (tms.cashvalue.type). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*), donde se gestionan los |
| ⬜ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_01_equipamientos.png` | Configuración de Equipamientos (tms.equipment). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*): Equipamientos |
| ⬜ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_02_vehiculos.png` | Modelos y Categorías de Vehículo (fleet.vehicle.model / fleet.vehicle.model.category). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*): Equipamientos |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_01_planes-transporte.png` | Configuración de un Plan de Transporte (tms.transport.plan). | TMS › Configuración: Planes de Transporte (``tms.transport.plan``), Zonas Geográficas |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_02_areas-geograficas.png` | Configuración de un Área Geográfica (tms.area). | TMS › Configuración: Planes de Transporte (``tms.transport.plan``), Zonas Geográficas |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_03_tiempos-servicio.png` | Configuración de Tiempos de Servicio (tms.service.time). | TMS › Configuración: Planes de Transporte (``tms.transport.plan``), Zonas Geográficas |
| ⬜ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_01_zonas-tarifarias.png` | Configuración de una Zona de tarifa (tms.pricelist.zone). | TMS › Configuración › Tarifas: Zonas de tarifa (``tms.pricelist.zone``), Tarifas Base |
| ⬜ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_02_tarifa.png` | Configuración de una Tarifa (tms.pricelist) y sus versiones. | TMS › Configuración › Tarifas: Zonas de tarifa (``tms.pricelist.zone``), Tarifas Base |
| ⬜ | `4_5_project-configuration.rst` | `4_5_project-configuration_01_proyecto.png` | Formulario de configuración de un Proyecto (project.project). | TMS › Configuración › Proyectos (el Proyecto, ``project.project``, extendido por el |
| ⬜ | `4_5_project-configuration.rst` | `4_5_project-configuration_02_kanban-proyectos.png` | Vista Kanban de Proyectos con sus KPIs e indicadores de configuración. | TMS › Configuración › Proyectos (el Proyecto, ``project.project``, extendido por el |
| ⬜ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_03_reglas-tarifa.png` | Formulario de una Regla de tarifa (unidad de medida): casillas Bultos/Cantidad/Metros/Pallets, Físico y dimensiones por defecto. | TMS › Configuración › Ajustes › Datos auxiliares › Regla de tarifa |
| ⬜ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_04_tipos-bulto.png` | Lista de Tipos de Bulto. | TMS › Configuración › Ajustes › Datos auxiliares › Tipos de Bulto |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_04_planning.png` | Formulario de un Planning: plan de transporte, tiempos de recogida/entrega y modo de división. | TMS › Configuración › Ajustes › Datos auxiliares › Planificaciones |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_05_franjas-horarias.png` | Lista de Franjas Horarias. | TMS › Configuración › Ajustes › Datos auxiliares › Franjas Horarias |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_06_horas-conduccion.png` | Formulario de un preset de Horas de Conducción (ajustes de secuenciación y optimización, pausas). | TMS › Configuración › Ajustes › Optimización de ruta › Horas de Conducción |
| ⬜ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_03_tarifa-base.png` | Lista de Tarifas Base con su tipo de cálculo. | TMS › Administración › Opciones de Tarifa › Tarifa Base |
| ⬜ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_04_linea-tarifa.png` | Una Línea de tarifa dentro de una versión, con sus condiciones arriba y la lista de detalles (zonas, rango, precio) debajo. | TMS › Administración › Opciones de Tarifa › Tarifa › pestaña Reglas Tarifa |
| ⬜ | `4_5_project-configuration.rst` | `4_5_project-configuration_03_otros-parametros.png` | Grupo Otros parámetros del Proyecto con los interruptores de automatización. | TMS › Configuración › Proyectos › pestaña TMS › Otros parámetros |
| ⬜ | `4_5_project-configuration.rst` | `4_5_project-configuration_04_app.png` | Grupo Aplicación móvil del Proyecto (perfil, POD digital, POD físico, escaneos). | TMS › Configuración › Proyectos › pestaña TMS › Aplicación móvil |

## Capítulo 5 — Flujos operativos

> Carpeta: `source/_static/img/5_operational-flows/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| ⬜ | `5_1_order-creation.rst` | `5_1_order-creation_01_orden-nueva.png` | Formulario de creación de una Orden (sale.order). | TMS › Operaciones › Tráfico › Órdenes (la Orden, ``sale.order``). |
| ⬜ | `5_1_order-creation.rst` | `5_1_order-creation_02_validar.png` | Botón **Validar** de la orden: valida y genera las Paradas. | TMS › Operaciones › Tráfico › Órdenes (la Orden, ``sale.order``). |
| ⬜ | `5_2_trip-generation.rst` | `5_2_trip-generation_01_generacion-viajes.png` | Generación de Viajes (tms.trip): asistente manual u optimizador PTV. | TMS › Operaciones › Planificación (Optimizador de Paradas) y TMS › Operaciones › Tráfico › Viajes (``tms.trip``). |
| ⬜ | `5_3_resource-assignment.rst` | `5_3_resource-assignment_01_recursos.png` | Viaje (tms.trip) con conductor, vehículo y transportista asignados. | TMS › Operaciones › Tráfico › Viajes (``tms.trip``). |
| ⬜ | `5_5_trip-closing.rst` | `5_5_trip-closing_01_cierre.png` | Viaje cerrado tras completarse sus paradas. | TMS › Operaciones › Tráfico › Viajes (``tms.trip``). |
| ⬜ | `5_6_settlement.rst` | `5_6_settlement_01_liquidacion.png` | Liquidación económica de venta (cliente) y de compra (transportista). | TMS › Administración (liquidación de venta y de compra). |
| ⬜ | `5_7_invoicing.rst` | `5_7_invoicing_01_factura.png` | Generación de la factura de cliente / proveedor (account.move). | TMS › Administración (facturación de cliente y de proveedor). |
| 🔁 | `5_8_kpi-indicators.rst` | `5_8_kpi-indicators_01_kpi-parada.png` | Indicador KPI en la lista de Paradas (triángulos de estado, barra de puntualidad y secuencia). | Columna de KPI en las listas de TMS › Operaciones › Tráfico › Órdenes y de las Paradas |
| 🔁 | `5_8_kpi-indicators.rst` | `5_8_kpi-indicators_02_kpi-orden.png` | Indicador KPI en la lista de Órdenes (parada activa + validación, factura/candado y POD). | Columna de KPI en las listas de TMS › Operaciones › Tráfico › Órdenes y de las Paradas |

## Capítulo 7 — Integraciones

> Carpeta: `source/_static/img/7_edi-integrations/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `7_1_integration-strategy.rst` | `7_1_integration-strategy_01_menu-edi.png` | Menú de configuración EDI en Odoo. | TMS › Configuración › EDI |
| ⬜ | `7_2_1_field-mapping.rst` | `7_2_1_field-mapping_01_lista-mapeos.png` | Mapeos de columnas de un fichero EDI. | TMS › Configuración › EDI › Definición de Fichero |
| ⬜ | `7_2_1_field-mapping.rst` | `7_2_1_field-mapping_02_selector-campo.png` | Catálogo de campos destino agrupado por entidad (selector *Tms Field*). | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_2_1_field-mapping.rst` | `7_2_1_field-mapping_03_parcel-array.png` | Configuración del campo computado Parcel_Array (*Computed* + *Apply Code?*). | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_2_2_python-transformations.rst` | `7_2_2_python-transformations_01_lista-funciones.png` | Catálogo de funciones preestablecidas. | TMS › Configuración › EDI › Funciones preestablecidas |
| ⬜ | `7_2_2_python-transformations.rst` | `7_2_2_python-transformations_02_funcion-detalle.png` | Detalle de una función preestablecida (descripción y código de ejemplo). | TMS › Configuración › EDI › Funciones preestablecidas |
| ⬜ | `7_2_file-import.rst` | `7_2_file-import_01_asistente.png` | Asistente de importación de fichero. | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_2_file-import.rst` | `7_2_file-import_02_validacion.png` | Reporte de validación del fichero importado. | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_3_api-integrations.rst` | `7_3_api-integrations_01_integracion.png` | Configuración de una integración API y su autenticación. | TMS › Configuración › EDI › Integraciones API |
| ⬜ | `7_3_api-integrations.rst` | `7_3_api-integrations_02_inbox.png` | Bandeja de entrada API con los estados de las líneas. | TMS › Configuración › EDI › Integraciones API |
| 🔁 | `7_4_endpoint-configuration.rst` | `7_4_endpoint-configuration_01_endpoint.png` | Configuración de un endpoint saliente. | TMS › Configuración › EDI › Endpoints API |
| ⬜ | `7_5_webhooks.rst` | `7_5_webhooks_01_endpoint-webhook.png` | Endpoint configurado como webhook. | TMS › Configuración › EDI › Endpoints API |
| ⬜ | `7_6_automated-actions.rst` | `7_6_automated-actions_01_crons.png` | Tareas programadas que orquestan las integraciones. | Ajustes › Técnico › Automatización › Acciones planificadas |
| ⬜ | `7_7_integration-best-practices.rst` | `7_7_integration-best-practices_01_api-log.png` | Registro de actividad de las APIs (tms.api.log). |  |

## Manual del conductor (cap. 10) — app móvil

> Carpeta: `source/_static/img/10_manual_app/`
>
> Todas se rehacen con una **ruta de prueba** (datos inventados). Son capturas del teléfono,
> sin recortar. Mismo nombre de fichero que la actual. Al hacer la tarea D11 del plan pueden
> cambiar algunos nombres; Paco avisará.

| Estado | Sección (.rst) | Fichero |
|---|---|---|
| 🔁 | `10_1_application-access.rst` | `10_1_application-access_01_activar-cuenta-step-1.png` |
| 🔁 | `10_1_application-access.rst` | `10_1_application-access_02_activar-cuenta-step-2.png` |
| 🔁 | `10_1_application-access.rst` | `10_1_application-access_03_login.png` |
| 🔁 | `10_2_route.rst` | `10_2_route_01_dashboard.png` |
| 🔁 | `10_2_route.rst` | `10_2_route_02_dashboard-header.png` |
| 🔁 | `10_2_route.rst` | `10_2_route_03_parada-card.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_01_parada-report-inicio.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_02_parada-report-botones-exito.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_03_orden-card.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_04_parada-footer.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_05_parada-acciones.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_06_parada-accion.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_07_parada-report-he-llegado.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_08_bultos-lista-scan-off.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_09_bulto-card.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_10_bultos-lista-scan-on.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_11_bultos-lista-footer.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_12_reembolso-step-1.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_13_reembolso-step-2.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_14_reporte-carga-1.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_15_reporte-carga-2.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_16_reporte-carga-3.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_17_reporte-entrega.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_18_reporte-entrega-4.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_19_scanmatrix-step-1.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_20_scanmatrix-step-2.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_21_scanmatrix-step-3.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_22_parada-report-pod-phisical-pre-scan.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_23_parada-report-pod-phisical-post-scan.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_24_parada-report-pre-sign-digital.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_25_parada-report-pod-digital-post-sign.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_26_img-1021.png` |
| 🔁 | `10_3_report.rst` | `10_3_report_27_img-1020.png` |

---

*Regenerada el 2026-09-08 (tarea D1). Se mantiene al día con `/capturas` y `/cerrar-tarea`.*
