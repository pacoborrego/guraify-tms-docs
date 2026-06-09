5 Flujos Operativos
===================

Este capítulo describe el flujo operativo completo de una orden TMS, desde su creación hasta su facturación.

El objetivo es identificar qué objeto del sistema participa en cada fase, qué validaciones se ejecutan y qué automatismos pueden intervenir según la parametrización del proyecto.

El flujo se apoya en cuatro entidades principales:

- La Orden o Expedición, representada por ``sale.order``
- El Tramo, representado por ``tms.shipment.leg``
- La Parada, representada por ``tms.stop``
- El Viaje o Ruta, representado por ``tms.trip``

Cada una agrupa un nivel distinto de información y permite separar:

- La venta al cliente
- La estructura logística
- La planificación
- La liquidación al transportista

A nivel funcional, el proceso puede iniciarse mediante:

- Creación manual desde Odoo
- Importación de fichero
- Integración API

Independientemente del canal de entrada, el sistema normaliza la información hacia una estructura interna común.

Esto garantiza que:

- La validación
- La planificación
- La ejecución en app
- La facturación


.. toctree::
   :maxdepth: 2

   5_1_orders
   5_2_shipments
   5_3_stops
   5_4_trips
   5_5_planning
   5_6_driver-app
   5_7_execution-and-tracking
   5_8_tarification-and-purchase
   5_9_billing-and-closing
   5_10_exceptions-and-incidents
   5_11_kpi-indicators