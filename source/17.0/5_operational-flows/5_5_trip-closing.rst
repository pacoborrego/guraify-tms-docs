5.5 Cierre de Viaje
-------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes · TMS › Operaciones › Tráfico › Órdenes

.. CAPTURA: 5_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_5_trip-closing_01_cierre.png
      :alt: Cierre de un viaje

      Viaje cerrado tras completarse sus paradas.

Nadie cierra un Viaje (``tms.trip``) a mano. El cierre es la consecuencia de que su última
Parada haya terminado, y arrastra en cadena al Viaje, a su :term:`Orden de compra` (OC) y a las
Órdenes que transportaba. Esta sección cuenta esa cadena; lo que hacen los botones Bloquear y
Desbloquear está en :doc:`/17.0/3_functional-architecture/3_2_1_orders`.

5.5.1 Qué dispara el cierre
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una Parada está cerrada cuando tiene uno de los seis :term:`estados de cierre <Estados de la
Parada>`. El cierre operativo no exige que todo haya salido bien: una Parada fallida está tan
cerrada como una completada. Lo que indica es que ya no queda nada por ejecutar.

Cuando **todas** las Paradas del Viaje están cerradas, el sistema recalcula el Viaje. Lo hace
cada vez que cambia el estado de una Parada, así que el cierre ocurre en el momento en que la
app registra el último resultado.

5.5.2 La cadena de efectos
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   flowchart LR
       P["Última Parada<br/>cerrada"] --> T["Viaje<br/>tarifica el coste · bloquea la OC<br/>→ Completado"]
       P --> O["Orden<br/>marcada pendiente de confirmar"]
       O -->|tarificación| C["Orden<br/>tarificada · confirmada<br/>→ Pedido de venta"]
       T --> L["Liquidación al transportista<br/>(5.6)"]
       C --> F["Facturación al cliente<br/>(5.7)"]

**En el Viaje.** Si su OC no está confirmada ni facturada, el sistema tarifica el coste con la
tarifa del transportista (o el precio cerrado), fija en la OC las cantidades recibidas y a
facturar, la confirma y deja el Viaje en **Completado**. Es exactamente lo que hace el botón
**Bloquear**, sin que nadie lo pulse. Si el transportista es de flota propia no hay OC (ver
:doc:`/17.0/8_economic-administration/8_1_active-passive-margin`) y el Viaje pasa a Completado
sin más.

**En la Orden.** Cuando todos sus Tramos están cerrados y la Orden no está confirmada ni
facturada, queda marcada como **pendiente de confirmar**. La tarea programada de tarificación
(ver :doc:`5_6_settlement`) la recoge, calcula sus líneas de venta con la tarifa del Proyecto y
la **confirma**: pasa a *Pedido de venta*, el estado nativo de Odoo, y, si la compañía bloquea
los pedidos confirmados, queda bloqueada. El desfase de unos minutos entre el cierre y la
confirmación es normal.

A partir de aquí el flujo es económico: la OC confirmada es la base de la liquidación al
transportista (:doc:`5_6_settlement`) y la Orden confirmada, la base de la factura al cliente
(:doc:`5_7_invoicing`).

5.5.3 Reapertura
~~~~~~~~~~~~~~~~

La cadena funciona también hacia atrás. Si una Parada cerrada vuelve a abrirse, o se añade una
nueva al Viaje, el sistema deshace lo que había hecho: la OC vuelve a borrador con las
cantidades a cero y el Viaje regresa a **Procesado**; la Orden, si estaba confirmada, vuelve a
*Presupuesto*. Es el equivalente automático de **Desbloquear**. Si todas las Paradas del Viaje
vuelven a borrador, el Viaje también.

Un caso frecuente de reapertura es la **reprogramación**. Desde **Acciones operativas ›
Reprogramar parada**, el planificador indica la nueva fecha y franja (y, si hace falta, una
dirección nueva). El sistema deja la Parada original como **Reprogramada**, que es un estado
de cierre, y crea un Tramo nuevo con una Parada nueva en borrador, pendiente de planificar en
otro Viaje. La Orden, por tanto, sigue abierta aunque el primer Viaje se cierre.

5.5.4 Lo que el cierre protege
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una vez **facturada** la OC, el Viaje no se reabre ni por la app ni a mano; una vez
**facturada** la Orden, tampoco ella. El sistema deja de recalcular sus estados y trata la
operación como definitiva: costes, importes, recursos y estados quedan como estaban en el
momento de facturar. Si algo tiene que cambiar después, el camino es el contable (abono y nueva
factura, ver :doc:`5_7_invoicing`), no el operativo.
