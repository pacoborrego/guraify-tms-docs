3.4 Modelo de tarificación
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración (Tarifas, Reglas, Productos)

El modelo de tarificación define las reglas mediante las cuales el sistema calcula
automáticamente el precio de los servicios de transporte. Su arquitectura permite
representar distintos modelos comerciales y aplicar reglas de cálculo basadas en
múltiples variables logísticas (peso, volumen, bultos, kilómetros, zonas, etc.). Lo
esencial es que el precio **nace de la estructura operativa**: no es un cálculo externo,
sino una consecuencia de la Orden y sus Tramos.

3.4.1 Componentes
~~~~~~~~~~~~~~~~~~

El cálculo se apoya en un conjunto de entidades de configuración:

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Elemento
     - Papel
   * - Productos (``product.product``)
     - Conceptos facturables que se asocian a las líneas económicas.
   * - Reglas de tasación (``tms.pricelist.rule``)
     - Condiciones que determinan qué tarifa y qué cálculo se aplican a cada operación.
   * - Reglas de negocio (``tms.rule`` / ``tms.rule.model``)
     - Lógica configurable que adapta el comportamiento del sistema sin tocar el código.
   * - Zonas tarifarias (``tms.pricelist.zone``)
     - Agrupaciones geográficas sobre las que se definen precios diferenciados.
   * - Tarifas base (``tms.pricelist.base``)
     - Estructura de precios de referencia, con rangos (``tms.pricelist.base.range``).
   * - Tarifas (``tms.pricelist``)
     - Tarifa aplicable, versionable (``tms.pricelist.version``), que combina los
       elementos anteriores.

3.4.2 Cálculo del ingreso
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando se valida o tarifica una Orden (``sale.order``), el sistema aplica las reglas de
tasación configuradas y genera las líneas de venta correspondientes. El importe puede
segmentarse por Tramo (``tms.shipment.leg``) cuando la operativa lo requiere, de modo que
distintas fases del servicio tengan impacto económico diferenciado. El detalle de la
división de ventas y de costes, así como la liquidación, se desarrolla en el capítulo 8
(Administración y Control Económico).

.. CAPTURA: 3_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_4_pricing-model_01_tarifa.png
      :alt: Configuración de una Tarifa en Odoo

      Configuración de una Tarifa (``tms.pricelist``) en Odoo.
