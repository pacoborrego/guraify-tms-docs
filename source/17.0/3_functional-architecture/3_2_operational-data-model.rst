3.2 Modelo de datos operativo
-----------------------------

Una vez descrita la organización funcional del sistema, el siguiente paso es analizar las
entidades de datos que soportan la operativa del transporte dentro de la aplicación.

Las cuatro entidades estructurales son la Orden (``sale.order``), el Tramo
(``tms.shipment.leg``), la Parada (``tms.stop``) y el Viaje (``tms.trip``). La
:doc:`Orden <3_2_1_orders>` es el encargo del Cliente y el origen del ingreso; se descompone en
:doc:`Tramos <3_2_6_legs-and-stops>`, cada uno un movimiento entre un punto de carga y uno de
descarga, y estos dan lugar a las :doc:`Paradas <3_2_6_legs-and-stops>`, los eventos físicos
que se planifican y se ejecutan. Las Paradas se agrupan en :doc:`Viajes <3_2_2_trips>`, la
unidad de ejecución y de coste. Como la cabecera de la Orden muestra en cada momento los datos
de un solo Tramo, el :doc:`tramo activo <3_2_5_active-leg>` tiene una sección propia.

A ellas se añaden dos entidades propias de la ingesta de demanda, que actúan como antesala antes
de materializar la estructura operativa: el :doc:`Manifiesto <3_2_3_manifests>`
(``tms.edi.manifest``) y la :doc:`Bandeja de entrada API <3_2_4_api-inbox>`
(``tms_int.api.inbox``).

Completan el modelo los Bultos (``tms.shipment.pack``) y las líneas económicas de venta y de
compra. Los Bultos se tratan donde se escanean, en la
:doc:`ejecución con la app </17.0/5_operational-flows/5_4_app-execution>`; las líneas
económicas, en la :doc:`tarificación </17.0/5_operational-flows/5_6_settlement>` y la
:doc:`facturación </17.0/5_operational-flows/5_7_invoicing>`, y su modelo (activo, pasivo,
margen y divisiones) en :doc:`/17.0/8_economic-administration/index`.

.. toctree::
   :maxdepth: 1

   3_2_1_orders
   3_2_2_trips
   3_2_3_manifests
   3_2_4_api-inbox
   3_2_5_active-leg
   3_2_6_legs-and-stops
