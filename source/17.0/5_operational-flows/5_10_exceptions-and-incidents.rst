Facturación
---------------

La facturación del TMS se divide en dos flujos diferenciados:

- facturación de cliente
- facturación de proveedor

Ambos se apoyan en los mecanismos estándar de Odoo, reutilizando la capa financiera del ERP sobre la estructura logística generada por el TMS.



Facturación de cliente
~~~~~~~~~~~~~~~~~~~~~~~

La facturación al cliente se apoya en las órdenes de venta TMS.

Una vez que:

- las líneas económicas han sido calculadas
- la orden se encuentra confirmada

Odoo puede generar la factura de cliente utilizando el flujo estándar de facturación.

El módulo TMS añade capacidades específicas, como la facturación agrupada.

En este modo, el sistema puede consolidar líneas según criterios como:

- producto
- servicio
- zona tarifaria

Esto permite generar documentos comerciales más compactos sin perder trazabilidad con las líneas originales.

Durante la creación de facturas, el sistema controla:

- que no se vuelvan a facturar líneas ya facturadas
- que el proceso pueda limitarse a líneas seleccionadas
- que se mantenga la relación entre origen logístico y documento financiero



Facturación de proveedor
~~~~~~~~~~~~~~~~~~~~~~~~~

La facturación al transportista se apoya en la orden de compra vinculada al viaje.

Desde el propio viaje puede iniciarse la creación de la factura de proveedor, siempre que se cumplan las condiciones necesarias.

El cierre administrativo del viaje prepara previamente:

- cantidades recibidas
- cantidades pendientes de facturar
- consistencia económica de compra

Esto garantiza que la liquidación del transportista se apoye en información cerrada y validada.



Controles relevantes
~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+--------------------------------------------------------------+
| Control                                  | Descripción                                                  |
+==========================================+==============================================================+
| Líneas cliente ya facturadas             | No deben volver a facturarse.                                |
+------------------------------------------+--------------------------------------------------------------+
| Viaje sin orden de compra                | No puede generar factura proveedor.                          |
+------------------------------------------+--------------------------------------------------------------+
| Orden compra sin líneas pendientes       | No procede facturación.                                      |
+------------------------------------------+--------------------------------------------------------------+
| Operación ya facturada                   | Limita modificaciones posteriores.                           |
+------------------------------------------+--------------------------------------------------------------+

Una vez emitida la factura, determinados cambios operativos o económicos quedan restringidos para preservar consistencia documental.

Esto afecta especialmente a:

- viajes
- órdenes
- costes
- importes
- liquidaciones

El estado de facturación queda visible tanto en:

- la orden
- el viaje

Esto permite construir filtros operativos como:

- expediciones pendientes de facturar
- rutas pendientes de liquidar
- operaciones ya facturadas
- incidencias económicas pendientes de revisión

De este modo, el ciclo operativo puede cerrarse con trazabilidad completa entre ejecución logística y documentación financiera.