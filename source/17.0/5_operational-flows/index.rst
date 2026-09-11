5 Flujos Operativos
===================

Este capítulo recorre el ciclo completo de una Orden en Guraify TMS, desde que entra en el
sistema hasta que se factura, en el orden en que ocurre. Cada sección cuenta qué hace el
usuario, qué comprueba el sistema y qué automatismos se disparan según la parametrización del
Proyecto. El comportamiento de cada entidad (estados, botones, campos) está en el
:doc:`capítulo 3 </17.0/3_functional-architecture/index>` y aquí se enlaza en lugar de
repetirlo.

La Orden puede entrar a mano, por fichero o por API, pero a partir de la validación el camino
es el mismo para todas: la planificación, la ejecución en la app, el cierre, la tarificación y
la facturación trabajan sobre la misma estructura de Tramos, Paradas y Viajes, venga de donde
venga la Orden. La tarificación no es un paso del recorrido sino un proceso que lo acompaña,
recalculando el precio de venta y el coste de compra cada vez que algo cambia; se explica en
:doc:`5_6_settlement`.

.. mermaid::

   flowchart LR
       MAN["Alta manual"] --> ORD["Orden"]
       FILE["Fichero"] --> MF["Manifiesto"]
       API["API"] --> MF
       MF -->|cerrar| ORD
       ORD -->|validar| ST["Paradas<br/>(desde los Tramos)"]
       ST -->|asignar · optimizar| TR["Viaje"]
       TR -->|enviar a la app| EXE["Ejecución<br/>parada a parada"]
       EXE -->|última parada cerrada| CLO["Cierre<br/>Viaje completado · Orden confirmada"]
       CLO --> OC["Orden de compra<br/>al transportista"]
       CLO --> FAC["Factura<br/>al cliente"]
       TAR["Tarificación"] -.-> ORD
       TAR -.-> TR

Las siete primeras secciones siguen ese recorrido. La última, :doc:`5_8_kpi-indicators`, no es
un paso del flujo: describe los indicadores visuales con los que las listas de Órdenes y de
Paradas resumen la situación de cada registro, y sirve de ayuda para leer cualquiera de los
pasos anteriores.

.. toctree::
   :maxdepth: 2

   5_1_order-creation
   5_2_trip-generation
   5_3_resource-assignment
   5_4_app-execution
   5_5_trip-closing
   5_6_settlement
   5_7_invoicing
   5_8_kpi-indicators
