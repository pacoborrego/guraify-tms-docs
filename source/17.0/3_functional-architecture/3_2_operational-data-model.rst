3.2 Modelo de datos operativo
-----------------------------

Una vez descrita la organización funcional del sistema, el siguiente paso consiste en
analizar las principales entidades de datos que soportan la operativa del transporte
dentro de la aplicación.

Las entidades principales del modelo de datos operativo son la Orden (``sale.order``),
el Tramo (``tms.shipment.leg``), la Parada (``tms.stop``) y el Viaje (``tms.trip``),
junto con los Bultos (``tms.shipment.pack``) y las líneas económicas de venta y de
compra. A ellas se añaden dos entidades propias de la ingesta de demanda: el Manifiesto
EDI (``tms.edi.manifest``) y la Bandeja de Entrada API (``tms_int.api.inbox``), que
actúan como antesala antes de materializar la estructura operativa.

Cada una cumple un papel específico dentro del ciclo operativo del transporte. Las
cuatro entidades estructurales y las dos de ingesta se detallan en las subsecciones
siguientes; los Bultos y las líneas económicas se tratan en su contexto operativo
(capítulo 5) y económico (capítulo 8).

.. toctree::
   :maxdepth: 1

   3_2_1_orders
   3_2_2_trips
   3_2_3_manifests
   3_2_4_api-inbox
   3_2_5_active-leg
