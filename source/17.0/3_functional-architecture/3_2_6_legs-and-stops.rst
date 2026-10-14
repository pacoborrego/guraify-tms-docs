3.2.6 Tramos y Paradas
----------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Maestros › Tramos, y TMS › Operaciones › Maestros › Paradas

El Tramo y la Parada son las dos entidades que están entre la Orden y el Viaje. El Tramo es la
unidad de movimiento de la Orden; la Parada, el evento físico que se planifica y se ejecuta. Las
dos nacen solas al validar la Orden o al cerrar el Manifiesto que la trae, y por eso viven en el
submenú **Maestros** de Operaciones: se consultan y se corrigen, pero en condiciones normales no
se crean a mano.

3.2.6.1 El Tramo
~~~~~~~~~~~~~~~~

El :term:`Tramo` (``tms.shipment.leg``) es el movimiento de la mercancía de una Orden entre un
punto de carga y un punto de descarga. Tiene dos lados simétricos, carga y descarga, cada uno
con su contacto, su fecha, su franja horaria, su hub y su agencia de referencia. De la Orden
hereda el Cliente, el Proyecto, el Planning, el tipo de servicio, la categoría de vehículo y la
Tarifa; de la División de ventas recibe su parte del importe de la Orden. Una Orden puerta a
puerta tiene un Tramo; una con paso por Hub, dos o más, encadenados por el hub que cierra uno y
abre el siguiente.

El Tramo no tiene un tipo propio: lo toma del :term:`Tipo de Orden` de su Orden, que lleva
cuatro marcas excluyentes con las etiquetas **Entrega**, **Recogida**, **Directo** y **Hub**.
De esa naturaleza depende casi todo lo que el sistema hace con el Tramo:

.. list-table::
   :header-rows: 1
   :widths: 16 44 40

   * - Tipo de Tramo
     - Qué representa
     - Qué completa el sistema al validar
   * - Entrega
     - Reparto desde el hub del Proyecto hasta el destinatario.
     - El lado de carga: el hub, la agencia y la franja de carga que fija el Proyecto.
   * - Recogida
     - Recogida en el remitente con destino al hub del Proyecto.
     - El lado de descarga: el hub, la agencia y la franja de descarga del Proyecto.
   * - Directo
     - Carga en origen y descarga en destino sin pasar por hub.
     - Nada: los dos lados vienen dados por la Orden.
   * - Hub
     - Movimiento cuyo punto de carga es un hub (arrastre o salida de hub).
     - El lado de descarga, como en la recogida.

A esas cuatro marcas se suman dos que no vienen del Tipo de Orden. La **recogida a domicilio**
la calcula la propia Orden: una Orden de recogida con un solo Tramo cuya carga es el punto de
recogida configurado en el Proyecto se trata como recogida a domicilio, y su Tramo se agrupa y
se planifica de forma distinta a una recogida ordinaria. La marca **Es transferencia** la lleva
el Tramo que representa un **arrastre** entre hubs (a una agencia o a un hub propio, ver
:ref:`arrastre`): ese Tramo no cuenta para el estado de la Orden ni recibe parte del importe de
venta.

Cada Tramo apunta a dos Paradas, la de carga y la de descarga, y de su tipo depende cuál de las
dos es su :term:`Parada activa <Tramo activo>` en cada momento, mecanismo que se explica en
:doc:`3_2_5_active-leg`. El Tramo lleva también su propio estado, con los mismos valores que la
Parada (ver :ref:`estados-parada`), que se deriva de su última anotación de
:term:`Trazabilidad`: validar la Orden lo deja *Validado*, despachar su Viaje lo pasa a
*Despachado*, y los eventos de la app lo hacen avanzar hasta un estado de cierre. Planificar la
Parada no mueve el Tramo (ver :ref:`ciclo-estados`).

3.2.6.2 La Parada
~~~~~~~~~~~~~~~~~

La :term:`Parada` (``tms.stop``) es el evento físico planificable: un contacto con coordenadas,
una fecha, una franja horaria y un tiempo de servicio, en el que un vehículo carga, descarga o
pasa por un hub. Es la unidad mínima de la planificación: el Optimizador de Paradas y el
asistente de asignación manual trabajan sobre Paradas, nunca sobre Órdenes ni Tramos, y un
Viaje no es más que una secuencia de Paradas. Una Parada pertenece como máximo a un Viaje y
agrupa uno o varios Tramos, que la usan como lado de carga o como lado de descarga.

Cada Parada lleva un :term:`Tipo de Parada` (``tms.stop.type``) que dice qué papel cumple en el
flujo. El sistema distingue seis papeles, cada uno definido por una marca del catálogo, y solo
puede haber un Tipo de Parada por papel y compañía:

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Papel (etiqueta de la marca)
     - Cuándo lo recibe una Parada
   * - Parada de Ruta
     - Carga de una recogida ordinaria o descarga de una entrega en el cliente: la parada que
       el conductor visita en su recorrido.
   * - Operaciones de Hub
     - Carga o descarga en un hub: la salida del hub de las entregas, la llegada de las
       recogidas y los arrastres entre hubs.
   * - Punto de Recogida
     - Carga de una recogida a domicilio.
   * - Recogida Directo
     - Carga de un Tramo directo.
   * - Entrega Directo
     - Descarga de un Tramo directo.
   * - Paradas Optimizador
     - Parada auxiliar que genera el Optimizador de Paradas; no cuenta para el estado del
       Viaje.

El Tipo de Parada decide si la Parada se puede asignar a un Viaje con el asistente, si aparece
en la app del conductor, si participa en la optimización y si recibe parte del coste del Viaje
(las paradas de hub no lo reciben). Su configuración, y las marcas que gobiernan cada
comportamiento, se describen en :doc:`/17.0/4_parametrization/4_1_operational-configuration`.

**Adjuntos.** La Parada y el Tramo, como la Orden y el Viaje, tienen una pestaña **Adjuntos** con
los ficheros que les tocan: las fotos y firmas de la prueba de entrega que hace el conductor (ver
:doc:`/17.0/5_operational-flows/5_4_app-execution`) y lo que suba la oficina. Se ven como
miniaturas que se abren en el visor al pulsarlas; el menú de cada una permite abrir su ficha,
descargarla o borrarla. **Adjuntar archivos**, encima de la lista, abre el asistente **Subir
adjuntos**, donde se arrastran o se eligen varios ficheros a la vez. Lo que se sube en la Parada
aparece también en su Viaje y en la Orden y el Tramo de la Parada (si la Parada reúne varias
Órdenes, solo en la primera); lo que se sube en el Tramo, en su Parada, su Orden y su Viaje. Las
pruebas de entrega de la app, en cambio, se enlazan al Tramo y la Orden del evento que las trae.

.. CAPTURA: 3_2_6_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_6_legs-and-stops_03_adjuntos.png
      :alt: Pestaña Adjuntos de una Parada con la firma y la foto del albarán

      Pestaña Adjuntos de una Parada: la prueba de entrega que hizo el conductor.

3.2.6.2.1 Agrupación de Tramos en Paradas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Varios Tramos pueden compartir una misma Parada. Al validar la Orden, o al cerrar el Manifiesto,
el sistema recorre los Tramos y genera para cada uno dos candidatos a Parada, el de carga y el
de descarga, con una clave que reúne el tipo de evento (según el tipo de Tramo y el lado), el
contacto de la dirección, la franja horaria, el Planning, el Proyecto y, si viene informado, el
nombre de viaje del fichero. Los candidatos con la misma clave se funden en un solo grupo. A
continuación se funden también los grupos compatibles cuyas franjas horarias se solapan al
menos una hora; la Parada resultante toma la franja común.

.. mermaid::

   flowchart TB
       O1["Orden 1"] --> L1a["Tramo 1<br/>carga en A"] & L1b["Tramo 1<br/>descarga en B"]
       O2["Orden 2"] --> L2a["Tramo 2<br/>carga en A"] & L2b["Tramo 2<br/>descarga en D"]
       O3["Orden 3"] --> L3a["Tramo 3<br/>carga en C"] & L3b["Tramo 3<br/>descarga en B"]
       L1a --> SA["Parada en A"]
       L2a --> SA
       L1b --> SB["Parada en B"]
       L3b --> SB
       L3a --> SC["Parada en C"]
       L2b --> SD["Parada en D"]

Tres Órdenes con un Tramo cada una dan seis lados de carga y descarga, pero solo cuatro
Paradas: las dos cargas en A y las dos descargas en B se funden, porque coinciden en lugar,
franja y clave de agrupación.

No todos los Tramos se consolidan igual. Las **entregas** y las **recogidas ordinarias** pueden
compartir Parada con Tramos de otras Órdenes, siempre que lleguen juntas en el mismo
Manifiesto; validar una Orden a mano solo consolida sus propios Tramos. Los Tramos **directos**,
los de paso por **hub** y las **recogidas a domicilio** solo se consolidan dentro de su propia
Orden. Por último, si la Orden ya tenía una Parada compatible (del mismo tipo, en el mismo
contacto, el mismo día y con el mismo nombre de viaje) cuya franja contiene la del grupo, los
Tramos se añaden a ella en vez de crear otra; así, revalidar una Orden no duplica Paradas.

Cuando el grupo necesita una Parada nueva, su Tipo de Parada sale del tipo de evento: el lado de
hub de una entrega o de una recogida recibe Operaciones de Hub, el lado de cliente recibe Parada
de Ruta, la carga de una recogida a domicilio recibe Punto de Recogida y los dos lados de un
Tramo directo reciben Recogida Directo y Entrega Directo. Esta consolidación es lo que evita
Paradas duplicadas en operativas densas y la razón de que un Viaje tenga menos Paradas que
Tramos.

.. mermaid::

   flowchart TB
       Q1{"¿Tramo directo?"} -->|"sí"| D["Recogida Directo<br/>y Entrega Directo"]
       Q1 -->|"no"| Q2{"¿Lado de hub?"}
       Q2 -->|"sí"| H["Operaciones de Hub"]
       Q2 -->|"no"| Q3{"¿Carga de una<br/>recogida a domicilio?"}
       Q3 -->|"sí"| C["Punto de Recogida"]
       Q3 -->|"no"| R["Parada de Ruta"]

.. _arrastre:

3.2.6.3 El arrastre
~~~~~~~~~~~~~~~~~~~

Un **arrastre** es el movimiento de mercancía de un hub a otro antes de la última milla: a una
**agencia** que reparte en su zona, o a un **hub propio** desde el que se optimizan después las
entregas. Lo crea el asistente Asignar (:doc:`/17.0/5_operational-flows/5_2_trip-generation`)
cuando se activa **Crear transferencia hub**, y tiene siempre la misma forma, sea cual sea el
destino:

.. mermaid::

   flowchart LR
       O["Hub de origen<br/><b>Parada de carga</b>"] -->|"Tramo del arrastre (HUB)<br/>expedición propia _ARR"| D["Hub de destino<br/><b>Parada de llegada</b>"]
       D --> R["<b>Parada de relevo</b><br/>(operación de hub)"]
       R -->|"Tramo de última milla<br/>(la expedición del cliente)"| C["Destinatario"]

- **Una expedición propia.** El arrastre es el único registro de ese movimiento, así que tiene su
  propia Orden, con la referencia de la Orden del cliente y el sufijo ``_ARR``, emitida a quien
  diga el Proyecto (**Contacto de la transferencia hub**, por defecto la propia compañía; ver
  :doc:`/17.0/4_parametrization/4_5_project-configuration`). Lleva las líneas de todo lo
  arrastrado y toma del Proyecto servicio, tipos y categoría de vehículo. Validarla a mano no la
  reconstruye.
- **Un solo Tramo, de tipo HUB**, de nuestro hub al de destino. Que sea de hub y no de entrega es
  lo que permite que el conductor de la última milla siga viendo en la app la expedición del
  cliente (ver :doc:`3_2_5_active-leg`): la línea del cliente comparte el Tramo del arrastre y el
  de su entrega, y el de hub no se le propone como activo.
- **Tres Paradas**, tipadas para que el optimizador las trate como un par recogida → entrega:
  la **carga** en el hub de origen y la **llegada** al hub de destino, como servicio directo, y el
  **relevo**, una operación de hub en el destino desde la que arranca la última milla. Llegada y
  relevo son dos Paradas a propósito: con una sola, al entrar las entregas en el Viaje de la
  agencia el arrastre dejaba de poderse planificar.
- **El movimiento se ve en la Orden del cliente**: al cargar queda *Cargada* y al llegar al hub de
  destino *En curso*, sin que la última milla cambie; los Bultos se escanean en las dos Paradas.

La diferencia entre los tres arrastres es **quién se queda la última milla**:

.. list-table::
   :header-rows: 1
   :widths: 22 26 26 26

   * -
     - Agencia
     - Hub propio
     - Recogida a domicilio
   * - Cuándo
     - **Enviar a agencia** con **Crear transferencia hub**
     - **Crear transferencia hub** con **Dejar la última milla sin planificar**
     - Lo crea el cierre del Manifiesto o la validación de la Orden
   * - Expedición del arrastre
     - La del arrastre (``_ARR``)
     - La del arrastre (``_ARR``)
     - La de recogida
   * - Tipo del Tramo
     - HUB
     - HUB
     - El del Proyecto
   * - Las Paradas van en un Viaje
     - No: las coloca la agencia
     - Carga y llegada sí, en el Viaje del arrastre (uno por hub de origen); el relevo no
     - No
   * - La última milla
     - Entra en el Viaje de la agencia
     - **Queda libre**, sin Viaje, con el hub de destino escrito en su Parada, para optimizarla
       desde allí
     - Carga en el hub

**El arrastre se deshace solo.** Quitar la Parada del cliente del Viaje de la agencia, borrar ese
Viaje o sacar una Orden del flujo revierte el envío: el Tramo del arrastre y las Paradas que ya no
hacen falta desaparecen, la expedición ``_ARR`` se queda solo con lo que sigue arrastrado y, si no
queda nada, se va con el Viaje. Para los envíos a agencia el sistema guarda una **foto previa** de
cada Parada y cada Tramo en el momento de enviarlos, con la que la reversión es exacta; esas fotos
se consultan en **TMS › Configuración › EDI › Envíos a agencia** (Agency Hand-overs) y desde el
botón de la Parada, y sobreviven al borrado del Viaje, con el nombre del Viaje y de la agencia
como texto. Si la agencia recibe las instrucciones por API, la reversión le avisa antes con sus
llamadas de cancelación y, si la agencia no lo acepta, no se revierte. Los envíos hechos antes de
que existieran las fotos se revierten con lo que se puede reconstruir, y lo que no (fechas, horas,
tipo de carga) queda anotado en el chatter.

.. figure:: /_static/img/3_functional-architecture/3_2_6_legs-and-stops_02_envios-agencia.png
   :alt: Lista Envíos a agencia (Agency Hand-overs)

   Envíos a agencia: una fila por Parada enviada, con su Viaje, su agencia y si se ha revertido.

.. _estados-parada:

3.2.6.4 Estados de la Parada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El estado de la Parada no se fija a mano: se deriva de la última anotación de Trazabilidad que
lleva estado, venga de la oficina (asignar a un Viaje, traspasar a una agencia), de la app del
conductor o de una integración. Junto al estado, la Parada conserva el último **evento** que
envió la app (en espera, en camino, en curso, cargado, ok, fallo…), que es más fino que el
estado y permite saber, por ejemplo, que el conductor va de camino aunque la Parada siga
abierta. Esos eventos y su correspondencia con los estados están en la tabla de referencia de
:doc:`/17.0/5_operational-flows/5_4_app-execution`. Cuando el Viaje de la Parada ya está
facturado, el estado deja de recalcularse.

Los estados se dividen en **abiertos**, mientras la Parada está pendiente de ejecutarse, y de
**cierre**, que dan por terminada la ejecución. El :term:`glosario <Estados de la Parada>`
fija los nombres con que esta documentación los cita; la última columna es la etiqueta que
muestra Odoo.

.. list-table::
   :header-rows: 1
   :widths: 18 50 14 18

   * - Estado
     - Significado
     - Tipo
     - Etiqueta en pantalla
   * - Sin planificar
     - Parada creada y sin Viaje. Es el único estado en que se puede borrar.
     - Abierto
     - Borrador
   * - Planificada
     - Asignada a un Viaje que aún no se ha despachado. Quitarla del Viaje la devuelve a Sin
       planificar; el asistente de asignación la acepta mientras nadie la haya reportado.
     - Abierto
     - Planificado
   * - Despachada
     - Su Viaje se ha despachado: es el estado con el que llega a la app del conductor o a la
       agencia (ver :ref:`ciclo-estados`).
     - Abierto
     - Despachado
   * - En curso
     - El conductor la tiene activa en la app: en espera, en camino o en el punto.
     - Abierto
     - En curso
   * - Cargada
     - La mercancía se ha cargado; la Parada sigue abierta hasta que se cierre la descarga.
     - Abierto
     - Cargado
   * - Completada
     - Ejecutada sin incidencias.
     - Cierre
     - Completada
   * - Con reservas
     - Ejecutada con incidencias anotadas (bultos dañados o ausentes, rechazo parcial…).
     - Cierre
     - Con reservas
   * - Fallida
     - No se pudo ejecutar.
     - Cierre
     - Fallida
   * - Reprogramada
     - Se volverá a intentar en otra fecha.
     - Cierre
     - Reprogramado
   * - Devuelta
     - La mercancía se ha devuelto.
     - Cierre
     - Devuelto
   * - Cancelada
     - Anulada.
     - Cierre
     - Cancelado

Los seis estados de cierre son los que el sistema mira para cerrar lo que está por encima: cuando
todas las Paradas de un Viaje están cerradas, el Viaje se completa o queda por validar
(:doc:`3_2_2_trips`), y cuando todos los Tramos de una Orden están cerrados y el actual terminó
en un desenlace, la Orden queda pendiente de confirmar (:doc:`3_2_1_orders`). Cómo encajan los
cuatro niveles está en :ref:`ciclo-estados`. El detalle de ese cierre está en
:doc:`/17.0/5_operational-flows/5_5_trip-closing`.

.. figure:: /_static/img/3_functional-architecture/3_2_6_legs-and-stops_01_parada.png
   :alt: Formulario de una Parada con su Tipo de Parada, sus Tramos y su estado

   Formulario de una Parada: Tipo de Parada, Tramos agrupados y estado.

3.2.6.5 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Campo
   * - Tipo del Tramo (heredado del Tipo de Orden)
     - ``tms.shipment.leg.is_delivery``, ``is_collection``, ``is_direct``, ``is_hub``
       (relacionados de ``shipment_type_id``)
   * - Recogida a domicilio y transferencia
     - ``tms.shipment.leg.is_home_collection`` (de ``sale.order.is_home_collection``),
       ``tms.shipment.leg.is_transfer``
   * - Paradas de carga y de descarga del Tramo
     - ``tms.shipment.leg.load_stop_id``, ``unload_stop_id``
   * - Estado y evento del Tramo
     - ``tms.shipment.leg.state``, ``event`` (de ``leg_traceability_ids``)
   * - Tramos de la Parada
     - ``tms.stop.legs_ids`` (y ``load_legs_ids``, ``unload_legs_ids`` por lado)
   * - Tipo de Parada
     - ``tms.stop.stop_type``; marcas de ``tms.stop.type``: ``is_route_stop``,
       ``is_hub_operation``, ``is_home_collection``, ``is_direct_collection``,
       ``is_direct_delivery``, ``is_optimizator_stop``
   * - Estado, evento y motivo de la Parada
     - ``tms.stop.state``, ``event``, ``reason_id`` (de ``stop_traceability_ids``)
   * - Estados abiertos
     - ``draft`` (Sin planificar), ``in_process`` (Planificada), ``processed`` (Despachada),
       ``running``, ``loaded``; en el Tramo, ``in_process`` es Validado
   * - Estados de cierre
     - ``completed``, ``reserves``, ``failed``, ``rescheduled``, ``returned``, ``canceled``
   * - Agrupación de estados para los tableros
     - ``tms.stop.state_group`` (``pending``, ``done``, ``reserves``, ``failed``, ``canceled``)
   * - ETA de la Parada
     - ``tms.stop.eta`` (el actual), ``eta_planned`` (el prometido), ``eta_drift_min`` (calculado:
       actual menos prometido), ``eta_source``, ``eta_updated_at``, ``eta_stale``,
       ``eta_traffic_delay_min``, ``eta_violated``
   * - Histórico de ETA
     - ``tms.stop.eta.history`` (``eta``, ``source``, ``recorded_at``, ``traffic_delay_min``,
       ``violated``, ``position_lat``, ``position_lon``); se purga a los 180 días (parámetro
       ``tms.eta_history_retention_days``)
   * - Tramo de ruta que termina en la Parada
     - ``tms.stop.distance``, ``drivingTime``, ``route_leg_*``, ``co2e_wtw_kg``, ``co2e_ttw_kg``;
       los acumulados desde la salida, en ``distance_from_start_km`` y
       ``driving_time_from_start_h``
   * - Adjuntos
     - ``ir.attachment`` con ``stop_id``, ``leg_id``, ``sale_order_id``, ``trip_id`` y
       ``traceability_id`` (más ``modal_type``, ``recipient_name``, ``recipient_ID_card`` en las
       pruebas de entrega); pestaña ``tms_attachment_ids``; asistente
       ``tms.attachment.upload.wizard``
