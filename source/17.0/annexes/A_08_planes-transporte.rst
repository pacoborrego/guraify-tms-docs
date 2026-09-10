A.8 Planes de transporte
========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Planes de Transporte

Modelo Odoo: ``tms.transport.plan``. La red territorial: el conjunto de áreas geográficas por las que circula una operativa y la agencia responsable.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre del plan.
   * - Agencia
     - Relación con Contacto (agencia)
     - La agencia responsable de la red. Se propaga a los tramos cuya dirección cae en un área del plan.
   * - Áreas
     - Lista de Áreas geográficas
     - Las áreas de tipo Plan de transporte que forman la red.
   * - Vista Seguimiento
     - Mapa (calculado)
     - Previsualización de la agencia y los polígonos del plan.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
