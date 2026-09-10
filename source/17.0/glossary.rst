Glosario
========

Vocabulario de Guraify TMS. Cada término se usa siempre con este nombre en toda la
documentación; los sinónimos que aparecen entre paréntesis en la definición son los que
**no** se emplean. Entre paréntesis y en monoespaciado, el modelo de Odoo que lo implementa,
para quien lo necesite.

.. glossary::
   :sorted:

   Agencia
      Delegación territorial del operador de transporte a la que se adscriben Órdenes, Paradas
      y Viajes para su gestión y su análisis. Es un contacto marcado como agencia
      (``res.partner`` con *Is Agency*). No confundir con :term:`Hub`.

   Área geográfica
      Polígono o multipolígono que delimita un territorio operativo. Se usa para asignar
      Paradas a redes de transporte, a Agencias y a Transportistas, y para alimentar la
      planificación. (No se dice *zona geográfica*.) Modelo ``tms.area``.

   Bandeja de entrada API
      Registro de los pedidos que llegan por integración API antes de convertirse en Órdenes.
      Cada línea conserva el mensaje recibido y su estado: recibido, inválido o vinculado.
      (No se dice *API Inbox* ni *Inbox*.) Modelo ``tms_int.api.inbox``.

   Bulto
      Unidad física de carga identificada con una etiqueta escaneable. Una Orden puede tener
      varios bultos; la app del conductor los escanea en carga y en entrega. (No se dice
      *paquete*, *parcel* ni *pack*.) Modelo ``tms.shipment.pack``.

   Cálculo de ruta
      Enriquecimiento de un Viaje con la red viaria de PTV: trazado, distancia, duración y,
      por Parada, hora estimada de llegada (ETA), llegada y salida. No cambia el orden de las
      Paradas; eso es la secuenciación. (No se dice *routing*.)

   Cliente
      Empresa o persona que encarga el servicio y a quien se factura la Orden. (No se dice
      *shipper* ni *cargador*.) Modelo ``res.partner``.

   Conductor
      Persona que ejecuta el Viaje y reporta desde la app móvil. Puede ser empleado propio o
      del Transportista. (No se dice *chófer*, *driver* ni *repartidor*.) Es un contacto,
      ``res.partner``.

   Control de service
      Seguimiento de los dos services de un vehículo (de combustible cada 15.000 km y completo cada
      30.000, por defecto) sobre el kilometraje del último service registrado. Sin ese dato el
      estado es «Sin datos», nunca vencido. Campos de ``fleet.vehicle`` en ``tms_maintenance``.

   Definición de fichero
      Plantilla que describe cómo leer el fichero de un cliente: formato, columnas, mapeo de
      cada columna a un campo del TMS y transformaciones. Cada importación con esa plantilla
      genera un :term:`Manifiesto`. (No se dice *fichero EDI* ni *plantilla EDI*.) Modelo
      ``tms.edi.file``.

   Destinatario
      Contacto de destino de la mercancía: quien la recibe en la entrega. (No se dice
      *receiver* ni *consignatario*.) Modelo ``res.partner``.

   Dominio
      Dirección del servidor de la empresa que el conductor escribe una sola vez al entrar en
      la app, junto a su usuario y su contraseña. Se la facilita su empresa.

   Estados de la Parada
      Resultado de la ejecución de una Parada: **Completada** (todo conforme), **Con reservas**
      (ejecutada con incidencias), **Fallida** (no ejecutada), **Reprogramada** (se volverá a
      intentar), **Devuelta** (mercancía devuelta) y **Cancelada**. Son los estados que cierran
      la Parada y, con ella, el Viaje. (No se dice *Hecho*, *KO* ni *OK*.) Campo ``state`` de
      ``tms.stop``.

   Franja horaria
      Ventana de servicio reutilizable (por ejemplo, "mañanas 9 a 14") que se asigna a
      contactos, Proyectos o Paradas para fijar cuándo se puede cargar o entregar. Modelo
      ``tms.time.zone``.

   Hub
      Punto físico donde la mercancía se consolida, se cruza o cambia de vehículo. Es un
      contacto marcado como hub (``res.partner`` con *Is Hub*). (No se dice *almacén* ni
      *depósito*.) No confundir con :term:`Agencia`.

   Incidencia
      Anomalía registrada por el conductor en una carga o una entrega: bulto dañado, bulto
      ausente, rechazo del destinatario, ausente, etc. Queda en la trazabilidad de la Parada.
      (No se dice *problema* ni *issue*.) Modelo ``tms.traceability.incidents``.

   Línea de tarifa
      Elemento de una :term:`Tarifa` que dice **cuándo** aplica un precio (ámbito: Orden,
      Tramo, Parada o Viaje; tipo de servicio) y cuyos **detalles** fijan el importe por
      :term:`Zona de tarifa`, rango y tipo de vehículo. (En versiones anteriores de esta
      documentación se llamaba *regla de tarifa*, nombre que hoy designa otra cosa.) Modelo
      ``tms.pricelist.item.zone`` y su detalle ``tms.pricelist.item.zone.detail``.

   Liquidación
      Cierre económico del Viaje con el Transportista: comprobación del coste y generación o
      confirmación de la :term:`Orden de compra` de la que saldrá su factura. (No se dice
      *settlement*.)

   Manifiesto
      Lote de Órdenes recibido de una vez, por importación de fichero o por API, que al
      cerrarse se convierte en Órdenes, Tramos y Paradas. Tiene sus propios estados (abierto,
      en cola, procesando, cerrado). (No se dice *fichero EDI*.) Modelo ``tms.edi.manifest``.

   Objetivo periódico
      Trabajo de taller que se mide en días desde la última vez: lavado y engrase (30 días),
      calibración y relevamiento de cubiertas (90). Son Trabajos del catálogo cuyo intervalo es el
      objetivo; alimentan los rankings y la orden de trabajo impresa.

   Odómetro único
      La serie de kilometraje de cada vehículo, en la que confluyen todas las lecturas (taller,
      combustible, app, telemetría) con detección de anomalías y validación. Sólo las lecturas
      válidas cuentan. Modelo ``fleet.vehicle.odometer`` extendido por ``tms_resources``.

   Optimizador de Paradas
      Herramienta visual con mapa que agrupa Paradas en Viajes y las secuencia usando el
      motor de PTV, por franja de disponibilidad o por categoría. Modelo ``tms.optimizator``.

   Orden
      Encargo de un Cliente. Define qué servicio se presta y en qué condiciones se factura;
      es el origen del ingreso. Se descompone en uno o varios Tramos. (No se dice
      *expedición*, *pedido*, *envío* ni *shipment*; "pedido de venta" se usa sólo para
      nombrar el estado nativo de Odoo.) Modelo ``sale.order``.

   Orden de compra
      Documento que formaliza el coste de un Viaje hacia su Transportista y del que sale la
      factura de compra. Tras la primera mención puede abreviarse **OC**. Modelo
      ``purchase.order``.

   Orden de trabajo
      Solicitud de mantenimiento sobre un vehículo: correctiva (algo que reparar) o preventiva
      (generada por una regla o una recurrencia). No se puede cerrar sin el kilometraje del
      vehículo. (No se dice *request* ni *solicitud*.) Modelo ``maintenance.request``.

   Parada
      Evento físico planificable y trazable: una carga, una descarga o un paso por Hub, con
      coordenadas, franja horaria y tiempo de servicio. Se genera automáticamente al validar
      la Orden y es la unidad mínima de planificación. Modelo ``tms.stop``.

   Plan de disponibilidad de conductores
      Vista de calendario (Gantt) donde se declara en qué franjas está disponible cada
      conductor con qué vehículo, transportista y tarifa. El Optimizador de Paradas la usa en
      el modo por franja. (No se dice *slots* ni *Drivers Hub Planning*.) Registros
      ``planning.slot``.

   Plan de transporte
      Red de Áreas geográficas y Hubs por la que circula una operativa. Determina cómo se
      encadenan los Tramos entre origen, hubs y destino. Modelo ``tms.transport.plan``.

   Planning
      Segmentación operativa que agrupa las Órdenes que comparten una misma lógica de
      transporte: última milla, recogidas, distribución urbana, larga distancia… Se hereda
      del Proyecto y se propaga a Tramos, Paradas y Viajes. Se escribe siempre *Planning*, sin
      traducir, para no confundirlo con la actividad de planificar. Modelo ``tms.planning``.

   POD
      Prueba de entrega (*proof of delivery*). Puede ser **POD digital** (firma del
      destinatario en la pantalla del móvil) o **POD físico** (fotografía del albarán
      firmado). Se adjunta a la Parada y queda disponible para el Cliente.

   Proyecto
      Contenedor de configuración de una operativa o de un cliente: tarifa, Planning, tipos
      de servicio permitidos, división de ventas, comportamiento de la app y demás
      parámetros. Toda Orden pertenece a un Proyecto y hereda su configuración. Modelo
      ``project.project``.

   Reembolso
      Importe que el conductor debe cobrar al destinatario en el momento de la entrega y
      cuyo resultado (pagado, pagado en parte, no pagado) reporta desde la app. (No se dice
      *contra reembolso*, *COD* ni *cobro*.)

   Regla de preventivo
      Para un vehículo y un trabajo, cada cuántos kilómetros o días toca. El motor calcula su
      estado (al día, por vencer, vencido, no evaluada) a partir del último realizado y del
      kilometraje actual. Modelo ``tms.maintenance.rule``.

   Regla de tarifa
      Define **qué se mide** para tarificar (peso, bultos, kilómetros, pallets, metros…) y
      cómo se convierte, por ejemplo peso volumétrico. No fija precios: eso lo hacen las
      :term:`Líneas de tarifa <Línea de tarifa>`. Modelo ``tms.pricelist.rule``.

   Remitente
      Contacto de origen de la mercancía cuando no coincide con el Cliente que encarga el
      servicio. (No se dice *shipper*.) Modelo ``res.partner``.

   Tarea de mantenimiento
      Clasificación con la que el taller filtra las órdenes: Preventivo, Taller, Reparación,
      Gomería, Lavado, Engrase, Mejora... Modelo ``tms.maintenance.task``.

   Tarifa
      Conjunto de Líneas de tarifa que determina el precio de venta de las Órdenes de un
      Proyecto o el coste de compra de los Viajes de un Transportista. (No se dice
      *pricelist*.) Modelo ``tms.pricelist``.

   Tarifa base
      Escalado de precios por rangos que sirve de plantilla para generar Líneas de tarifa de
      forma automática. Modelo ``tms.pricelist.base``.

   Tiempo de servicio
      Duración estimada de una Parada según el tipo de operación, el contacto o el Proyecto.
      La planificación lo usa para calcular horarios. Modelo ``tms.service.time``.

   Tipo de Orden
   Tipo de Servicio
   Tipo de Parada
      Catálogos de configuración operativa que clasifican, respectivamente, la Orden (entrega,
      recogida, directo…), el servicio contratado (con sus variables logísticas) y la Parada
      (carga, descarga, hub…). (No se dice *tipo de expedición*.) Modelos
      ``tms.shipment.type``, ``tms.service.type`` y ``tms.stop.type``.

   Trabajo
      Lo que se hace en una orden de mantenimiento: cambio de aceite, filtro de aire, frenos. Es
      el tipo de servicio de la Flota de Odoo con tarea, material e intervalo por defecto. (No se
      dice *job* ni *tipo de servicio* para hablar del taller.) Modelo ``fleet.service.type``.

   Tramo
      Movimiento de una Orden entre un punto de carga y un punto de descarga. Una Orden
      puerta a puerta tiene un Tramo; una con paso por Hub, dos o más. Da origen a las
      Paradas. (No se dice *leg* ni *envío*.) Modelo ``tms.shipment.leg``.

   Transportista
      Empresa o autónomo que ejecuta Viajes por cuenta del operador y recibe la Orden de
      compra. (No se dice *carrier*, *proveedor* ni *colaborador*.) Modelo ``res.partner``.

   Trazabilidad
      Histórico de eventos de una Parada, un Tramo o una Orden: cada cambio de estado,
      escaneo, POD e incidencia, con fecha, autor y origen (app, backoffice o integración).
      Modelo ``tms.traceability``.

   Viaje
      Conjunto de Paradas que ejecuta un recurso (conductor y vehículo) en una salida.
      Materializa el coste del transporte y genera la Orden de compra al Transportista. En el
      manual del conductor se le llama **"tu ruta"**, que es como lo ve quien conduce. (En el
      resto de la documentación no se dice *ruta* ni *trip*.) Modelo ``tms.trip``.

   Zona de tarifa
      Agrupación de Áreas geográficas o de códigos postales a efectos de precio. Los detalles
      de las Líneas de tarifa fijan importes por zona de origen y de destino. (No se dice
      *zona tarifaria*.) Modelo ``tms.pricelist.zone``.
