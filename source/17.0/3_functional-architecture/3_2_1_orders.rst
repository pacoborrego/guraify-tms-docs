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

Cada Orden está vinculada a un cliente y a un proyecto (``project.project``), del que
hereda parámetros como la tarifa aplicable, el modo de división de ventas o los tipos de
servicio permitidos. A partir de la Orden se despliega la estructura operativa: una
Orden contiene uno o varios Tramos (``tms.shipment.leg``) y, al validarse, genera las
Paradas (``tms.stop``) que materializan los eventos físicos. La Orden mantiene siempre su
unidad económica, con independencia de en cuántos Viajes se ejecute.

Cuando la Orden tiene varios Tramos, su cabecera (lugares, fechas, estado) muestra
siempre los datos de **uno solo: el tramo activo**. Este mecanismo, esencial para leer
correctamente una Orden multitramo, se explica en :doc:`3_2_5_active-leg`.

3.2.1.2 Estado operativo
------------------------

La Orden lleva un estado operativo propio (campo ``tms_status``, *Oper State*) que se
**calcula a partir del estado de sus Paradas y Tramos**, no se fija a mano. Sus valores
son:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Borrador (``draft``)
     - Orden creada, aún sin ejecución.
   * - En proceso (``in_process``)
     - Ejecución iniciada en alguna de sus paradas.
   * - Procesada (``processed``)
     - Paradas completadas a falta del cierre.
   * - Completada (``completed``)
     - Servicio ejecutado en su totalidad.
   * - Reservas (``reserves``)
     - Entregada con reservas.
   * - Fallida (``failed``)
     - Ejecución fallida.
   * - Reprogramada (``rescheduled``)
     - Reagendada para otra fecha.
   * - Devuelta (``returned``)
     - Mercancía devuelta.
   * - Cargada (``loaded``)
     - Mercancía cargada.
   * - En ruta (``running``)
     - En ejecución sobre la ruta.
   * - Cancelada (``canceled``)
     - Orden anulada.

Este cálculo automático es lo que convierte a la Orden en un reflejo fiel de la realidad
operativa: el estado comercial no se declara, emerge de los eventos físicos registrados
en las Paradas.

3.2.1.3 Estado administrativo
-----------------------------

Junto al estado operativo, la Orden conserva el **estado administrativo nativo del pedido
de venta de Odoo** (campo ``state``), que gobierna su ciclo comercial y contable:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Presupuesto (``draft``)
     - Pedido en borrador, editable; aún no compromete.
   * - Presupuesto enviado (``sent``)
     - Presupuesto remitido al cliente.
   * - Pedido de venta (``sale``)
     - Pedido confirmado: queda fijada la base contractual y económica.
   * - Cancelado (``cancel``)
     - Pedido anulado.

El estado operativo y el administrativo no son redundantes: el operativo refleja **qué
está pasando en la calle** (paradas, ejecución) y el administrativo refleja **en qué punto
del ciclo comercial/contable** está el pedido. En la práctica, cuando la ejecución se
completa, el TMS confirma automáticamente el pedido (lo lleva a ``sale``); ver
:ref:`orden-bloqueo`.

3.2.1.4 Estado de facturación
-----------------------------

El tercer indicador, también **nativo de Odoo**, es el estado de facturación
(``invoice_status``), que resume la situación del pedido respecto a las facturas de
cliente:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Nada que facturar (``no``)
     - El pedido aún no genera derecho a factura.
   * - A facturar (``to invoice``)
     - Hay importe pendiente de facturar.
   * - Facturado (``invoiced``)
     - El pedido está completamente facturado.
   * - Venta adicional (``upselling``)
     - Procede revisar un posible *upselling*.

El estado de facturación tiene un efecto importante sobre el resto del ciclo: cuando la
Orden está **facturada** (``invoiced``), el sistema la considera cerrada y **deja de
recalcular su estado operativo**, de modo que una orden ya facturada queda congelada y
protegida frente a cambios automáticos posteriores.

.. _orden-bloqueo:

3.2.1.5 Bloqueo y desbloqueo
----------------------------

Sobre el pedido de venta, Odoo ofrece los botones **Bloquear** y **Desbloquear** (el
candado del pedido). Bloquear marca el pedido como bloqueado (campo ``locked``) e impide
su edición; desbloquear lo libera para poder modificarlo de nuevo.

En Guraify TMS este mecanismo se integra con el ciclo operativo:

- **Bloqueo automático al completar.** Cuando **todas** las Paradas válidas de la Orden
  alcanzan un estado de cierre (completada, con reservas, fallida, reprogramada, devuelta
  o cancelada), el sistema tarifica la Orden y la **confirma automáticamente**
  (``action_confirm`` → estado ``sale``). Si la política de la compañía "bloquear pedidos
  confirmados" está activa, el pedido queda además bloqueado, fijando la operación.
- **Desbloqueo / reapertura.** El botón **Desbloquear** del TMS
  (``action_unlock_shipment``) libera el candado y devuelve la Orden a borrador para poder
  reeditarla. El sistema lo dispara también de forma automática cuando una Orden ya
  confirmada deja de tener todas sus paradas cerradas (p. ej. se reabre o se añade una
  parada): vuelve a borrador para seguir evolucionando.
- **Protección por facturación.** Una Orden **facturada** no puede desbloquearse ni
  reabrirse automáticamente; el sistema la trata como definitiva.

Así, el bloqueo no es un gesto aislado, sino la consecuencia de que la ejecución física
ha concluido: el candado sigue al estado operativo, y la facturación actúa como cierre
final.

.. note::

   Estos tres estados (operativo, administrativo y de facturación) y el bloqueo se
   resumen visualmente en el indicador KPI de la Orden, descrito en
   :doc:`/17.0/5_operational-flows/5_11_kpi-indicators`.

.. CAPTURA: 3_2_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_1_orders_01_orden.png
      :alt: Formulario de una Orden con su estado operativo

      Formulario de una Orden (``sale.order``) con su estado operativo.

.. CAPTURA: 3_2_1_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_1_orders_02_orden-bloqueada.png
      :alt: Orden bloqueada (candado cerrado)

      Orden bloqueada: candado cerrado tras confirmarse la ejecución.
