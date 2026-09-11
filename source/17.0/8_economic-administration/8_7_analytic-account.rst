8.7 Cuenta analítica
--------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Campo **Cuenta analítica** del Proyecto (pestaña TMS › Administración); Contabilidad ›
   Informes › Analítica en Odoo.

La contabilidad analítica de Odoo es la forma estándar de agrupar ingresos y gastos por algo
distinto de la cuenta contable: un cliente, un contrato, una línea de negocio. El TMS la
alimenta desde el Proyecto (``project.project``), que es justo la unidad de contrato del
sistema.

Cada Proyecto puede llevar una **cuenta analítica**. Cuando el Proyecto la tiene, la Orden la
hereda al crearse, y de la Orden pasa a sus líneas de venta y de ahí a las facturas de cliente.
La Orden que un Viaje crea para facturar al cliente (ver :doc:`8_1_active-passive-margin`) toma
también la cuenta del Proyecto de ese cliente.

Con eso, los informes analíticos de Odoo dan por Proyecto lo facturado, sin ningún desarrollo:
es la vía para el control económico por contrato que no necesita el detalle de Tramos y Paradas.
Cuando el detalle hace falta, están los importes por nivel del TMS
(:doc:`8_1_active-passive-margin`) y los indicadores y tableros
(:doc:`8_8_control-reporting`).

Es una decisión de implantación que conviene tomar al principio: una cuenta analítica por
Proyecto, o una por cliente compartida por sus proyectos, según el nivel al que administración
quiera leer los resultados. Las Órdenes ya creadas no cambian de cuenta al cambiar la del
Proyecto.
