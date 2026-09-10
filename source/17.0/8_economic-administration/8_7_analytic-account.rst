8.7 Cuenta analítica
--------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Campo **Cuenta analítica** del Proyecto (pestaña TMS › Administración); Contabilidad ›
   Informes › Analítica en Odoo.

La contabilidad analítica de Odoo es la forma estándar de agrupar ingresos y gastos por algo
distinto de la cuenta contable: un cliente, un contrato, una línea de negocio. El TMS la
alimenta desde el Proyecto, que es justo la unidad de contrato del sistema.

Cada Proyecto puede llevar una **cuenta analítica**. Cuando el Proyecto la tiene, la Orden la
hereda al crearse, y de la Orden pasa a sus líneas de venta y de ahí a las facturas de cliente.
Del lado del coste, la Orden que un Viaje crea para facturar al cliente toma la cuenta del
Proyecto de ese cliente, y las líneas de compra que la tarifa genera llevan la distribución
analítica que corresponda a sus líneas de venta, de modo que la factura del transportista cae en
la misma cuenta que el ingreso al que sirve.

Con eso, los informes analíticos de Odoo dan por Proyecto lo facturado y lo pagado, sin ningún
desarrollo: es la vía para el control económico por contrato que no necesita el detalle de
Tramos y Paradas. Cuando el detalle hace falta, están los importes por nivel del TMS (8.1) y los
indicadores y tableros (8.8).

Es una decisión de implantación que conviene tomar al principio: una cuenta analítica por
Proyecto, o una por cliente compartida por sus proyectos, según el nivel al que administración
quiera leer los resultados. Las Órdenes ya creadas no cambian de cuenta al cambiar la del
Proyecto.
