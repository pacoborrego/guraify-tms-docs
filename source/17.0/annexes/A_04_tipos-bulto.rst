A.4 Tipos de bulto
==================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › Tipos de Bulto

Modelo Odoo: ``tms.temperature``. Qué mercancía se transporta: seco, refrigerado, congelado, frágil,
con su rango de temperatura cuando lo tiene.

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
     - Nombre del tipo.
   * - Descripción
     - Texto
     - Explicación breve. Obligatoria.
   * - Información
     - Texto
     - Notas internas.
   * - Mín. (°C) / Máx. (°C)
     - Número
     - Límites de la clase de temperatura. Una lectura fuera de ellos es una excursión. Con los dos
       a cero no hay rango y no se juzga ninguna lectura.
   * - Tiene rango
     - Sí/No (calculado)
     - Si la clase tiene límites configurados.
   * - Equipamientos
     - Lista de Equipamientos
     - Lo que el vehículo necesita para llevar este tipo de mercancía (por ejemplo, frío).
   * - Imagen
     - Imagen
     - Icono del tipo, para la app y las etiquetas.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_2_logistic-configuration`.
