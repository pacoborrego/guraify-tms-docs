A.27 Tipos de Transportista
===========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › «Tipos de transportista»

Modelo Odoo: ``tms.carrier.type``. La clase de quien ejecuta el transporte: flota propia, transportista con contrato estable, transportista para picos, agencia.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece) y **Defecto** (marca el tipo considerado estándar). El nombre debe ser único dentro de cada compañía.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la clase, tal y como aparece en Órdenes, Tramos, Viajes, Proyectos y tarifas. Es traducible. La etiqueta de la interfaz es «Id».
   * - Descripción
     - Texto
     - Descripción breve de la clase. Obligatoria.
   * - Información
     - Texto
     - Notas internas de parametrización.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`.
