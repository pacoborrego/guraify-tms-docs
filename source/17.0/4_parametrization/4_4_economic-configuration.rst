4.4 Configuración económica
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Opciones de Tarifa: Tarifa, Zonas de Tarifa, Tarifa Base y Detalle
   de regla de tarifa. Los productos, en TMS › Administración › Maestros › Productos.

La configuración económica es la que convierte la actividad en dinero: qué se cobra al cliente
por cada Orden y qué se paga al transportista por cada Viaje. Son cinco maestros encadenados.
Las **Zonas de tarifa** dicen entre qué territorios se fijan precios; las **Tarifas base**, qué
magnitud se cobra; la **Tarifa**, con sus versiones, agrupa los precios de un cliente o de un
transportista; las **Líneas de tarifa** y sus detalles, dentro de cada versión, dicen cuándo
aplica un precio y cuánto es; y los **Productos** llevan las líneas económicas a la
contabilidad de Odoo.

Tres conceptos de nombre parecido se reparten el trabajo y conviene no confundirlos. La
:term:`Regla de tarifa` del capítulo logístico dice **cómo se mide la mercancía** de una línea
de la Orden (por bultos, por palés, por cantidad o por metros) y no lleva precios. La
:term:`Tarifa base` dice **qué magnitud se cobra** (el peso, el volumen, los bultos, los
kilómetros, las paradas) y con qué escalado de rangos. Y la **Aplicación del precio**, en cada
detalle de una Línea de tarifa, dice **sobre qué unidad se multiplica** el precio unitario. Una
Orden puede medirse en palés (Regla), cobrarse por peso (Tarifa base) y llevar un suplemento
por kilómetro (Aplicación del precio) sin contradicción.

El motor de tarificación combina estos maestros con el contexto de cada operación: quién
paga, Proyecto, fecha, zonas de origen y destino, magnitudes de la carga y los catálogos del
capítulo 4.1 como condiciones. Cuándo se lanza y qué pasa cuando no encuentra precio está en
:doc:`/17.0/5_operational-flows/5_6_settlement`; el modelo, en
:doc:`/17.0/3_functional-architecture/3_4_pricing-model`; y la lista completa de campos, en el
:doc:`anexo A </17.0/annexes/index>`.

4.4.1 Zonas de tarifa
~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_4_economic-configuration_01_zonas-tarifarias.png
      :alt: Configuración de una Zona de tarifa

      Una Zona de tarifa con sus áreas sobre el mapa.

La :term:`Zona de tarifa` (``tms.pricelist.zone``) agrupa áreas geográficas a efectos de
precio. Es independiente de los planes de transporte: el plan organiza la operación y la zona
organiza el precio, y un mismo territorio puede estar dividido de dos maneras distintas.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué áreas forman la zona
     - Las áreas de tipo «Zona Tarifa» entre las que los detalles de tarifa fijan precios. Cuanto
       más fina la división, más precios distintos se pueden dar y más detalles hay que
       mantener.
   * - Una zona por tarifa
     - Cada Tarifa se apoya en una zona. Un cliente con precios por provincias y un
       transportista con precios por comarcas necesitan dos zonas.

Al recalcular un Tramo, el sistema toma la tarifa del cliente (para la venta) y la del
transportista (para la compra), va a su zona y resuelve las direcciones de carga y descarga
contra sus áreas. Si el Proyecto lo permite, una dirección fuera de todas las áreas toma la
más cercana y anota los kilómetros extra (ver :doc:`4_5_project-configuration`). Campos en
:doc:`/17.0/annexes/A_13_zonas-tarifa`.

4.4.2 Tarifas base
~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_4_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_4_economic-configuration_03_tarifa-base.png
      :alt: Lista de Tarifas Base

      Tarifas Base: qué magnitud se mide para aplicar un precio.

La :term:`Tarifa base` (``tms.pricelist.base``) define **qué magnitud se cobra**: peso,
volumen, bultos, palés, metros, cantidad, distancia, tiempo u otras. No contiene precios; es el
puente entre las magnitudes de la operación y los rangos de los detalles de tarifa.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - El tipo de cálculo
     - La magnitud que leerá el motor. Según el ámbito de la línea (Orden, Tramo, Parada o
       Viaje) esa magnitud sale de un sitio distinto: el peso de la Orden es la suma de sus
       tramos; el de la Parada, lo que se entrega en ella.
   * - Las plantillas de rangos
     - Escalados reutilizables (de 0 a 100 kg, de 100 a 500, de 500 a 1.000) con los que el
       asistente genera de golpe los detalles de una línea en vez de teclearlos uno a uno.

Cuando la Línea de tarifa activa la conversión volumétrica, el motor compara el peso real con
el volumen convertido a kilos y tarifica el mayor: es el :term:`peso tasable <Peso tasable>`.
Campos en :doc:`/17.0/annexes/A_14_tarifas-base`.

4.4.3 Tarifas y versiones
~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_4_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_4_economic-configuration_02_tarifa.png
      :alt: Configuración de una Tarifa

      Una Tarifa con sus versiones y las líneas de la versión actual.

La :term:`Tarifa` (``tms.pricelist``) es el contenedor de precios de un cliente o de un
transportista: su moneda, su zona de tarifa, sus contactos y sus versiones, cada una con sus
Líneas de tarifa. La misma entidad sirve para el precio de venta y para el coste de compra; lo
que la distingue es a quién se asigna y en qué tipo de Proyecto. Se crea antes que sus líneas:
primero la Tarifa con su zona y su primera versión, después las líneas dentro de la versión.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Zona de tarifa
     - Sobre qué territorios se definen los detalles. Fija la geografía de toda la tarifa.
   * - Modo de referencia de zona
     - Cómo se decide la zona de un Viaje: por su primera y última Parada, o por la carga y la
       descarga del Tramo más largo. Importa en los Viajes con muchas Paradas.
   * - Contactos
     - Los clientes o transportistas a los que aplica. Una tarifa puede compartirse entre varios.
   * - Las versiones
     - Cada cambio de precios es una :term:`versión <Versión de tarifa>` nueva con su vigencia
       y sus propias líneas. El sistema exige que las versiones de una Tarifa sean consecutivas:
       toda versión tiene fecha de inicio, cada una empieza el día siguiente al fin de la
       anterior (ni solapes ni huecos), solo la última puede quedar sin fecha de fin y solo
       una, la última, puede estar activa. Si al guardar no se cumple, el sistema no lo permite
       y dice qué versiones chocan.

Para calcular, el motor elige la versión vigente en la fecha administrativa de la operación,
que el Proyecto decide con su política de fecha (ver :doc:`4_5_project-configuration`); las
operaciones ya calculadas conservan la versión con la que se tarificaron. El estado de la
Tarifa (borrador, activa, caducada, archivada) se sincroniza con las fechas de sus versiones,
y una Tarifa caducada se puede ocultar sin perder el histórico. Campos en
:doc:`/17.0/annexes/A_16_tarifas`.

4.4.4 Líneas de tarifa y sus detalles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_4_04 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_4_economic-configuration_04_linea-tarifa.png
      :alt: Línea de tarifa con sus detalles

      Una Línea de tarifa: las condiciones arriba, los detalles con los importes debajo.

La :term:`Línea de tarifa` (``tms.pricelist.item.zone``) tiene dos niveles: la línea dice
**cuándo** aplica un precio (sobre qué ámbito y con qué condiciones) y sus detalles dicen
**cuánto** (el importe por zonas y rango). La línea vive dentro de una versión de la Tarifa.
Con esta separación, una misma Tarifa puede tener líneas por Orden, por Tramo, por Parada y
por Viaje, cada una con sus condiciones.

Lo que se decide en la **línea**:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Aplicar en
     - Sobre qué se calcula: la Orden completa, cada Tramo, cada Parada o el Viaje. Determina de
       dónde salen las magnitudes y dónde nace la línea económica.
   * - Tarifa base
     - Qué magnitud se mide para elegir el detalle.
   * - Producto
     - Con qué producto se crea la línea de venta o de compra, y por tanto con qué cuenta e
       impuestos llega a la contabilidad.
   * - Las condiciones
     - Los catálogos de :doc:`4_1_operational-configuration` (Tipo de Orden, de Servicio, de
       Transportista, de Destinatario y de Parada), el Planning y el hub. Vacío es
       «cualquiera»; informado, la línea solo aplica si la operación coincide. Así reparto y
       recogida, o urgente y normal, tienen precios distintos.
   * - Conversión volumétrica
     - Activa el peso tasable, con el factor de kilos por metro cúbico.

Lo que se decide en cada **detalle**:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Zonas de origen y destino
     - Entre qué áreas de la zona de tarifa aplica el importe. Vacío es cualquiera.
   * - Rango desde / hasta
     - El tramo de la magnitud (de 0 a 100 kg) en el que aplica.
   * - Precio unitario, forfait o porcentaje
     - Cómo se calcula el importe: por unidad de la magnitud, un precio cerrado, o un
       porcentaje sobre otra base.
   * - Aplicación del precio
     - Sobre qué unidad se multiplica el precio unitario: peso, volumen, bultos, palés, metros,
       cantidad, kilómetros u horas; o bien el importe del Reembolso (una comisión del 2 % sobre
       lo cobrado en la entrega) o un suplemento geográfico (un fijo por entrar en un área de
       tipo «Tarifa Extra»).
   * - Mínimo y máximo
     - El importe no baja del mínimo ni sube del máximo, sea cual sea la magnitud.
   * - Categorías de vehículo, clientes, transportistas
     - Restringen el detalle a unos vehículos o a unos contactos concretos.

Al tarificar, el motor selecciona las líneas del ámbito que calcula, las filtra por las
condiciones, mide la magnitud con la Tarifa base y aplica el detalle cuyo rango la incluye,
ajustado al mínimo y al máximo. Cada línea económica generada conserva la Tarifa, la línea, el
detalle, la zona y el producto de los que salió, lo que permite auditarla. Cuando ninguna línea
encaja, el :term:`diagnóstico de tarifa <Diagnóstico de tarifa>` dice por qué (ver
:doc:`/17.0/5_operational-flows/5_6_settlement`). Campos en
:doc:`/17.0/annexes/A_15_lineas-tarifa`.

4.4.5 Productos
~~~~~~~~~~~~~~~

Los productos conectan el TMS con la contabilidad estándar de Odoo. Solo los productos marcados
como **Producto TMS** pueden usarse en las líneas de tarifa y como producto por defecto de un
Proyecto. Todo lo demás (unidad de medida, impuestos, cuentas contables) es la configuración
normal de un producto de Odoo.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué productos existen
     - Un producto por concepto que se quiera ver separado en la factura y en los informes:
       portes, suplementos, reembolsos, servicios especiales. Con un solo producto todo se
       mezcla en una línea.
   * - «Tipo de servicio TMS» del producto
     - La familia del concepto (portes, suplemento de portes, logística y almacenaje,
       suministros refacturados, servicios y consultoría, otros), con la que los informes y
       tableros separan transporte de conceptos accesorios. No es el Tipo de Servicio de
       :doc:`4_1_operational-configuration`, que clasifica la Orden; este clasifica el producto.
   * - Cuentas e impuestos
     - Los de Odoo. Es lo que decide cómo contabiliza cada concepto.

Cuando el motor crea una línea de venta o de compra, le pone el producto de la línea de tarifa
(o del detalle, si lo tiene propio), y con él viajan la cuenta, los impuestos y la unidad.
Campos en :doc:`/17.0/annexes/A_17_productos`.
