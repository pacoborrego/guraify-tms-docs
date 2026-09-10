8.5 Liquidación al transportista
--------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Transacciones › Líneas de Orden de Compra; botón **Crear factura** del
   Viaje; TMS › Administración › Opciones de Tarifa › Diagnosis de tarifa de viajes.

La :term:`Liquidación` al transportista no es un documento aparte: es la orden de compra del
Viaje, confirmada al cerrarlo, y la factura de proveedor que sale de ella. El flujo paso a paso
está en :doc:`/17.0/5_operational-flows/5_6_settlement` y
:doc:`/17.0/5_operational-flows/5_7_invoicing`; aquí, lo que hace falta saber para controlarla.

**La unidad de liquidación es el Viaje.** Cada Viaje tiene su orden de compra y ésta sus líneas,
así que el transportista se liquida viaje a viaje o, agrupando, por periodo: seleccionando los
Viajes completados de un transportista en la lista y pulsando **Crear factura**, o desde la
lista de Líneas de Orden de Compra con **Crear factura agrupada**, que consolida las líneas
seleccionadas del mismo proveedor en una factura. El sistema no factura una línea dos veces, no
factura un Viaje sin orden de compra ni una orden de compra sin líneas pendientes, y lo dice
con el nombre del Viaje.

**Qué se puede corregir y cuándo.** Mientras la orden de compra está en borrador, cualquier
recálculo la rehace. Confirmada, se puede desbloquear y recomponer. Facturada, no: la corrección
es contable, con **Línea de abono** sobre la línea facturada, que genera la rectificativa.

**El diagnóstico pasivo.** Cada Viaje lleva un diagnóstico de tarifa de compra, con un motivo
cuando el cálculo no ha podido hacerse: sin transportista, sin tarifa de compra, sin líneas de
tarifa aplicables, condiciones que no coinciden, zona sin resolver, detalle sin vehículo o sin
transportista, factor fuera de rango, orden de compra bloqueada. La lista **Diagnosis de tarifa
de viajes** agrupa todo lo pendiente, y los botones **Resolver diagnosis** y **Crear trayecto
faltante** llevan a la corrección. Un Viaje con diagnóstico pendiente no debe liquidarse.

**Flota propia.** Los viajes de conductores propios no generan orden de compra ni entran en la
liquidación; su diagnóstico pasivo queda limpio a propósito. El coste de la flota propia se
trata en la contabilidad general, no aquí.
