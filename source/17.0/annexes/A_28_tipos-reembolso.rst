A.28 Tipos de Reembolso
=======================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › Tipos de Reembolso

Modelo Odoo: ``tms.cashvalue.type``. La forma de cobro de un Reembolso: en metálico, con TPV propio o del cliente, con cheque. En el formulario del Reembolso el campo que la recoge se llama «Forma de Pago».

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece) y **Defecto** (marca la forma de cobro considerada estándar). El nombre debe ser único dentro de cada compañía.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la forma de cobro, tal y como lo ve el conductor en la app junto al importe del Reembolso. Es traducible. La etiqueta de la interfaz es «Id».
   * - Descripción
     - Texto
     - Descripción breve de la forma de cobro. Obligatoria.
   * - Información
     - Texto
     - Notas internas de parametrización.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`; el ciclo del Reembolso, en :doc:`/17.0/8_economic-administration/8_6_refunds`.
