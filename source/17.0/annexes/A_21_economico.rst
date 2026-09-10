A.21 Campos económicos
======================

Los campos económicos que el TMS añade a la Orden, el Tramo, la Parada y el Viaje, a la orden de compra y sus líneas, y el modelo del reembolso. Las etiquetas son las de la interfaz en español.

Viaje (tms.trip)
----------------

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
     - La parte del activo y del pasivo que no está ligada a ninguna parada: líneas de ámbito Viaje. Se reparte entre las paradas con el factor de división.
   * - Factor División
     - Número (calculado)
     - La suma de los factores de división de las paradas facturables en pasivo: la base del reparto de costes.
   * - Tarifa activa / Tarifa pasiva
     - Sí/No
     - Si el Viaje entra en el cálculo de activo y de pasivo. Activas por defecto.
   * - Precio Cerrado
     - Importe
     - Importe fijo pactado con el transportista; sustituye a la tarifa de compra en la orden de compra.
   * - Tarifa de cliente / Tarifa de transportista
     - Relaciones con Tarifa
     - La tarifa con la que se factura al cliente (viajes que facturan por viaje) y la de compra del transportista.
   * - Orden de compra
     - Relación
     - La orden de compra automática del Viaje.
   * - Importe de reembolsos
     - Importe (calculado)
     - Suma de los reembolsos de las paradas del Viaje.

Parada (tms.stop)
-----------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Activo / Pasivo / Beneficio / Margen %
     - Importe / % (calculados)
     - Las tres cifras al nivel de parada.
   * - Factor División
     - Número (calculado)
     - El factor de la parada según el Modo División Viaje del Planning: la magnitud, uno, o la magnitud por los kilómetros hasta la parada. Cero en paradas de hub y en cargas de reparto.
   * - Tarifa activa / Tarifa pasiva
     - Sí/No
     - Si la parada entra en el cálculo. Activas por defecto.
   * - Líneas de compra
     - Lista
     - Las líneas de la orden de compra ligadas a la parada.

Tramo (tms.shipment.leg)
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Activo / Activo de carga / Activo de descarga
     - Importe (calculados)
     - La parte del Tramo en las líneas de venta de la Orden, y su reparto entre la parada de carga y la de descarga con los porcentajes del tipo de orden.
   * - Pasivo
     - Importe (calculado)
     - El pasivo de sus paradas de carga y descarga ponderado por su porcentaje de división.
   * - Factor División / Porcentaje de división / Porcentaje activo
     - Número (calculados)
     - El factor del Tramo según el Modo de División del Proyecto, su porcentaje sobre los tramos de la Orden que comparten parada, y su porcentaje en la parada a efectos de activo.
   * - Líneas de venta
     - Lista
     - Las líneas de venta de la Orden ligadas al Tramo.

Orden (sale.order)
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Fecha administrativa
     - Fecha (calculada)
     - La fecha que decide la versión de tarifa, según la política del Proyecto. Estable: no cambia con la fecha de pedido de Odoo.
   * - Cuenta analítica
     - Relación
     - Heredada del Proyecto al crear la Orden.
   * - Importe de reembolsos / Reembolso
     - Importe / Relación
     - Suma de los reembolsos de la Orden y el registro de reembolso vinculado.
   * - Diagnóstico de tarifa activo y pasivo (clave, mensaje, ayuda, fecha, antigüedad)
     - Selección, textos y fechas
     - El resultado del último cálculo de venta y de compra: OK, no facturable, sin tarifa de cliente, sin transportista, sin tarifa de transportista, orden de compra bloqueada, sin líneas de tarifa, condiciones no coincidentes, sin trayecto entre zonas, sin detalle de vehículo o de contacto, sin detalle de zona, sin valor del factor, factor fuera de rango, sin resultado, error.
   * - Trayecto activo / pasivo faltante
     - Sí/No (calculados)
     - Si el motivo del diagnóstico es un trayecto entre zonas sin precio; activa el botón Crear trayecto faltante.

Línea de venta y de compra (campos TMS)
---------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tramo / Parada / Viaje
     - Relaciones
     - El origen operativo de la línea. Una línea de venta lleva el tramo o la parada que la generó; una de compra, la parada y el viaje.
   * - Tarifa / Línea de tarifa / Tarifa base / Detalle / Área de zona
     - Relaciones
     - De qué elemento de la tarifa salió el importe, para auditarlo.
   * - Identificador de sincronización
     - Texto
     - Clave con la que el recálculo reconoce la línea para actualizarla en lugar de duplicarla.

Orden de compra (purchase.order, campos TMS)
--------------------------------------------

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

Reembolso (tms.shipment.refund)
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Orden / Tramos / Parada / Viaje
     - Relaciones
     - Dónde se cobra el reembolso.
   * - Forma de Pago
     - Relación con Tipo de valor de caja
     - Efectivo, tarjeta, cheque... El catálogo de Datos auxiliares «Tipos de valores de caja».
   * - Importe
     - Importe
     - Lo que había que cobrar.
   * - Recopilado / Ingresado / Pagado
     - Importe
     - Lo cobrado por el conductor, lo que ingresó en la empresa y lo devuelto al cliente. En la interfaz «Recopilado» es lo cobrado.
   * - Saldo Conductor / Saldo Cliente
     - Importe (calculados)
     - Ingresado menos cobrado, y pagado menos cobrado.
   * - Estado
     - Selección
     - Borrador, En proceso, Cobrado, Ingresado, Pagado, Rechazado, Cancelado.
   * - Referencia del cliente / Fecha de la Orden / Fecha de la parada / Cliente / Localización / Conductor
     - Textos, fechas y relaciones
     - Los datos de contexto para el cuadre de caja.

Cómo se usa y qué decide el cliente: :doc:`/17.0/8_economic-administration/index`.
