A.2 Categorías de carga
=======================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Optimización de ruta › Categoría de Carga

Modelo Odoo: ``tms.load.category``. La naturaleza logística de la mercancía: refrigerada, seca,
paletizada, ADR, voluminosa.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos
del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué
compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando
hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la categoría.
   * - Descripción
     - Texto
     - Explicación breve. Obligatoria.
   * - Información
     - Texto
     - Notas internas.
   * - Equipamiento requerido
     - Lista de Equipamientos
     - Lo que un vehículo debe llevar para transportar esta carga. Un Tramo exige la unión de los
       equipamientos de todas sus categorías de carga; el optimizador solo asigna vehículos que los
       tengan.
   * - Incompatible con
     - Lista de Categorías de carga
     - Categorías que no pueden viajar en el mismo vehículo a la vez que esta. La relación se lee en
       los dos sentidos: basta rellenarla en una de las dos.
   * - Recuento de reglas
     - Número (calculado)
     - Cuántas reglas de automatización del TMS (``tms.rule``) usan esta categoría.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_2_logistic-configuration`.
