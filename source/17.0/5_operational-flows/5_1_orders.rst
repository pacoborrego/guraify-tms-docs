Creación de Orden
---------------------

La creación de la Orden es el punto de entrada operativo.

En Guraify TMS, la orden se registra como una expedición TMS sobre el modelo estándar de ventas de Odoo, marcada con el indicador ``is_tms_order``.

Esta decisión permite reutilizar:

- trazabilidad comercial
- líneas de venta
- facturación
- estados administrativos estándar

sobre los que se añade la capa logística propia del TMS.

La orden puede crearse desde:

- formulario manual de expedición
- fichero EDI
- importación Excel / CSV
- integración API

En entradas automáticas, la referencia externa del cliente se almacena como referencia de orden.

Este dato se utiliza para determinar si la expedición debe:

- crearse
- actualizarse

La configuración del Proyecto determina la mayor parte de los valores por defecto:

- Cliente
- Tarifa
- Tipo de orden
- Tipo de servicio
- Tipo de transportista
- Tipo de destinatario
- Planning
- Agencia
- Hub
- Categoría de vehículo
- Lugar de recogida
- Parámetros de automatización

Por este motivo, una orden sin un proyecto correctamente parametrizado no puede avanzar de forma fiable dentro del flujo operativo.

**Datos principales de la orden**

+----------------------------------+--------------------------------------------------------------+
| Campo                            | Descripción                                                  |
+==================================+==============================================================+
| Proyecto TMS                     | Define operativa, tarifa, hub y parámetros de ejecución.     |
+----------------------------------+--------------------------------------------------------------+
| Cliente y referencia externa     | Identifican la expedición frente al sistema origen.          |
+----------------------------------+--------------------------------------------------------------+
| Tipo de orden y servicio         | Determinan el flujo operativo.                               |
+----------------------------------+--------------------------------------------------------------+
| Fechas y ventanas horarias       | Definen ventanas de carga y descarga.                        |
+----------------------------------+--------------------------------------------------------------+
| Líneas y magnitudes              | Packs, pallets, peso, volumen, metros, quantity, etc.        |
+----------------------------------+--------------------------------------------------------------+
| Importes cerrados o tarifa       | Base económica de cálculo.                                   |
+----------------------------------+--------------------------------------------------------------+
| Datos de viaje importados        | Vehículo, conductor, carrier, viaje o compra.                |
+----------------------------------+--------------------------------------------------------------+

.. note::

   Aunque el usuario vea una Orden TMS, técnicamente el registro principal
   es una orden de venta estándar de Odoo (``sale.order``).

   Esto explica por qué la confirmación, facturación y estado administrativo
   utilizan mecanismos estándar del ERP.