A.17 Productos TMS
==================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Maestros › Productos

Modelo Odoo: ``product.template``. Los productos de Odoo que el TMS puede usar en tarifas y líneas económicas. Sólo se añaden dos campos al producto estándar.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Producto TMS
     - Sí/No
     - Habilita el producto para las líneas de tarifa y los proyectos. Sin esta marca no aparece en el TMS.
   * - Tipo de servicio TMS
     - Selección
     - La familia del concepto: Portes, Suplemento de portes, Logística y almacenaje, Suministros refacturados, Servicios y consultoría. Sirve para agrupar en informes y en la factura agrupada.
   * - Nombre comercial (TMS)
     - Texto
     - Cómo debe leer el cliente el concepto en el documento de tarifa. Si está vacío se usa el nombre del producto. Lo añade el módulo comercial.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_4_economic-configuration`.
