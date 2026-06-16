# Changelog — Documentación Guraify TMS

Registro de cambios de la documentación oficial. Formato basado en
[Keep a Changelog](https://keepachangelog.com/es/).

Convención de release: cada publicación se etiqueta con tag git `AAMMDD_VNN`
(p. ej. `260521_V01`) y se añade aquí su sección con el capítulo afectado y un resumen.

## [Sin publicar]

### Pendiente
- Insertar las capturas pendientes listadas en `CAPTURAS_PENDIENTES.md` (responsable: María).
- Portar cap. 6 Aplicación Móvil → `source/17.0/6_mobile-app/`.
- Portar cap. 8 Administración y Control Económico → `source/17.0/8_administration/`.
- Revisar caps. 4 y 5 (incl. warnings históricos y orden de títulos del cap. 5) y cap. 10.

---

## [260609_V01] — 2026-06-09

Primera publicación con control de versiones real (tag git). Recoge el portado del
capítulo 7 y la revisión de los capítulos 1–3 contra el estándar v2, además del contenido
de comportamiento del release de producto 260603_V05 (que no se había llegado a commitear).

### Añadido
- **Cap. 7 EDI e Integraciones** migrado a `source/17.0/7_edi-integrations/`: prosa
  final de 7.1 a 7.7 con subsecciones 7.2.1/7.2.2, y diagramas mermaid de flujo
  entrante (7.1) y saliente (7.4). Contenido redactado desde el código (`tms_int`),
  ya que el cap. 7 del Google Doc estaba vacío. Compila con 0 warnings nuevos.
  - Reestructurado tras revisión del propietario (2026-06-04): canales de entrada =
    fichero (XLSX/CSV), API REST (JSON), webhooks y alta manual — se elimina "EDI"
    como canal; la orquestación y la materialización pasan de 7.1 a 7.3 (solo aplican
    al camino de integración); Mapeo de Campos y Transformaciones Python se anidan
    bajo Importación de Ficheros como 7.2.1 y 7.2.2; el resto se renumera
    (7.3 Integraciones API, 7.4 Endpoints, 7.5 Webhooks, 7.6 Acciones Automáticas,
    7.7 Buenas Prácticas).
  - Discrepancia anotada: los guiones previos citaban modelos `tms.int.*`; el código
    define `tms_int.*` (guion bajo). Corregido en la prosa conforme a "manda el código".
  - 7.2.1 Mapeo de Campos ampliado: tabla del catálogo de campos destino (`field`)
    agrupada por entidad (Viaje, Expedición, Tramos, Líneas, Paquetes, Clientes,
    Transportistas, Conductores, Vehículos) con el significado de cada campo, extraída
    de la selección de `tms.edi.field.mapping`.
  - 7.2.1: nueva sección "El campo especial `Parcel_Array`" — mecanismo de campo
    computado (`is_computed` → `_Cmptd_Parcel_Array`, `apply_code` + `python_code`) que
    devuelve la lista de paquetes generada por código para clientes con 1 registro por
    expedición, con ejemplo de construcción de códigos de barras de etiquetas de origen.
  - 7.2.2 Transformaciones Python ampliado: un apartado por cada una de las 15
    funciones preestablecidas de `tms_int/data/tms_int_preset_function.xml` y guía de
    creación de funciones personalizadas (contrato `value`/`row`/`rows` → `result`).
  - Diagrama de 7.1 actualizado según el flujo Lucid del propietario (2026-06-04):
    decisión en el webhook (¿Orden? Sí → Bandeja de Entrada / No → creación-actualización
    de registros) y cadena Orden → Tramo → Cerrar Manifiesto o Validar Orden → Parada →
    Viaje. Prosa de 7.5 Webhooks ajustada en consecuencia.

### Añadido (continuación)
- **Rutas de UI en el cap. 7**: cada sección indica la ruta de Odoo (**Ruta:** TMS › …)
  extraída de los menús reales del módulo, para que el lector sepa dónde está la pantalla.
- **Capturas de pantalla (delegación)**: marcadores `.. CAPTURA: <id>` con un `.. figure::`
  comentado y listo para activar en cada punto del cap. 7, carpeta de imágenes
  `source/_static/img/7_edi-integrations/`, y lista de trabajo para el equipo en
  `CAPTURAS_PENDIENTES.md` (qué capturar, ruta UI, fichero destino, nombre del PNG y pie).

### Infraestructura de documentación
- **Estándar de portado v2** consolidado a partir del cap. 7 en `CLAUDE.md`: procedimiento
  por fases (esqueleto → contenido → UI/capturas → cierre), *Definición de Hecho*,
  catálogos desde el código, rutas de UI en español y convención de imágenes por capítulo.
- `REVISION_ESTANDAR.md`: checklist para auditar los capítulos ya hechos (1–5, 10) contra
  el estándar v2.
- `INSTRUCCIONES_PROYECTO_COWORK_snippet.md`: resumen del estándar para las instrucciones
  del proyecto Cowork.

### Añadido (continuación)
- **3.2.5 Tramo activo y Parada activa**: nueva subsección que explica por qué la cabecera
  de la Orden muestra siempre los datos de un único tramo (el activo). Documenta la cadena
  `active_leg` (`is_active`) → `active_stop` (calculada según tipo de tramo y estado de las
  paradas) → `active_trip`, con diagrama mermaid y un ejemplo de tramo directo donde la
  parada activa salta de carga a descarga al cerrarse. Enlazada desde 3.2.1 y referida por
  el KPI de Orden (cap. 5).
- **3.2.1 Órdenes** ampliado con los tres estados: operativo (`tms_status`),
  administrativo nativo (`state`) y de facturación nativo (`invoice_status`), y una
  sección de **bloqueo/desbloqueo** (botones Bloquear/Desbloquear, `locked`) con sus
  triggers automáticos (bloqueo al completar todas las paradas vía `action_confirm`;
  desbloqueo/reapertura al dejar de estarlo; protección de las órdenes facturadas).
- **3.2.2 Viajes**: nueva sección de **bloqueo/desbloqueo** sobre la orden de compra
  (`button_confirm`/`button_done` vs `button_unlock`), con sus triggers y la protección
  por facturación (`purchase_order_blocked`).
- **Indicadores KPI (SVG)** documentados en el cap. 5 (`5_11_kpi-indicators.rst`): el KPI
  de Parada (`stop_kpi_badge`: flujo, estado operativo por color, puntualidad y secuencia)
  y el de Orden (`so_kpi_badge`: KPI de la parada activa + validación, factura/candado y
  reclamación de POD), analizados desde el código. Referencia cruzada desde 3.2 y capturas
  pendientes (KPI parada, KPI orden y orden bloqueada).

### Planificación detallada (cap. 3) y enlaces desde el flujo
- **3.3.1 Disponibilidad de recursos** ampliado: el **Plan de Disponibilidad de
  Conductores** (slots ``planning.slot`` en vista Gantt) y qué define cada *slot*
  (conductor, vehículo, transportista, tarifa de compra, ventana temporal, planning).
- **3.3.2 Optimizador de Paradas** desarrollado como sección propia (la herramienta visual
  con **mapa** sobre `tms.optimizator`): niveles PTV, **modo por slot** y **modo por
  categoría**, requisitos previos y qué devuelve (viajes en borrador, ETAs, distancias,
  polilínea, mapa). En 5.2.4 (cap. 5) se deja un resumen que enlaza aquí, sin duplicar.
- 5.2.4.1 (Modo por slot) ahora indica dónde se crean los slots (Plan de Disponibilidad de
  Conductores) y enlaza a 3.3.1.

### Flujo operativo (cap. 5) redactado desde la óptica de usuario
- **5.1 Creación de Orden** reescrito con la narrativa del propietario: alta **manual**
  paso a paso (Nuevo → Cliente → autocarga/elección de Proyecto → Guardar → Tramos →
  líneas/reembolsos/info operativa → **Validar**) y alta **masiva por manifiesto**
  (Fichero EDI; con o sin cliente; o por integración API). El botón **Validar** se
  documenta como lo que es: valida **y genera las Paradas**.
- **Reestructuración del cap. 5**: la Validación y la Generación de Paradas se integran en
  **5.1.3** y se elimina la sección independiente de Tramos; el resto del capítulo se
  renumera (5.2 Viajes … 5.8 KPI) y se actualizan las referencias cruzadas. (Los ficheros
  obsoletos `5_2_leg-generation`, `5_3_stop-generation` y `5_4_order-validation` quedan
  como stubs `:orphan:` pendientes de `git rm`.)
- **3.2.3 Manifiestos ampliado**: pantalla y **botones mágicos** (Stops, Normalizar),
  **colas** de importación y cierre (tareas cada 5 min, forzado con "Validar e importar" /
  "Cerrar Manifiesto") y los **criterios de normalización** de contactos que bloquean el
  cierre (sin coordenadas, `tms_geo_score` < 80, geolocalización a nivel de código postal,
  o sin franjas horarias), verificados en el código.

### Revisado (estándar v2) — cap. 5
- **Cap. 5 Flujos Operativos** revisado y alineado. Era el capítulo más desordenado:
  - **Renombrados los 10 ficheros** para que el slug coincida con el contenido del flujo
    (p. ej. `5_4_trips.rst` → `5_4_order-validation.rst`, `5_10_exceptions-and-incidents.rst`
    → `5_10_invoicing.rst`); toctree actualizado. (No había contenido de excepciones/
    incidencias; el paso 10 es Facturación.)
  - **Warnings históricos resueltos** (build global ahora **0 warnings**): las tablas grid
    de los 10 ficheros convertidas a `list-table` (resueltas las 4 mal formadas de 5_2,
    5_5, 5_6 y 5_9) y corregida la estructura de 5_5 (un `^` que iba antes de un `~` y
    subrayados cortos).
  - **Numeración jerárquica** de títulos y subtítulos (5.1–5.11, 5.x.y.z), **rutas de UI**
    en español con modelos citados, y **10 marcadores de captura** (5.7 remite al cap. 10
    para las pantallas de la app). Registrado en `CAPTURAS_PENDIENTES.md`.

### Imágenes alineadas al estándar
- **Cap. 4 (4.1)**: las 8 imágenes que ya estaban embebidas (`Config_*` en
  `_static/images/`) se han migrado a `_static/img/4_parametrization/`, renombradas a la
  convención y convertidas de `.. image::` a `.. figure::` con `:alt:` y pie. El 4.1 queda
  totalmente ilustrado; marcadas como hechas en `CAPTURAS_PENDIENTES.md`.
- **Cap. 10 (Manual App)**: las 33 capturas existentes migradas de `_static/images/` a
  `_static/img/10_manual_app/` con la convención de nombres y rutas actualizadas (las
  sueltas como `.. figure::` con `:alt:`; las que van en celdas de tabla siguen como
  `.. image::` hasta la revisión de texto). Ningún `.rst` referencia ya la carpeta antigua
  `_static/images/` (quedan 7 imágenes huérfanas allí, pendientes de limpieza).

### Revisado (estándar v2)
- **Cap. 4 Parametrización** revisado y alineado: índice "4 Parametrización del Sistema";
  **numeración jerárquica completa** de los ~88 títulos y subtítulos (4.x, 4.x.y,
  4.x.y.z); **rutas de UI** (aviso "Ruta en Odoo" en español) por sección con los modelos
  citados (`tms.service.type`, `tms.stop.type`, `tms.equipment`, `tms.transport.plan`,
  `tms.area`, `tms.service.time`, `tms.pricelist*`, `project.project`…); y 11 marcadores
  de captura registrados en `CAPTURAS_PENDIENTES.md`.
  - **Warnings históricos resueltos** (build verde): las tablas *grid* de 4_3/4_4/4_5
    (26) convertidas a `list-table` —incluido el arreglo de las 2 tablas mal formadas—,
    el subtítulo "Campos principales" duplicado de 4_2 resuelto por la numeración, el
    encabezado "Tarifas" con sangría de 4_4 y la ancla pandoc `_section-25` de 4_1.
- **Cap. 3 Arquitectura Funcional** revisado y ampliado: títulos en español y numerados
  (`3 Arquitectura Funcional del Sistema`, secciones 3.1–3.5); arreglado el subtítulo
  "Maestros operativos" (le faltaba el subrayado); modelos citados; rutas de UI en cada
  sección y marcadores de captura; diagrama mermaid del árbol funcional en 3.1.
  - **3.2 ampliado**: nuevo modelo de datos operativo con 4 subficheros y sub-toctree —
    **3.2.1 Órdenes** (estado operativo calculado), **3.2.2 Viajes** (creación,
    secuenciación/routing, relación con la OC y estados en 3 dimensiones: `state` /
    `po_state` / `invoice_status`), **3.2.3 Manifiestos** (estados open→in_queue→
    processing→closed y materialización al cierre) y **3.2.4 API Inbox** (estados de
    línea received/invalid/linked y relación con el Manifiesto). Redactado desde el
    código `tms_suite`.
  - **3.3 Planificación**, **3.4 Tarificación** y **3.5 Integración** ampliados desde el
    código (3.5 remite al cap. 7 y al gateway, sin duplicar). Build sin warnings nuevos.
- **Cap. 2 Modelo Conceptual** alineado con el estándar: títulos en español y numerados
  (`2 Modelo Conceptual`, secciones `2.1`–`2.7`); modelos Odoo citados en 2.1
  (`sale.order`, `tms.shipment.leg`, `tms.stop`, `tms.trip`); limpieza de las 11 anclas
  de conversión pandoc; los diagramas de 2.5 (ingreso/coste) y 2.6 (modelo relacional)
  convertidos de imagen a `.. mermaid::`; y **redactada la conclusión 2.7**, que era una
  plantilla en inglés sin rellenar (fichero renombrado a `2_7_conclusion.rst`). Las
  imágenes `mi_imagen.png` y `modelo_relacional.png` quedan sin uso. Build sin warnings
  nuevos.
  - Añadidas **rutas de UI** (`.. admonition:: Ruta en Odoo`) en 2.1 y 2.3 con los menús
    reales en español (TMS › Operaciones › Tráfico › Órdenes / Viajes / Trazabilidad) y
    **3 marcadores de captura** (Orden, Viaje, Trazabilidad), registrados en
    `CAPTURAS_PENDIENTES.md`. Las secciones de diagrama (2.5, 2.6) y las puramente
    conceptuales no llevan captura.
- **Cap. 1 Introducción** alineado con el estándar: títulos en español y numerados
  (capítulo `1 Introducción`, secciones `1.1`–`1.5`); corregido el título erróneo de 1.1
  ("Organización funcional…" → "Propósito del documento") y la errata de 1.5 ("del
  sistemas" → "del sistema"); modelos Odoo citados en su primera mención
  (`sale.order`, `tms.shipment.leg`, `tms.stop`, `tms.trip`); diagrama `.. mermaid::` de
  arquitectura en 1.4; limpieza de anclas de conversión pandoc. Además, se restauraron
  las subsecciones "Parámetros…"/"Resultados…" de PTV bajo Secuenciación, que la
  conversión había dejado **sin título visible** (ahora en negrita, coherentes con las de
  Routing y OptiFlow). Build sin warnings nuevos.

---

## [260603_V05] — 2026-06-03

Documentación de la release de producto **260603_V05** (TMS Odoo 17, módulos
`tms` / `tms_int` / `tms_app`) — Remediación de rendimiento, Fase 1: alivio
inmediato + red de tests de caracterización. Validada en pruebas (0 fallos / 39 tests).

### Cambios de comportamiento documentados
- **Fecha administrativa (`order_date`)**: ahora es un campo calculado y estable,
  independiente de `date_order`, resuelto por la política `tms_admin_date_policy`
  del proyecto (creación / carga / descarga / cierre; por defecto cierre).
  Actualizado en `4_4_economic-configuration.rst` y `4_5_project-configuration.rst`.
- **Geocodificación no bloqueante**: al elegir un contacto sin coordenadas, el tramo
  muestra un aviso en vez de bloquear la interfaz con la petición HTTP de
  geolocalización. Actualizado en `5_2_shipments.rst`.

### Notas de la release de producto (no afectan a capítulos de la doc)
- QW-1 / QW-2: badges SVG (KPI) fuera de las listas de paradas y envíos; ocultos por
  defecto y reactivables en el selector de columnas.
- QW-10: eliminado código muerto; resuelto recálculo de zonas de carrier al asignar/
  cambiar viaje; definición duplicada de sincronización de carrier resuelta.
- Migración `name_get` → `display_name` (Odoo 17).
- Corrección de bloqueo (deadlock) con reintento de la petición.
- Red de tests de caracterización del núcleo (order / leg / trip / stop).

### Infraestructura de documentación
- `CLAUDE.md` ampliado con flujo de migración Drive → Sphinx, convenciones de portado
  y proceso de releases (Opción A).
- `MIGRACION.md`: roadmap de migración por capítulos (prioridad 7 → 6 → 8 → 3.2 ampliado).
- `CHANGELOG.md`: alta de este registro de cambios.

---

## [260521_V01] — 2026-05-21
- Estado de partida del repositorio (capítulos 1–5 y 10 en Sphinx). Marcador de
  release previo a la adopción formal de este changelog.
