3.4 Modelo de tarificación
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Opciones de Tarifa

El modelo de tarificación define las reglas mediante las cuales el sistema calcula
automáticamente el precio de los servicios de transporte. Su arquitectura permite representar
distintos modelos comerciales y aplicar reglas de cálculo basadas en múltiples variables
logísticas (peso, volumen, bultos, kilómetros, zonas). Lo esencial es que el precio **nace de la
estructura operativa**: no es un cálculo externo, sino una consecuencia de la Orden
(``sale.order``) y sus Tramos.

3.4.1 Componentes
~~~~~~~~~~~~~~~~~

El cálculo se apoya en un conjunto de entidades de configuración:

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Elemento
     - Papel
   * - Productos (``product.template``)
     - Conceptos facturables que se asocian a las líneas económicas.
   * - :term:`Reglas de tarifa <Regla de tarifa>` (``tms.pricelist.rule``)
     - Cómo se mide la mercancía de cada línea de la Orden: por bultos, palés, cantidad o metros
       lineales.
   * - :term:`Tarifas base <Tarifa base>` (``tms.pricelist.base``)
     - Qué magnitud se cobra (peso, volumen, bultos, kilómetros, paradas…) y con qué rangos;
       plantilla para generar Líneas de tarifa.
   * - :term:`Zonas de tarifa <Zona de tarifa>` (``tms.pricelist.zone``)
     - Agrupaciones geográficas sobre las que se definen precios diferenciados.
   * - :term:`Líneas de tarifa <Línea de tarifa>` (``tms.pricelist.item.zone``)
     - El precio: condiciones de aplicación y detalles con el importe por zona de origen y de
       destino.
   * - :term:`Tarifas <Tarifa>` (``tms.pricelist``)
     - La tarifa de un Proyecto o de un transportista, que combina los elementos anteriores.
       Se organiza en :term:`versiones <Versión de tarifa>` consecutivas con fecha de vigencia,
       y se tarifica con la vigente en la fecha de la Orden.

3.4.2 Cálculo del ingreso
~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando se valida o tarifica una Orden, el sistema aplica la tarifa del Proyecto y genera las
líneas de venta correspondientes. El importe puede segmentarse por Tramo cuando la operativa lo
requiere, de modo que distintas fases del servicio tengan impacto económico diferenciado. La
configuración de cada elemento se recorre en
:doc:`/17.0/4_parametrization/4_4_economic-configuration`; cuándo se tarifica, el cálculo del
coste y la liquidación al transportista, en :doc:`/17.0/5_operational-flows/5_6_settlement`, y
la facturación al cliente en :doc:`/17.0/5_operational-flows/5_7_invoicing`. Cómo se reparten
ventas y costes entre Tramos y Paradas y cómo se controla el margen, en
:doc:`/17.0/8_economic-administration/index`.

.. figure:: /_static/img/3_functional-architecture/3_4_pricing-model_01_tarifa.png
   :alt: Configuración de una Tarifa en Odoo

   Configuración de una Tarifa en Odoo.
