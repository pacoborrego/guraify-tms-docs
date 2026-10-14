3.2.1 Órdenes
-------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Órdenes

La :term:`Orden` (``sale.order``) es la entidad contractual del sistema: representa el encargo
del cliente y es el origen del ingreso. Se construye como una extensión del pedido de venta de
Odoo, de modo que hereda toda la maquinaria económica del ERP (líneas de venta, tarifas,
facturación) y la especializa con la estructura logística del TMS.

3.2.1.1 Papel estructural
~~~~~~~~~~~~~~~~~~~~~~~~~

Cada Orden está vinculada a un cliente y a un :term:`Proyecto`, del que hereda parámetros como
la Tarifa aplicable, el modo de división de ventas o los tipos de servicio permitidos. A partir
de la Orden se despliega la estructura operativa: una Orden contiene uno o varios Tramos y, al
validarse, genera las Paradas que materializan los eventos físicos
(:doc:`3_2_6_legs-and-stops`). La Orden mantiene siempre su unidad económica, con independencia
de en cuántos Viajes se ejecute.

Cuando la Orden tiene varios Tramos, su cabecera (lugares, fechas, estado) muestra siempre los
datos de **uno solo: el tramo activo**. Este mecanismo, esencial para leer correctamente una
Orden multitramo, se explica en :doc:`3_2_5_active-leg`.

3.2.1.2 Estado operativo
~~~~~~~~~~~~~~~~~~~~~~~~

La Orden lleva un **Estado operativo** propio que no se fija a mano: **es el estado de su tramo
activo**, y el Tramo, a su vez, toma el suyo de su última anotación de Trazabilidad. Cuando la
ejecución avanza y cambia el tramo activo, el estado de la Orden cambia con él. Los valores son
los mismos que los del Tramo (ver :ref:`estados-parada`) y se ordenan así; cómo encajan con los
de la Parada, el Viaje y el pedido de venta está en :ref:`ciclo-estados`:

.. list-table::
   :header-rows: 1
   :widths: 22 60 18

   * - Estado
     - Significado
     - Tipo
   * - Borrador
     - Orden creada y aún sin validar: no tiene Paradas.
     - Abierto
   * - Validada
     - Orden validada (a mano o al cerrar el Manifiesto): sus Paradas existen y se pueden
       planificar. Planificarlas no cambia este estado.
     - Abierto
   * - Despachada
     - El Viaje del tramo activo se ha despachado al conductor o a la agencia.
     - Abierto
   * - En curso
     - El conductor tiene activa en la app la parada del tramo activo.
     - Abierto
   * - Cargada
     - La mercancía del tramo activo se ha cargado y falta la descarga.
     - Abierto
   * - Completada
     - Servicio ejecutado sin incidencias.
     - Cierre
   * - Con reservas
     - Ejecutado con incidencias anotadas.
     - Cierre
   * - Fallida
     - No se pudo ejecutar.
     - Cierre
   * - Reprogramada
     - Se volverá a intentar en otra fecha.
     - Cierre
   * - Devuelta
     - Mercancía devuelta.
     - Cierre
   * - Cancelada
     - Orden anulada.
     - Cierre

Este cálculo automático es lo que convierte a la Orden en un reflejo fiel de la realidad
operativa: el estado comercial no se declara, emerge de los eventos físicos registrados en las
Paradas. Los seis estados de cierre son los mismos que cierran una Parada y un Tramo (ver
:term:`Estados de la Parada` y :doc:`3_2_6_legs-and-stops`); el Viaje tiene sus propios estados,
descritos en :doc:`3_2_2_trips`.

3.2.1.3 Estado del pedido de venta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Junto al estado operativo, la Orden conserva el **estado nativo del pedido de venta de Odoo**,
que gobierna su ciclo comercial y contable:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Presupuesto
     - Orden sin validar. Editable; aún no compromete.
   * - Presupuesto enviado
     - Orden validada. Lo pone el sistema al validar la Orden o cerrar el Manifiesto, y
       también al desbloquearla; no envía ningún correo al cliente, es solo el estado. Sigue
       siendo editable. Reabrir el Manifiesto la devuelve a *Presupuesto*.
   * - Pedido de venta
     - Ejecución terminada y confirmada: queda fijada la base contractual y económica.
   * - Cancelado
     - Pedido anulado.

El estado operativo y el del pedido no son redundantes: el operativo refleja **qué está pasando
en la calle** (paradas, ejecución) y el del pedido refleja **en qué punto del ciclo comercial y
contable** está el documento. El TMS mueve el segundo por sí solo: a *Presupuesto enviado* al
validar y a *Pedido de venta* cuando la ejecución termina (ver :ref:`orden-bloqueo`). Si el
Proyecto exige validar el Viaje antes de facturar, la confirmación espera a esa validación
(:doc:`3_2_2_trips`).

3.2.1.4 Estado de facturación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El tercer indicador, también **nativo de Odoo**, es el **estado de facturación**, que resume la
situación del pedido respecto a las facturas de cliente:

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
     - Todo facturado, pero alguna línea se ha entregado por encima de lo pedido: Odoo señala
       una oportunidad de venta adicional.

El estado de facturación tiene un efecto importante sobre el resto del ciclo: cuando la Orden
está **facturada**, el sistema la considera cerrada y **deja de recalcular su estado
operativo**, de modo que una orden ya facturada queda congelada y protegida frente a cambios
automáticos posteriores.

.. _orden-bloqueo:

3.2.1.5 Bloqueo y desbloqueo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La cabecera de la Orden ofrece los botones **Bloquear** y **Desbloquear**, que integran el
candado del pedido de venta de Odoo con el ciclo operativo del TMS:

- **Bloquear** confirma el pedido (lo pasa a *Pedido de venta*) y, si la política de la
  compañía «bloquear pedidos confirmados» está activa, lo deja además bloqueado frente a
  ediciones, fijando la operación.
- **Desbloquear** libera el candado y devuelve la Orden a *Presupuesto enviado* para poder
  reeditarla: sigue validada.

El sistema aplica los dos gestos por sí solo siguiendo el estado de los Tramos:

- **Bloqueo automático al completar.** Cuando **todos** los Tramos de la Orden (sin contar los
  de transferencia) alcanzan un estado de cierre **y el tramo actual ha terminado en Completada,
  Con reservas o Fallida**, la Orden queda marcada como **pendiente de confirmar**. Un tramo
  actual Reprogramado o Cancelado no cuenta como desenlace: la Orden espera al siguiente
  intento. La tarea programada de tarificación, que corre cada cinco minutos, la recoge,
  vuelve a comprobar la regla (la app levanta la marca al cerrar un solo Tramo, con los demás
  aún abiertos), calcula sus líneas de venta si hacía falta y la confirma. El desfase de unos
  minutos entre el cierre de la última parada y la confirmación es deliberado: confirmar en
  lote evita cargar el servidor cuando cierran muchas paradas a la vez (ver
  :doc:`/17.0/5_operational-flows/5_6_settlement`).
- **Desbloqueo automático al reabrir.** Si una Orden ya confirmada deja de tener todos sus
  Tramos cerrados (se reabre una parada, se añade otra), vuelve a *Presupuesto enviado* para
  seguir evolucionando.
- **Protección por facturación.** Una Orden **facturada** no puede desbloquearse ni reabrirse
  automáticamente; el sistema la trata como definitiva.

Así, el bloqueo no es un gesto aislado, sino la consecuencia de que la ejecución física ha
concluido: el candado sigue al estado operativo, y la facturación actúa como cierre final. El
flujo completo de cierre, con lo que ocurre en el Viaje y en la orden de compra, está en
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

**Adjuntos de la Orden.** La pestaña **Adjuntos** de la Orden reúne las pruebas de entrega que
el conductor hace en sus Paradas (fotos del albarán firmado, firmas) y lo que la oficina suba con
**Adjuntar archivos**: el albarán del cliente, una reclamación. Es el sitio donde mirar antes de
validar o facturar si la entrega está probada. Funciona igual que en la Parada y el Tramo (ver
:doc:`3_2_6_legs-and-stops`).

3.2.1.6 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~~~

Para filtros, exportaciones e integraciones, estos son los campos de la Orden que corresponden a
lo descrito en esta sección:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Campo de ``sale.order``
   * - Estado operativo
     - ``tms_status`` (valores ``draft``, ``in_process``, ``processed``, ``running``,
       ``loaded``, ``completed``, ``reserves``, ``failed``, ``rescheduled``, ``returned``,
       ``canceled``); toma el valor de ``active_leg.state``
   * - Pendiente de confirmar por la tarea programada
     - ``app_confirm_pending``
   * - Estado del pedido de venta
     - ``state`` (``draft`` Presupuesto, ``sent`` Presupuesto enviado, ``sale`` Pedido de
       venta, ``cancel``)
   * - Estado de facturación
     - ``invoice_status`` (``no``, ``to invoice``, ``invoiced``, ``upselling``)
   * - Bloqueo
     - ``locked``
