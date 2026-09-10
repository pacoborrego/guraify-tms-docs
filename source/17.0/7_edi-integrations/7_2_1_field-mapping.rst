7.2.1 Mapeo de Campos
=====================

El mapeo de campos establece la correspondencia entre los campos del sistema externo y
los campos del modelo de Odoo. Es la pieza que hace posible que datos con nomenclaturas
y formatos dispares acaben encajando en la misma estructura interna.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Definición de Fichero

7.2.1.1 Modelo de mapeo
-----------------------

.. CAPTURA: 7_2_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_1_field-mapping_01_lista-mapeos.png
      :alt: Mapeos de columnas de una Definición de fichero

      Mapeos de columnas de una Definición de fichero.

El mapeo de entrada se define en ``tms.edi.field.mapping``, que asocia una columna de
origen (``column_name``) con un campo de destino (``field``) y declara las conversiones
de tipo aplicables tanto a la entrada como a la respuesta. Cada Definición de fichero
(``tms.edi.file``) agrupa los mapeos que le corresponden, de manera que un mismo tipo de
intercambio reutiliza siempre la misma configuración de columnas (ver
:doc:`7_2_file-import`).

7.2.1.2 Campos destino disponibles
----------------------------------

El campo de destino (``field``) no es texto libre: se elige de un catálogo cerrado de
campos que el TMS sabe materializar. Ese catálogo está agrupado por la entidad de
negocio a la que pertenece cada campo, de modo que un mismo fichero puede alimentar a la
vez los datos del Viaje, de la Orden, de los Tramos, de las líneas y de los datos
maestros (clientes, transportistas, conductores y vehículos). La función de este
catálogo es doble: garantiza que la columna del fichero externo apunta a un destino
válido del modelo y sirve de referencia al consultor para saber qué información puede
importarse y bajo qué nombre.

.. CAPTURA: 7_2_1_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_1_field-mapping_02_selector-campo.png
      :alt: Catálogo de campos destino agrupado por entidad

      Catálogo de campos destino agrupado por entidad (selector *Tms Field*).

El catálogo completo, campo a campo, está en el
:doc:`anexo A.22 </17.0/annexes/A_22_campos-mapeo>`. Estas son las entidades que cubre y
algunos de sus campos, para hacerse una idea de qué puede traer un fichero:

.. list-table::
   :header-rows: 1
   :widths: 34 12 54

   * - Entidad
     - Campos
     - Ejemplos
   * - Viaje (``tms.trip``)
     - 11
     - ``TripName``, ``TripDate``, ``TripPlanning`` …
   * - Orden (``sale.order``)
     - 13
     - ``Project``, ``Customer``, ``PriceList`` …
   * - Tramos — carga y descarga (``tms.shipment.leg``)
     - 22
     - ``LoadAddressKey``, ``LoadName``, ``LoadAddress`` …
   * - Líneas de mercancía (``tms.shipment.pack``)
     - 9
     - ``Packs``, ``Pallets``, ``Quantity`` …
   * - Bultos / trazabilidad (``tms.shipment.pack.traceability``)
     - 4
     - ``Parcel_Barcode``, ``Parcel_Cube``, ``Parcel_GrossWeight`` …
   * - Clientes (``res.partner``)
     - 13
     - ``CustomerId``, ``CustomerName``, ``CustomerShortName`` …
   * - Transportistas (``res.partner``)
     - 13
     - ``CarrierId``, ``CarrierName``, ``CarrierShortName`` …
   * - Conductores (``res.partner`` / ``hr.employee``)
     - 12
     - ``DriverId``, ``DriverName``, ``DriverShortName`` …
   * - Vehículos (``fleet.vehicle``)
     - 10
     - ``VehicleId``, ``VehicleName``, ``VehicleLicensePl`` …

El catálogo incluye además separadores no seleccionables (``<<<<TRIPS>>>>``,
``<<<<SHIPMENTS>>>>``…) que sólo agrupan visualmente los campos en el desplegable; no son
destinos de mapeo.

7.2.1.3 El campo especial ``Parcel_Array``
------------------------------------------

Los campos ``Parcel_Barcode``, ``Parcel_Cube`` y ``Parcel_GrossWeight`` son escalares:
cada uno toma el valor de una columna y describe **un** bulto. Funcionan bien cuando
el fichero trae **una fila por bulto**.

``Parcel_Array`` resuelve el caso contrario: clientes que envían **un único registro por
orden** (sin detalle de bultos), pero cuyos códigos de barras impresos en las
etiquetas de origen siguen una regla de construcción conocida. En lugar de un valor
escalar, ``Parcel_Array`` espera la **lista completa de bultos** de la orden, que
se genera por código a partir de los datos de la fila.

7.2.1.3.1 Cómo funciona internamente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A diferencia del resto de campos de bulto, cuando la transformación escribe en
``Parcel_Array`` el importador **sustituye** la estructura de bultos completa por el
valor devuelto (no asigna un atributo suelto). Por eso la función debe devolver una
**lista de diccionarios**, uno por bulto, con las claves que el importador sabe
materializar:

- ``Parcel_Barcode`` — código de barras de la etiqueta de origen.
- ``Parcel_GrossWeight`` — peso bruto del bulto.
- ``Parcel_Cube`` — volumen del bulto.

Esa lista se asigna directamente a los bultos (``Parcels``) de la línea de mercancía
de la orden.

7.2.1.3.2 Configuración del mapeo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Parcel_Array`` se configura como un **campo computado**, no como un mapeo de columna
directo:

#. En el mapeo, marcar **Computed** (``is_computed``). Al hacerlo, el nombre de columna
   pasa automáticamente a ``_Cmptd_Parcel_Array``: el importador lo trata como campo
   calculado tras procesar las columnas normales de la fila.
#. Marcar **Apply Code?** (``apply_code``) y escribir la lógica de construcción en
   **Python Code** (``python_code``).

.. figure:: /_static/img/7_edi-integrations/7_2_1_field-mapping_03_parcel-array.png
   :alt: Configuración del campo computado Parcel_Array

   Configuración del campo computado ``Parcel_Array`` (*Computed* + *Apply Code?*).

El código se ejecuta en el mismo entorno controlado que las demás transformaciones
(:doc:`7_2_2_python-transformations`): dispone de ``value``, ``row`` (la fila actual,
indexada por posición de columna), ``rows`` (todas las filas) y las librerías ``json``,
``re`` y ``datetime``; el resultado se deja en ``result``. Como el cálculo es a nivel de
fila completa, la lógica lee los datos de ``row`` por índice de columna, no de ``value``.

7.2.1.3.3 Ejemplo de uso
~~~~~~~~~~~~~~~~~~~~~~~~

Supongamos un cliente que envía una fila por orden con, entre otras, una columna de
**referencia de orden**, una de **número de bultos** y una de **peso bruto total**.
Las etiquetas de origen imprimen un código de barras con la regla
``<Referencia><NN>``, donde ``NN`` es el número de bulto correlativo con dos dígitos
(``01``, ``02``, …). La función ``Parcel_Array`` reconstruye la lista de bultos y
reparte el peso a partes iguales:

.. code-block:: python

   # Índices (base 0) de las columnas de origen en la fila
   ref_index    = 0   # Referencia de orden (ExternalRef)
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

Con una fila de referencia ``ALB12345`` y 3 bultos, la función genera tres bultos con
códigos ``ALB1234501``, ``ALB1234502`` y ``ALB1234503``, cada uno con su parte
proporcional del peso. El importador los materializa como la trazabilidad de bultos
(``tms.shipment.pack.traceability``) de la línea de la orden.

.. tip::

   La regla de construcción del código de barras es específica de cada cliente. Ajusta
   el patrón (prefijos fijos, dígitos de control, relleno de ceros, segmentos derivados
   de otras columnas) a lo que realmente venga impreso en la etiqueta de origen, y
   valida el resultado con la prueba inline del mapeo antes de pasar a producción.

7.2.1.4 Transformación por campo
--------------------------------

Cuando la correspondencia no es directa, cada mapeo puede aplicar una transformación:
código Python a medida (``python_code``) o una función preestablecida del catálogo
(``preset_function_id``). Las funciones preestablecidas cubren los casos habituales sin
necesidad de escribir código y se documentan en :doc:`7_2_2_python-transformations`.

7.2.1.5 Prueba previa
---------------------

Antes de aplicar un mapeo a datos reales, el sistema permite probarlo de forma
interactiva: se introduce un valor de ejemplo y se comprueba el resultado de la
transformación. Esta validación previa reduce el riesgo de propagar errores de mapeo a
las Órdenes en producción.

7.2.1.6 Entrada frente a salida
-------------------------------

Conviene distinguir el **mapeo de entrada** —``tms.edi.field.mapping``, que normaliza
los datos que llegan al TMS— del **patrón de salida** —``tms_int.pattern.line``, que
construye el *payload* enviado a sistemas remotos (ver :doc:`7_4_endpoint-configuration`).
Ambos comparten la lógica de transformación por campo, pero operan en sentidos opuestos
del intercambio.
