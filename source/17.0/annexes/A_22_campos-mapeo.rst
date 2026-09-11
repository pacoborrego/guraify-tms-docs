A.22 Catálogo de campos de mapeo
================================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Definición de Fichero › pestaña de mapeo de columnas

Modelo Odoo: ``tms.edi.field.mapping``. Los campos de destino que admite una :term:`Definición de
fichero` al mapear las columnas de un fichero o los campos de un mensaje de API, agrupados por la
entidad que alimentan. Es el catálogo cerrado que el TMS sabe materializar: una columna solo puede
apuntar a uno de ellos, y los mensajes que llegan por la Bandeja de entrada API usan las mismas
claves. Cómo se configura el mapeo y cómo se transforman los valores está en
:doc:`/17.0/7_edi-integrations/7_2_1_field-mapping` y
:doc:`/17.0/7_edi-integrations/7_2_2_python-transformations`.

Este anexo no sigue el formato Campo / Tipo / Qué es de los demás: aquí no hay campos de un
formulario sino claves de un catálogo, y lo que importa de cada una es a qué dato del TMS
corresponde.

.. list-table:: Viaje (``tms.trip``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``TripName``
     - Nombre o identificador del Viaje.
   * - ``TripDate``
     - Fecha del Viaje.
   * - ``TripPlanning``
     - Planning del Viaje.
   * - ``TripHub``
     - Hub o base logística del Viaje.
   * - ``Sequence``
     - Posición de la Parada dentro del Viaje.
   * - ``Carrier``
     - Transportista asignado al Viaje.
   * - ``CarrierProject``
     - Proyecto del transportista.
   * - ``CPriceList``
     - Tarifa de compra (transportista).
   * - ``Driver``
     - Conductor asignado.
   * - ``Vehicle``
     - Vehículo asignado.
   * - ``Trailers``
     - Semirremolque(s) asignado(s).

.. list-table:: Orden (``sale.order``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``Project``
     - Proyecto al que pertenece la Orden.
   * - ``Customer``
     - Cliente de la Orden.
   * - ``PriceList``
     - Tarifa de venta aplicable.
   * - ``ExternalRef``
     - Referencia externa de la Orden. Volver a recibir la misma referencia actualiza la Orden en
       vez de duplicarla.
   * - ``ShipmentType``
     - Tipo de Orden.
   * - ``ServiceType``
     - Tipo de Servicio contratado.
   * - ``CashValue``
     - Importe del Reembolso.
   * - ``CashCurrency``
     - Divisa del Reembolso.
   * - ``CashPaymentType``
     - Forma de pago del Reembolso.
   * - ``CashNote``
     - Nota asociada al Reembolso.
   * - ``Info``
     - Información / observaciones de la Orden.
   * - ``State``
     - Estado de la Orden.
   * - ``ClosedPrice``
     - Importe fijo de la Orden, para Proyectos sin Tarifa: la Orden se tarifica con ese importe en
       lugar de con Líneas de tarifa. Si el Proyecto tiene Tarifa, se ignora.

.. list-table:: Tramos — carga y descarga (``tms.shipment.leg``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``LoadAddressKey`` / ``UnLoadAddressKey``
     - Clave de la dirección de carga / descarga (para reutilizar direcciones).
   * - ``LoadName`` / ``UnLoadName``
     - Nombre del punto de carga / descarga.
   * - ``LoadAddress`` / ``UnLoadAddress``
     - Dirección de carga / descarga.
   * - ``LoadAddress2`` / ``UnLoadAddress2``
     - Segunda línea de dirección.
   * - ``LoadCity`` / ``UnLoadCity``
     - Población.
   * - ``LoadZip`` / ``UnLoadZip``
     - Código postal.
   * - ``LoadState`` / ``UnLoadState``
     - Provincia / estado.
   * - ``LoadCountry`` / ``UnLoadCountry``
     - País.
   * - ``LoadFullAddress`` / ``UnLoadFullAddress``
     - Dirección completa en un solo campo.
   * - ``LoadLatitude`` / ``UnLoadLatitude``
     - Latitud (geolocalización).
   * - ``LoadLongitude`` / ``UnLoadLongitude``
     - Longitud (geolocalización).
   * - ``LoadInfo`` / ``UnLoadInfo``
     - Observaciones del punto.
   * - ``LoadTel`` / ``UnLoadTel``
     - Teléfono de contacto.
   * - ``LoadTel2`` / ``UnLoadTel2``
     - Teléfono secundario.
   * - ``LoadEmail`` / ``UnLoadEmail``
     - Correo de contacto.
   * - ``LoadContact`` / ``UnLoadContact``
     - Persona de contacto.
   * - ``LoadDate`` / ``UnLoadDate``
     - Fecha prevista de carga / descarga.
   * - ``LoadStartTime`` / ``UnLoadStartTime``
     - Inicio de la franja horaria.
   * - ``LoadEndTime`` / ``UnLoadEndTime``
     - Fin de la franja horaria.
   * - ``LoadPriority`` / ``UnLoadPriority``
     - Prioridad de la Parada.
   * - ``LoadElevator`` / ``UnLoadElevator``
     - Disponibilidad de ascensor.
   * - ``LoadLevels`` / ``UnLoadLevels``
     - Número de plantas / niveles.

.. list-table:: Líneas de mercancía (``tms.shipment.pack``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``Packs``
     - Número de Bultos.
   * - ``Pallets``
     - Número de palés.
   * - ``Quantity``
     - Cantidad.
   * - ``Meters``
     - Metros lineales.
   * - ``Cube``
     - Volumen (m³).
   * - ``GrossWeight``
     - Peso bruto.
   * - ``PacksDescription``
     - Descripción de los Bultos.
   * - ``PacksTypeID``
     - Regla de tarifa de la línea: cómo se mide la mercancía (bultos, palés, cantidad, metros).
   * - ``PacksTemperature``
     - Tipo de bulto (seco, refrigerado, congelado...).

.. list-table:: Bultos / trazabilidad (``tms.shipment.pack.traceability``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``Parcel_Barcode``
     - Código de barras del Bulto.
   * - ``Parcel_Cube``
     - Volumen del Bulto.
   * - ``Parcel_GrossWeight``
     - Peso bruto del Bulto.
   * - ``Parcel_Array``
     - Conjunto de Bultos (estructura agrupada).

.. list-table:: Clientes (``res.partner``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``CustomerId``
     - Identificador externo del cliente.
   * - ``CustomerName``
     - Nombre del cliente.
   * - ``CustomerShortName``
     - Nombre corto / abreviado.
   * - ``CustomerAddress``
     - Dirección.
   * - ``CustomerZIP``
     - Código postal.
   * - ``CustomerCity``
     - Población.
   * - ``CustomerState``
     - Provincia / estado.
   * - ``CustomerCountry``
     - País.
   * - ``CustomerVat``
     - NIF / VAT.
   * - ``CustomerPaymentTerms``
     - Condiciones de pago.
   * - ``CustomerTelf``
     - Teléfono.
   * - ``CustomerEmail``
     - Correo electrónico.
   * - ``CustomerContact``
     - Persona de contacto.

.. list-table:: Transportistas (``res.partner``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``CarrierId``
     - Identificador externo del transportista.
   * - ``CarrierName``
     - Nombre del transportista.
   * - ``CarrierShortName``
     - Nombre corto / abreviado.
   * - ``CarrierAddress``
     - Dirección.
   * - ``CarrierZIP``
     - Código postal.
   * - ``CarrierCity``
     - Población.
   * - ``CarrierState``
     - Provincia / estado.
   * - ``CarrierCountry``
     - País.
   * - ``CarrierVat``
     - NIF / VAT.
   * - ``CarrierPaymentTerms``
     - Condiciones de pago.
   * - ``CarrierTelf``
     - Teléfono.
   * - ``CarrierEmail``
     - Correo electrónico.
   * - ``CarrierContact``
     - Persona de contacto.

.. list-table:: Conductores (``res.partner`` marcado como conductor)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``DriverId``
     - Identificador externo del conductor.
   * - ``DriverName``
     - Nombre del conductor.
   * - ``DriverShortName``
     - Nombre corto / abreviado.
   * - ``DriverAddress``
     - Dirección.
   * - ``DriverZIP``
     - Código postal.
   * - ``DriverCity``
     - Población.
   * - ``DriverState``
     - Provincia / estado.
   * - ``DriverCountry``
     - País.
   * - ``DriverVat``
     - NIF / VAT.
   * - ``DriverTelf``
     - Teléfono.
   * - ``DriverEmail``
     - Correo electrónico.
   * - ``DriverParent``
     - Transportista al que pertenece el conductor.

.. list-table:: Vehículos (``fleet.vehicle``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``VehicleId``
     - Identificador externo del vehículo.
   * - ``VehicleName``
     - Nombre del vehículo.
   * - ``VehicleLicensePl``
     - Matrícula.
   * - ``VehicleBrand``
     - Marca.
   * - ``VehicleModel``
     - Modelo.
   * - ``VehicleCategory``
     - Categoría.
   * - ``VehicleType``
     - Tipo de vehículo.
   * - ``VehicleParent``
     - Vehículo o flota a la que pertenece.
   * - ``VehicleStartDate``
     - Fecha de alta.
   * - ``VehicleEndDate``
     - Fecha de baja.

.. note::

   El catálogo incluye además separadores no seleccionables (``<<<<TRIPS>>>>``,
   ``<<<<SHIPMENTS>>>>``, etc.) que solo sirven para agrupar visualmente los campos en
   el desplegable; no representan destinos de mapeo.

Cómo se usa: :doc:`/17.0/7_edi-integrations/7_2_1_field-mapping`.
