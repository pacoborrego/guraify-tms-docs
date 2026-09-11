Glosario
========

Vocabulario de Guraify TMS. Cada término se usa siempre con este nombre en toda la
documentación; los sinónimos que aparecen entre paréntesis en la definición son los que
**no** se emplean. Entre paréntesis y en monoespaciado, el modelo de Odoo que lo implementa,
para quien lo necesite.

.. glossary::
   :sorted:

   Activo y pasivo
      Lo que se cobra al cliente (activo) y lo que se paga al transportista (pasivo) por una
      operación. Existen en los cuatro niveles del modelo: Orden, Tramo, Parada y Viaje. La
      diferencia es el margen. En la prosa se habla de ingreso, coste y margen; los campos de la
      interfaz se llaman Activo, Pasivo y Beneficio.

   Agencia
      Delegación territorial del operador de transporte a la que se adscriben Órdenes, Paradas y
      Viajes para su gestión y su análisis. Es un contacto marcado como agencia (``res.partner`` con
      la casilla de agencia marcada). No confundir con :term:`Hub`.

   Área geográfica
      Polígono o multipolígono que delimita un territorio operativo. Se usa para asignar Paradas a
      redes de transporte, a Agencias y a Transportistas, y para alimentar la planificación. (No se
      dice *zona geográfica*.) Modelo ``tms.area``.

   Bandeja de entrada API
      Registro de los pedidos que llegan por integración API antes de convertirse en Órdenes. Cada
      línea conserva el mensaje recibido y su estado: recibido, inválido o vinculado. (No se dice
      *API Inbox* ni *Inbox*.) Modelo ``tms_int.api.inbox``.

   Bulto
      Unidad física de carga identificada con una etiqueta escaneable. Una Orden puede tener varios
      bultos; la app del conductor los escanea en carga y en entrega. (No se dice *paquete*,
      *parcel* ni *pack*.) Modelo ``tms.shipment.pack``.

   Cálculo de ruta
      Enriquecimiento de un Viaje con la red viaria de PTV: trazado, distancia, duración y, por
      Parada, hora estimada de llegada (ETA), llegada y salida. No cambia el orden de las Paradas;
      eso es la secuenciación. En el Viaje lo lanza el botón **Enrutar Viaje** (**Secuenciar Viaje**
      lanza la secuenciación). Durante la ejecución, el ETA de las Paradas pendientes se recalcula
      sobre la ruta ya calculada según la :term:`Política operativa` (capítulo 1.4.2). (No se dice
      *routing*.)

   Cliente
      Empresa o persona que encarga el servicio y a quien se factura la Orden. (No se dice *shipper*
      ni *cargador*.) Modelo ``res.partner``.

   Conductor
      Persona que ejecuta el Viaje y reporta desde la app móvil. Puede ser empleado propio o del
      Transportista. (No se dice *chófer*, *driver* ni *repartidor*.) Es un contacto,
      ``res.partner``.

   Control de revisiones
      Seguimiento de las dos revisiones periódicas de un vehículo (revisión de combustible cada
      15.000 km y revisión completa cada 30.000, por defecto) sobre el kilometraje de la última
      revisión registrada. Sin ese dato el estado es «Sin datos», nunca vencido. En la interfaz,
      «Control de service». Campos de ``fleet.vehicle`` en ``tms_maintenance``.

   Definición de fichero
      Plantilla que describe cómo leer el fichero de un cliente: formato, columnas, mapeo de cada
      columna a un campo del TMS y transformaciones. Cada importación con esa plantilla genera un
      :term:`Manifiesto`. (No se dice *fichero EDI* ni *plantilla EDI*.) Modelo ``tms.edi.file``.

   Destinatario
      Contacto de destino de la mercancía: quien la recibe en la entrega. (No se dice *receiver* ni
      *consignatario*.) Modelo ``res.partner``.

   División de ventas
      Reparto del importe de una Orden entre sus Tramos con el Modo de División del Proyecto (peso,
      volumen, bultos, palés, cantidad, metros, lineal, o combinados con kilómetros), y dentro del
      Tramo entre carga y descarga con los porcentajes del Tipo de Orden.

   División de costes
      Reparto del coste de un Viaje entre sus Paradas con el Modo División Viaje del Planning. Las
      paradas de hub y las cargas de reparto no reciben coste.

   Diagnóstico de tarifa
      Resultado del último cálculo de venta (Orden) o de compra (Viaje), con el motivo cuando no
      pudo hacerse. Se revisa en TMS › Administración › Opciones de Tarifa › Diagnóstico de tarifa
      de órdenes / de viajes. (No se dice *diagnosis*.)

   Dominio
      Dirección del servidor de la empresa que el conductor escribe una sola vez al entrar en la
      app, junto a su usuario y su contraseña. Se la facilita su empresa.

   Estados de la Parada
      Resultado de la ejecución de una Parada: **Completada** (todo conforme), **Con reservas**
      (ejecutada con incidencias), **Fallida** (no ejecutada), **Reprogramada** (se volverá a
      intentar), **Devuelta** (mercancía devuelta) y **Cancelada**. Son los estados que cierran la
      Parada. Antes de cerrarse pasa por estados abiertos (borrador, en proceso, en camino, en
      curso, cargada…), que se detallan en el capítulo 3.2.6 y, para los eventos de la app, en la
      tabla de 5.4.4. (No se dice *Hecho*, *KO* ni *OK*.) Campo ``state`` de ``tms.stop``.

   Franja horaria
      Ventana de servicio reutilizable (por ejemplo, «mañanas, de 9 a 14») que se asigna a
      contactos, Proyectos o Paradas para fijar cuándo se puede cargar o entregar. Modelo
      ``tms.time.zone``.

   Hub
      Punto físico donde la mercancía se consolida, se cruza o cambia de vehículo. Es un contacto
      marcado como hub (``res.partner`` con la casilla de hub marcada). (No se dice *almacén* ni
      *depósito*.) No confundir con :term:`Agencia`.

   Incidencia
      Anomalía registrada por el conductor en una carga o una entrega: bulto dañado, bulto ausente,
      rechazo del destinatario, destinatario ausente, etc. Queda en la trazabilidad de la Parada.
      (No se dice *problema* ni *issue*.) Modelo ``tms.traceability.incidents``.

   Indicador visual
   Indicador KPI
      Marca de color con texto que acompaña a cada Orden y a cada Parada en las listas: resume de un
      vistazo su situación operativa y económica (en hora o con retraso, cobrada o pendiente, con
      reclamación de POD). Se llama «KPI» en la interfaz y así puede nombrarse. Campos calculados de
      ``sale.order`` y ``tms.stop`` (capítulo 5.8).

   Indicador configurable
      Registro del motor de indicadores: un cálculo con formato, sección, objetivo y audiencia
      (quién lo ve dentro de Odoo) que se define desde Odoo sin desarrollar pantallas nuevas. Al
      pulsarlo abre el listado que lo compone (capítulo 8.8). Modelo ``tms.kpi``.

   Línea de tarifa
      Elemento de una :term:`Tarifa` que dice **cuándo** aplica un precio (ámbito: Orden, Tramo,
      Parada o Viaje; tipo de servicio) y cuyos **detalles** fijan el importe por :term:`Zona de
      tarifa`, rango y tipo de vehículo. (No se dice *regla de tarifa*, que es otra cosa.) Modelo
      ``tms.pricelist.item.zone`` y su detalle ``tms.pricelist.item.zone.detail``.

   Liquidación
      Cierre económico del Viaje con el Transportista: comprobación del coste y generación o
      confirmación de la :term:`Orden de compra` de la que saldrá su factura. (No se dice
      *settlement*.)

   Manifiesto
      Lote de Órdenes recibido de una vez, por importación de fichero o por API, que al cerrarse se
      convierte en Órdenes, Tramos y Paradas. Tiene sus propios estados (abierto, en cola,
      procesando, cerrado). (No se dice *fichero EDI*.) No confundir con el informe «Manifiesto de
      transporte», que es la hoja de carga imprimible de un Viaje. Modelo ``tms.edi.manifest``.

   Objetivo periódico
      Trabajo de taller que se mide en días desde la última vez: lavado y engrase (30 días),
      calibración y revisión de neumáticos (90). Son Trabajos del catálogo cuyo intervalo es el
      objetivo; alimentan las clasificaciones y la orden de trabajo impresa. (En los datos de serie,
      «Calibración de cubiertas» y «Relevamiento de cubiertas».)

   Odómetro único
      La serie de kilometraje de cada vehículo, en la que confluyen todas las lecturas (taller,
      combustible, app, telemetría) con detección de anomalías y validación. Solo las lecturas
      válidas cuentan. Modelo ``fleet.vehicle.odometer`` extendido por ``tms_resources``.

   Optimizador de Paradas
      Herramienta visual con mapa que agrupa Paradas en Viajes y las secuencia usando el motor de
      PTV, por franja de disponibilidad o por categoría. Modelo ``tms.optimizator``.

   Orden
      Encargo de un Cliente. Define qué servicio se presta y en qué condiciones se factura; es el
      origen del ingreso. Se descompone en uno o varios Tramos. (No se dice *expedición*, *pedido*,
      *envío* ni *shipment*; «pedido de venta» se usa solo para nombrar el estado nativo de Odoo.)
      Modelo ``sale.order``.

   Orden de compra
      Documento que formaliza el coste de un Viaje hacia su Transportista y del que sale la factura
      de compra. Tras la primera mención puede abreviarse **OC**. Modelo ``purchase.order``.

   Orden de trabajo
      Solicitud de mantenimiento sobre un vehículo: correctiva (algo que reparar) o preventiva
      (generada por una regla o una recurrencia). No se puede cerrar sin el kilometraje del
      vehículo. (No se dice *request* ni *solicitud*.) Modelo ``maintenance.request``.

   Parada
      Evento físico planificable y trazable: una carga, una descarga o un paso por Hub, con
      coordenadas, franja horaria y tiempo de servicio. Se genera automáticamente al validar la
      Orden y es la unidad mínima de planificación. Modelo ``tms.stop``.

   Plan de disponibilidad de conductores
      Vista de calendario (Gantt) donde se declara en qué franjas está disponible cada conductor con
      qué vehículo, transportista y tarifa. El Optimizador de Paradas la usa en el modo por franja.
      (No se dice *slots* ni *Drivers Hub Planning*.) Registros ``planning.slot``.

   Plan de transporte
      Red de Áreas geográficas y Hubs por la que circula una operativa. Determina cómo se encadenan
      los Tramos entre origen, hubs y destino. Modelo ``tms.transport.plan``.

   Planning
      Segmentación operativa que agrupa las Órdenes que comparten una misma lógica de transporte:
      última milla, recogidas, distribución urbana, larga distancia… Se hereda del Proyecto y se
      propaga a Tramos, Paradas y Viajes. Se escribe siempre *Planning*, sin traducir, para no
      confundirlo con la actividad de planificar. Modelo ``tms.planning``.

   POD
   Prueba de entrega
      Prueba de entrega (*proof of delivery*), «POD» tras la primera mención. Puede ser **POD
      digital** (firma del destinatario en la pantalla del móvil) o **POD físico** (fotografía del
      albarán firmado). Se adjunta a la Parada y queda disponible para el Cliente.

   Precio cerrado
      Importe fijo pactado con el transportista por un Viaje, que sustituye a la tarifa de compra en
      la orden de compra.

   Proyecto
      Contenedor de configuración de una operativa o de un cliente: tarifa, Planning, tipos de
      servicio permitidos, división de ventas, comportamiento de la app y demás parámetros. Toda
      Orden pertenece a un Proyecto y hereda su configuración. Modelo ``project.project``.

   Reembolso
      Importe que el conductor debe cobrar al destinatario en el momento de la entrega. Su cobro, su
      ingreso en la empresa y su devolución al cliente se siguen con siete estados (Borrador, En
      proceso, Cobrado, Ingresado, Pagado, Rechazado, Cancelado; capítulo 8.6). (No se dice *contra
      reembolso*, *COD* ni *cobro*.) Modelo ``tms.shipment.refund``.

   Regla de preventivo
      Para un vehículo y un trabajo, cada cuántos kilómetros o días toca. El motor calcula su estado
      (al día, por vencer al 85 % del intervalo, vencido al 100 %, o no evaluada con su motivo) a
      partir del último realizado y del kilometraje actual. Modelo ``tms.maintenance.rule``.

   Regla de tarifa
      Define **cómo se mide la mercancía** de una línea de la Orden: por bultos, por palés, por
      cantidad o por metros lineales, con las dimensiones y el peso por defecto de la unidad. Si es
      física, genera un Bulto por unidad. A pesar del nombre, no fija precios: la magnitud que se
      cobra la dice la :term:`Tarifa base` y el importe las :term:`Líneas de tarifa <Línea de
      tarifa>`. Modelo ``tms.pricelist.rule``.

   Remitente
      Contacto de origen de la mercancía cuando no coincide con el Cliente que encarga el servicio.
      (No se dice *shipper*.) Modelo ``res.partner``.

   Tablero
      Hoja de cálculo de Odoo con tablas dinámicas sobre los datos vivos del TMS, en TMS ›
      Operaciones › Tableros. Vienen tres, con nombre en inglés en la interfaz: «Operations KPI»
      (Órdenes por cliente y rentabilidad, puntualidad por conductor, cliente y Planning), «Stops
      Operations» (Paradas de reparto, recogida y Hub por estado y puntualidad, Bultos por Viaje) y
      «Pending Invoicing» (Órdenes y órdenes de compra por estado y mes). (No se dice *dashboard*.)

   Tarea de mantenimiento
      Clasificación con la que el taller filtra las órdenes: preventivo, taller, reparación,
      repuesto, neumáticos, lavado, engrase, mejora, asistencia en carretera… Los datos de serie
      conservan algún nombre original («Gomeria», «Auxilio»). Modelo ``tms.maintenance.task``.

   Tarifa
      Conjunto de Líneas de tarifa que determina el precio de venta de las Órdenes de un Proyecto o
      el coste de compra de los Viajes de un Transportista. (No se dice *pricelist*.) Modelo
      ``tms.pricelist``.

   Tarifa base
      Define **qué magnitud se cobra** (peso, volumen, bultos, palés, kilómetros, paradas…) y con
      qué escalado de rangos, y sirve de plantilla para generar Líneas de tarifa de forma
      automática. Modelo ``tms.pricelist.base``.

   Tiempo de servicio
      Duración estimada de una Parada según el tipo de operación, el contacto o el Proyecto. La
      planificación lo usa para calcular horarios. Modelo ``tms.service.time``.

   Tipo de Orden
   Tipo de Servicio
   Tipo de Parada
   Tipo de Destinatario
   Tipo de Transportista
   Tipo de Reembolso
      Catálogos de configuración operativa (capítulo 4.1, anexos A.23 a A.28) que clasifican,
      respectivamente, el servicio contratado (con sus variables logísticas), la Orden (entrega,
      recogida, directo, hub: sus marcas deciden los lados del Tramo y el Tipo de Parada), la Parada
      (seis papeles fijos, un registro por papel y compañía: Parada de Ruta, Operaciones de Hub,
      Punto de Recogida, Recogida directa, Entrega directa y Paradas Optimizador), el Destinatario,
      el Transportista y la forma de cobro de un Reembolso. (No se dice *tipo de expedición* ni
      *tipo de receptor*.) Modelos ``tms.service.type``, ``tms.shipment.type``, ``tms.stop.type``,
      ``tms.receiper.type``, ``tms.carrier.type`` y ``tms.cashvalue.type``.

   Trabajo
      Lo que se hace en una orden de mantenimiento: cambio de aceite, filtro de aire, frenos. Es el
      tipo de servicio de la Flota de Odoo con tarea, material e intervalo por defecto. (No se dice
      *job* ni *tipo de servicio* para hablar del taller.) Modelo ``fleet.service.type``.

   Tramo
      Movimiento de una Orden entre un punto de carga y un punto de descarga. Una Orden puerta a
      puerta tiene un Tramo; una con paso por Hub, dos o más. Toma del Tipo de Orden sus marcas
      (entrega, recogida, directo, hub) y añade dos propias: recogida a domicilio y transferencia
      (el Tramo que nace al dividir por un hub intermedio). Da origen a las Paradas (capítulo
      3.2.6). (No se dice *leg* ni *envío*.) Modelo ``tms.shipment.leg``.

   Transportista
      Empresa o autónomo que ejecuta Viajes por cuenta del operador y recibe la Orden de compra. (No
      se dice *carrier*, *proveedor* ni *colaborador*.) Modelo ``res.partner``.

   Trazabilidad
      Histórico de eventos de una Parada, un Tramo o una Orden: cada cambio de estado, escaneo, POD
      e incidencia, con fecha, autor y origen (app, backoffice o integración). Modelo
      ``tms.traceability``.

   Viaje
      Conjunto de Paradas que ejecuta un recurso (conductor y vehículo) en una salida. Materializa
      el coste del transporte y genera la Orden de compra al Transportista. En el manual del
      conductor se le llama **«tu ruta»**, que es como lo ve quien conduce. (En el resto de la
      documentación no se dice *ruta* ni *trip*.) Modelo ``tms.trip``.

   PTV
      Proveedor de cartografía y de cálculo de rutas para transporte profesional (PTV Developer) que
      usa el TMS para geocodificar, dibujar el mapa, calcular rutas, secuenciar Paradas y proponer
      Viajes. Se contrata por vehículo; el token se configura por compañía. Sin PTV el sistema
      planifica a mano sobre OpenStreetMap.

   Webhook
      Aviso automático que un sistema envía a otro en cuanto ocurre algo, mediante una llamada a una
      dirección acordada. El TMS los recibe (para estados de sistemas externos) y los emite (para
      avisar a los clientes). (No se dice *callback*.)

   Secuenciación
      Servicio de PTV que ordena las Paradas de un Viaje ya formado respetando franjas horarias,
      tiempos de servicio y capacidad. Se lanza desde el Optimizador de Paradas o, si el Proyecto
      tiene activado **Secuenciar Viaje**, al cerrar un Manifiesto. (No se dice *sequence* ni
      *autosecuenciación*.)

   Optimización completa
      Servicio de PTV que, a partir de las Paradas pendientes de una fecha, propone qué Viajes
      crear, con qué vehículo y conductor y en qué orden. Se lanza desde el Optimizador de Paradas
      en **modo por franja** (turnos del Plan de disponibilidad; en la interfaz, «Por franja») o en
      **modo por categoría de vehículo**. (No se dice *por turno*.)

   Perfil de jornada
      Conjunto de reglas de horas de conducción y pausas (por defecto, el reglamento europeo
      561/2006) que se envía a PTV al calcular o secuenciar. Se elige en la categoría de vehículo y
      en la franja del Plan de disponibilidad. (No se dice *preset*.) Modelo
      ``tms.driver.working.hours``.

   Equipamiento
      Capacidad instalada en un vehículo (plataforma, frío, ADR…) que la mercancía puede exigir y el
      optimizador comprueba. Modelo ``tms.equipment``.

   Categoría de carga
      Naturaleza logística de la mercancía (refrigerada, seca, paletizada…): qué equipamiento exige
      y con qué otras categorías no puede viajar. Modelo ``tms.load.category``.

   Tipo de bulto
      Qué mercancía es el bulto (seco, refrigerado, congelado, frágil…), con su rango de temperatura
      y su icono. Modelo ``tms.temperature``.

   Peso tasable
      Peso que se toma para tarificar cuando la tarifa compara el peso real con el volumétrico y se
      queda con el mayor.

   Tramo activo
      El Tramo de una Orden que está en ejecución o es el siguiente en ejecutarse; de él toma la
      Orden su Parada activa y su Viaje activo (capítulo 3.2.5). (No se dice *leg activo*.)

   Versión de tarifa
      Periodo de vigencia de una Tarifa con sus propias Líneas de tarifa. Las versiones son
      consecutivas (cada una empieza el día siguiente al fin de la anterior), sin solapes ni huecos;
      solo la última puede quedar sin fecha de fin y solo ella está activa. Se tarifica con la
      vigente en la fecha administrativa de la Orden. Modelo ``tms.pricelist.version``.

   Hora de convocatoria
      Hora única de una recogida o carga programada, en lugar de una franja. La puntualidad de la
      Parada se mide contra ella con la tolerancia que fija el Proyecto. Campos de
      ``project.project`` y ``tms.stop``.

   Política operativa
      Decisiones por compañía, y opcionalmente por Proyecto, sobre el recálculo del ETA (cuándo,
      cada cuánto, espaciado mínimo y tope diario), los extras que se piden a PTV (peajes, esquema
      de emisiones) y el reparto del CO₂ a las Órdenes. La del Proyecto gana a la de la compañía.
      Modelo ``tms.operations.policy``.

   ETA
      Hora estimada de llegada a una Parada. El **ETA prometido** es el de la planificación y no
      cambia; el **ETA vigente** se recalcula durante la ejecución y guarda historial; si PTV falla,
      el vigente se conserva y queda marcado como **obsoleto**. Campos de ``tms.stop``.

   Perímetro de mantenimiento
      Vehículos con al menos una Regla de preventivo activa: son la población de los indicadores
      de odómetro y mantenimiento del capítulo 6.

   Anomalía de odómetro
      Lectura que queda en borrador porque su fecha es futura, está duplicada, retrocede respecto
      a la anterior o da un salto inverosímil. Se revisa y se valida o se rechaza a mano (capítulo
      6.2). Campo de ``fleet.vehicle.odometer``.

   Bulto previo
      Bulto creado al recibir una Orden por API, antes de que la Orden exista, para que el cliente
      disponga ya de la etiqueta y de su **token de etiqueta** (identificador con el que descarga la
      etiqueta desde la pasarela). Al cerrarse el Manifiesto pasa a Bulto definitivo con el mismo
      código de barras. Solo existe en el camino API. (No se dice *preview pack*.)

   Integración
   Integración API
      La **Integración** (``tms_int.integration``) es la ficha de negocio que asocia clientes y
      Proyecto, agrupa sus canales (API o webhook, fichero, base de datos) y designa el patrón de
      salida. La **Integración API** (``tms_int.api.integration``) es una conexión HTTP concreta
      (dirección base y autenticación) de la que cuelgan los Endpoints. No hay campo que las una.

   Endpoint
      Cada operación configurable de una Integración API: dirección, método, disparador y patrón
      de salida. Es el nombre de la entidad en la interfaz («Endpoints API»); para la URL genérica
      de un servicio se dice «punto de conexión». Modelo ``tms_int.api.endpoint``.

   Registro de actividad de las APIs
      Traza de cada llamada entrante o saliente (fecha, dirección, contenido, respuesta) que
      consulta el integrador cuando algo falla (capítulo 7.7). Modelo ``tms.api.log``.

   Lote de la Bandeja de entrada API
      Registro de cada envío recibido por API: el mensaje completo, el número de Órdenes que
      trae y los bloques que no son Órdenes (clientes, transportistas, conductores, vehículos,
      viajes). Las líneas de la Bandeja se tratan una a una; el lote es el soporte de la
      recepción (capítulo 3.2.4). Modelo ``tms_int.api.inbox.batch``.

   Regla de asignación
      Regla de asignación, restricción o prioridad entre un origen (contacto, empleado,
      vehículo, categoría de vehículo, Área geográfica o Categoría de carga) y unos destinos, que
      el planificador tiene en cuenta al asignar recursos. No tiene que ver con la tarificación.
      (No se dice *regla de negocio*.) Modelo ``tms.rule``.

   Perfil de la app
      Conjunto de motivos (de reserva, de fallo, de bulto con problema y de reembolso no cobrado)
      que la app ofrece al conductor en las Paradas de un Proyecto. Se crea en TMS › Configuración
      › App › Perfiles de la app; no hay perfiles de serie. Modelo ``tms_app.profile``.

   Zona de tarifa
      Agrupación de Áreas geográficas o de códigos postales a efectos de precio. Los detalles de las
      Líneas de tarifa fijan importes por zona de origen y de destino. (No se dice *zona
      tarifaria*.) Modelo ``tms.pricelist.zone``.
