5.4 Ejecución desde la app
--------------------------

.. admonition:: Dónde ocurre
   :class: tip

   En la **app móvil del conductor**, no en el backend de Odoo. Las pantallas y el uso paso a
   paso están en el :doc:`Manual del conductor </17.0/10_manual_app/index>`; aquí se explica
   qué le llega al conductor y qué hace cada evento suyo en el TMS.

5.4.1 Despachar el Viaje
~~~~~~~~~~~~~~~~~~~~~~~~

El conductor no ve todos los Viajes que tiene asignados, sino los que el planificador ha
**despachado**. El botón **Despachar** de un Viaje planificado (``tms.trip``) decide por sí solo
a quién van las instrucciones, según el tipo de Viaje:

- **Al conductor**, por la app. Es el caso general, también para el arrastre a un hub propio.
  Exige que el Viaje tenga conductor; la app lee el Viaje en vivo, así que despachar es la
  marca. Mientras el sistema de seguimiento externo siga en medio, el Viaje se le envía también
  a él, con la conexión configurada en la compañía.
- **A la agencia**, cuando el Viaje es un traslado a una agencia ajena (ver
  :doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`). Si el Proyecto de la agencia
  tiene configuradas llamadas de despacho (:doc:`Guía del integrador
  </17.0/7_edi-integrations/7_4_endpoint-configuration>`), se ejecutan en orden, las de Viaje
  sobre el Viaje y las de Parada sobre cada Parada; si la agencia no tiene API, el despacho se
  anota como **manual** y las instrucciones viajan fuera de Odoo.

Al despachar, Viaje, Paradas, Tramos y Órdenes pasan a **Despachado** (:ref:`ciclo-estados`),
la orden de compra se marca enviada y el Viaje guarda la **fecha**, el **canal** (app, Axylog,
API de la agencia o manual) y el **resultado** del envío. Si el envío falla, el Viaje queda con
un aviso rojo y el error, sin cambiar de estado: las llamadas que sí se hicieron quedan en el
registro de actividad de las APIs del Viaje y un Viaje que falla no para a los demás de la
selección. Desde entonces conductor, vehículo, remolques, transportista y agencia quedan en solo
lectura (:ref:`viaje-validacion`), y cualquier Parada que entre en el Viaje se despacha con él.
**Reenviar** repite el envío al mismo destino, por ejemplo tras cambiar una Parada; la lista de
Viajes avisa de los que tienen instrucciones pendientes de reenviar.

Despachar también ocurre sin pulsar el botón. Al asignar Paradas a una agencia con el asistente
(:doc:`5_2_trip-generation`), el Viaje nuevo se despacha en el mismo acto si la agencia recibe
las instrucciones por API o si el Proyecto tiene activado **Procesar viaje de agencia
automáticamente**; si no, se queda planificado hasta que alguien pulse Despachar.

Antes de despachar es cuando se imprime la **hoja de ruta** del Viaje: **Imprimir › Manifiesto
de transporte** saca la hoja de ruta (teléfonos, zona operativa, recogidas, bultos y palés por
temperatura) o el manifiesto clásico, según lo que la compañía haya elegido en Ajustes › TMS ›
Informes; las compañías que ya existían siguen con el clásico hasta que lo cambien.

La app, al iniciar sesión o al refrescar, carga el Viaje **despachado o en curso más reciente**
del conductor con todo lo que necesita para trabajar sin conexión: las Paradas en orden con sus
Tramos, líneas, Bultos y Reembolsos; los perfiles de la app y sus motivos de incidencia (ver
:doc:`/17.0/4_parametrization/4_5_project-configuration`); las coordenadas y el trazado; y las
métricas del recorrido.

.. CAPTURA: 5_4_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_4_app-execution_02_despacho.png
      :alt: Viaje despachado con su grupo Despacho

      Un Viaje despachado: el botón Reenviar y el grupo Despacho con fecha, canal y resultado.

5.4.2 El ciclo de una Parada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El conductor avanza Parada a Parada. En cada una, la app registra el mismo ciclo: la Parada
está en espera, el conductor indica que va en camino, al llegar la pone en curso y, al
terminar, registra el **resultado**. Estos pasos intermedios son los estados de la app, que se
listan en la tabla de 5.4.5. El resultado depende de lo que se hace en la Parada:

- En una **carga** (recogida, recogida a domicilio o paso por hub), la mercancía queda cargada,
  cargada con reservas o no cargada (tabla de 5.4.5). Los Bultos se comprueban escaneando (ver
  :doc:`/17.0/1_introduction/1_4_technological-architecture`).
- En una **entrega**, la Parada queda **Completada**, **Con reservas** o **Fallida** (ver
  :term:`Estados de la Parada`). La app pide la :term:`prueba de entrega (POD) <POD>` (firma en
  pantalla o foto del albarán firmado), el motivo cuando hay reservas o la entrega falla, el
  cobro del Reembolso si lo hay, y permite comentarios y fotos.
- En una **Parada de hub**, se registra la entrada o la salida de la mercancía del hub.

Una Parada puede agrupar Tramos de varias Órdenes. El resultado se aplica a la Parada y, salvo
que el conductor lo indique Tramo a Tramo, a todos sus Tramos que no estuvieran ya cerrados.

5.4.3 Qué hace cada evento en el TMS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada evento de la app llega a Odoo y se guarda como un apunte de :term:`Trazabilidad` sobre la
entidad afectada (Parada, Tramo, Bulto o reembolso) con todo su contexto: fecha y hora,
conductor, coordenadas y precisión del GPS, dispositivo y sistema operativo, batería, tipo de
red, motivo, comentario, importe cobrado y adjuntos. A partir de ese apunte el sistema
actualiza la estructura, en este orden:

#. La **Parada** toma el estado que corresponde al evento y lo hereda cada uno de sus **Tramos**
   que no estuviera ya en un estado de cierre.
#. La **Orden** refleja el estado de su tramo activo (ver
   :doc:`/17.0/3_functional-architecture/3_2_5_active-leg`): el planificador ve avanzar la
   Orden sin que nadie la toque.
#. El **Viaje** recalcula su estado a partir de sus Paradas; cuando la última se cierra, arranca
   el cierre (:doc:`5_5_trip-closing`).
#. Si hay integraciones de salida configuradas, el evento se envía al sistema del cliente
   (:doc:`Guía del integrador </17.0/7_edi-integrations/index>`).

El resultado, por tanto, se registra **una sola vez** y los demás niveles lo heredan. El
esquema muestra de dónde toma cada uno su estado y qué pasa con los dos resultados que no
terminan la Orden:

.. mermaid::

   flowchart LR
       A["Evento de la app<br/>(o de la oficina)"] --> S["Parada<br/>resultado individual"]
       S -->|"heredan los Tramos<br/>no cerrados"| L["Tramo"]
       B["Bulto con incidencia"] -. "Con reservas" .-> L
       L -->|"hereda del tramo activo"| O["Orden"]
       S -->|"hereda de todas<br/>sus Paradas"| T["Viaje"]
       L -->|"Reprogramado"| N["Tramo nuevo<br/>y Parada nueva,<br/>sin planificar"]
       N --> O
       L -->|"Devuelto"| R["Mercancía de vuelta<br/>en el remitente"]

Dos resultados mantienen la Orden abierta aunque la Parada se cierre. **Reprogramado** deja el
Tramo cerrado y crea otro con una Parada nueva, pendiente de planificar: el tramo activo pasa
al nuevo y la Orden sigue en marcha (:doc:`5_5_trip-closing`). **Devuelto** es para la entrega
que falló, volvió al almacén y el cliente quiere de vuelta en sus instalaciones (o viene a
buscarla): cierra el Tramo anotando que la mercancía está en el remitente. Hoy ese movimiento
de vuelta no genera por sí solo un Tramo ni una Parada: se gestiona como una Orden nueva. El
resto de resultados (Completado, Con reservas, Fallido) cierran el Tramo y, cuando era
el último, dejan la Orden lista para confirmarse (ver :ref:`ciclo-estados`).

Si el mismo evento llega dos veces (la app reintenta cuando no tiene cobertura), se procesa
una sola. Si Odoo rechaza un evento por una regla de negocio, la app se lo dice al conductor
en el momento.

**Entrega parcial.** Un Tramo no se cierra como Completado si arrastra Bultos que nadie ha
reportado como gestionados: el sistema lo deja **Con reservas** con el motivo automático
**A17 «No se han entregado todos los bultos»** y un comentario con los Bultos que faltan. Es
una red de seguridad para el conductor que confirma la entrega sin haber comprobado todos los
Bultos; el motivo viaja a las integraciones como cualquier otro, y el conductor lo ve en su
ruta (:doc:`/17.0/10_manual_app/10_7_incidents`).

**Los Bultos.** Cada Bulto lleva su propia traza de dónde está, que la app escribe al escanear y
el sistema completa al cerrar la Parada. Su ciclo son cuatro eventos:

.. mermaid::

   flowchart LR
       C["Recogida<br/>en casa del cliente"] -->|"el conductor lo lleva"| H["Entrada en el hub"]
       H -->|"en el hub"| L["Carga en el vehículo<br/>(salida del hub)"]
       L -->|"el conductor lo lleva"| D["Entrega<br/>en el destinatario"]
       D -. "no entregado" .-> H

Lo que la app no escanea se registra desde la oficina con el asistente **Registrar
trazabilidad** del Bulto (botón en su ficha y acción sobre varios a la vez): pide el evento
(recogida en domicilio, entrada en hub, carga, entrega), opcionalmente la Parada (solo las de
los Tramos de su línea, arrastre incluido), la fecha y, con la app instalada, el resultado, el
motivo y un comentario. Dónde queda el Bulto lo calcula el sistema con la misma regla que el
cierre de Parada: si sale, va con quien lo lleva; si llega o se entrega, se queda en el sitio.
El asistente **solo mueve el Bulto**: el estado del Tramo, la Parada, el Viaje y la Orden lo
mueven los eventos de Parada (Establecer evento o la app). No admite un Viaje completado ni una
Orden facturada, ni el resultado Devuelto, para el que no hay regla de dónde queda el Bulto.

**Cerrar desde la oficina.** El asistente **Establecer evento** de la Parada (Acciones
operativas) registra el mismo resultado que la app, pero **sin posición**: la traza de oficina
no lleva coordenadas ni dispositivo inventados, de modo que quien mire después desde dónde se
reportó una entrega no encuentre al conductor «en la puerta» cuando fue la oficina quien cerró.

**Las pruebas de entrega en Odoo.** Las fotos que hace el conductor (albarán firmado, mercancía,
recibo de un cobro) y la firma en pantalla, con el nombre y el documento de quien firma, llegan
como **adjuntos** de la Parada donde se hicieron, enlazados también a su Tramo, su Orden y su
Viaje. Se ven en la pestaña **Adjuntos** de cualquiera de las cuatro fichas, como miniaturas
que se abren en el visor de Odoo al pulsarlas, y en el historial (chatter) de cada una, con el
mensaje del evento. El fichero se guarda una sola vez aunque aparezca en cuatro sitios. El apunte
de Trazabilidad del evento tiene también su pestaña Adjuntos.

.. figure:: /_static/img/5_operational-flows/5_4_app-execution_03_registrar-trazabilidad.png
   :alt: Asistente Registrar trazabilidad de un Bulto

   Registrar trazabilidad: evento, Parada, fecha y resultado para uno o varios Bultos.

.. figure:: /_static/img/5_operational-flows/5_4_app-execution_01_paradas-estado-app.png
   :alt: Lista de Paradas con su estado

   Las Paradas en Odoo con su estado (borrador, completada) según lo que reporta la app.

5.4.4 Seguir la ETA durante la ejecución
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   Viaje › pestañas **ETA y ruta** y **Mapa** · Parada › pestañas **Puntualidad** (grupo **ETA:
   promesa y desviación**) e **Histórico de ETA**

.. CAPTURA: 5_4_04 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_4_app-execution_04_eta-y-ruta.png
      :alt: Pestaña ETA y ruta de un Viaje

      Pestaña ETA y ruta: el último recálculo, la ruta de PTV, peajes, coste, violaciones y
      emisiones.

Mientras el Viaje está en la calle, la hora prevista de llegada (:term:`ETA`) de las Paradas que
quedan se vuelve a calcular. Cuándo lo decide la :term:`Política operativa` de la compañía o del
Proyecto (:ref:`politica-operativa`): por defecto, cada vez que se cierra una Parada; también
puede hacerse cada cierto número de minutos, ambas cosas, o nunca. El cálculo es el de PTV y
cuesta una llamada, por eso la política fija un espaciado mínimo y un tope diario.

**Hoy el recálculo parte de la última Parada cerrada, no de la posición del vehículo.** La app
del conductor todavía no envía su posición y no hay otra fuente de telemática conectada (ver
:ref:`17.0/1_introduction/1_4_technological-architecture:1.4.6 Evolución prevista`), así que PTV
calcula la llegada a lo pendiente desde la Parada que se cerró la última, contando el tiempo de
servicio que se pasó en ella. Si el conductor va con retraso entre dos Paradas, el ETA no lo
recoge hasta que cierra la siguiente.

En la pestaña **ETA y ruta** del Viaje:

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Grupo
     - Qué dice
   * - **Recalcular ETA ahora**
     - El botón pide el recálculo en el momento, sin esperar a la tarea programada. La política
       se aplica igual: si está desactivada, si el último recálculo fue hace menos del espaciado
       mínimo o si se ha alcanzado el tope del día, no se hace, y un aviso lo dice.
   * - Recálculo
     - Cuándo fue el último, cuántos van hoy, si hay uno pedido y esperando, por qué se pidió y,
       si falló, el error.
   * - Ruta PTV
     - El identificador de la ruta en PTV y cuándo se calculó. PTV lo guarda doce horas: mientras
       sirve, el recálculo es el barato; después, se calcula la ruta de nuevo.
   * - Última posición conocida
     - Fecha, origen y coordenadas de la última posición del vehículo. Hoy, vacío.
   * - Peajes, Coste de ruta (PTV)
     - Los peajes del Viaje y el coste de la ruta que estima PTV, desglosado en distancia,
       tiempo, peajes y energía.
   * - Violaciones y zonas
     - Si la ruta incumple alguna restricción del vehículo (y cuántas) y el desnivel acumulado.
   * - Emisiones
     - El esquema aplicado, el CO₂ del pozo a la rueda y del depósito a la rueda, y el consumo.
   * - Informe del Viaje (en la interfaz, «Viaje Informe»), Totales, Zonas
     - Conducción, servicio, espera y pausas; las cantidades del Viaje; las zonas operativas que
       recorre.

En cada **Parada**, la pestaña **Puntualidad** enfrenta la hora planificada, la ETA en vivo y la
hora ejecutada, y el grupo **ETA: promesa y desviación** distingue dos ETA:

- El **Prometido** es el de la planificación. Lo fija el primer cálculo de ruta y ningún recálculo
  lo mueve: es la hora que se dio al cliente.
- El **Actual** es el último recálculo. La **Desviación (min)** es la diferencia entre los dos
  (positiva, más tarde de lo prometido);
  **Origen** dice qué produjo el actual (el plan, un recálculo a mano, el cierre de una Parada, el
  intervalo); **Retraso por tráfico** es lo que PTV atribuye al tráfico; **Sin ruta válida**
  avisa de que PTV no encontró ruta para el vehículo hasta esa Parada.
- **Caducado** marcado significa que el último recálculo falló y la ETA que se ve es la anterior,
  conservada a propósito: un fallo de PTV no borra ninguna hora.

La pestaña **Histórico de ETA** de la Parada guarda cada recálculo con su fecha, la ETA, el
origen, el retraso por tráfico y, cuando la haya, la posición desde la que se calculó; arriba,
los datos del tramo de ruta que termina en ella (kilómetros, CO₂, peaje, desnivel). El histórico
se conserva 180 días. La pestaña **Mapa** del Viaje dibuja todo esto sobre el mapa
(:ref:`17.0/3_functional-architecture/3_2_2_trips:3.2.2.5 El mapa del Viaje`).

5.4.5 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

La Parada tiene dos campos de estado. El **estado de la Parada** (``state`` de ``tms.stop``) es
el del glosario: los estados abiertos y los seis de cierre, que se describen en
:doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`. El **estado de la app**
(``app_state``) registra el paso en que está el conductor dentro de la Parada y el resultado
que ha reportado; es el que llega con cada evento y del que el sistema deriva el estado de la
Parada. Estos son los estados de la app y cómo se nombran en esta documentación:

.. list-table::
   :header-rows: 1
   :widths: 22 30 48

   * - Código
     - Etiqueta en Odoo
     - Nombre en la documentación
   * - ``standby``
     - Modo de espera
     - En espera
   * - ``on_way``
     - En camino
     - En camino
   * - ``running``
     - En curso
     - En curso
   * - ``lo_ok``
     - Cargado
     - Cargada
   * - ``lo_ok_reserve``
     - Reserva cargada
     - Cargada con reservas
   * - ``lo_failed``
     - No cargado
     - No cargada
   * - ``ok``
     - Completada
     - Completada
   * - ``ok_reserve``
     - Con reservas
     - Con reservas
   * - ``failed``
     - Fallida
     - Fallida
