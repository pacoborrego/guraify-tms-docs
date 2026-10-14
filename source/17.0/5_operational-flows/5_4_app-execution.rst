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
listan en la tabla de 5.4.4. El resultado depende de lo que se hace en la Parada:

- En una **carga** (recogida, recogida a domicilio o paso por hub), la mercancía queda cargada,
  cargada con reservas o no cargada (tabla de 5.4.4). Los Bultos se comprueban escaneando (ver
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

.. figure:: /_static/img/5_operational-flows/5_4_app-execution_03_registrar-trazabilidad.png
   :alt: Asistente Registrar trazabilidad de un Bulto

   Registrar trazabilidad: evento, Parada, fecha y resultado para uno o varios Bultos.

.. figure:: /_static/img/5_operational-flows/5_4_app-execution_01_paradas-estado-app.png
   :alt: Lista de Paradas con su estado

   Las Paradas en Odoo con su estado (borrador, completada) según lo que reporta la app.

5.4.4 Referencia técnica
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
