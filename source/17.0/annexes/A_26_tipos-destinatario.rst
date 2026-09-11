A.26 Tipos de Destinatario
==========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › Tipos de Destinatario

Modelo Odoo: ``tms.receiper.type``. El segmento del destinatario de la mercancía: empresa, particular, comercio, hostelería, gran superficie.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece) y **Defecto** (marca el tipo considerado estándar). El nombre debe ser único dentro de cada compañía.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre del segmento, tal y como aparece en Órdenes, Tramos, Viajes, Proyectos y tarifas. Es traducible.
   * - Descripción
     - Texto
     - Descripción breve del segmento. Obligatoria.
   * - Información
     - Texto
     - Notas internas de parametrización. Es traducible.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`.
