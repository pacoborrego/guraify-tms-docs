A.12 Horas de conducción
========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Optimización de ruta › Horas de Conducción

Modelo Odoo: ``tms.driver.working.hours``. El preset de jornada y regulación que se envía a PTV, y las pausas explícitas que usará OptiFlow.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando hay que elegir uno y nadie ha elegido).

Preset (tms.driver.working.hours)
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Id / Descripción / Información
     - Texto
     - Nombre, explicación breve y notas del preset. En la interfaz el nombre se llama «Id».
   * - Ajuste Secuencia
     - Selección (presets de PTV)
     - El preset que se envía a la secuenciación: EU_DRIVING_TIME_REGULATION, EU_DRIVING_TIME_REGULATION_FOR_LONG_DAY, EU_WORKING_TIME_DIRECTIVE, US_HOURS_OF_SERVICE...
   * - Ajustes de Optimización
     - Selección (presets de PTV)
     - El preset que se envía al cálculo de ruta y a la optimización completa: las variantes FOR_SINGLE_DAY, FOR_LONG_SINGLE_DAY, FOR_MULTIPLE_DAYS de las regulaciones europea y americana.
   * - Duración máxima de ruta (h)
     - Número
     - Duración máxima de una ruta bajo esta regla, si la categoría de vehículo no define la suya.
   * - Pausas de trabajo / Pausas de conducción
     - Lista de pausas
     - Las pausas explícitas, para OptiFlow.

Pausa (tms.driver.working.hours.break)
--------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tipo
     - Selección
     - De trabajo (tiempo máximo trabajando antes de la pausa) o de conducción (tiempo máximo conduciendo).
   * - Duración máxima (min)
     - Número
     - Minutos continuos de trabajo o conducción antes de que toque la pausa.
   * - Duraciones de pausa (min)
     - Texto
     - Minutos de pausa, separados por comas. «45» es una pausa de 45 minutos; «15,30» permite partirla en 15 y 30.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
