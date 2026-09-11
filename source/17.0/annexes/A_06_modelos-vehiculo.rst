A.6 Modelos de vehículo
=======================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Maestros › Equipos › Modelos

Modelo Odoo: ``fleet.vehicle.model``. El modelo concreto (marca y modelo) con sus datos técnicos.
Extiende el modelo de la Flota de Odoo con lo que PTV necesita para el cálculo de ruta, los peajes y
las emisiones.

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
   * - Modelo de vehículo TMS
     - Sí/No
     - Marca el modelo como usable por el TMS.
   * - Tipo de vehículo
     - Selección
     - Rígido, tractor, semirremolque, furgoneta u otros, según la Flota de Odoo.
   * - Versión del modelo
     - Texto
     - Variante del modelo.
   * - Peso total técnicamente autorizado / Peso total autorizado / Peso en vacío / Carga (kg)
     - Número
     - Los pesos del vehículo. La carga se calcula como diferencia entre el total autorizado y el
       vacío.
   * - Peso por eje, Número de ejes, Número de neumáticos
     - Número
     - Datos de ejes, incluidos los del remolque. Los usa PTV para restricciones viarias y peajes.
   * - Altura, Ancho, Longitud (cm)
     - Número
     - Dimensiones exteriores, para restricciones de gálibo.
   * - Altura sobre el eje delantero (cm)
     - Número
     - Dato de PTV para túneles y puentes.
   * - Altura, Anchura y Longitud de carga interior (cm)
     - Número
     - Dimensiones de la caja, para el cálculo de volumen útil.
   * - Tipo de motor / Combustible / Tipo eléctrico
     - Selección
     - Combustión, eléctrico o híbrido; el combustible; y, en eléctricos, batería o pila de
       hidrógeno.
   * - Cilindrada / Potencia neta
     - Número
     - Datos del motor.
   * - Consumo de combustible / de electricidad
     - Número
     - Consumo medio, en litros o kilos por 100 km y en kWh por 100 km. Base del cálculo de
       emisiones.
   * - Ratio de biocombustible / Relación híbrida / Relación de combustible dual
     - Número (%)
     - Porcentajes que afinan el cálculo de emisiones según el tipo de motor.
   * - Clase Euro / Clase de emisión de CO₂ / Clase de reducción de partículas
     - Selección
     - Clasificación ambiental del vehículo. La clase de CO₂ se calcula según la directiva europea
       de peajes.
   * - Autorizaciones de zonas de bajas emisiones
     - Lista
     - Distintivos que permiten entrar en zonas de bajas emisiones.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_2_logistic-configuration`.
