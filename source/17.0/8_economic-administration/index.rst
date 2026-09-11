8 Administración y Control Económico
====================================

Este capítulo explica el **modelo económico** del TMS: cómo cada operación tiene un importe que
se cobra, un coste que se paga y un margen, en qué nivel viven esas tres cifras, cómo se
reparten hacia abajo (de la Orden a sus Tramos, del Viaje a sus Paradas) y con qué herramientas
se controlan. El capítulo 2 da el principio (:doc:`la Orden es el ingreso y el Viaje el coste
</17.0/2_conceptual-model/2_3_economic-model>`); el capítulo 5 cuenta cuándo se tarifica,
se liquida y se factura (:doc:`5.6 </17.0/5_operational-flows/5_6_settlement>` y
:doc:`5.7 </17.0/5_operational-flows/5_7_invoicing>`). Aquí está lo que hay entre medias: el
modelo con el que un consultor configura la economía de una operativa y un responsable de
administración la controla.

.. mermaid::

   flowchart LR
       O["Orden<br/>activo del cliente"] -->|"división de ventas<br/>(modo del Proyecto)"| L["Tramos"]
       L --> S["Paradas<br/>activo · pasivo · margen"]
       T["Viaje<br/>pasivo del transportista"] -->|"división de costes<br/>(modo del Planning)"| S
       T -->|"transportista + tarifa<br/>o precio cerrado"| OC["Orden de compra<br/>automática"]
       OC --> FP["Factura de proveedor"]
       O --> FC["Factura de cliente"]
       R["Reembolsos"] --> O
       S --> M["Margen por Orden, Viaje,<br/>Tramo y Parada"]
       M --> K["Indicadores · Tableros<br/>Transacciones · Diagnósticos"]

.. toctree::
   :maxdepth: 1

   8_1_active-passive-margin
   8_2_sales-split
   8_3_cost-split
   8_4_purchase-orders
   8_5_carrier-settlement
   8_6_refunds
   8_7_analytic-account
   8_8_control-reporting
