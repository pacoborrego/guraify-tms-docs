3.2.1 Órdenes
=============

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Órdenes

La Orden (``sale.order``) es la entidad contractual del sistema: representa el encargo
del cliente y es el origen del ingreso. Se construye como una extensión del pedido de
venta de Odoo, de modo que hereda toda la maquinaria económica del ERP (líneas de venta,
tarifas, facturación) y la especializa con la estructura logística del TMS.

3.2.1.1 Papel estructural
-------------------------

Cada Orden está vinculada a un cliente y a un :term:`Proyecto`, del que hereda parámetros
como la tarifa aplicable, el modo de división de ventas o los tipos de servicio permitidos.
A partir de la Orden se despliega la estructura operativa: una Orden contiene uno o varios
Tramos y, al validarse, genera las Paradas que materializan los eventos físicos. La Orden
mantiene siempre su unidad económica, con independencia de en cuántos Viajes se ejecute.

Cuando la Orden tiene varios Tramos, su cabecera (lugares, fechas, estado) muestra
siempre los datos de **uno solo: el tramo activo**. Este mecanismo, esencial para leer
correctamente una Orden multitramo, se explica en :doc:`3_2_5_active-leg`.

3.2.1.2 Estado operativo
------------------------

La Orden lleva un **Estado operativo** propio que se **calcula a partir del estado de sus
Paradas y Tramos**, no se fija a mano. Sus valores son:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Borrador
     - Orden creada, aún sin ejecución.
   * - En proceso
     - Ejecución iniciada en alguna de sus paradas.
   * - Procesada
     - Paradas completadas a falta del cierre.
   * - Completada
     - Servicio ejecutado en su totalidad.
   * - Con reservas
     - Ejecutada con incidencias o reservas.
   * - Fallida
     - Ejecución fallida.
   * - Reprogramada
     - Reagendada para otra fecha.
   * - Devuelta
     - Mercancía devuelta.
   * - Cargada
     - Mercancía cargada.
   * - En ruta
     - En ejecución sobre la ruta.
   * - Cancelada
     - Orden anulada.

Este cálculo automático es lo que convierte a la Orden en un reflejo fiel de la realidad
operativa: el estado comercial no se declara, emerge de los eventos físicos registrados
en las Paradas. Los seis estados de cierre (completada, con reservas, fallida,
reprogramada, devuelta y cancelada) son los mismos que cierran una Parada y un Viaje; ver
:term:`Estados de la Parada`.

3.2.1.3 Estado del pedido de venta
----------------------------------

Junto al estado operativo, la Orden conserva el **estado nativo del pedido de venta de
Odoo**, que gobierna su ciclo comercial y contable:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Presupuesto
     - Pedido en borrador, editable; aún no compromete.
   * - Presupuesto enviado
     - Presupuesto remitido al cliente.
   * - Pedido de venta
     - Pedido confirmado: queda fijada la base contractual y económica.
   * - Cancelado
     - Pedido anulado.

El estado operativo y el del pedido no son redundantes: el operativo refleja **qué está
pasando en la calle** (paradas, ejecución) y el del pedido refleja **en qué punto del ciclo
comercial y contable** está el documento. En la práctica, cuando la ejecución se completa,
el TMS confirma automáticamente el pedido; ver :ref:`orden-bloqueo`.

3.2.1.4 Estado de facturación
-----------------------------

El tercer indicador, también **nativo de Odoo**, es el **estado de facturación**, que
resume la situación del pedido respecto a las facturas de cliente:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Nada que facturar
     - El pedido aún no genera derecho a factura.
   * - A facturar
     - Hay importe pendiente de facturar.
   * - Facturado
     - El pedido está completamente facturado.
   * - Venta adicional
     - Procede revisar una posible venta adicional.

El estado de facturación tiene un efecto importante sobre el resto del ciclo: cuando la
Orden está **facturada**, el sistema la considera cerrada y **deja de recalcular su estado
operativo**, de modo que una orden ya facturada queda congelada y protegida frente a
cambios automáticos posteriores.

.. _orden-bloqueo:

3.2.1.5 Bloqueo y desbloqueo
----------------------------

La cabecera de la Orden ofrece los botones **Bloquear** y **Desbloquear**, que integran el
candado del pedido de venta de Odoo con el ciclo operativo del TMS:

- **Bloquear** confirma el pedido (lo pasa a *Pedido de venta*) y, si la política de la
  compañía "bloquear pedidos confirmados" está activa, lo deja además bloqueado frente a
  ediciones, fijando la operación.
- **Desbloquear** libera el candado y devuelve la Orden a *Presupuesto* para poder
  reeditarla.

El sistema aplica los dos gestos por sí solo siguiendo el estado de las Paradas:

- **Bloqueo automático al completar.** Cuando **todas** las Paradas válidas de la Orden
  alcanzan un estado de cierre, el sistema tarifica la Orden y la confirma.
- **Desbloqueo automático al reabrir.** Si una Orden ya confirmada deja de tener todas sus
  paradas cerradas (se reabre una, se añade otra), vuelve a *Presupuesto* para seguir
  evolucionando.
- **Protección por facturación.** Una Orden **facturada** no puede desbloquearse ni
  reabrirse automáticamente; el sistema la trata como definitiva.

Así, el bloqueo no es un gesto aislado, sino la consecuencia de que la ejecución física ha
concluido: el candado sigue al estado operativo, y la facturación actúa como cierre final.
El flujo completo de cierre, con lo que ocurre en el Viaje y en la orden de compra, está en
:doc:`/17.0/5_operational-flows/5_5_trip-closing`.

.. note::

   Estos tres estados (operativo, del pedido y de facturación) y el bloqueo se resumen
   visualmente en el indicador KPI de la Orden, descrito en
   :doc:`/17.0/5_operational-flows/5_8_kpi-indicators`.

.. figure:: /_static/img/3_functional-architecture/3_2_1_orders_01_orden.png
   :alt: Formulario de una Orden con su estado operativo

   Formulario de una Orden con su estado operativo.

.. figure:: /_static/img/3_functional-architecture/3_2_1_orders_02_orden-bloqueada.png
   :alt: Orden bloqueada (candado cerrado)

   Orden bloqueada: candado cerrado tras confirmarse la ejecución.

3.2.1.6 Referencia técnica
--------------------------

Para filtros, exportaciones e integraciones, estos son los campos de la Orden que
corresponden a lo descrito en esta sección:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Campo de ``sale.order``
   * - Estado operativo
     - ``tms_status`` (valores ``draft``, ``in_process``, ``processed``, ``completed``,
       ``reserves``, ``failed``, ``rescheduled``, ``returned``, ``loaded``, ``running``,
       ``canceled``)
   * - Estado del pedido de venta
     - ``state`` (``draft``, ``sent``, ``sale``, ``cancel``)
   * - Estado de facturación
     - ``invoice_status`` (``no``, ``to invoice``, ``invoiced``, ``upselling``)
   * - Bloqueo
     - ``locked``
