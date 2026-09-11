A.19 Odómetro único
===================

.. admonition:: Ruta en Odoo
   :class: tip

   Pestaña «Odometer (TMS)» de la ficha del vehículo (TMS › Maestros › Equipos › Vehículos) · Gestión de Recursos › Configuración › «Odometer Anomalies» · umbral en la ficha de la compañía

Modelo Odoo: ``fleet.vehicle.odometer``, extendido, y los campos añadidos al vehículo
(``fleet.vehicle``) y a la compañía (``res.company``). Las pantallas del área Gestión de Recursos no
llevan todavía traducción y muestran sus etiquetas en inglés; aquí se dan en español.

A.19.1 Lectura
--------------

La lectura (``fleet.vehicle.odometer``) es cada registro de la serie de kilometraje.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Origen
     - Selección
     - De dónde viene la lectura: Manual, Mantenimiento, Importación de combustible, Combustible
       manual, App del conductor o Telemetría. Obligatorio.
   * - Modelo de fuente / Registro de origen
     - Texto / Número
     - El registro concreto del que salió la lectura (la orden de trabajo, el albarán).
   * - Referencia externa
     - Texto
     - Identificador de la lectura en el sistema de origen. Volver a importar la misma referencia no
       duplica la lectura.
   * - Estado de validación
     - Selección
     - Válida, Borrador (pendiente de revisar) o Rechazada. Solo las válidas cuentan para el
       kilometraje actual, el ritmo y las estimaciones.
   * - Anomalía
     - Selección
     - Ninguna, Retroceso, Salto inverosímil, Duplicada o Fecha futura.
   * - Nota de anomalía
     - Texto
     - La explicación de la regla que saltó, con los valores comparados.
   * - Revisada por / Revisada el
     - Usuario / Fecha y hora
     - Quién validó o rechazó la lectura y cuándo.
   * - Lectura válida anterior
     - Número (calculado)
     - La última lectura válida en la fecha de esta o antes: la referencia contra la que se midió la
       anomalía.
   * - Diferencia
     - Número (calculado)
     - Esta lectura menos la anterior válida. Negativa en un retroceso.

A.19.2 Vehículo
---------------

El resumen del odómetro vive en el vehículo (``fleet.vehicle``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Último odómetro (TMS) / Fecha / Origen
     - Número / Fecha / Selección
     - La lectura válida más reciente, su fecha y de dónde vino.
   * - Antigüedad de la última lectura (días)
     - Número (calculado)
     - Días desde la última lectura válida.
   * - Km por día
     - Número
     - Ritmo medio calculado sobre la serie válida. Se usa para estimar kilometrajes en fechas sin
       lectura.
   * - Tipo de contador
     - Selección
     - Odómetro (kilómetros) u Horas de motor. Con horas de motor no se aplica el salto inverosímil.
   * - Anomalías de odómetro
     - Número (calculado)
     - Lecturas en borrador pendientes de revisar; el botón inteligente de la ficha.
   * - Referencia del dispositivo de telemetría
     - Texto
     - Identificador del dispositivo que envía lecturas por telemetría.
   * - Configuración del vehículo
     - Texto
     - Ejes o carrocería como los llama el taller (4x2, 3 ejes, Cisterna). Se imprime junto al tipo
       en las salidas de taller. En la interfaz, «Unit Configuration».

A.19.3 Compañía
---------------

El umbral de la detección de saltos se configura en la compañía (``res.company``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Máximo de km por día
     - Número
     - Umbral del salto inverosímil: incremento diario por encima del cual la lectura entra en
       borrador. Por defecto 1.500.

Cómo se usa y qué decide el cliente: :doc:`/17.0/6_resources/6_2_odometer`.
