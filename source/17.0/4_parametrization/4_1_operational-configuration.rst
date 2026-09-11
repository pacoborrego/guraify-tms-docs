4.1 Configuración operativa
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes, bloque **Datos auxiliares**: «Tipos de servicios», Tipos de
   Orden, «Tipos de parada», Tipos de Destinatario, «Tipos de transportista» y Tipos de
   Reembolso. Cada enlace del bloque abre la lista del catálogo, desde la que se crean, se
   modifican y se archivan los registros.

La configuración operativa son seis catálogos pequeños que clasifican lo que se mueve por el
sistema: el servicio que se vende, la Orden, la Parada, el Destinatario, el Transportista y la
forma de cobrar un Reembolso. Ninguno lleva precios ni horarios, pero casi todos los procesos
los usan como criterio: el Tipo de Orden decide qué lado de un Tramo es el hub y cuál el
cliente; el Tipo de Parada, qué Paradas se pueden planificar; los tipos de servicio, de
destinatario y de transportista son condiciones de las Líneas de tarifa y filtros del
Proyecto. Por eso se configuran antes que el resto del capítulo y se cambian poco después.

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_01_datos-auxiliares.png
   :align: center
   :alt: Panel de Datos auxiliares en Ajustes

   El bloque «Datos auxiliares» de TMS › Configuración › Ajustes, punto de entrada a los seis
   catálogos.

Cada maestro se describe aquí por lo que decide el cliente y por dónde se nota después. La
lista completa de campos de cada pantalla está en el :doc:`anexo A </17.0/annexes/index>`.

4.1.1 Tipos de Servicio
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_02_tipos-servicio-lista.png
   :align: center
   :alt: Lista de Tipos de Servicio

   Lista de Tipos de Servicio: productos, Tipos de Orden compatibles y variables logísticas de
   cada uno.

El Tipo de Servicio (``tms.service.type``) clasifica el servicio de transporte que se vende:
carga completa, grupaje, distribución urbana, entrega con compromiso horario, larga distancia,
movimiento interno. Es la dimensión comercial de la Orden y el puente entre lo que se hace y
lo que se factura: cada Orden, cada Tramo y cada Viaje llevan un tipo de servicio, y las
Líneas de tarifa lo usan para dar precios distintos a servicios distintos.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué servicios existen
     - Una operativa con precios, plazos o exigencias distintas merece un tipo propio; dos
       servicios que se cobran y se planifican igual no. Cada tipo es un criterio más que la
       tarifa y el Proyecto tendrán que contemplar.
   * - Productos
     - Los productos TMS con los que se relaciona el servicio. Es obligatorio informar al
       menos uno y solo se admiten productos marcados como Producto TMS (ver
       :doc:`4_4_economic-configuration`). El producto que finalmente lleva cada línea
       económica lo fija la Línea de tarifa.
   * - Tipos de Orden compatibles
     - Con qué Tipos de Orden se puede combinar el servicio. Sirve de referencia al
       configurar el Proyecto y las tarifas.
   * - Variables logísticas
     - Las casillas Bultos, Cantidad, Metros y Palés dicen qué magnitudes intervienen en
       el servicio. Al añadir mercancía a un Tramo, el sistema solo ofrece las Reglas de tarifa
       que miden alguna de las magnitudes marcadas (ver :doc:`4_2_logistic-configuration`).

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_03_tipos-servicio-form.png
   :align: center
   :alt: Formulario de un Tipo de Servicio

   Formulario de un Tipo de Servicio con sus variables logísticas.

El tipo de servicio aparece después en tres sitios. En el **Proyecto**, la lista de servicios
activados limita los que se pueden elegir en sus Órdenes, uno de ellos se propone por
defecto, y un servicio aparte tarifica la recogida a domicilio (ver
:doc:`4_5_project-configuration`). En las **Líneas de tarifa**, el servicio es una de las
condiciones que deciden si la línea aplica (ver :doc:`4_4_economic-configuration`). Y en las
**Franjas horarias**, cada franja puede limitarse a unos servicios (ver
:doc:`4_3_planning-configuration`). Campos en :doc:`/17.0/annexes/A_23_tipos-servicio`.

4.1.2 Tipos de Orden
~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_04_tipos-orden.png
   :align: center
   :alt: Lista de Tipos de Orden

   Lista de Tipos de Orden: las cuatro marcas de comportamiento y los porcentajes de carga y
   descarga.

El Tipo de Orden (``tms.shipment.type``) define el comportamiento logístico de la Orden dentro
de la red: si es una entrega desde el hub, una recogida hacia el hub, un servicio directo
entre dos puntos del cliente o una operación de hub. Mientras el Tipo de Servicio dice qué se
vende, el Tipo de Orden dice cómo circula la mercancía.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - La marca de comportamiento
     - Cada tipo lleva una de las cuatro marcas: **Entrega**, **Recogida**, **Directo** o
       **Hub**. Al crear un Tramo con ese tipo, el sistema propone qué lado es el del cliente
       y cuál el del hub o la agencia del Proyecto (en una entrega se carga en el hub; en una
       recogida se descarga en él; en un directo los dos lados son del cliente; en una
       operación de hub los dos lados son el hub). Al validar la Orden, esa misma marca decide
       qué Tipo de Parada recibe cada lado y con qué otros Tramos puede compartir Parada (ver
       :doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`).
   * - Activo Carga % y Activo Descarga %
     - Cómo se reparte el ingreso de un Tramo entre su Parada de carga y su Parada de
       descarga. Los dos porcentajes deben sumar el 100 %; el sistema no guarda el registro si
       no lo hacen. Es la segunda mitad de la :term:`División de ventas` (ver
       :doc:`/17.0/8_economic-administration/8_2_sales-split`).
   * - Punto de Recogida Habitual
     - Marca el tipo con el que el sistema crea la Orden de recogida a domicilio cuando el
       Proyecto trabaja con punto de recogida en casa del cliente. Tiene que existir uno, o el
       cierre del Manifiesto se detiene.
   * - Imagen y color
     - El icono que acompaña a la Orden y al Tramo en las listas, para reconocer el tipo de un
       vistazo.

El Tipo de Orden no crea los Tramos: los crea el usuario, o el fichero, o la integración. Lo
que hace es decidir cómo se interpretan. Después aparece como condición en las Líneas de
tarifa y en sus detalles, y en el Proyecto como lista de tipos admitidos y tipo por defecto.
El Manifiesto cuenta sus Órdenes por tipo (entregas, recogidas, directos y operaciones de hub).
Campos en :doc:`/17.0/annexes/A_24_tipos-orden`.

4.1.3 Tipos de Parada
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_05_tipos-parada.png
   :align: center
   :alt: Lista de Tipos de Parada

   Lista de Tipos de Parada: seis registros, cada uno con una única marca activa.

El Tipo de Parada (``tms.stop.type``) dice qué papel juega una Parada en la operativa. A
diferencia de los otros catálogos, aquí el cliente no decide cuántos registros hay: el modelo
define **seis papeles**, cada registro lleva exactamente uno y no puede haber dos registros de
la misma compañía con el mismo papel. Los seis papeles son **Operaciones de Hub** (la entrada o
la salida de mercancía en un hub), **Punto de Recogida** (la carga de una recogida a
domicilio), **Parada de Ruta** (la parada en casa del cliente, la que se planifica y se
reparte), **Recogida Directo** y **Entrega Directo** (los dos lados de un servicio directo) y
**Paradas Optimizador** (las paradas de inicio y fin que genera el optimizador; no son eventos
ejecutables).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Nombre, descripción e imagen de cada papel
     - Es lo único que el cliente adapta: cómo se llama cada tipo en su casa y con qué icono
       lo ven el planificador en las listas y el conductor en la app. El papel no se cambia:
       al marcar una casilla se desmarcan las demás.
   * - Que existan los seis
     - El sistema busca cada papel por su marca cuando lo necesita: al validar una Orden
       asigna Parada de Ruta, Operaciones de Hub, Punto de Recogida o los dos directos según el
       Tramo; al optimizar crea las paradas de inicio y fin con el papel de optimizador. Si
       falta el registro de un papel, el flujo que lo busca no encuentra tipo.

El papel condiciona lo que se puede hacer con la Parada. Solo las Paradas de Ruta y las
directas se asignan a un Viaje, se envían a una agencia o se reprograman; las de hub las crea
y las quita el propio Viaje, y las de optimizador quedan fuera de la secuenciación y de los
documentos de carga. Cómo se asigna el tipo al validar y qué estados recorre después la
Parada está en :doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`. Campos en
:doc:`/17.0/annexes/A_25_tipos-parada`.

4.1.4 Tipos de Destinatario
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_06_tipos-destinatario.png
   :align: center
   :alt: Lista de Tipos de Destinatario

   Lista de Tipos de Destinatario.

El Tipo de Destinatario (``tms.receiper.type``) segmenta a quién se entrega: empresa o
particular, comercio, hostelería, gran superficie, punto de conveniencia. Es un catálogo
libre, sin comportamiento propio, cuyo valor está en lo que permite condicionar.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué segmentos existen
     - Solo merecen un tipo los segmentos que cambian el precio o la operativa (una entrega a
       particular con franja estrecha frente a una entrega a un almacén). Cada segmento es una
       condición más que las tarifas pueden usar.

El tipo se informa en la Orden y lo heredan sus Tramos y su Viaje. El Proyecto lista los
tipos que admite y propone uno por defecto; las Líneas de tarifa lo usan como condición para
que el mismo servicio tenga precios distintos según a quién se entregue (ver
:doc:`4_4_economic-configuration` y :doc:`4_5_project-configuration`). Campos en
:doc:`/17.0/annexes/A_26_tipos-destinatario`.

4.1.5 Tipos de Transportista
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_07_tipos-transportista.png
   :align: center
   :alt: Lista de Tipos de Transportista

   Lista de Tipos de Transportista.

El Tipo de Transportista (``tms.carrier.type``) clasifica a quien ejecuta el transporte:
flota propia, transportista con contrato estable, transportista para picos de demanda,
agencia. Como el anterior, es un catálogo libre que sirve de condición.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué clases de transportista existen
     - Las que se pagan o se asignan de forma distinta. El tipo no sustituye a la marca de
       flota propia del contacto, que es la que decide si el Viaje genera Orden de compra (ver
       :doc:`/17.0/8_economic-administration/8_1_active-passive-margin`).

El tipo se informa en la Orden, en el Tramo y en el Viaje, y el asistente **Asignar a viaje**
permite fijarlo al crear el Viaje. El Proyecto lista los tipos que admite y propone uno por
defecto; las Líneas de tarifa lo usan como condición, de modo que un mismo recorrido puede
costar distinto según la clase de transportista que lo haga (ver
:doc:`4_4_economic-configuration` y :doc:`/17.0/5_operational-flows/5_2_trip-generation`).
Campos en :doc:`/17.0/annexes/A_27_tipos-transportista`.

4.1.6 Tipos de Reembolso
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_08_tipos-reembolso.png
   :align: center
   :alt: Lista de Tipos de Reembolso

   Lista de Tipos de Reembolso.

El Tipo de Reembolso (``tms.cashvalue.type``) es la forma de cobro de un :term:`Reembolso`:
en metálico, con TPV propio o del cliente, con cheque bancario. No es el importe ni el estado
del cobro; es la modalidad con la que el conductor debe cobrarlo.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué formas de cobro existen
     - Las que la empresa acepta en la entrega. Cada Reembolso de un Tramo lleva una, y el
       conductor la ve en la app junto al importe, así que el nombre debe entenderse en la
       calle («Efectivo», «TPV», «Cheque»).

El tipo se elige al dar de alta el Reembolso en el Tramo, viaja con él a la app y queda en el
registro del cobro, con lo que la administración puede agrupar lo cobrado por modalidad. El
ciclo completo del Reembolso está en :doc:`/17.0/8_economic-administration/8_6_refunds` y el
cobro en la calle, en el :doc:`Manual del conductor </17.0/10_manual_app/index>`. Campos en
:doc:`/17.0/annexes/A_28_tipos-reembolso`.
