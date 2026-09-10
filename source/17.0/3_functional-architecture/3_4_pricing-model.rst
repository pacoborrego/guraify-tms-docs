3.4 Modelo de tarificación
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Opciones de Tarifa

El modelo de tarificación define las reglas mediante las cuales el sistema calcula
automáticamente el precio de los servicios de transporte. Su arquitectura permite
representar distintos modelos comerciales y aplicar reglas de cálculo basadas en
múltiples variables logísticas (peso, volumen, bultos, kilómetros, zonas). Lo esencial es
que el precio **nace de la estructura operativa**: no es un cálculo externo, sino una
consecuencia de la Orden y sus Tramos.

3.4.1 Componentes
~~~~~~~~~~~~~~~~~

El cálculo se apoya en un conjunto de entidades de configuración:

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Elemento
     - Papel
   * - Productos (``product.product``)
     - Conceptos facturables que se asocian a las líneas económicas.
   * - :term:`Reglas de tarifa <Regla de tarifa>` (``tms.pricelist.rule``)
     - Qué se mide para tarificar: peso, volumen, bultos, kilómetros, paradas.
   * - :term:`Líneas de tarifa <Línea de tarifa>` (``tms.pricelist.item.zone``)
     - El precio: condiciones de aplicación y detalles con el importe por zona de origen y
       de destino.
   * - :term:`Zonas de tarifa <Zona de tarifa>` (``tms.pricelist.zone``)
     - Agrupaciones geográficas sobre las que se definen precios diferenciados.
   * - :term:`Tarifas base <Tarifa base>` (``tms.pricelist.base``)
     - Estructura de precios de referencia, con rangos.
   * - :term:`Tarifas <Tarifa>` (``tms.pricelist``)
     - Tarifa aplicable, con versiones, que combina los elementos anteriores.
   * - Reglas de negocio (``tms.rule``)
     - Lógica configurable que adapta el comportamiento del sistema sin tocar el código.

3.4.2 Cálculo del ingreso
~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando se valida o tarifica una Orden (``sale.order``), el sistema aplica la tarifa del
Proyecto y genera las líneas de venta correspondientes. El importe puede segmentarse por
Tramo cuando la operativa lo requiere, de modo que distintas fases del servicio tengan
impacto económico diferenciado. La configuración de cada elemento se recorre en
:doc:`/17.0/4_parametrization/4_4_economic-configuration`; el cálculo del coste y la
liquidación al transportista, en :doc:`/17.0/5_operational-flows/5_6_settlement`, y la
facturación al cliente en :doc:`/17.0/5_operational-flows/5_7_invoicing`. Cómo se reparten
ventas y costes entre Tramos y Paradas y cómo se controla el margen, en
:doc:`/17.0/8_economic-administration/index`.

.. figure:: /_static/img/3_functional-architecture/3_4_pricing-model_01_tarifa.png
   :alt: Configuración de una Tarifa en Odoo

   Configuración de una Tarifa en Odoo.
