3.2.5 Tramo activo y Parada activa
==================================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Órdenes (la cabecera de la Orden muestra los datos del
   tramo activo)

Una Orden (``sale.order``) puede contener varios Tramos (``tms.shipment.leg``) y cada
Tramo, a su vez, varias Paradas (``tms.stop``). Sin embargo, la cabecera de la Orden
—lugares, fechas, ventanas horarias, estado, importe— **no muestra todos los tramos a la
vez, sino siempre uno solo: el tramo activo**. Entender este mecanismo es clave para no
confundirse al leer una Orden multitramo: lo que se ve "se mueve" a medida que avanza la
ejecución.

3.2.5.1 La cadena: Parada activa → Tramo activo → Orden
-------------------------------------------------------

El concepto se apoya en tres campos calculados que se encadenan:

- **Parada activa del Tramo** (``tms.shipment.leg.active_stop``): cada Tramo determina
  cuál de sus Paradas es la "que toca ahora", según su tipo:

  - Tramo de **entrega** → su Parada de descarga.
  - Tramo de **recogida**, **recogida a domicilio** o **paso por hub** → su Parada de
    carga.
  - Tramo **directo** → la Parada de **carga** mientras siga abierta (estados borrador, en
    proceso, procesada, cargada o en ruta) y, en cuanto esta se cierra, **salta** a la
    Parada de **descarga**.

- **Tramo activo de la Orden** (``sale.order.active_leg``): la Orden elige como activo el
  Tramo marcado como tal (``is_active``). Si no hay ninguno marcado pero solo existe un
  Tramo no domiciliario, ese se toma como activo; si no hay un candidato claro, la Orden
  se queda sin tramo activo.

- **Parada activa y Viaje activo de la Orden**: derivan por relación del tramo activo —
  ``active_stop`` es la parada activa de ese tramo y ``active_trip``
  (``tms.trip``) es el Viaje de esa parada.

Como consecuencia, **el estado operativo de la Orden se toma del tramo activo**: la Orden
no inventa su estado, lo refleja del Tramo que está en curso.

.. mermaid::

   flowchart LR
       O["Orden (sale.order)"] -->|active_leg<br/>is_active| L["Tramo activo<br/>(tms.shipment.leg)"]
       L -->|active_stop<br/>según tipo/estado| S["Parada activa<br/>(tms.stop)"]
       S -->|trip_id| T["Viaje activo<br/>(tms.trip)"]
       L -. "lugares · fechas · estado · importe" .-> O

3.2.5.2 Por qué la información "se mueve"
----------------------------------------

Dado que la cabecera de la Orden refleja el tramo activo, la información que muestra cambia
conforme avanza la operación: cuando el tramo activo se completa y otro pasa a estar
activo, los lugares, las fechas y el estado que se ven en la Orden son ya los del nuevo
tramo. No es que los datos "desaparezcan": siguen en cada Tramo, pero la Orden solo
proyecta los del tramo activo en cada momento.

Esto es lo que permite que una operación compleja (varios tramos, arrastres entre hubs,
última milla) se lea en la cabecera de la Orden como una única foto coherente del "ahora",
sin perder el detalle, que permanece accesible tramo a tramo.

3.2.5.3 Ejemplo: un tramo directo
----------------------------------

Supongamos una Orden con un único Tramo **directo** (recogida en origen y entrega en
destino, sin paso por hub):

#. Al crearse, la Parada de **carga** está abierta (borrador/en proceso). El tramo activo
   apunta a ella, así que la Orden muestra el **lugar y la ventana de carga** y el estado
   de esa parada.
#. El conductor ejecuta la carga y la Parada de carga pasa a un estado de cierre. En ese
   momento, la parada activa del tramo **salta automáticamente a la Parada de descarga**.
#. La cabecera de la Orden pasa entonces a mostrar el **lugar y la ventana de descarga** y
   el estado de la entrega, sin que nadie cambie nada a mano.

El mismo principio se aplica con varios tramos: el tramo marcado como activo determina qué
ve la Orden, y dentro de él, la parada activa determina si lo que se muestra es la fase de
carga o la de descarga.

.. note::

   Estos campos (``active_leg``, ``active_stop``, ``active_trip``) son la base de otras
   vistas del sistema: el estado operativo de la Orden (:doc:`3_2_1_orders`) y el indicador
   KPI de la Orden (:doc:`/17.0/5_operational-flows/5_11_kpi-indicators`) se construyen a
   partir de la parada activa.

.. CAPTURA: 3_2_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_5_active-leg_01_tramo-activo.png
      :alt: Cabecera de una Orden mostrando los datos del tramo activo

      Cabecera de una Orden multitramo mostrando los datos del tramo activo.
