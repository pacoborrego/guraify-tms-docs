# Changelog — Documentación Guraify TMS

Registro de cambios de la documentación oficial. Formato basado en
[Keep a Changelog](https://keepachangelog.com/es/).

Convención de release: cada publicación se etiqueta con tag git `AAMMDD_VNN`
(p. ej. `260521_V01`) y se añade aquí su sección con el capítulo afectado y un resumen.

## [Sin publicar]

### Publicación (2026-09-10)
- `deploy.sh` compila siempre completo (`-E -a`). La compilación incremental del servidor dejaba
  obsoleta la barra lateral de las páginas sin cambios al añadir un capítulo: tras publicar el
  cap. 6, la portada lo mostraba y las páginas de los caps. 1 a 5 y 7 no. Corregido con una
  recompilación completa en el servidor.

### Cap. 6 Gestión de Recursos (tarea D14 del plan, 2026-09-10)
- **Capítulo nuevo** del Manual de implantación (`source/17.0/6_resources/`, 8 páginas) para los
  módulos `tms_resources` y `tms_maintenance`, verificado contra el código y los handoffs:
  6.1 el área y su menú; 6.2 el odómetro único (fuentes, referencia externa, estados, las cuatro
  anomalías en orden, pantalla de anomalías, resumen del vehículo y estimación con confianza);
  6.3 el vehículo como elemento mantenible, la orden de trabajo y sus cuatro etapas, trabajos y
  tareas; 6.4 las reglas de preventivo (motor por km y por días, umbrales 85/100, motivos de
  exclusión, recálculo, generación idempotente de pendientes por la tarea diaria, recurrencia
  nativa por días) y el control de service a dos niveles con «Sin datos» en vez del falso
  vencido; 6.5 cerrar orden con km, carga masiva y alta/baja; 6.6 orden impresa, texto de
  WhatsApp y rankings; 6.7 los once indicadores y el perímetro de mantenimiento; 6.8
  configuración. Mermaid del ciclo en el index.
- **Numeración**: Gestión de Recursos es el cap. 6; Administración y Control Económico (D10) será
  el cap. 8. Portada actualizada.
- **Glosario**: Control de service, Objetivo periódico, Odómetro único, Orden de trabajo, Regla
  de preventivo, Tarea de mantenimiento, Trabajo.
- **Anexo A**: A.19 Odómetro único y A.20 Mantenimiento (regla, orden, trabajo, tarea, vehículo y
  umbrales de compañía).
- **Capturas**: trece nuevas registradas, con figures comentados.
- Las etiquetas de la interfaz de estos dos módulos están aún en inglés (Odometer Anomalies,
  Close Order, Print Work Order, Maintenance (TMS)...): la doc las cita tal cual. El plan de
  traducción de los módulos (`specs/resources/05_PLAN_i18n.md`) está pendiente en `tms_suite`.

### Cap. 4 Parametrización y anexo A (tarea D7 del plan, 2026-09-10)
- **4.2 a 4.5 reescritas en prosa** desde los modelos de `tms_suite` (campos, selecciones y
  ayudas verificados con un volcado del código y las traducciones de `es.po`). Cada maestro se
  explica por lo que decide el cliente y el efecto que tiene en planificación, tarifa y
  ejecución, con una tabla corta «Decisión / Efecto»; se enlaza al cap. 5 para el flujo y al
  anexo para los campos.
- **Anexo A · Catálogo de campos** (`source/17.0/annexes/`, 18 páginas, A.1 a A.18): una página
  por maestro (equipamientos, categorías de carga, reglas de tarifa, tipos de bulto, categorías
  y modelos de vehículo, Planning, planes de transporte, áreas, franjas, tiempos de servicio,
  horas de conducción, zonas de tarifa, tarifas base, líneas de tarifa y detalles, tarifas y
  versiones, productos, proyecto) con la etiqueta en español de la interfaz, el tipo y el
  significado. Colgado del Manual de implantación en la portada. Sustituye a las 25 tablas
  «Campos principales» que estaban en el cuerpo.
- **Correcciones de fondo**: «Reglas de tarifa» queda sólo para la unidad de medida (4.2.3) y
  «Líneas de tarifa» para el precio (4.4.3); los Tipos de Bulto son el modelo
  `tms.temperature`, no un modelo propio; el Modo de división se explica con sus valores en
  español y no con `km_weight`; el grupo de asignación del proyecto se llama «Tarea» en la
  interfaz. Fuera las notas de desarrollador (validación dimensional, cachés de geometría,
  onchange con comandos One2many, read_group) y las dos tablas rotas de 4.5.10.
- **4.5.9 (antes 4.5.10) kanban de proyectos** reescrita en español y en prosa; la interfaz sigue
  en inglés en esas cadenas (anotado como corrección de Odoo).
- **Capturas**: nueve nuevas registradas en `CAPTURAS_PENDIENTES.md`, con su `figure` comentado
  bajo el marcador `.. CAPTURA:` hasta que exista la imagen. Build limpio con `-W`.
- Discrepancias para Odoo anotadas en PLAN.md: etiquetas de Datos auxiliares fuera del glosario
  (Tipos de expediciones, receptor, valores de caja, Planificaciones), «Zona Horaria» por
  franja, y las cadenas de la kanban sin traducir.

### Cap. 5 Flujos operativos (tarea D8 del plan, 2026-09-08)
- **Index** reescrito: desaparece la frase cortada y entra un mermaid del ciclo completo (alta,
  Manifiesto, validación, Viaje, ejecución, cierre, orden de compra y factura, con la
  tarificación como tarea periódica).
- **5.1** ajustado: 5.1.2 pasa a ser los cinco pasos del alta por Manifiesto; identificadores
  fuera de la prosa.
- **5.2 a 5.7 redactados como flujo** al nivel de 5.1, verificados en el código:
  - 5.2: el asistente **Asignar a viaje** (desde Órdenes o desde Paradas con **Acciones
    operativas**), sus modos Nuevo y Existente, lo que completa el Proyecto, los botones
    Secuenciar Viaje, Enrutar Viaje y Actualizar, y los pasos del Optimizador. Ya no dice que el
    cálculo de ruta devuelva peajes.
  - 5.3: los cuatro orígenes de los recursos, cuándo nace la orden de compra (transportista más
    tarifa de compra o precio cerrado), la flota propia sin orden de compra y la propagación a
    las Paradas (campos calculados desde el Viaje).
  - 5.4: **Enviar a la app** pone el Viaje en Procesado; la app carga el procesado más reciente
    del conductor; cada evento es un apunte de Trazabilidad con su contexto; orden de
    actualización Parada → Tramos → Orden → Viaje. Remite al cap. 10, no al 6. Códigos de
    estado en una tabla de referencia técnica.
  - 5.5: la cadena de cierre tal y como está programada (Viaje: tarifica, bloquea la OC,
    Completado; Orden: pendiente de confirmar y confirmada por la tarea programada cada cinco
    minutos, con la explicación de por qué el desfase), la reapertura, la reprogramación y la
    protección por facturación.
  - 5.6: cuándo se tarifica (validar, cerrar, botón Tarificar, tarea cada 5 min con lote y
    tope de tiempo), venta y compra, y el diagnóstico de tarifa con **Resolver diagnosis** y
    **Crear trayecto faltante**.
  - 5.7: **Modo de facturación TMS** del asistente estándar (Grupo TMS por producto, servicio y
    zona / Estándar Odoo), **Crear factura agrupada** y **Línea de abono** desde las listas de
    líneas, **Crear factura** desde el Viaje y sus condiciones.
- **5.8**: campos fuera de la prosa, a una referencia técnica.
- **Reparto con el cap. 3** aplicado: el 5 enlaza al 3 para estados y botones; 3.2.1.5,
  3.2.2.4, 3.2.3 y 3.3 ya enlazaban al 5.
- **Detectado**: la tarea P3 de la torre de control se cerró el 2026-09-08, así que 1.4.6 da por
  futuro (ETA incremental, peajes, CO₂) lo que ya está en el código. Anotado en PLAN.md como
  pendiente suelto.

### Cap. 3 Arquitectura funcional (tarea D6 del plan, 2026-09-08)
- **Identificadores fuera de la prosa** en 3.1 a 3.5. Los estados se nombran como en pantalla
  (sin el código entre paréntesis), los botones por su etiqueta en español (**Bloquear**,
  **Desbloquear**, **Validar e importar**, **Importar Fichero Ahora**, **Cerrar Manifiesto
  Ahora**) y los métodos desaparecen. Los campos que un consultor necesita para filtros y
  exportaciones van a una tabla **Referencia técnica** al final de 3.2.1 (Órdenes), 3.2.2
  (Viajes) y 3.2.5 (Tramo activo). El mermaid de 3.2.5 se dibuja con conceptos, no con campos.
- **3.1 alineado con el menú real** de Odoo (verificado en los `menuitem` de `tms` y `tms_int`
  y en `es.po`): Trazabilidad cuelga de Tráfico y no de Maestros operativos, que incluye
  Líneas; Administración son Opciones de tarifa, maestros económicos, Reembolsos y
  Transacciones (antes decía "facturación, liquidación, control de costes"); Maestros son
  Equipos, Recursos humanos y Operaciones; Configuración incluye el submenú EDI.
- **Referencias a los capítulos 6 y 8** (3.2 y 3.4) sustituidas por enlaces a 5.4, 5.6 y 5.7
  hasta que D10 escriba Administración y Control Económico.
- **Duplicidades con el cap. 5**: el cap. 3 se queda con qué es y cómo se comporta cada
  entidad y enlaza al flujo (3.2.1.5 y 3.2.2.4 a 5.5; 3.2.3.3 y 3.3.2 a 5.2). Nada de 5.x
  se ha tocado salvo la palabra *routing*.
- **3.3 corregido**: el planificador no elige el objetivo de la optimización (no existe tal
  opción); el resultado se describe con lo que devuelve PTV (ETA, distancias, tiempos de
  conducción, trazado) sin "esperas y descansos". 3.2.2.1 ya no atribuye "costes" al cálculo
  de ruta.
- **3.4**: ruta corregida a TMS › Administración › Opciones de Tarifa; la tabla de componentes
  distingue Reglas de tarifa (qué se mide) de Líneas de tarifa (el precio) según el glosario.
- **Anglicismos**: *slot* → franja, *smart buttons* / botones mágicos → botones inteligentes,
  *gateway* → pasarela de API, *routing* → **cálculo de ruta**. Este último entra en el
  glosario como término nuevo y se aplica también en 1.4 y en 5.2.
- Discrepancia detectada para Odoo: el botón `Import File` del Manifiesto está traducido como
  "Fichero de Importación"; debería ser "Importar fichero". Añadida a la lista de
  correcciones de PLAN.md.

### Cap. 1 Introducción (tarea D5 del plan, 2026-09-08)
- **1.1 y 1.3** reescritos para el recorrido "Manual de implantación": el capítulo ya no dice
  que la doc no es para el usuario final; presenta el manual, su público (consultores,
  responsables de operaciones, equipos financieros, arquitectos ERP) y remite a los otros tres
  recorridos y al glosario.
- **1.4 Arquitectura tecnológica** reescrita desde el código (de 3.577 a 2.300 palabras, con
  subsecciones numeradas 1.4.1 a 1.4.6 y el mermaid actualizado). Verificado en `tms_suite` y
  en `tms_odoo_app`:
  - PTV: los tres servicios existen (`routing/v1`, `sequenceoptimization/v1` y
    `routeoptimization/v1`); el tercero **no es OptiFlow**, como decía el texto antiguo. Se
    documenta qué se envía y qué vuelve en cada uno, los dos modos del optimizador (turnos del
    Planning o categorías de vehículo) y el reintento de la secuenciación.
  - Geocodificación: la cascada real es PTV → Google → PTV sólo código postal → Nominatim
    (antes decía PTV → Google → centroide). Umbral 80 y normalización confirmados. Se añade la
    geocodificación inversa.
  - Mapa base: teselas vectoriales PTV con respaldo OpenStreetMap (antes se presentaba OSM
    como el mapa de las áreas). Áreas: cinco tipos, dibujo o importación desde OSM, fusión,
    opción por Proyecto de asignar el área más cercana.
  - Scandit: los tres modos reales de la app (Barcode Capture, SparkScan para comprobar carga
    y entrega con reservas, Barcode Find para encontrar bultos). Se quitan la "entrada de
    mercancía en almacén", el semáforo verde/rojo por viaje y los efectos de un escaneo sobre
    facturación, ETA o alertas, que no existen.
  - Lo que el texto antiguo daba por hecho y está en desarrollo (peajes, emisiones, ETA
    incremental desde la posición del conductor, telemática, OptiFlow con categorías de carga,
    costes y motivos de no planificación) pasa a **1.4.6 Evolución prevista**, etiquetado como
    trabajo en curso, por decisión de Paco (2026-09-08).
- **1.2** sin modelos Odoo en las viñetas; **1.5** deja el principio ingreso/coste en una frase
  con enlace a 2.1 y remite a 1.4 para las tecnologías.
- Discrepancias detectadas para otras tareas: 3.3 afirma que el planificador elige el objetivo
  del optimizador (no existe; D6) y 5.2 que el routing devuelve peajes (no se piden; D8).

### Capa de producto y portada (tarea D4 del plan, 2026-09-08)
- **Nueva sección "Conocer Guraify TMS"** (`source/17.0/0_product-overview/`, 8 páginas) para
  clientes y distribuidores: qué es, para quién (cinco operativas y para quién no), cómo
  funciona (los cuatro conceptos y el ciclo completo, con un mermaid), qué incluye (nueve
  áreas y su cruce con los módulos, verificado contra los `__manifest__.py`; `tms_crm` queda
  fuera por ser interno), la app del conductor, integraciones, cuatro casos de uso sin nombres
  de cliente y preguntas frecuentes. Sin modelos ni campos de Odoo; títulos sin numerar.
  Los aspectos comerciales (edición de Odoo, despliegue, licencia, soporte) remiten a Guraify.
- **Portada nueva** (`17.0/index.rst`): título "Documentación de Guraify TMS", cuatro
  tarjetas (Conocer Guraify TMS, Manual de implantación, Guía del integrador, Manual del
  conductor) y un toctree con `:caption:` por recorrido. El manual del conductor sigue
  `:orphan:` con su cabecera propia.
- **Barra lateral**: los captions de los toctree vuelven a verse con el nombre de cada
  recorrido. `custom.css` los ocultaba y pintaba un rótulo fijo "📦 TMS User Docs".
- Dos capturas nuevas registradas (tablero de operaciones y portal del cliente); las páginas
  reutilizan además capturas de los caps. 3 y 10.

### Glosario y terminología (tarea D3 del plan, 2026-09-08)
- Nueva página **Glosario** (`source/17.0/glossary.rst`, directiva `glossary` de Sphinx,
  40 términos con definición, sinónimos descartados y modelo Odoo), enlazada desde la portada
  y desde un toctree "Referencia".
- **Terminología unificada** en los 56 `.rst` (29 ficheros tocados): Orden (antes también
  Expedición y Pedido), Viaje (antes también Ruta), Bandeja de entrada API (antes API Inbox,
  Inbox, Bandeja de Entrada), Definición de fichero frente a Manifiesto (antes ambos "Fichero
  EDI"), Zona de tarifa (antes Zona tarifaria), Transportista (antes carrier, proveedor),
  Remitente (antes Shipper/Cargador), Bulto (antes paquete), Tipos de Orden (antes Tipos de
  expedición).
- **Reglas de tarifa desambiguadas**: la sección 4.4.3 pasa a llamarse **Líneas de tarifa**
  (`tms.pricelist.item.zone` y su detalle); "Regla de tarifa" queda sólo para la unidad de
  medida (`tms.pricelist.rule`, sección 4.2.3). Referencias en 4.1 y 4.3 ajustadas.
- **Estados de la Parada** en femenino y sin siglas: Completada, Con reservas, Fallida,
  Reprogramada, Devuelta, Cancelada. En el manual del conductor "KO" pasa a "Fallido", que es
  lo que muestra la app.
- Decisiones del propietario (2026-09-08): *Planning* se mantiene sin traducir; "tu ruta" se
  admite en el manual del conductor; las discrepancias con la interfaz se corrigen en Odoo y
  en la app, no en la doc (lista en `PLAN.md`, "Correcciones en Odoo y en la app").
- Subrayados de títulos normalizados a la longitud exacta del título en todos los ficheros
  (antes muchos eran más largos; sin efecto visible).

### Infraestructura (tarea D1 del plan, 2026-09-08)
- **Plan de cierre** en `PLAN.md` (tareas D1–D13, estructura objetivo del índice con cuatro
  recorridos, diagnóstico). Sustituye a `MIGRACION.md` y `REVISION_ESTANDAR.md`, borrados.
- **`CLAUDE.md` v3**: públicos y política de nombres técnicos por recorrido, terminología
  provisional hasta el glosario (D3), guía de capturas, publicación y alcance (versiones y
  traducciones aparcadas por decisión de Paco).
- **Comandos** `.claude/commands/`: `/estado`, `/d3`…`/d13`, `/capturas`, `/publicar`,
  `/cerrar-tarea`.
- **Publicación documentada**: `deploy.sh` (pull + build con `-W` + rsync a
  `/var/www/tms-docs` en epartner). Se descubre que la web servía el build del 21 de mayo;
  publicado el estado actual el 2026-09-08.
- **CI**: `.github/workflows/build.yml` compila con `-W` en cada push.
- **Selectores de idioma y versión ocultos** en la cabecera (no había traducciones y las tres
  versiones apuntaban a 17.0). Plantillas conservadas. Botón "More Info" → "Más información".
- **Capturas**: activadas las 20 que ya tenían imagen (estaban comentadas y no se veían);
  6 ficheros renombrados (espacios en el nombre, numeración vieja `5_11_*`, `_7_3_01-*`);
  marcadores del cap. 5 renumerados a la numeración actual. `CAPTURAS_PENDIENTES.md`
  regenerada como lista de trabajo de María: todas las existentes se rehacen (recorte, Odoo en
  español, sin datos reales) y quedan 26 por hacer.
- **Limpieza**: borrados `manual.rst` (conversión antigua del Word), `make.bat`, los tres
  stubs `:orphan:` del cap. 5, `source/_static/images/` (4 MB sin referenciar, incluidos los
  originales sin anonimizar) y los `.DS_Store` versionados.

### Pendiente
- Resto del plan: ver `PLAN.md`.

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
