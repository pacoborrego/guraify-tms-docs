A.12 Horas de conducción
========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Optimización de ruta › Horas de Conducción

Modelo Odoo: ``tms.driver.working.hours``. El perfil de jornada (horas de conducción y regulación)
que se envía a PTV, y las pausas explícitas de la jornada.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos
del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué
compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando
hay que elegir uno y nadie ha elegido).

A.12.1 Perfil de jornada
------------------------

El perfil de jornada (``tms.driver.working.hours``) es lo que eligen la categoría de vehículo y la
franja del Plan de disponibilidad.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Id / Descripción / Información
     - Texto
     - Nombre, explicación breve y notas del perfil. En la interfaz el nombre se llama «Id».
   * - Ajuste Secuencia
     - Selección (perfiles de PTV)
     - El perfil que se envía a la secuenciación: EU_DRIVING_TIME_REGULATION,
       EU_DRIVING_TIME_REGULATION_FOR_LONG_DAY, EU_WORKING_TIME_DIRECTIVE, US_HOURS_OF_SERVICE...
   * - Ajustes de Optimización
     - Selección (perfiles de PTV)
     - El perfil que se envía al cálculo de ruta y a la optimización completa: las variantes
       FOR_SINGLE_DAY, FOR_LONG_SINGLE_DAY, FOR_MULTIPLE_DAYS de las regulaciones europea y
       americana.
   * - Duración máxima de ruta (h)
     - Número
     - Duración máxima de un Viaje bajo esta regla, si la categoría de vehículo no define la suya.
   * - Pausas de trabajo / Pausas de conducción
     - Lista de pausas
     - Las pausas explícitas de la jornada. Se registran aquí para el optimizador con pausas, en
       desarrollo (ver :doc:`/17.0/1_introduction/1_4_technological-architecture`).

A.12.2 Pausa
------------

Cada pausa (``tms.driver.working.hours.break``) describe cuándo toca parar y cuánto.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tipo
     - Selección
     - De trabajo (tiempo máximo trabajando antes de la pausa) o de conducción (tiempo máximo
       conduciendo).
   * - Duración máxima (min)
     - Número
     - Minutos continuos de trabajo o conducción antes de que toque la pausa.
   * - Duraciones de pausa (min)
     - Texto
     - Minutos de pausa, separados por comas. «45» es una pausa de 45 minutos; «15,30» permite
       partirla en 15 y 30.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
