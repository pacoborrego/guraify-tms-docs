A.21 Campos económicos
======================

.. admonition:: Ruta en Odoo
   :class: tip

   Formularios y listas de Viajes, Paradas, Tramos y Órdenes (TMS › Operaciones) · TMS › Administración › Transacciones · TMS › Administración › Reembolsos

Modelo Odoo: los campos que el TMS añade al Viaje (``tms.trip``), la Parada (``tms.stop``), el Tramo
(``tms.shipment.leg``) y la Orden (``sale.order``), a la orden de compra (``purchase.order``) y a
las líneas de venta y de compra, y el modelo del Reembolso (``tms.shipment.refund``). Las etiquetas
son las de la interfaz en español.

A.21.1 Viaje
------------

Los campos económicos del Viaje (``tms.trip``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Activo / Pasivo / Beneficio / Margen %
     - Importe / Importe / Importe / % (calculados)
     - Lo que se cobra, lo que se paga, la diferencia y la diferencia sobre el activo.
   * - Fijo (activo) / Fijo (pasivo)
     - Importe (calculados)
     - La parte del activo y del pasivo que no está ligada a ninguna Parada: líneas de ámbito Viaje.
       Se reparte entre las Paradas con el factor de división.
   * - Factor División
     - Número (calculado)
     - La suma de los factores de división de las Paradas que entran en el cálculo del pasivo: la
       base del reparto de costes.
   * - Tarifa activa / Tarifa pasiva
     - Sí/No
     - Si el Viaje entra en el cálculo de activo y de pasivo. Activas por defecto.
   * - Precio Cerrado
     - Importe
     - Importe fijo pactado con el transportista; sustituye a la tarifa de compra en la orden de
       compra.
   * - Tarifa de cliente / Tarifa de transportista
     - Relaciones con Tarifa
     - La Tarifa con la que se factura al cliente (Viajes que facturan por Viaje) y la de compra del
       transportista.
   * - Orden de compra
     - Relación
     - La orden de compra automática del Viaje.
   * - Importe de reembolsos
     - Importe (calculado)
     - Suma de los Reembolsos de las Paradas del Viaje.

A.21.2 Parada
-------------

Los campos económicos de la Parada (``tms.stop``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Activo / Pasivo / Beneficio / Margen %
     - Importe / % (calculados)
     - Las tres cifras al nivel de Parada.
   * - Factor División
     - Número (calculado)
     - El factor de la Parada según el Modo División Viaje del Planning: la magnitud, uno, o la
       magnitud por los kilómetros hasta la Parada. Cero en Paradas de hub y en cargas de reparto.
   * - Tarifa activa / Tarifa pasiva
     - Sí/No
     - Si la Parada entra en el cálculo. Activas por defecto.
   * - Líneas de compra
     - Lista
     - Las líneas de la orden de compra ligadas a la Parada.

A.21.3 Tramo
------------

Los campos económicos del Tramo (``tms.shipment.leg``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Activo / Activo de carga / Activo de descarga
     - Importe (calculados)
     - La parte del Tramo en las líneas de venta de la Orden, y su reparto entre la Parada de carga
       y la de descarga con los porcentajes del Tipo de Orden.
   * - Pasivo
     - Importe (calculado)
     - El pasivo de sus Paradas de carga y descarga ponderado por su porcentaje de división.
   * - Factor División / Porcentaje de división / Porcentaje activo
     - Número (calculados)
     - El factor del Tramo según el Modo de División del Proyecto; su porcentaje sobre los Tramos de
       la misma Orden que comparten su Parada de referencia (el que baja el pasivo de la Parada al
       Tramo); y su porcentaje sobre los Tramos facturables de la Orden (el que reparte entre Tramos
       las líneas de venta de ámbito Orden). Ver
       :doc:`/17.0/8_economic-administration/8_2_sales-split`.
   * - Líneas de venta
     - Lista
     - Las líneas de venta de la Orden ligadas al Tramo.

A.21.4 Orden
------------

Los campos económicos de la Orden (``sale.order``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Fecha administrativa
     - Fecha (calculada)
     - La fecha que decide la Versión de tarifa, según la política del Proyecto. Estable: no cambia
       con la fecha del documento de venta de Odoo.
   * - Cuenta analítica
     - Relación
     - Heredada del Proyecto al crear la Orden.
   * - Importe de reembolsos / Reembolso
     - Importe / Relación
     - Suma de los Reembolsos de la Orden y el registro de Reembolso vinculado.
   * - Diagnóstico de tarifa activo y pasivo (clave, mensaje, ayuda, fecha, antigüedad)
     - Selección, textos y fechas
     - El resultado del último cálculo de venta y de compra: correcto («OK»), no facturable, sin
       tarifa de cliente, sin transportista, sin tarifa de transportista, orden de compra bloqueada,
       sin líneas de tarifa, condiciones no coincidentes, sin precio entre zonas, sin detalle de
       vehículo o de contacto, sin detalle de zona, sin valor del factor, factor fuera de rango, sin
       resultado, error.
   * - Trayecto activo / pasivo faltante
     - Sí/No (calculados)
     - Si el motivo del diagnóstico es que no hay precio entre las dos zonas; activa el botón «Crear
       trayecto faltante», que da de alta ese precio.

A.21.5 Línea de venta y de compra
---------------------------------

Los campos que el TMS añade a las líneas de venta (``sale.order.line``) y de compra
(``purchase.order.line``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tramo / Parada / Viaje
     - Relaciones
     - El origen operativo de la línea. Una línea de venta lleva el Tramo o la Parada que la generó;
       una de compra, la Parada y el Viaje.
   * - Tarifa / Línea de tarifa / Tarifa base / Detalle / Área de zona
     - Relaciones
     - De qué elemento de la Tarifa salió el importe, para auditarlo.
   * - Identificador de sincronización
     - Texto
     - Clave con la que el recálculo reconoce la línea para actualizarla en lugar de duplicarla.

A.21.6 Orden de compra
----------------------

Los campos que el TMS añade a la orden de compra (``purchase.order``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Orden TMS
     - Sí/No
     - Marca las órdenes de compra generadas por el TMS.
   * - Viaje
     - Relación
     - El Viaje del que sale la orden de compra.
   * - Estado TMS
     - Texto
     - El estado operativo del Viaje, para las listas de compras.

A.21.7 Reembolso
----------------

El Reembolso (``tms.shipment.refund``) es una entidad propia.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Orden / Tramos / Parada / Viaje
     - Relaciones
     - Dónde se cobra el Reembolso.
   * - Tipo de Reembolso
     - Relación con Tipo de valor de caja
     - Efectivo, tarjeta, cheque... El catálogo de Datos auxiliares «Tipos de Reembolso».
   * - Importe
     - Importe
     - Lo que había que cobrar.
   * - Cobrado / Ingresado / Pagado
     - Importe
     - Lo cobrado por el conductor, lo que ingresó en la empresa y lo devuelto al cliente.
   * - Saldo Conductor / Saldo Cliente
     - Importe (calculados)
     - Ingresado menos cobrado, y pagado menos cobrado.
   * - Estado
     - Selección
     - Borrador, En proceso, Cobrado, Ingresado, Pagado, Rechazado, Cancelado. Ver
       :doc:`/17.0/8_economic-administration/8_6_refunds`.
   * - Referencia del cliente / Fecha de la Orden / Fecha de la parada / Cliente / Localización /
       Conductor
     - Textos, fechas y relaciones
     - Los datos de contexto para el cuadre de caja.

Cómo se usa y qué decide el cliente: :doc:`/17.0/8_economic-administration/index`.
