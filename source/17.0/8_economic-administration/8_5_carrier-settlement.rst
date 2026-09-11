8.5 Liquidación al transportista
--------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Transacciones › Líneas de Orden de Compra; botón **Crear factura** del
   Viaje; TMS › Administración › Opciones de Tarifa › Diagnóstico de tarifa de viajes.

La :term:`Liquidación` al transportista no es un documento aparte: es la orden de compra del
Viaje (``tms.trip``), confirmada al cerrarlo, y la factura de proveedor de Odoo que sale de
ella. El flujo paso a paso, con la factura agrupada y la línea de abono, está en
:doc:`/17.0/5_operational-flows/5_6_settlement` y
:doc:`/17.0/5_operational-flows/5_7_invoicing`; aquí, lo que hace falta saber para controlarla.

**La unidad de liquidación es el Viaje.** Cada Viaje tiene su orden de compra y esta sus líneas,
así que el transportista se liquida Viaje a Viaje o, agrupando, por periodo: desde la lista de
Viajes o desde la de Líneas de Orden de Compra, consolidando en una factura las líneas del mismo
transportista. El sistema no factura una línea dos veces, no factura un Viaje sin orden de compra
ni una orden de compra sin líneas pendientes, y lo dice con el nombre del Viaje.

**Qué se puede corregir y cuándo.** Mientras la orden de compra está en borrador, cualquier
recálculo la rehace. Confirmada, se puede desbloquear y recomponer. Facturada, no: la corrección
es contable, con una línea de abono sobre la línea facturada, que genera la rectificativa.

**El diagnóstico pasivo.** Cada Viaje lleva un diagnóstico de tarifa de compra, con un motivo
cuando el cálculo no ha podido hacerse; los motivos se describen en
:doc:`/17.0/5_operational-flows/5_6_settlement`. La lista **Diagnóstico de tarifa de viajes**
agrupa todo lo pendiente, y los botones **Resolver diagnóstico** y **Crear trayecto faltante**
(así se llama en la interfaz el alta de un precio entre dos zonas que no existía) llevan a la
corrección. Un Viaje con diagnóstico pendiente no debe liquidarse.

**Flota propia.** Los Viajes de conductores propios no generan orden de compra ni entran en la
liquidación, y su diagnóstico pasivo queda limpio a propósito (ver
:doc:`8_1_active-passive-margin`).
