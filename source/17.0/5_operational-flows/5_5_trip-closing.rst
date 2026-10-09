5.5 Cierre de Viaje
-------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes · TMS › Operaciones › Tráfico › Viajes por validar ·
   TMS › Operaciones › Tráfico › Órdenes

.. figure:: /_static/img/5_operational-flows/5_5_trip-closing_01_cierre.png
   :alt: Cierre de un viaje

   Viaje cerrado tras completarse sus paradas.

Nadie cierra un Viaje (``tms.trip``) a mano. El cierre es la consecuencia de que su última
Parada haya terminado, y arrastra en cadena al Viaje, a su :term:`Orden de compra` (OC) y a las
Órdenes que transportaba. Esta sección cuenta esa cadena, con el paso de revisión que un
Proyecto puede exigir antes de facturar; qué hace cada botón de la cabecera del Viaje está en
:ref:`viaje-validacion`, y cómo encajan los estados de los cuatro niveles, en
:ref:`ciclo-estados`.

5.5.1 Qué dispara el cierre
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una Parada está cerrada cuando tiene uno de los seis :term:`estados de cierre <Estados de la
Parada>`. El cierre operativo no exige que todo haya salido bien: una Parada fallida está tan
cerrada como una completada. Lo que indica es que ya no queda nada por ejecutar.

Cuando **todas** las Paradas de ruta del Viaje están cerradas, el sistema recalcula el Viaje. Lo
hace cada vez que cambia el estado de una Parada, así que el cierre ocurre en el momento en que
la app registra el último resultado. Si todas fallaron, el Viaje queda **Fallido** y su OC se
cancela; en cualquier otra combinación, el Viaje cierra.

5.5.2 La cadena de efectos
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   flowchart LR
       P["Última Parada<br/>cerrada"] --> V{"¿El Proyecto<br/>exige revisión?"}
       V -->|"no"| T["Viaje<br/>tarifica el coste · bloquea la OC<br/>→ Completado"]
       V -->|"sí"| W["Viaje<br/>tarifica la venta<br/>→ Por validar"]
       W -->|"Validar"| T
       P --> O["Orden<br/>marcada pendiente de confirmar"]
       O -->|"tarificación"| C["Orden<br/>tarificada · confirmada<br/>→ Pedido de venta"]
       W -. "la confirmación<br/>espera" .-> C
       T --> L["Liquidación al transportista<br/>(5.6)"]
       C --> F["Facturación al cliente<br/>(5.7)"]

**En el Viaje, sin revisión.** Si su OC no está confirmada ni facturada, el sistema tarifica el
coste con la tarifa del transportista (o el precio cerrado), fija en la OC las cantidades
recibidas y a facturar, la confirma y bloquea, y deja el Viaje en **Completado**. También anota
el Viaje en el historial del conductor con el vehículo (:doc:`5_3_resource-assignment`). Si el
transportista es de flota propia no hay OC (ver
:doc:`/17.0/8_economic-administration/8_1_active-passive-margin`) y el Viaje pasa a Completado
sin más.

**En el Viaje, con revisión.** Si el Proyecto del Viaje tiene activado **Los viajes requieren
validación** (:doc:`/17.0/4_parametrization/4_5_project-configuration`), el Viaje no cierra: se
queda en **Por validar**. En ese momento se tarifica el lado de la venta, para que el revisor vea
los importes, pero el coste, la OC y la confirmación de las Órdenes esperan. Un usuario con el
permiso **Validador de viajes** lo revisa desde **Tráfico › Viajes por validar** (la lista los
ordena del más antiguo al más reciente y los marca en rojo a partir de tres días) y pulsa
**Validar**, que ejecuta entonces la cadena de arriba, o **Rechazar**, que lo deja marcado con el
motivo hasta que se corrija lo que haga falta y se valide. Si el Proyecto exige además **prueba
de entrega**, la validación se niega mientras alguna Orden no tenga firma ni albarán escaneado;
solo un responsable puede validar en ese caso, dejando el motivo. Las Órdenes sin prueba se
listan en la pestaña **Revisión** del Viaje.

**En la Orden.** Cuando todos sus Tramos están cerrados y el tramo actual terminó en Completada,
Con reservas o Fallida, la Orden queda marcada como **pendiente de confirmar** (un tramo actual
Reprogramado espera al siguiente intento; ver :doc:`/17.0/3_functional-architecture/3_2_1_orders`).
La tarea programada de tarificación (ver :doc:`5_6_settlement`) la recoge, vuelve a comprobar
que está lista, calcula sus líneas de venta con la tarifa del Proyecto y la **confirma**: pasa de
*Presupuesto enviado* a *Pedido de venta*, el estado nativo de Odoo, y, si la compañía bloquea
los pedidos confirmados, queda bloqueada. El desfase de unos minutos entre el cierre y la
confirmación es normal. En un Proyecto con revisión, la Orden espera a que el Viaje se valide.

Los efectos económicos del cierre no siempre corren en el instante del último evento: cuando el
evento llega desde la app, el estado del Viaje cambia en el acto y el dinero (tarifa de compra,
OC, historial) lo ejecuta la misma tarea programada de tarificación unos minutos después, para
que un cierre con muchas Paradas a la vez no retrase a la app. Un Viaje cuyo dinero falla (una
línea a cero, por ejemplo) conserva la marca y se reintenta en la pasada siguiente sin parar a
los demás.

A partir de aquí el flujo es económico: la OC confirmada es la base de la liquidación al
transportista (:doc:`5_6_settlement`) y la Orden confirmada, la base de la factura al cliente
(:doc:`5_7_invoicing`).

5.5.3 Reapertura
~~~~~~~~~~~~~~~~

La cadena funciona también hacia atrás. Si el conductor vuelve a abrir una Parada cerrada, el
Viaje regresa a **En curso** y, si su OC estaba confirmada, el sistema la devuelve a solicitud
de presupuesto con las cantidades a cero; la Orden, si estaba confirmada, vuelve a *Presupuesto
enviado*. Es el equivalente automático de **Revertir validación**, que hace lo mismo a mano
sobre un Viaje completado cuya OC no esté facturada (:ref:`viaje-validacion`).

Un caso frecuente de reapertura es la **reprogramación**. Desde **Acciones operativas ›
Reprogramar parada**, el planificador indica la nueva fecha y franja (y, si hace falta, una
dirección nueva). El sistema deja la Parada original como **Reprogramada**, que es un estado
de cierre, y crea un Tramo nuevo con una Parada nueva sin planificar, pendiente de asignar a
otro Viaje. La Orden, por tanto, sigue abierta aunque el primer Viaje se cierre: su tramo activo
pasa al nuevo y no se confirma hasta que ese intento termine.

Otro caso es el **Viaje repartido**: cuando una ruta se cae a media jornada y sus Paradas
pendientes se llevan a otras con *Repartir este viaje* (:doc:`5_2_trip-generation`), el Viaje
original se queda solo con lo que ya entregó. Como todas sus Paradas están cerradas, cerraría en
el acto; para que el reparto se pueda deshacer, el Viaje se mantiene **En curso** con la marca
«repartido» hasta que alguien pulsa **Cerrar viaje repartido**, se revierte el reparto o termina
su día, momento en que una tarea programada diaria lo cierra con la cadena normal.

5.5.4 Lo que el cierre protege
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una vez **facturada** la OC, el Viaje no se reabre ni por la app ni a mano; una vez
**facturada** la Orden, tampoco ella. El sistema deja de recalcular sus estados y trata la
operación como definitiva: costes, importes, recursos y estados quedan como estaban en el
momento de facturar. Si algo tiene que cambiar después, el camino es el contable (abono y nueva
factura, ver :doc:`5_7_invoicing`), no el operativo.
