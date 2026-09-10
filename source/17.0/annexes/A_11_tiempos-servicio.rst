A.11 Tiempos de servicio
========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Tiempos de Servicio

Modelo Odoo: ``tms.service.time``. El esquema con el que se calcula cuánto dura una parada más allá de la conducción. Se compone de líneas, cada una con una operación y una matriz de detalles.

Esquema (tms.service.time)
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre del esquema. El Proyecto elige uno.
   * - Kg Defecto Nivel 0 / Kg Defecto Nivel > 0
     - Número
     - Kilos por defecto que se asumen para una parada en planta baja y para una en pisos, cuando la línea no trae peso.
   * - Líneas de Tiempo Servicio
     - Lista de líneas
     - Las operaciones que suman tiempo, con su matriz.

Línea (tms.service.time.line)
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Operación
     - Relación con Operación de tiempos de servicio
     - La plantilla que fija tipo, ámbito y factor. Al elegirla se copian a la línea y se genera la matriz de detalles.
   * - Tipo Operación
     - Selección
     - Dificultad (según la dificultad de aparcamiento del contacto), Niveles (según pisos y ascensor) o Fijo (siempre el mismo tiempo).
   * - Aplicar
     - Selección
     - Si la operación se cuenta por Tramo o por Parada. Una parada con cuatro tramos suma cuatro veces una operación por tramo y una sola vez una por parada.
   * - Detalles
     - Lista de detalles
     - La matriz de la línea.

Detalle (tms.service.time.line.detail)
--------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Dificultad
     - Selección
     - Muy baja, Baja, Normal o Alta. Fila de la matriz en operaciones de tipo Dificultad.
   * - Niveles
     - Número
     - Número de pisos. Fila de la matriz en operaciones de tipo Niveles.
   * - Tipo Factor / Valor del Factor
     - Selección / Número
     - Si el tiempo es por Operación (una vez) o por Kg (proporcional al peso), y el valor de referencia.
   * - Tiempo en seg
     - Número
     - Los segundos que suma esa celda de la matriz.

Operación (tms.service.time.operation)
--------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la plantilla: «Descarga con dificultad», «Subida a piso».
   * - Tipo Operación / Aplicar / Tipo Factor
     - Selección
     - Los mismos tres valores que hereda la línea. Se mantienen en TMS › Configuración › Ajustes › Optimización de ruta › Operación de tiempos de servicio.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
