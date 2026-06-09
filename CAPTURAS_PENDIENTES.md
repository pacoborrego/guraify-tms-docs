# Capturas pendientes — Documentación Guraify TMS

Lista de capturas de pantalla de la UI de Odoo que hay que insertar en la documentación
Sphinx. **Responsable: María.**

## Cómo trabajar esta lista

1. **Hacer la captura** navegando a la *Ruta en Odoo* indicada en cada fila.
2. **Guardar el PNG** en la carpeta de imágenes del capítulo (columna de cada bloque),
   con el *nombre de fichero* exacto de la columna correspondiente.
3. **Activar la imagen** en el `.rst` de destino: abre el fichero, busca el marcador
   `.. CAPTURA: <ID>` y **descomenta** el bloque `.. figure::` que hay justo debajo
   (quita la indentación que lo mantiene como comentario). El `figure` ya viene escrito
   con la ruta y el pie correctos.
4. **Compilar** para comprobar que se ve: `make html` y abrir `build/html/index.html`.
5. Marcar la fila como hecha (cambiar `⬜` por `✅`).

### Convenciones

- Carpeta: `source/_static/img/<slug-capítulo>/` (una por capítulo, p. ej.
  `source/_static/img/2_conceptual-model/` o `source/_static/img/7_edi-integrations/`).
- Nombre de fichero: `<sección>_<slug>_<NN>_<slug-captura>.png` (en minúsculas, sin
  espacios ni acentos). El nombre exacto está en cada fila.
- Formato: PNG. Recortar a la zona relevante de la pantalla; ocultar datos sensibles de
  clientes reales si los hubiera.
- Resolución recomendada: ancho ~1400–1600 px (legible sin pesar de más).
- La ruta raíz en todas las imágenes del `.rst` es absoluta desde `source/`:
  `/_static/img/<slug-capítulo>/...`.

---

## Capítulo 2 — Modelo Conceptual

> Carpeta de imágenes: `source/_static/img/2_conceptual-model/`
>
> Capítulo conceptual: solo llevan captura las secciones que tienen pantalla propia en
> Odoo (las entidades del modelo y la trazabilidad). Las secciones de diagrama (2.5, 2.6)
> y las puramente conceptuales no llevan captura.

| Estado | ID | Sección (.rst destino) | Qué capturar | Ruta en Odoo | Nombre del fichero PNG | Pie de figura |
|---|---|---|---|---|---|---|
| ⬜ | 2_1_01 | 2.1 Lógica estructural (`2_1_structural-logic.rst`) | Formulario de una Orden (datos de cliente, proyecto, tramos, líneas) | TMS › Operaciones › Tráfico › Órdenes | `2_1_structural-logic_01_orden.png` | Formulario de una Orden (`sale.order`) en Odoo. |
| ⬜ | 2_1_02 | 2.1 Lógica estructural (`2_1_structural-logic.rst`) | Formulario de un Viaje (paradas agrupadas, recurso asignado) | TMS › Operaciones › Tráfico › Viajes | `2_1_structural-logic_02_viaje.png` | Formulario de un Viaje (`tms.trip`) en Odoo. |
| ⬜ | 2_3_01 | 2.3 Trazabilidad (`2_3_traceability-model.rst`) | Vista de Trazabilidad con el histórico de eventos | TMS › Operaciones › Tráfico › Trazabilidad | `2_3_traceability-model_01_trazabilidad.png` | Vista de Trazabilidad (`tms.traceability`) en Odoo. |

---

## Capítulo 3 — Arquitectura Funcional

> Carpeta de imágenes: `source/_static/img/3_functional-architecture/`

| Estado | ID | Sección (.rst destino) | Qué capturar | Ruta en Odoo | Nombre del fichero PNG | Pie de figura |
|---|---|---|---|---|---|---|
| ⬜ | 3_1_01 | 3.1 Organización funcional (`3_1_functional-organization.rst`) | Menú raíz de TMS desplegado mostrando las cuatro áreas | TMS (menú raíz: Operaciones, Administración, Maestros, Configuración) | `3_1_functional-organization_01_menu-raiz.png` | Áreas funcionales del menú raíz de Guraify TMS. |
| ⬜ | 3_2_1_01 | 3.2.1 Órdenes (`3_2_1_orders.rst`) | Formulario de una Orden con su estado operativo (Oper State) | TMS › Operaciones › Tráfico › Órdenes | `3_2_1_orders_01_orden.png` | Formulario de una Orden (`sale.order`) con su estado operativo. |
| ⬜ | 3_2_1_02 | 3.2.1 Órdenes (`3_2_1_orders.rst`) | Orden bloqueada: candado cerrado tras confirmarse la ejecución | TMS › Operaciones › Tráfico › Órdenes › (una orden confirmada/bloqueada) | `3_2_1_orders_02_orden-bloqueada.png` | Orden bloqueada: candado cerrado tras confirmarse la ejecución. |
| ⬜ | 3_2_2_01 | 3.2.2 Viajes (`3_2_2_trips.rst`) | Formulario de un Viaje mostrando estado operativo, de compra (OC) y de facturación | TMS › Operaciones › Tráfico › Viajes | `3_2_2_trips_01_viaje.png` | Formulario de un Viaje (`tms.trip`) con sus tres estados. |
| ⬜ | 3_2_3_01 | 3.2.3 Manifiestos (`3_2_3_manifests.rst`) | Formulario de un Manifiesto EDI con su estado (open/in_queue/processing/closed) | TMS › Operaciones › Tráfico › Manifiestos | `3_2_3_manifests_01_manifiesto.png` | Formulario de un Manifiesto EDI (`tms.edi.manifest`) y su estado. |
| ⬜ | 3_2_4_01 | 3.2.4 API Inbox (`3_2_4_api-inbox.rst`) | Bandeja de Entrada API con sus líneas y estados (recibido/inválido/vinculado) | TMS › Operaciones › Tráfico › Bandeja de entrada API | `3_2_4_api-inbox_01_inbox.png` | Bandeja de Entrada API (`tms_int.api.inbox`) con sus líneas y estados. |
| ⬜ | 3_2_5_01 | 3.2.5 Tramo activo (`3_2_5_active-leg.rst`) | Cabecera de una Orden multitramo mostrando los datos del tramo activo (lugares/fechas/estado) | TMS › Operaciones › Tráfico › Órdenes › (orden con varios tramos) | `3_2_5_active-leg_01_tramo-activo.png` | Cabecera de una Orden multitramo mostrando los datos del tramo activo. |
| ⬜ | 3_3_01 | 3.3 Planificación (`3_3_planning-model.rst`) | Optimizador de Paradas | TMS › Operaciones › Planificación › Optimizador de Paradas | `3_3_planning-model_01_optimizador.png` | Optimizador de Paradas (`tms.optimizator`) en Odoo. |
| ⬜ | 3_4_01 | 3.4 Tarificación (`3_4_pricing-model.rst`) | Formulario de una Tarifa | TMS › Configuración › Tarifas | `3_4_pricing-model_01_tarifa.png` | Configuración de una Tarifa (`tms.pricelist`) en Odoo. |

---

## Capítulo 5 — Flujos Operativos

> Carpeta de imágenes: `source/_static/img/5_operational-flows/`
>
> (El cap. 5 está pendiente de revisión completa; de momento solo se listan las capturas
> de la sección de indicadores KPI.)

| Estado | ID | Sección (.rst destino) | Qué capturar | Ruta en Odoo | Nombre del fichero PNG | Pie de figura |
|---|---|---|---|---|---|---|
| ⬜ | 5_11_01 | Indicadores KPI (`5_11_kpi-indicators.rst`) | Columna KPI en la lista de Paradas (triángulos de estado + barra de puntualidad + secuencia) | TMS › Operaciones › Maestros operativos › Paradas | `5_11_kpi-indicators_01_kpi-parada.png` | Indicador KPI en la lista de Paradas. |
| ⬜ | 5_11_02 | Indicadores KPI (`5_11_kpi-indicators.rst`) | Columna KPI en la lista de Órdenes (badge compuesto: parada activa + validación/factura/candado/POD) | TMS › Operaciones › Tráfico › Órdenes | `5_11_kpi-indicators_02_kpi-orden.png` | Indicador KPI en la lista de Órdenes. |

---

## Capítulo 7 — EDI e Integraciones

> Carpeta de imágenes: `source/_static/img/7_edi-integrations/`

| Estado | ID | Sección (.rst destino) | Qué capturar | Ruta en Odoo | Nombre del fichero PNG | Pie de figura |
|---|---|---|---|---|---|---|
| ⬜ | 7_1_01 | 7.1 Estrategia (`7_1_integration-strategy.rst`) | Submenú EDI desplegado mostrando sus opciones | TMS › Configuración › EDI | `7_1_integration-strategy_01_menu-edi.png` | Menú de configuración EDI en Odoo. |
| ⬜ | 7_2_01 | 7.2 Importación (`7_2_file-import.rst`) | Asistente de importación con el fichero subido y el selector de formato | TMS › Configuración › EDI › Definición de Fichero › (asistente de importación) | `7_2_file-import_01_asistente.png` | Asistente de importación de fichero. |
| ⬜ | 7_2_02 | 7.2 Importación (`7_2_file-import.rst`) | Reporte de validación tras procesar (estados borrador→validado) | TMS › Configuración › EDI › Definición de Fichero › (asistente, log de validación) | `7_2_file-import_02_validacion.png` | Reporte de validación del fichero importado. |
| ⬜ | 7_2_1_01 | 7.2.1 Mapeo (`7_2_1_field-mapping.rst`) | Formulario de un fichero EDI con sus líneas de mapeo (columna → campo) | TMS › Configuración › EDI › Definición de Fichero | `7_2_1_field-mapping_01_lista-mapeos.png` | Mapeos de columnas de un fichero EDI. |
| ⬜ | 7_2_1_02 | 7.2.1 Mapeo (`7_2_1_field-mapping.rst`) | Desplegable del campo destino mostrando los grupos (TRIPS, SHIPMENTS, LEGS…) | TMS › Configuración › EDI › Definición de Fichero › (línea de mapeo, campo *Tms Field*) | `7_2_1_field-mapping_02_selector-campo.png` | Catálogo de campos destino agrupado por entidad. |
| ⬜ | 7_2_1_03 | 7.2.1 Mapeo (`7_2_1_field-mapping.rst`) | Mapeo computado de `Parcel_Array`: casillas *Computed* y *Apply Code?* + Python Code | TMS › Configuración › EDI › Definición de Fichero › (línea de mapeo, opciones de transformación) | `7_2_1_field-mapping_03_parcel-array.png` | Configuración del campo computado Parcel_Array. |
| ⬜ | 7_2_2_01 | 7.2.2 Transformaciones (`7_2_2_python-transformations.rst`) | Lista de funciones preestablecidas | TMS › Configuración › EDI › Funciones preestablecidas | `7_2_2_python-transformations_01_lista-funciones.png` | Catálogo de funciones preestablecidas. |
| ⬜ | 7_2_2_02 | 7.2.2 Transformaciones (`7_2_2_python-transformations.rst`) | Formulario de una función con descripción y código de ejemplo | TMS › Configuración › EDI › Funciones preestablecidas › (una función) | `7_2_2_python-transformations_02_funcion-detalle.png` | Detalle de una función preestablecida. |
| ⬜ | 7_3_01 | 7.3 Integraciones API (`7_3_api-integrations.rst`) | Formulario de Integración API con el selector de tipo de autenticación | TMS › Configuración › EDI › Integraciones API | `7_3_api-integrations_01_integracion.png` | Configuración de una integración API y su autenticación. |
| ⬜ | 7_3_02 | 7.3 Integraciones API (`7_3_api-integrations.rst`) | Bandeja de Entrada API con líneas y sus estados (recibido/inválido/vinculado) | TMS › Operaciones › Tráfico › Bandeja de entrada API | `7_3_api-integrations_02_inbox.png` | Bandeja de Entrada API con los estados de las líneas. |
| ⬜ | 7_4_01 | 7.4 Endpoints (`7_4_endpoint-configuration.rst`) | Formulario de Endpoint: método, ruta, plantillas Jinja y `send_mode`/`max_batch_size` | TMS › Configuración › EDI › Endpoints API | `7_4_endpoint-configuration_01_endpoint.png` | Configuración de un endpoint saliente. |
| ⬜ | 7_5_01 | 7.5 Webhooks (`7_5_webhooks.rst`) | Endpoint marcado como webhook: `is_webhook`, `webhook_route`, `webhook_secret` | TMS › Configuración › EDI › Endpoints API › (endpoint con *Is Webhook?*) | `7_5_webhooks_01_endpoint-webhook.png` | Endpoint configurado como webhook. |
| ⬜ | 7_6_01 | 7.6 Acciones Automáticas (`7_6_automated-actions.rst`) | Lista de tareas programadas (ir.cron) relacionadas con las integraciones | Ajustes › Técnico › Automatización › Acciones planificadas (filtrar TMS) | `7_6_automated-actions_01_crons.png` | Tareas programadas que orquestan las integraciones. |
| ⬜ | 7_7_01 | 7.7 Buenas Prácticas (`7_7_integration-best-practices.rst`) | Registro de actividad API (`tms.api.log`): entrada/salida, estado, código HTTP | (acción del modelo `tms.api.log`) | `7_7_integration-best-practices_01_api-log.png` | Registro de actividad de las APIs. |

---

*Última actualización: 2026-06-04. Cuando se migren los capítulos 6, 8 y 3.2, se añadirán
sus bloques siguiendo esta misma convención (manteniendo el orden por número de capítulo).*
