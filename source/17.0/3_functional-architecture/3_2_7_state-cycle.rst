.. _ciclo-estados:

3.2.7 El ciclo de estados en todos los niveles
----------------------------------------------

Cada entidad del modelo lleva su estado, y cada sección lo describe para la suya: la Orden en
:doc:`3_2_1_orders`, el Viaje en :doc:`3_2_2_trips`, el Tramo y la Parada en
:doc:`3_2_6_legs-and-stops`. Esta sección los pone **uno al lado del otro**: qué momento de la
operación mueve cada nivel y hasta dónde. Es la que hay que tener delante cuando una Orden dice
una cosa y su Viaje otra.

3.2.7.1 Tres reglas
~~~~~~~~~~~~~~~~~~~

Los estados no se escriben a mano: el sistema los deriva de la última anotación de
:term:`Trazabilidad` de cada entidad (Tramo y Parada), del tramo activo (Orden) y de las Paradas
(Viaje). Tres reglas gobiernan el ciclo:

#. **Planificar mueve solo la Parada.** Asignarla a un Viaje la deja **Planificada**; quitarla
   del Viaje la devuelve a **Sin planificar**. La Orden y el Tramo no se enteran: siguen en
   **Validado** desde que se validó la Orden o se cerró el Manifiesto. Por eso borrar un Viaje
   nunca deja una Orden sin validar.
#. **Despachado solo lo escribe el despacho.** El botón **Despachar** del Viaje (ver
   :doc:`/17.0/5_operational-flows/5_4_app-execution`) es el único que lleva a **Despachado**, y
   lo hace en los cuatro niveles a la vez: Viaje, Paradas, Tramos y Órdenes. Una Parada que
   entra en un Viaje ya despachado se despacha con él.
#. **«¿Está planificada?» se mira en el Viaje, no en el estado.** Una Parada está planificada si
   tiene Viaje. El estado la acompaña, pero la pregunta que hacen el asistente de asignación, el
   Optimizador de Paradas y las guardas de borrado es si la Parada tiene Viaje y si ese Viaje
   está aún sin despachar.

3.2.7.2 La matriz: qué mueve cada momento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada fila es un momento de la operación; cada columna, un nivel. Una celda vacía significa que
ese momento no toca ese nivel. Los nombres son los de esta documentación; la etiqueta que muestra
Odoo está en la referencia técnica de cada sección.

.. list-table::
   :header-rows: 1
   :widths: 17 11 15 15 14 14 14

   * - Momento
     - Manifiesto
     - Pedido de venta
     - Orden y Tramo
     - Parada
     - Viaje
     - Orden de compra
   * - **Crear la Orden** (a mano, por fichero o por API)
     - Abierto
     - Presupuesto
     - Borrador
     -
     -
     -
   * - **Validar la Orden / Cerrar el Manifiesto** (nacen las Paradas)
     - Cerrado
     - Presupuesto enviado
     - **Validado**
     - Sin planificar
     -
     -
   * - **Planificar** (la Parada entra en un Viaje)
     -
     -
     - Validado
     - **Planificada**
     - Planificado
     - Solicitud de presupuesto
   * - **Despachar** (el Viaje sale al conductor o a la agencia)
     -
     -
     - **Despachado**
     - **Despachada**
     - **Despachado**
     - Solicitud enviada
   * - **El conductor actúa** (en camino, en el punto, carga)
     -
     -
     - En curso · Cargado
     - En curso · Cargada
     - **En curso**
     -
   * - **Resultado** (todas las Paradas cerradas)
     -
     - Pedido de venta
     - Completado · Con reservas · Fallido · Reprogramado · Devuelto · Cancelado
     - los mismos
     - **Por validar** (si el Proyecto pide revisión) · Completado · Fallido
     - Pedido de compra, bloqueada · Cancelada si el Viaje falla

Tres lecturas de la matriz:

- **La Orden y el Tramo se quedan en Validado mientras se planifica.** Lo que cambia entre
  «validar» y «despachar» es solo la Parada (y el Viaje, que existe desde que tiene Paradas).
- **El pedido de venta va por detrás.** Validar la Orden la deja en *Presupuesto enviado* (sin
  enviar ningún correo: es solo el estado); reabrir el Manifiesto la devuelve a *Presupuesto*.
  Pasa a *Pedido de venta* cuando todos sus Tramos están cerrados **y el Tramo actual terminó en
  Completado, Con reservas o Fallido**: una entrega reprogramada espera al siguiente intento. Lo
  hace la tarea programada de tarificación, no el evento de la app, por lo que hay unos minutos
  de desfase (:doc:`/17.0/5_operational-flows/5_6_settlement`).
- **El Viaje tiene dos estados que los demás no tienen.** *En curso* aparece en cuanto el
  conductor (o la API de la agencia) toca una Parada, aunque el Viaje no se hubiera despachado.
  *Por validar* solo existe en los Proyectos que exigen revisar el Viaje antes de facturar; el
  resto pasa directamente a *Completado* (ver :doc:`/17.0/5_operational-flows/5_5_trip-closing`).

3.2.7.3 La escalera del Viaje y sus vueltas atrás
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El Viaje sube por una escalera fija, y cada peldaño que se sube a mano tiene su botón para
bajarlo. La cabecera del Viaje solo muestra el botón que se puede pulsar en ese estado.

.. mermaid::

   flowchart LR
       D["Sin Paradas"] --> P["Planificado"]
       P -->|"Despachar"| S["Despachado"]
       S -->|"el conductor actúa"| R["En curso"]
       R -->|"todas las Paradas cerradas"| V["Por validar"]
       V -->|"Validar"| C["Completado"]
       R -->|"todas las Paradas cerradas,<br/>sin revisión"| C
       R -->|"todas fallidas"| F["Fallido"]
       S -. "Revertir despacho" .-> P
       C -. "Revertir validación" .-> V
       S -. "Cancelar viaje" .-> P
       R -. "Cancelar viaje<br/>(salen las Paradas no servidas)" .-> C

- Un Viaje **sin Paradas de ruta no existe**: cuando se le quita la última, se borra, salvo que
  su Orden de compra esté confirmada o facturada.
- **Revertir despacho** solo se admite en *Despachado*: en *En curso* el conductor ya ha actuado.
  Devuelve las Paradas a Planificada y los Tramos a Validado y, si el Viaje era de agencia, avisa
  a la agencia; si la agencia no lo acepta, no se revierte.
- **Cancelar viaje** no es un estado: las Paradas que nadie ha servido salen del Viaje y vuelven
  a Sin planificar. Si no se sirvió ninguna, el Viaje desaparece con su Orden de compra; si
  alguna se sirvió, el Viaje se queda con ellas y cierra con ellas, porque eso se paga.
- **Revertir validación** devuelve un Viaje completado a *Por validar* (o lo reabre, si el
  Proyecto no pide revisión) y su Orden de compra a solicitud de presupuesto. No es posible con
  la Orden de compra facturada.
- Si el conductor **reabre una Parada** cerrada, el Viaje vuelve a *En curso* por sí solo y la
  Orden de compra, a solicitud; es la reapertura automática de
  :doc:`/17.0/5_operational-flows/5_5_trip-closing`.
- Un Viaje cuya Orden de compra está **facturada** no se recalcula ni se borra.

3.2.7.4 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~~~

Los códigos son los mismos en los cuatro niveles hasta el despacho; la etiqueta cambia según
el nivel. Un mismo código, ``in_process``, se lee *Validado* en la Orden y el Tramo y
*Planificado* en la Parada y el Viaje.

.. list-table::
   :header-rows: 1
   :widths: 16 22 22 22 18

   * - Código
     - Orden (``tms_status``) y Tramo (``state``)
     - Parada (``state``)
     - Viaje (``state``)
     - Nombre en la documentación
   * - ``draft``
     - Borrador
     - Borrador
     - Borrador
     - Borrador · Sin planificar (Parada) · Sin Paradas (Viaje)
   * - ``in_process``
     - Validado
     - Planificado
     - Planificado
     - Validado · Planificada · Planificado
   * - ``processed``
     - Despachado
     - Despachado
     - Despachado
     - Despachado · Despachada
   * - ``running``
     - En curso
     - En curso
     - En curso
     - En curso
   * - ``loaded``
     - Cargado
     - Cargado
     - —
     - Cargado · Cargada
   * - ``to_validate``
     - —
     - —
     - Por validar
     - Por validar
   * - ``completed``, ``reserves``, ``failed``, ``rescheduled``, ``returned``, ``canceled``
     - Completado, Con reservas, Fallido, Reprogramado, Devuelto, Cancelado
     - los mismos
     - ``completed``, ``failed``
     - los seis :term:`estados de cierre <Estados de la Parada>`

Los momentos de la matriz corresponden a estos puntos del sistema: validar la Orden y cerrar el
Manifiesto escriben ``in_process`` en Tramo y Orden y dejan el pedido en ``sent``; asignar o
quitar una Parada de un Viaje escribe solo en la Parada; ``tms.trip.send_trip`` es el único punto
que escribe ``processed`` (en los cuatro niveles) y anota ``dispatch_date``; el estado del Viaje
lo calcula ``_compute_state_from_stops`` a partir de sus Paradas de ruta, de ``dispatch_date``,
de ``validation_date`` y de la marca de Viaje repartido; el pedido pasa a ``sale`` por la tarea
programada de tarificación cuando ``_tms_ready_to_confirm`` lo permite.
