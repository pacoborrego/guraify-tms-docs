# Capturas — lista de trabajo para María

Todas las capturas de la documentación hay que **rehacerlas** (las que existen) o **hacerlas**
(las que faltan). Motivo: las actuales son capturas a pantalla completa, con Odoo en inglés y,
en el caso de la app, con nombres, teléfonos y direcciones reales de destinatarios en un repo
público. Decisión de Paco, 2026-09-08.

## Requisitos de una captura válida

1. **Recorte**: solo la ventana de Odoo (o la zona relevante: un formulario, una lista, un
   menú). Sin barra de menús del Mac, sin dock, sin hora, sin pestañas ni barra de direcciones
   del navegador. En Windows, `Win+Shift+S` y arrastrar sobre la zona; en Mac, `Cmd+Shift+4`.
   El lote del 15/09 llegó a pantalla completa (pestañas, barra de direcciones y barra de
   tareas) y se recortó a mano; mejor recortar al capturar.
2. **Idioma de Odoo**: las capturas de Odoo se hacen con la interfaz **en inglés**, como se
   acordó el 12 de junio de 2026 (un mismo material para todos los mercados). El texto de la
   doc da las rutas de menú en español; la imagen las enseña en inglés y eso se asume. Las de
   la app del conductor van en español, que es como la usa el conductor.
3. **Sin datos reales**: ningún nombre de cliente, destinatario, conductor, teléfono,
   dirección, matrícula ni email real. Opciones, en este orden: usar una base de datos de
   demo; crear registros de prueba con nombres inventados; como último recurso, difuminar
   (pero el difuminado a mano se nota y deja rastros, mejor evitarlo). Las capturas de la app
   se hacen con una ruta de prueba, nunca con una ruta real.
   Difuminar con la herramienta acordada (nombres, referencias, direcciones, usuario de la
   esquina) vale: es lo que se ha hecho en el lote del 15/09 y ha quedado bien.
4. **Tamaño**: ancho entre 1400 y 1600 px para pantallas de Odoo; para la app, la captura
   nativa del teléfono. Formato PNG. Idealmente por debajo de 400 KB y **nunca por encima de
   500 KB** (si pesa más, pasarla por https://tinypng.com o similar). El cierre editorial (D12,
   2026-09-10) contó 18 capturas antiguas por encima de ese límite, todas del lote 🔁: al
   rehacerlas recortadas quedarán por debajo.
5. **Nombre de fichero**: exactamente el de la columna "Fichero" de las tablas de abajo, en la
   carpeta indicada. Si el nombre no coincide, la imagen no se muestra.

## Capturas automáticas (desde el 29/09/2026)

Las de Odoo se generan con `tools/capturas/capturas.py` (Playwright): abre cada pantalla de
`tools/capturas/manifest.json`, la recorta a la ventana de Odoo a 1600 px y la guarda con el nombre
exacto en `tools/capturas/raw/` (no se sube al repo: llevan datos reales). María solo tiene que
**anonimizar** las de `raw/` y dejarlas en `source/_static/img/<carpeta>/`. Cómo se usa, en
`tools/capturas/README.md`. Las 6 de la app se siguen haciendo en el teléfono.

## Cómo entregar

1. Guardar el PNG en `source/_static/img/<carpeta>/` con el nombre exacto.
2. Commit y push a la rama de trabajo acordada con Paco.
3. Avisar a Paco: él ejecuta `/capturas`, que activa las imágenes en el texto, comprueba los
   requisitos y actualiza esta lista. No hace falta tocar los `.rst`.

Estados: 🔁 existe pero hay que rehacerla · ⬜ no existe · ✅ hecha y validada.

**Decisión de Paco (29/09/2026):** las 61 antiguas marcadas 🔁 **quedan aplazadas**: no se rehacen
ahora, para poder cerrar. María hace solo las ⬜ (45, incluidas las 11 devueltas).

**Capturas automáticas sobre la demo (02/10/2026):** 20 generadas con `tools/capturas` contra
`tmsdemo.guraify.com` (datos inventados, sin anonimizar) y activadas.

**Lote del 15/09/2026** (revisado el 29/09): 28 imágenes entregadas; 17 validadas y activadas
(ocho de ellas renombradas porque el fichero llevaba el nombre de otra captura) y 11 que hay que
repetir, marcadas **Repetir (15/09)** con el motivo en su fila.


## Segunda ronda y app anonimizadas (14/10/2026)

Hechas: las 15 capturas de la app que estaban publicadas con datos reales, ya anonimizadas encima
(los originales, fuera de git en `tools/capturas/raw/10_manual_app_originales/`), y las 19 del lote
de la segunda ronda, anonimizadas y reducidas a 1600 px. Las del lote están marcadas ✅ en su
capítulo y sus figuras activas.

Quedan pendientes, para la demo cuando tenga P8: `3_2_2_trips_02_viajes-por-validar.png`,
`3_2_2_trips_03_revision.png` y `5_4_app-execution_02_despacho.png` (cerrar o despachar en la copia
| ⬜ | `3_2_2_trips.rst` | `3_2_2_trips_04_mapa.png` | Pestaña **Mapa** de un Viaje: la ruta calculada, las Paradas numeradas por orden y coloreadas por estado, y los hubs. | TMS › Operaciones › Tráfico › Viajes › un Viaje enrutado › pestaña Mapa (instancia local; no despachar ni cerrar nada) |
local llama a los sistemas reales).

## Conocer Guraify TMS (capa de producto)

> Carpeta: `source/_static/img/0_product-overview/`
>
> Estas páginas reutilizan además cuatro capturas de otros capítulos (Orden, Optimizador,
> pantalla principal de la app), que se actualizan solas cuando se rehagan las originales.

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| ✅ | `0_4_what-it-includes.rst` | `0_4_what-it-includes_01_tablero.png` | Tablero de operaciones: volumen, puntualidad y estado de las paradas del día. | TMS › Operaciones › Tableros (tablero de operaciones, con datos de demo) |

## Capítulo 2 — Modelo conceptual

> Carpeta: `source/_static/img/2_conceptual-model/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `2_1_structural-logic.rst` | `2_1_structural-logic_01_orden.png` | Formulario de una Orden en Odoo. | TMS › Operaciones › Tráfico › Órdenes |
| 🔁 | `2_1_structural-logic.rst` | `2_1_structural-logic_02_viaje.png` | Formulario de un Viaje en Odoo. | TMS › Operaciones › Tráfico › Viajes |
| 🔁 | `2_2_traceability-model.rst` | `2_3_traceability-model_01_trazabilidad.png` | Vista de Trazabilidad en Odoo. | TMS › Operaciones › Tráfico › Trazabilidad |

## Capítulo 3 — Arquitectura funcional

> Carpeta: `source/_static/img/3_functional-architecture/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `3_1_functional-organization.rst` | `3_1_functional-organization_01_menu-raiz.png` | Áreas funcionales del menú raíz de Guraify TMS. | Menú raíz: TMS, con las áreas TMS › **Operaciones**, TMS › **Administración**, |
| 🔁 | `3_2_1_orders.rst` | `3_2_1_orders_01_orden.png` | Formulario de una Orden (sale.order) con su estado operativo. | TMS › Operaciones › Tráfico › Órdenes |
| 🔁 | `3_2_1_orders.rst` | `3_2_1_orders_02_orden-bloqueada.png` | Orden bloqueada: candado cerrado tras confirmarse la ejecución. | TMS › Operaciones › Tráfico › Órdenes |
| 🔁 | `3_2_2_trips.rst` | `3_2_2_trips_01_viaje.png` | Formulario de un Viaje (tms.trip) con sus estados operativo, de compra y de facturación. | TMS › Operaciones › Tráfico › Viajes |
| ⬜ | `3_2_2_trips.rst` | `3_2_2_trips_02_viajes-por-validar.png` | Tráfico › Viajes por validar: los Viajes que esperan revisión, la más antigua primero (uno en rojo, de más de tres días). | TMS › Operaciones › Tráfico › Viajes por validar (usuario con permiso Validador de viajes) |
| ⬜ | `3_2_2_trips.rst` | `3_2_2_trips_03_revision.png` | Pestaña Revisión de un Viaje por validar: validación, rechazo y Órdenes sin prueba de entrega. | TMS › Operaciones › Tráfico › Viajes › pestaña Revisión (Viaje en Por validar) |
| 🔁 | `3_2_3_manifests.rst` | `3_2_3_manifests_01_manifiesto.png` | Formulario de un Manifiesto con sus estados y botones. | TMS › Operaciones › Tráfico › Manifiestos |
| ✅ | `3_2_3_manifests.rst` | `3_2_3_manifests_02_botones-inteligentes.png` | Botones inteligentes del Manifiesto: **Paradas**, **Normalizar** (contactos pendientes) y **Ficheros**. | TMS › Operaciones › Tráfico › Manifiestos |
| ✅ | `3_2_3_manifests.rst` | `3_2_3_manifests_03_fichero-error.png` | Lista de ficheros importados con uno en estado **Error** (en rojo). | TMS › Operaciones › Tráfico › Manifiestos › botón inteligente Ficheros (o la lista de ficheros importados) |
| ✅ | `3_2_6_legs-and-stops.rst` | `3_2_6_legs-and-stops_01_parada.png` | Formulario de una Parada con su Tipo de Parada, sus Tramos agrupados y su estado. | TMS › Operaciones › Maestros › Paradas |
| ✅ | `3_2_6_legs-and-stops.rst` | `3_2_6_legs-and-stops_02_envios-agencia.png` | Envíos a agencia (Agency Hand-overs): una fila por Parada enviada, con su Viaje, su agencia y su estado (activo / revertido). | TMS › Configuración › EDI › Envíos a agencia |
| ⬜ | `3_2_6_legs-and-stops.rst` | `3_2_6_legs-and-stops_03_adjuntos.png` | Pestaña **Adjuntos** de una Parada: la prueba de entrega que hizo el conductor (firma y foto del albarán). | TMS › Operaciones › Maestros › Paradas › una Parada entregada › pestaña Adjuntos. **Lleva datos reales** (nombre, DNI, albarán): anonimizar antes de publicar |
| 🔁 | `3_2_4_api-inbox.rst` | `3_2_4_api-inbox_01_inbox.png` | Bandeja de entrada API (tms_int.api.inbox) con sus líneas y estados. | TMS › Operaciones › Tráfico › Bandeja de entrada API |
| 🔁 | `3_2_5_active-leg.rst` | `3_2_5_active-leg_01_tramo-activo.png` | Cabecera de una Orden multitramo mostrando los datos del tramo activo. | TMS › Operaciones › Tráfico › Órdenes (la cabecera de la Orden muestra los datos del |
| ✅ | `3_3_planning-model.rst` | `3_3_planning-model_02_plan-disponibilidad.png` | Plan de Disponibilidad de Conductores: vista Gantt de *slots* (planning.slot). | TMS › Operaciones › Planificación (Plan Disponibilidad Conductores, Optimizador de Paradas) |
| 🔁 | `3_3_planning-model.rst` | `3_3_planning-model_01_optimizador.png` | Optimizador de Paradas (tms.optimizator) en Odoo. | TMS › Operaciones › Planificación (Plan Disponibilidad Conductores, Optimizador de Paradas) |
| 🔁 | `3_4_pricing-model.rst` | `3_4_pricing-model_01_tarifa.png` | Configuración de una Tarifa (tms.pricelist) en Odoo. | TMS › Configuración (Tarifas, Reglas, Productos) |

## Capítulo 4 — Parametrización

> Carpeta: `source/_static/img/4_parametrization/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_01_datos-auxiliares.png` | El bloque «Datos auxiliares» de TMS › Configuración › Ajustes, punto de entrada a los seis catálogos. | TMS › Configuración › Ajustes › Datos auxiliares |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_02_tipos-servicio-lista.png` | Lista de Tipos de Servicio: productos, Tipos de Orden compatibles y variables logísticas de cada uno. | TMS › Configuración › Ajustes › Datos auxiliares |
| ✅ | `4_1_operational-configuration.rst` | `4_1_operational-configuration_03_tipos-servicio-form.png` | Formulario de un Tipo de Servicio con sus variables logísticas. | TMS › Configuración › Ajustes › Datos auxiliares |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_04_tipos-orden.png` | Lista de Tipos de Orden: las cuatro marcas de comportamiento y los porcentajes de carga y descarga. | TMS › Configuración › Ajustes › Datos auxiliares |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_05_tipos-parada.png` | Lista de Tipos de Parada: seis registros, cada uno con una única marca activa. | TMS › Configuración › Ajustes › Datos auxiliares |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_06_tipos-destinatario.png` | Lista de Tipos de Destinatario. | TMS › Configuración › Ajustes › Datos auxiliares |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_07_tipos-transportista.png` | Lista de Tipos de Transportista. | TMS › Configuración › Ajustes › Datos auxiliares |
| 🔁 | `4_1_operational-configuration.rst` | `4_1_operational-configuration_08_tipos-reembolso.png` | Lista de Tipos de Reembolso. | TMS › Configuración › Ajustes › Datos auxiliares |
| ✅ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_01_equipamientos.png` | Configuración de Equipamientos (tms.equipment). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*): Equipamientos |
| ✅ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_02_vehiculos.png` | Modelos y Categorías de Vehículo (fleet.vehicle.model / fleet.vehicle.model.category). | TMS › Configuración › Ajustes (bloque *Datos auxiliares*): Equipamientos |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_01_planes-transporte.png` | Configuración de un Plan de Transporte (tms.transport.plan). | TMS › Configuración: Planes de Transporte (``tms.transport.plan``), Zonas Geográficas |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_02_areas-geograficas.png` | Configuración de un Área Geográfica (tms.area). | TMS › Configuración: Planes de Transporte (``tms.transport.plan``), Zonas Geográficas |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_03_tiempos-servicio.png` | Configuración de Tiempos de Servicio (tms.service.time). | TMS › Configuración: Planes de Transporte (``tms.transport.plan``), Zonas Geográficas |
| ✅ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_01_zonas-tarifarias.png` | Configuración de una Zona de tarifa (tms.pricelist.zone). | TMS › Configuración › Tarifas: Zonas de tarifa (``tms.pricelist.zone``), Tarifas Base |
| ✅ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_02_tarifa.png` | Configuración de una Tarifa (tms.pricelist) y sus versiones. | TMS › Configuración › Tarifas: Zonas de tarifa (``tms.pricelist.zone``), Tarifas Base |
| ✅ | `4_5_project-configuration.rst` | `4_5_project-configuration_01_proyecto.png` | Formulario de configuración de un Proyecto (project.project). | TMS › Configuración › Proyectos (el Proyecto, ``project.project``, extendido por el |
| ✅ | `4_5_project-configuration.rst` | `4_5_project-configuration_02_kanban-proyectos.png` | La kanban de Proyectos: cada tarjeta resume un contrato. | TMS › Configuración › Proyectos (el Proyecto, ``project.project``, extendido por el |
| ✅ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_03_reglas-tarifa.png` | Formulario de una Regla de tarifa (unidad de medida): casillas Bultos/Cantidad/Metros/Pallets, Físico y dimensiones por defecto. | TMS › Configuración › Ajustes › Datos auxiliares › Regla de tarifa |
| ✅ | `4_2_logistic-configuration.rst` | `4_2_logistic-configuration_04_tipos-bulto.png` | Lista de Tipos de Bulto. | TMS › Configuración › Ajustes › Datos auxiliares › Tipos de Bulto |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_04_planning.png` | Formulario de un Planning: plan de transporte, tiempos de recogida/entrega y modo de división. | TMS › Configuración › Ajustes › Datos auxiliares › Planificaciones |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_08_zbe.png` | Área geográfica de tipo **Bajas emisiones** (PTV07-ZBE ECO): polígono sobre el mapa, código y **Distintivo DGT mínimo**. | TMS › Configuración › Áreas Geográficas › un área de tipo Bajas emisiones (las `PTV07-` de la base local) |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_07_presets.png` | Lista **Presets de optimización** con los cuatro de serie y sus casillas por defecto. | TMS › Configuración › Presets de optimización |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_05_franjas-horarias.png` | Lista de Franjas Horarias. | TMS › Configuración › Ajustes › Datos auxiliares › Franjas Horarias |
| ✅ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_06_horas-conduccion.png` | Un perfil de jornada (Horas de Conducción) con sus ajustes para PTV. | TMS › Configuración › Ajustes › Optimización de ruta › Horas de Conducción |
| ✅ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_03_tarifa-base.png` | Lista de Tarifas Base con su tipo de cálculo. | TMS › Administración › Opciones de Tarifa › Tarifa Base |
| ✅ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_04_linea-tarifa.png` | Una Línea de tarifa dentro de una versión, con sus condiciones arriba y la lista de detalles (zonas, rango, precio) debajo. | TMS › Administración › Opciones de Tarifa › Tarifa › pestaña Reglas Tarifa |
| ✅ | `4_4_economic-configuration.rst` | `4_4_economic-configuration_05_linea-por-bulto.png` | Línea de tarifa con **Aplicar en = Línea de orden** y un detalle filtrado por **Tipos de bulto** con su precio unitario. | TMS › Configuración › Tarifas › una versión › Líneas de tarifa |
| ✅ | `4_5_project-configuration.rst` | `4_5_project-configuration_03_otros-parametros.png` | Grupo Otros parámetros del Proyecto con los interruptores de automatización. | TMS › Configuración › Proyectos › pestaña TMS › Otros parámetros |
| ⬜ | `4_5_project-configuration.rst` | `4_5_project-configuration_04_app.png` | **Repetir (15/09):** la entregada era la lista de Roles de la app; hace falta el grupo Aplicación móvil de la ficha del Proyecto. Grupo Aplicación móvil del Proyecto (perfil, POD digital, POD físico, escaneos). | TMS › Configuración › Proyectos › pestaña TMS › Aplicación móvil |
| ⬜ | `4_1_operational-configuration.rst` | `4_1_operational-configuration_09_marca.png` | La pestaña **Marca** de la compañía: logos, paleta de día y de noche, tipografía, dominio y remitente. | Ajustes › Usuarios y compañías › Compañías › la compañía › pestaña Marca (automática, instancia local) |
| ⬜ | `4_1_operational-configuration.rst` | `4_1_operational-configuration_10_contacto-hub.png` | La pestaña Propiedades TMS de un hub: sus marcas, la información de acceso y la geolocalización. | TMS › Maestros › Operaciones › Hubs › un hub › pestaña Propiedades TMS (empresa: sin datos personales) |
| ⬜ | `4_1_operational-configuration.rst` | `4_1_operational-configuration_11_usuario-roles.png` | El usuario de un conductor con su rol de la app. | Ajustes › Usuarios › un usuario de prueba con el rol Repartidor (o anonimizar nombre y correo) |
| ⬜ | `4_1_operational-configuration.rst` | `4_1_operational-configuration_12_tokens.png` | Tokens de dispositivo: un teléfono por fila, con su versión de la app y su último uso. | TMS › Configuración › App › Tokens de dispositivo. **Lleva nombres de conductores**: anonimizar; no pulsar Revocar |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_09_proveedores-geo.png` | Bloque **Proveedores geo** de Ajustes: qué servicio hace cada proceso para la compañía activa. | TMS › Configuración › Ajustes › Proveedores geo (automática, instancia local) |
| ⬜ | `4_3_planning-configuration.rst` | `4_3_planning-configuration_10_politica-operativa.png` | Ficha de una **política operativa**: recálculo de ETA, resultados del routing, enriquecimiento, geocercas, alarmas y privacidad. | TMS › Configuración › Ajustes › Operación › Políticas operativas (si no hay ninguna, crear la de la compañía con los valores por defecto) |
| ⬜ | `4_5_project-configuration.rst` | `4_5_project-configuration_05_operacion.png` | Pestaña **Operación** del Proyecto: coste de subcontratación por defecto y política operativa propia. | TMS › Configuración › Proyectos › un Proyecto › pestaña Operación (usuario responsable; automática, instancia local) |

## Capítulo 5 — Flujos operativos

> Carpeta: `source/_static/img/5_operational-flows/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| ✅ | `5_1_order-creation.rst` | `5_1_order-creation_01_orden-nueva.png` | Formulario de creación de una Orden (sale.order). | TMS › Operaciones › Tráfico › Órdenes (la Orden, ``sale.order``). |
| ⬜ | `5_1_order-creation.rst` | `5_1_order-creation_02_validar.png` | **Repetir (15/09):** la entregada era la ficha de una Orden en borrador (se ha usado como 5_1_01); hace falta la Orden con el botón Validar a la vista. Botón **Validar** de la orden: valida y genera las Paradas. | TMS › Operaciones › Tráfico › Órdenes (la Orden, ``sale.order``). |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_01_generacion-viajes.png` | Generación de Viajes: asistente manual u Optimizador de Paradas. | TMS › Operaciones › Planning › Optimizador de Paradas y TMS › Operaciones › Tráfico › Viajes (``tms.trip``). |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_02_asignar-nuevo.png` | Asistente Asignar en modo **Nuevo**: campos a la izquierda (conductor, vehículo, categoría, transportista, tarifa, Planning, servicios, hubs), lista de Paradas y mapa a la derecha. | Lista de Órdenes › seleccionar varias › **Asignar** |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_03_asignar-existente.png` | Asistente Asignar en modo **Existente**: los Viajes de esas fechas dibujados en el mapa y la ficha de uno con «Elegir este viaje». | Lista de Órdenes › **Asignar** › Modo Existente › pulsar una ruta del mapa |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_04_paradas-sin-hub.png` | Diálogo **Paradas sin hub** con «Aplicar a todas» y «Guardar y continuar». | Lista de Órdenes › **Asignar** › Ejecutar con una Parada sin hub |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_05_asignar-optimizacion.png` | Asistente Asignar en modo **Optimización**: categorías de vehículo disponibles (cantidad, hub y ventana de salida) y el bloque del motor (preset, casillas). | Lista de Órdenes › **Asignar** › Modo Optimización |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_06_secuenciar.png` | Diálogo **Secuenciar viajes**: Secuenciar todo, Mantener orden relativo, tolerancia y «Qué se puede violar». | Viaje planificado › botón Secuenciar Viaje |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_07_aplicar-plan.png` | Diálogo de progreso con el plan listo: Paradas por estado de ventana, excluidas y violaciones, y el botón **Aplicar plan**. | Lista de Órdenes › Asignar › Optimización › Ejecutar (esperar a que termine) |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_08_encontrar-ruta.png` | Asistente **Encontrar ruta**: Órdenes, rutas candidatas, Mantener / Romper estructura, preset y lo que se puede violar. | Lista de Órdenes › Acción › Encontrar ruta (datos `PTV10-` de la base local) |
| ✅ | `5_2_trip-generation.rst` | `5_2_trip-generation_09_candidatas.png` | Ejecución de Encontrar ruta en **Propuesta lista**, pestaña Órdenes: por Orden, la ruta elegida con sus diferencias. | TMS › Operaciones › Planning › Encontrar ruta › una ejecución |
| ⬜ | `5_2_trip-generation.rst` | `5_2_trip-generation_10_paradas-sin-planificar.png` | Paradas sin planificar: cada Parada que acabó sin ruta, con su origen y su motivo. | TMS › Operaciones › Planning › Ejecuciones de optimización › una con Paradas sin planificar › pestaña. **Lleva nombres y direcciones**: anonimizar; no pulsar Aplicar plan ni Revertir |
| ✅ | `5_4_app-execution.rst` | `5_4_app-execution_03_registrar-trazabilidad.png` | Asistente **Registrar trazabilidad** de un Bulto: evento, Parada, fecha, resultado y motivo. | TMS › Operaciones › Maestros › Bultos › un Bulto › Registrar trazabilidad |
| ⬜ | `5_4_app-execution.rst` | `5_4_app-execution_04_eta-y-ruta.png` | Pestaña **ETA y ruta** de un Viaje: el último recálculo, la ruta de PTV, peajes, coste, violaciones y emisiones. | TMS › Operaciones › Tráfico › Viajes › un Viaje enrutado › pestaña ETA y ruta (instancia local; no pulsar Recalcular ETA ahora) |
| ✅ | `5_9_labels.rst` | `5_9_labels_01_generar-etiquetas.png` | Asistente **Generar etiquetas** desde un Viaje: formato de salida, tamaño, diseño, impresora y orden del lote. | TMS › Operaciones › Tráfico › Viajes › Acción › Generar etiquetas |
| ✅ | `5_3_resource-assignment.rst` | `5_3_resource-assignment_01_recursos.png` | Viaje (tms.trip) con conductor, vehículo y transportista asignados. | TMS › Operaciones › Tráfico › Viajes (``tms.trip``). |
| ✅ | `5_5_trip-closing.rst` | `5_5_trip-closing_01_cierre.png` | Viaje cerrado tras completarse sus paradas. | TMS › Operaciones › Tráfico › Viajes (``tms.trip``). |
| ✅ | `5_4_app-execution.rst` | `5_4_app-execution_01_paradas-estado-app.png` | Las Paradas en Odoo con el estado que llega desde la app (columna de estado de la app). | TMS › Operaciones › Maestros › Paradas |
| ⬜ | `5_4_app-execution.rst` | `5_4_app-execution_02_despacho.png` | Un Viaje despachado: el botón Reenviar y el grupo Despacho con fecha, canal y resultado. | TMS › Operaciones › Tráfico › Viajes (Viaje en Despachado) |
| ✅ | `5_6_settlement.rst` | `5_6_settlement_01_liquidacion.png` | Tarificación de venta (cliente) y de compra (transportista). | Botón Tarificar en la Orden y en el Viaje. |
| ⬜ | `5_7_invoicing.rst` | `5_7_invoicing_01_factura.png` | **Repetir (15/09):** la entregada era la Lista de facturas casi vacía (una fila); hace falta la pantalla de crear la factura desde la Orden o el Viaje. Generación de la factura al cliente y de la factura del transportista. | TMS › Administración (facturación de cliente y de proveedor). |
| 🔁 | `5_8_kpi-indicators.rst` | `5_8_kpi-indicators_01_kpi-parada.png` | Indicador KPI en la lista de Paradas (triángulos de estado, barra de puntualidad y secuencia). | Columna de KPI en las listas de TMS › Operaciones › Tráfico › Órdenes y de las Paradas |
| 🔁 | `5_8_kpi-indicators.rst` | `5_8_kpi-indicators_02_kpi-orden.png` | Indicador KPI en la lista de Órdenes (parada activa + validación, factura/candado y POD). | Columna de KPI en las listas de TMS › Operaciones › Tráfico › Órdenes y de las Paradas |

## Capítulo 7 — Integraciones

> Carpeta: `source/_static/img/7_edi-integrations/`

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| 🔁 | `7_1_integration-strategy.rst` | `7_1_integration-strategy_01_menu-edi.png` | Menú de configuración EDI en Odoo. | TMS › Configuración › EDI |
| ✅ | `7_2_1_field-mapping.rst` | `7_2_1_field-mapping_01_lista-mapeos.png` | Mapeos de columnas de un fichero EDI. | TMS › Configuración › EDI › Definición de Fichero |
| ⬜ | `7_2_1_field-mapping.rst` | `7_2_1_field-mapping_02_selector-campo.png` | **Repetir (15/09):** la entregada era la lista de Definiciones de fichero, y además se veían nombres de clientes reales en las definiciones (no publicable); hace falta el desplegable del campo destino (Tms Field) abierto. Catálogo de campos destino agrupado por entidad (selector *Tms Field*). | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_2_1_field-mapping.rst` | `7_2_1_field-mapping_03_parcel-array.png` | Configuración del campo computado Parcel_Array (*Computed* + *Apply Code?*). | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_2_2_python-transformations.rst` | `7_2_2_python-transformations_01_lista-funciones.png` | Catálogo de funciones preestablecidas. | TMS › Configuración › EDI › Funciones preestablecidas |
| ✅ | `7_2_2_python-transformations.rst` | `7_2_2_python-transformations_02_funcion-detalle.png` | Detalle de una función preestablecida (descripción y código de ejemplo). | TMS › Configuración › EDI › Funciones preestablecidas |
| ✅ | `7_2_file-import.rst` | `7_2_file-import_01_asistente.png` | Asistente de importación de fichero. | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_2_file-import.rst` | `7_2_file-import_02_validacion.png` | Reporte de validación del fichero importado. | TMS › Configuración › EDI › Definición de Fichero |
| 🔁 | `7_3_api-integrations.rst` | `7_3_api-integrations_01_integracion.png` | Configuración de una integración API y su autenticación. | TMS › Configuración › EDI › Integraciones API |
| ✅ | `7_3_api-integrations.rst` | `7_3_api-integrations_02_inbox.png` | Bandeja de entrada API con los estados de las líneas. | TMS › Configuración › EDI › Integraciones API |
| 🔁 | `7_4_endpoint-configuration.rst` | `7_4_endpoint-configuration_01_endpoint.png` | Configuración de un endpoint saliente. | TMS › Configuración › EDI › Endpoints API |
| ⬜ | `7_5_webhooks.rst` | `7_5_webhooks_01_endpoint-webhook.png` | Endpoint configurado como webhook. | TMS › Configuración › EDI › Endpoints API |
| ✅ | `7_6_automated-actions.rst` | `7_6_automated-actions_01_crons.png` | Tareas programadas que orquestan las integraciones. | Ajustes › Técnico › Automatización › Acciones planificadas |
| ✅ | `7_7_integration-best-practices.rst` | `7_7_integration-best-practices_01_api-log.png` | Registro de actividad de las APIs (tms.api.log). |  |
| ⬜ | `7_8_telematics.rst` | `7_8_telematics_01_proveedor.png` | El proveedor «app del conductor», el que viene de serie, con su mapeo de la posición. | TMS › Configuración › Telemática › Proveedores › app del conductor (automática, instancia local) |
| ⬜ | `7_9_external-access.rst` | `7_9_external-access_01_politica-campos.png` | Política de campos del portal: qué campo de qué modelo se enseña a cada audiencia. | TMS › Configuración › Ajustes › Audiencias externas › Política de campos del portal (automática, instancia local) |

## Gestión de Recursos (cap. 6)

> Carpeta: `source/_static/img/6_resources/`
>
> **Aviso (D12, 2026-09-10)**: los módulos `tms_resources` y `tms_maintenance` no tienen traducción
> al español todavía, así que sus pestañas, botones y filtros salen en inglés («Odometer (TMS)»,
> «Maintenance (TMS)», «Bulk Preventive Service»…). Mejor hacer estas capturas cuando exista el
> `es.po` de los dos módulos (tarea anotada en `PLAN.md`); si urge, se aceptan en inglés.
>
> Odoo en español, unidades de prueba (matrículas inventadas), sin datos reales del cliente.

| Estado | Fichero .rst | Fichero | Qué muestra | Dónde |
|---|---|---|---|---|
| ⬜ | `6_1_area.rst` | `6_1_area_01_menu.png` | El menú Gestión de Recursos desplegado con sus cuatro bloques. | Menú raíz Gestión de Recursos |
| ⬜ | `6_2_odometer.rst` | `6_2_odometer_01_pestana-vehiculo.png` | Pestaña Odometer (TMS) de un vehículo: lectura actual, origen, antigüedad, km/día. | TMS › Maestros › Equipos › Vehículos › ficha › pestaña Odometer (TMS) |
| ⬜ | `6_2_odometer.rst` | `6_2_odometer_02_anomalias.png` | Pantalla Odometer Anomalies con lecturas en borrador agrupadas por vehículo. | Gestión de Recursos › Configuración › Odometer Anomalies |
| ⬜ | `6_3_maintenance-model.rst` | `6_3_maintenance-model_01_orden-trabajo.png` | Formulario de una orden de trabajo con vehículo, trabajo, tarea, odómetro y etapa. | Gestión de Recursos › Mantenimiento › Órdenes de trabajo |
| ⬜ | `6_3_maintenance-model.rst` | `6_3_maintenance-model_02_pestana-mantenimiento.png` | Pestaña Maintenance (TMS) del vehículo: control de service, fiabilidad, reglas y órdenes. | Ficha del vehículo › pestaña Maintenance (TMS) |
| ⬜ | `6_4_preventive-rules.rst` | `6_4_preventive-rules_01_reglas.png` | Lista de Reglas de preventivo con semáforo, restante y confianza. | Gestión de Recursos › Mantenimiento › Reglas de preventivo |
| ⬜ | `6_4_preventive-rules.rst` | `6_4_preventive-rules_02_control-service.png` | Pantalla Control de service con los dos niveles por unidad. | Gestión de Recursos › Mantenimiento › Control de service |
| ⬜ | `6_5_workshop-flows.rst` | `6_5_workshop-flows_01_cerrar-orden.png` | Asistente Close Order con fecha y kilometraje. | Orden de trabajo › botón Close Order |
| ⬜ | `6_5_workshop-flows.rst` | `6_5_workshop-flows_02_carga-masiva.png` | Asistente Carga masiva de service con las reglas marcadas. | Gestión de Recursos › Mantenimiento › Carga masiva de service |
| ⬜ | `6_6_outputs.rst` | `6_6_outputs_01_orden-impresa.png` | El PDF de la orden de trabajo impresa. | Ficha del vehículo › Print Work Order |
| ⬜ | `6_6_outputs.rst` | `6_6_outputs_02_copiar-estado.png` | Ventana Copy Workshop Status con el texto WhatsApp y el botón de copiar. | Ficha del vehículo › Copy Workshop Status |
| ⬜ | `6_6_outputs.rst` | `6_6_outputs_03_rankings.png` | Asistente Rankings de objetivos con el texto generado. | Gestión de Recursos › Mantenimiento › Rankings de objetivos |
| ⬜ | `6_7_kpis.rst` | `6_7_kpis_01_indicadores.png` | Lista de Indicadores de mantenimiento con sus valores. | Gestión de Recursos › Mantenimiento › Indicadores |

## DeCA (cap. 9)

> Carpeta: `source/_static/img/9_deca/`. Se capturan contra `Etransport_260908_deca` (local, Odoo en inglés); llevan datos reales: pasan por María.

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| ✅ | `9_2_configuration.rst` | `9_2_configuration_01_ficha-proyecto.png` | Pestaña **DeCA** de un Proyecto con la ficha activa: cargador, transportista efectivo, disparador, agrupación y envío. | TMS › Operaciones › Proyectos › un Proyecto con DeCA por proyecto › pestaña DeCA (usuario Responsable DeCA) |
| ✅ | `9_4_lifecycle.rst` | `9_4_lifecycle_01_documentos.png` | Lista **Documentos** DeCA: referencia, transportista, fecha, estado (alguno emitido, alguno modificado) y URL activa. | TMS › Operaciones › DeCA › Documentos |
| ✅ | `9_4_lifecycle.rst` | `9_4_lifecycle_02_documento-emitido.png` | Ficha de un DeCA **emitido**: cargador, transportista, vehículo, líneas, URL pública y los botones Revisar, Anular DeCA y Emitir nuevo desde este. | TMS › Operaciones › DeCA › Documentos › uno emitido |
| ✅ | `9_5_outputs.rst` | `9_5_outputs_01_pdf.png` | El **PDF** de un DeCA emitido: datos del transporte, QR, cargador, transportista y las expediciones (primera página, en el visor). | Botón Descargar PDF de un DeCA emitido (a mano, desde el visor de PDF) |

## Avisos al Destinatario (cap. 11)

> Carpeta: `source/_static/img/11_notifications/`. Sobre la base local (copia de producción): **no
> guardar ningún flujo activo ni pulsar Probar credenciales**; las que llevan datos reales pasan por
> anonimizar.

| Estado | Sección (.rst) | Fichero | Qué se ve (pie de figura) | Ruta en Odoo |
|---|---|---|---|---|
| ⬜ | `11_2_channels.rst` | `11_2_channels_01_esendex.png` | Enviar SMS con Esendex: cuenta, usuario, contraseña de la API, remitente y prueba de las credenciales. | Ajustes › Ajustes generales › Contactos › Enviar SMS › Send via Esendex (tapar referencia de cuenta y usuario si son reales) |
| ⬜ | `11_3_workflows.rst` | `11_3_workflows_01_flujo.png` | Un flujo de aviso: cuándo, a quién, por qué canal y con qué límites. | TMS › Configuración › Avisos › Workflows › Nuevo, rellenado y **sin guardar** |
| ⬜ | `11_4_recipient.rst` | `11_4_recipient_01_avisos.png` | El grupo AVISOS de un contacto: canal preferido, idioma y consentimientos. | Contacto › Propiedades TMS › AVISOS (contacto inventado o anonimizado) |
| ⬜ | `11_5_following.rst` | `11_5_following_01_pestana-avisos.png` | La pestaña Avisos de la Orden: qué se dijo, a quién, por qué canal y cómo acabó. | Orden › pestaña Avisos. **Lleva datos reales**: anonimizar |

## Administración y Control Económico (cap. 8)

> Carpeta: `source/_static/img/8_economic-administration/`
>
> Odoo en español, datos de demo, sin importes ni nombres reales de clientes o transportistas.

| Estado | Fichero .rst | Fichero | Qué muestra | Dónde |
|---|---|---|---|---|
| ✅ | `8_1_active-passive-margin.rst` | `8_1_active-passive-margin_01_viaje.png` | Lista de Viajes con las columnas Activo, Pasivo, Beneficio y Margen %. | TMS › Operaciones › Tráfico › Viajes |
| ⬜ | `8_4_purchase-orders.rst` | `8_4_purchase-orders_01_oc.png` | Orden de compra de un Viaje: línea de sección con la ruta y líneas por parada. | Viaje › botón inteligente de la orden de compra |
| ✅ | `8_6_refunds.rst` | `8_6_refunds_01_lista.png` | Lista de Reembolsos con importe, cobrado, ingresado, pagado, saldos y estado. | TMS › Administración › Reembolsos |
| ✅ | `8_8_control-reporting.rst` | `8_8_control-reporting_01_kpis.png` | Lista de KPIs del motor de indicadores con sección, formato y audiencias. | TMS › Métricas › KPIs |
| ✅ | `8_8_control-reporting.rst` | `8_8_control-reporting_02_tablero.png` | Tablero Pending Invoicing. | TMS › Operaciones › Tableros › Pending Invoicing |

## Manual del conductor (cap. 10) — app móvil

> Carpeta: `source/_static/img/10_manual_app/`
>
> Todas se rehacen con una **ruta de prueba** (datos inventados). Son capturas del teléfono,
> sin recortar. **Los nombres de fichero no cambian** aunque en D11 (2026-09-10) el capítulo se
> haya dividido en ocho páginas: las imágenes `10_3_report_NN` se usan ahora desde 10.3 a 10.7 y
> conservan su nombre para no chocar con el lote que María ya ha preparado. Las nuevas llevan el
> prefijo de su página.

| Estado | Sección (.rst) | Fichero | Qué muestra |
|---|---|---|---|
| 🔁 | `10_1_application-access.rst` | `10_1_application-access_01_activar-cuenta-step-1.png` | Correo de invitación con el botón Activar cuenta |
| 🔁 | `10_1_application-access.rst` | `10_1_application-access_02_activar-cuenta-step-2.png` | Pantalla de crear contraseña |
| 🔁 | `10_1_application-access.rst` | `10_1_application-access_03_login.png` | Pantalla de entrada: Dominio, correo, contraseña, botón ACCESO |
| 🔁 | `10_2_route.rst` | `10_2_route_01_dashboard.png` | Panel con la ruta y las paradas |
| 🔁 | `10_2_route.rst` | `10_2_route_02_dashboard-header.png` | Cabecera de la ruta |
| 🔁 | `10_2_route.rst` | `10_2_route_03_parada-card.png` | Tarjeta de una parada |
| ⬜ | `10_2_route.rst` | `10_2_route_04_pestanas.png` | Barra inferior con las cuatro pestañas del conductor (Panel, Mapas, Chat, Perfil): usuario con el rol de conductor, sin el de almacén |
| 🔁 | `10_3_stop.rst` | `10_3_report_01_parada-report-inicio.png` | Pantalla de la parada con el botón Inicio |
| 🔁 | `10_3_stop.rst` | `10_3_report_02_parada-report-botones-exito.png` | Los tres botones de resultado: Hecho, Con Reservas, Cancelado |
| 🔁 | `10_3_stop.rst` | `10_3_report_03_orden-card.png` | Tarjeta de una orden |
| 🔁 | `10_3_stop.rst` | `10_3_report_04_parada-footer.png` | Pie de la parada: navegar, botón central, escáner y menú |
| 🔁 | `10_3_stop.rst` | `10_3_report_05_parada-acciones.png` | Menú de tres puntos con Reiniciar |
| 🔁 | `10_3_stop.rst` | `10_3_report_06_parada-accion.png` | Confirmación de Reiniciar |
| 🔁 | `10_3_stop.rst` | `10_3_report_07_parada-report-he-llegado.png` | Parada con el botón He Llegado |
| 🔁 | `10_4_delivery.rst` | `10_3_report_19_scanmatrix-step-1.png` | Encontrar bultos: cámara sobre las etiquetas |
| 🔁 | `10_4_delivery.rst` | `10_3_report_20_scanmatrix-step-2.png` | Encontrar bultos: los de la parada en verde |
| 🔁 | `10_4_delivery.rst` | `10_3_report_21_scanmatrix-step-3.png` | Encontrar bultos: contador |
| 🔁 | `10_4_delivery.rst` | `10_3_report_08_bultos-lista-scan-off.png` | Comprobar bultos: la lista |
| 🔁 | `10_4_delivery.rst` | `10_3_report_09_bulto-card.png` | Tarjeta de un bulto |
| 🔁 | `10_4_delivery.rst` | `10_3_report_10_bultos-lista-scan-on.png` | Comprobar bultos con el escáner activo |
| 🔁 | `10_4_delivery.rst` | `10_3_report_11_bultos-lista-footer.png` | Contador de bultos y botón Siguiente |
| 🔁 | `10_4_delivery.rst` | `10_3_report_22_parada-report-pod-phisical-pre-scan.png` | POD física: fotografiar el albarán |
| 🔁 | `10_4_delivery.rst` | `10_3_report_23_parada-report-pod-phisical-post-scan.png` | POD física: albarán fotografiado |
| 🔁 | `10_4_delivery.rst` | `10_3_report_24_parada-report-pre-sign-digital.png` | POD digital: nombre, DNI, resumen y recuadro de firma |
| 🔁 | `10_4_delivery.rst` | `10_3_report_25_parada-report-pod-digital-post-sign.png` | POD digital: firma hecha |
| ⬜ | `10_5_loading.rst` | `10_5_loading_01_comprobar-carga.png` | Comprobar bultos en una parada de carga |
| 🔁 | `10_5_loading.rst` | `10_3_report_14_reporte-carga-1.png` | Tarjeta de un bulto en la carga |
| 🔁 | `10_5_loading.rst` | `10_3_report_15_reporte-carga-2.png` | Botón Reportar Problema |
| 🔁 | `10_5_loading.rst` | `10_3_report_16_reporte-carga-3.png` | Pregunta ¿Se entrega el bulto? |
| 🔁 | `10_6_refunds.rst` | `10_3_report_12_reembolso-step-1.png` | Orden con la línea de reembolso |
| 🔁 | `10_6_refunds.rst` | `10_3_report_13_reembolso-step-2.png` | Pantalla del reembolso: Cobrado, Cobrado en parte, No Cobrado |
| 🔁 | `10_7_incidents.rst` | `10_3_report_17_reporte-entrega.png` | Motivos de una entrega con reservas |
| 🔁 | `10_7_incidents.rst` | `10_3_report_18_reporte-entrega-4.png` | Motivos de una parada cancelada |
| ⬜ | `10_7_incidents.rst` | `10_7_incidents_01_foto.png` | Pantalla de foto que pide un motivo |
| 🔁 | `10_7_incidents.rst` | `10_3_report_26_img-1021.png` | Cobrado en parte: importe recibido |
| 🔁 | `10_7_incidents.rst` | `10_3_report_27_img-1020.png` | Motivos del cobro incompleto |
| ⬜ | `10_8_end-of-day.rst` | `10_8_end-of-day_01_sin-viaje.png` | Panel sin ruta: «No se encontró ningún viaje» |
| ⬜ | `10_8_end-of-day.rst` | `10_8_end-of-day_02_avatar-aviso.png` | Avatar con el número de pendientes/errores |
| ⬜ | `10_8_end-of-day.rst` | `10_8_end-of-day_03_cuenta.png` | Pantalla Cuenta con Sincronización y botones |

---

*Regenerada el 2026-09-08 (tarea D1). Se mantiene al día con `/capturas` y `/cerrar-tarea`.*
