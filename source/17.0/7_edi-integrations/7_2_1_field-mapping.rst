7.2.1 Mapeo de Campos
=====================

El mapeo de campos establece la correspondencia entre los campos del sistema externo y
los campos del modelo de Odoo. Es la pieza que hace posible que datos con nomenclaturas
y formatos dispares acaben encajando en la misma estructura interna.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Definición de Fichero

Modelo de mapeo
---------------

.. CAPTURA: 7_2_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_1_field-mapping_01_lista-mapeos.png
      :alt: Mapeos de columnas de un fichero EDI

      Mapeos de columnas de un fichero EDI.

El mapeo de entrada se define en ``tms.edi.field.mapping``, que asocia una columna de
origen (``column_name``) con un campo de destino (``field``) y declara las conversiones
de tipo aplicables tanto a la entrada como a la respuesta. Cada fichero EDI
(``tms.edi.file``) agrupa los mapeos que le corresponden, de manera que un mismo tipo de
intercambio reutiliza siempre la misma configuración de columnas (ver
:doc:`7_2_file-import`).

Campos destino disponibles
--------------------------

El campo de destino (``field``) no es texto libre: se elige de un catálogo cerrado de
campos que el TMS sabe materializar. Ese catálogo está agrupado por la entidad de
negocio a la que pertenece cada campo, de modo que un mismo fichero puede alimentar a la
vez los datos del Viaje, de la Expedición, de los Tramos, de las líneas y de los datos
maestros (clientes, transportistas, conductores y vehículos). La función de este
catálogo es doble: garantiza que la columna del fichero externo apunta a un destino
válido del modelo y sirve de referencia al consultor para saber qué información puede
importarse y bajo qué nombre.

.. CAPTURA: 7_2_1_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_1_field-mapping_02_selector-campo.png
      :alt: Catálogo de campos destino agrupado por entidad

      Catálogo de campos destino agrupado por entidad (selector *Tms Field*).

Los grupos disponibles y sus campos son los siguientes:

.. list-table:: Viaje / Ruta (``tms.trip``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``TripName``
     - Nombre o identificador del viaje.
   * - ``TripDate``
     - Fecha del viaje.
   * - ``TripPlanning``
     - Planificación asociada al viaje.
   * - ``TripHub``
     - Hub o base logística del viaje.
   * - ``Sequence``
     - Orden de la parada dentro del viaje.
   * - ``Carrier``
     - Transportista asignado al viaje.
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

.. list-table:: Expedición / Orden (``sale.order``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``Project``
     - Proyecto al que pertenece la expedición.
   * - ``Customer``
     - Cliente de la expedición.
   * - ``PriceList``
     - Tarifa de venta aplicable.
   * - ``ExternalRef``
     - Referencia externa de la expedición (clave de idempotencia).
   * - ``ShipmentType``
     - Tipo de expedición.
   * - ``ServiceType``
     - Tipo de servicio contratado.
   * - ``CashValue``
     - Importe del reembolso.
   * - ``CashCurrency``
     - Divisa del reembolso.
   * - ``CashPaymentType``
     - Forma de pago del reembolso.
   * - ``CashNote``
     - Nota asociada al reembolso.
   * - ``Info``
     - Información / observaciones de la expedición.
   * - ``State``
     - Estado de la expedición.
   * - ``ClosedPrice``
     - Precio cerrado de la expedición.

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
     - Inicio de la ventana horaria.
   * - ``LoadEndTime`` / ``UnLoadEndTime``
     - Fin de la ventana horaria.
   * - ``LoadPriority`` / ``UnLoadPriority``
     - Prioridad de la parada.
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
     - Número de bultos.
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
     - Descripción de los bultos.
   * - ``PacksTypeID``
     - Regla de precio de la línea.
   * - ``PacksTemperature``
     - Tipo de embalaje / temperatura.

.. list-table:: Paquetes / trazabilidad (``tms.shipment.pack.traceability``)
   :header-rows: 1
   :widths: 30 70

   * - Campo destino
     - Significado
   * - ``Parcel_Barcode``
     - Código de barras del paquete.
   * - ``Parcel_Cube``
     - Volumen del paquete.
   * - ``Parcel_GrossWeight``
     - Peso bruto del paquete.
   * - ``Parcel_Array``
     - Conjunto de paquetes (estructura agrupada).

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

.. list-table:: Conductores (``res.partner`` / ``hr.employee``)
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
     - Empresa / transportista al que pertenece el conductor.

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

El campo especial ``Parcel_Array``
----------------------------------

Los campos ``Parcel_Barcode``, ``Parcel_Cube`` y ``Parcel_GrossWeight`` son escalares:
cada uno toma el valor de una columna y describe **un** paquete. Funcionan bien cuando
el fichero trae **una fila por paquete**.

``Parcel_Array`` resuelve el caso contrario: clientes que envían **un único registro por
expedición** (sin detalle de paquetes), pero cuyos códigos de barras impresos en las
etiquetas de origen siguen una regla de construcción conocida. En lugar de un valor
escalar, ``Parcel_Array`` espera la **lista completa de paquetes** de la expedición, que
se genera por código a partir de los datos de la fila.

Cómo funciona internamente
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A diferencia del resto de campos de paquete, cuando la transformación escribe en
``Parcel_Array`` el importador **sustituye** la estructura de paquete completa por el
valor devuelto (no asigna un atributo suelto). Por eso la función debe devolver una
**lista de diccionarios**, uno por paquete, con las claves que el importador sabe
materializar:

- ``Parcel_Barcode`` — código de barras de la etiqueta de origen.
- ``Parcel_GrossWeight`` — peso bruto del paquete.
- ``Parcel_Cube`` — volumen del paquete.

Esa lista se asigna directamente a los paquetes (``Parcels``) de la línea de mercancía
de la expedición.

Configuración del mapeo
~~~~~~~~~~~~~~~~~~~~~~~

``Parcel_Array`` se configura como un **campo computado**, no como un mapeo de columna
directo:

#. En el mapeo, marcar **Computed** (``is_computed``). Al hacerlo, el nombre de columna
   pasa automáticamente a ``_Cmptd_Parcel_Array``: el importador lo trata como campo
   calculado tras procesar las columnas normales de la fila.
#. Marcar **Apply Code?** (``apply_code``) y escribir la lógica de construcción en
   **Python Code** (``python_code``).

.. CAPTURA: 7_2_1_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_1_field-mapping_03_parcel-array.png
      :alt: Configuración del campo computado Parcel_Array

      Configuración del campo computado ``Parcel_Array`` (*Computed* + *Apply Code?*).

El código se ejecuta en el mismo entorno controlado que las demás transformaciones
(:doc:`7_2_2_python-transformations`): dispone de ``value``, ``row`` (la fila actual,
indexada por posición de columna), ``rows`` (todas las filas) y las librerías ``json``,
``re`` y ``datetime``; el resultado se deja en ``result``. Como el cálculo es a nivel de
fila completa, la lógica lee los datos de ``row`` por índice de columna, no de ``value``.

Ejemplo de uso
~~~~~~~~~~~~~~

Supongamos un cliente que envía una fila por expedición con, entre otras, una columna de
**referencia de expedición**, una de **número de bultos** y una de **peso bruto total**.
Las etiquetas de origen imprimen un código de barras con la regla
``<Referencia><NN>``, donde ``NN`` es el número de bulto correlativo con dos dígitos
(``01``, ``02``, …). La función ``Parcel_Array`` reconstruye la lista de paquetes y
reparte el peso a partes iguales:

.. code-block:: python

   # Índices (base 0) de las columnas de origen en la fila
   ref_index    = 0   # Referencia de expedición (ExternalRef)
   packs_index  = 5   # Número de bultos
   weight_index = 6   # Peso bruto total

   ref = str(row[ref_index]).strip()
   num_packs = int(row[packs_index]) if row[packs_index] else 0
   total_weight = float(row[weight_index]) if row[weight_index] else 0.0

   # Peso por bulto, repartido a partes iguales
   weight_per_pack = round(total_weight / num_packs, 3) if num_packs else 0.0

   parcels = []
   for i in range(1, num_packs + 1):
       parcels.append({
           'Parcel_Barcode': f"{ref}{i:02d}",   # p. ej. ALB12345 -> ALB1234501, ALB1234502, ...
           'Parcel_GrossWeight': weight_per_pack,
           'Parcel_Cube': 0.0,
       })

   result = parcels

Con una fila de referencia ``ALB12345`` y 3 bultos, la función genera tres paquetes con
códigos ``ALB1234501``, ``ALB1234502`` y ``ALB1234503``, cada uno con su parte
proporcional del peso. El importador los materializa como la trazabilidad de bultos
(``tms.shipment.pack.traceability``) de la línea de la expedición.

.. tip::

   La regla de construcción del código de barras es específica de cada cliente. Ajusta
   el patrón (prefijos fijos, dígitos de control, relleno de ceros, segmentos derivados
   de otras columnas) a lo que realmente venga impreso en la etiqueta de origen, y
   valida el resultado con la prueba inline del mapeo antes de pasar a producción.

Transformación por campo
------------------------

Cuando la correspondencia no es directa, cada mapeo puede aplicar una transformación:
código Python a medida (``python_code``) o una función preestablecida del catálogo
(``preset_function_id``). Las funciones preestablecidas cubren los casos habituales sin
necesidad de escribir código y se documentan en :doc:`7_2_2_python-transformations`.

Prueba previa
-------------

Antes de aplicar un mapeo a datos reales, el sistema permite probarlo de forma
interactiva: se introduce un valor de ejemplo y se comprueba el resultado de la
transformación. Esta validación previa reduce el riesgo de propagar errores de mapeo a
los pedidos en producción.

Entrada frente a salida
-----------------------

Conviene distinguir el **mapeo de entrada** —``tms.edi.field.mapping``, que normaliza
los datos que llegan al TMS— del **patrón de salida** —``tms_int.pattern.line``, que
construye el *payload* enviado a sistemas remotos (ver :doc:`7_4_endpoint-configuration`).
Ambos comparten la lógica de transformación por campo, pero operan en sentidos opuestos
del intercambio.
