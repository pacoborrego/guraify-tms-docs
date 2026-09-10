A.1 Equipamientos
=================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Optimización de ruta › Equipamientos

Modelo Odoo: ``tms.equipment``. Lo que un vehículo lleva instalado o puede ofrecer: plataforma elevadora, frío, ADR, jaula.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre del equipamiento, tal y como se muestra en vehículos, categorías y proyectos. Es traducible.
   * - Código
     - Texto
     - Identificador estable que se envía al optimizador como capacidad del vehículo. Como el nombre se traduce, el código es la clave de emparejamiento entre lo que exige la carga y lo que tiene el vehículo.
   * - Descripción
     - Texto
     - Explicación breve del equipamiento. Obligatoria.
   * - Información
     - Texto
     - Notas internas de parametrización.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_2_logistic-configuration`.
