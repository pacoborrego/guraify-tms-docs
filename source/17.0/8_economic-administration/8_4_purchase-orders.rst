8.4 La orden de compra automática
---------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Botón inteligente de la orden de compra en el Viaje; TMS › Administración › Transacciones ›
   Líneas de Orden de Compra.

.. CAPTURA: 8_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/8_economic-administration/8_4_purchase-orders_01_oc.png
      :alt: Orden de compra de un Viaje

      La orden de compra de un Viaje: la sección con el recorrido y las líneas por Parada.

El TMS no pide crear la orden de compra al transportista: la genera y la mantiene el sistema. La
:term:`Orden de compra` es la orden de compra estándar de Odoo (``purchase.order``), marcada
como del TMS y vinculada a su Viaje (``tms.trip``), y con ella el coste del transporte entra en
el circuito de compras, facturación de proveedores y contabilidad sin ningún paso manual.

**Cuándo nace.** En la primera tarificación pasiva del Viaje que encuentra un transportista y
una tarifa de compra, o un precio cerrado mayor que cero. Eso ocurre al asignar el transportista
(el proceso periódico de tarificación, descrito en
:doc:`/17.0/5_operational-flows/5_6_settlement`, la crea en su siguiente pasada), al pulsar
**Tarificar** en el Viaje, o a más tardar al cerrarlo. Si el transportista es flota propia no se
crea (ver :doc:`8_1_active-passive-margin`).

**Qué lleva.** El proveedor es el transportista; el origen, el nombre del Viaje. Una **línea de
sección** describe el recorrido: fecha, descripción, matrícula, kilómetros y duración. Debajo,
las **líneas de compra** que genera la tarifa: una por cada detalle de tarifa que aplica, con su
producto, y ligada a la Parada o al Tramo cuando la línea de tarifa es de ese ámbito, o sin
Parada cuando es del Viaje entero (la parte fija). Con precio cerrado, una sola línea con el
importe pactado.

**Cómo se mantiene.** Cada nueva tarificación del Viaje rehace las líneas de compra mientras la
orden de compra esté en borrador. Si el Viaje pierde el transportista o la tarifa, las líneas se
eliminan. Al cerrar el Viaje, la orden de compra se confirma y se fijan las cantidades
recibidas y a facturar; reabrirlo la devuelve a borrador y las pone a cero. Los botones
**Bloquear** y **Desbloquear** del Viaje hacen lo mismo a mano (ver
:doc:`/17.0/3_functional-architecture/3_2_1_orders`). Una orden de compra facturada, hecha o
cancelada ya no se toca: el diagnóstico de tarifa lo indica como «orden de compra bloqueada».

La lista **Líneas de Orden de Compra** de Administración muestra todas las líneas de coste de
todos los Viajes, con su Parada, su tarifa y su estado de factura, y es desde donde se facturan
líneas sueltas o se abonan (:doc:`8_5_carrier-settlement`).
