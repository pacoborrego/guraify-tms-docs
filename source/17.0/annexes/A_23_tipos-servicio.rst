A.23 Tipos de Servicio
======================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › «Tipos de servicios»

Modelo Odoo: ``tms.service.type``. El servicio de transporte que se vende (carga completa, grupaje, distribución urbana, larga distancia…) y sus variables logísticas.

Además de los campos de la tabla, el maestro lleva tres de los campos comunes a los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual) y **Compañía** (a qué compañía pertenece; la etiqueta de la interfaz es «Compañia», sin tilde). El nombre debe ser único dentro de cada compañía.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre del servicio, tal y como aparece en Órdenes, Tramos, Viajes y tarifas. Es traducible.
   * - Descripción
     - Texto
     - Descripción breve del servicio. Obligatoria y traducible.
   * - Productos
     - Relación múltiple con Producto
     - Productos TMS relacionados con el servicio. Obligatorio; solo admite productos marcados como Producto TMS (anexo :doc:`A_17_productos`).
   * - Tipo de Orden
     - Relación múltiple con Tipo de Orden
     - Tipos de Orden con los que el servicio se puede combinar (anexo :doc:`A_24_tipos-orden`).
   * - Bulto
     - Sí/No
     - El número de bultos interviene en el servicio. Con las tres casillas siguientes decide qué Reglas de tarifa se ofrecen en las líneas de mercancía de sus Tramos. La etiqueta de la interfaz es «Bulto», en singular.
   * - Cantidad
     - Sí/No
     - La cantidad de unidades interviene en el servicio.
   * - Metros
     - Sí/No
     - Los metros lineales intervienen en el servicio.
   * - Pallets
     - Sí/No
     - El número de palés interviene en el servicio.
   * - Información
     - Texto
     - Notas internas de parametrización.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`.
