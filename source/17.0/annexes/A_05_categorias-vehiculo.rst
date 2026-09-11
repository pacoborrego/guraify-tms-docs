A.5 Categorías de vehículo
==========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Maestros › Equipos › Categorías

Modelo Odoo: ``fleet.vehicle.model.category``. La clase de vehículo con la que planifica el TMS:
tráiler, camión de 12 t, furgoneta. Extiende la categoría de modelo de la Flota de Odoo.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos
del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué
compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando
hay que elegir uno y nadie ha elegido).

A.5.1 Capacidades y compatibilidad
----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Categoría Vehículo TMS
     - Sí/No
     - Marca la categoría como usable por el TMS. Solo las marcadas aparecen en Proyectos, Viajes y
       en el Optimizador de Paradas.
   * - Perfil Vehículo
     - Selección (perfiles de PTV)
     - El perfil de red viaria que PTV usa en el cálculo de ruta: EUR_TRAILER_TRUCK, EUR_TRUCK_40T,
       EUR_TRUCK_11_99T, EUR_TRUCK_7_49T, EUR_VAN, etc. Determina por dónde puede pasar el vehículo
       y a qué velocidad.
   * - Equipamientos
     - Lista de Equipamientos
     - Lo que llevan de serie los vehículos de esta categoría. Un vehículo concreto puede tener los
       suyos y prevalecen.
   * - Categorías de Carga
     - Lista de Categorías de carga
     - Qué mercancía admite la categoría.
   * - Peso Kg Máximo, Volumen Máximo, Bultos Máximo, Pallets Máximo, Cantidad Máxima, Metros Máximo
     - Número
     - Las seis capacidades que el optimizador respeta al llenar un vehículo de esta categoría. El
       vehículo concreto puede sobreescribirlas.
   * - Zonas Disponibles
     - Relación con Zona de tarifa
     - Zona de tarifa en la que se usa la categoría, para tarifas por tipo de vehículo.
   * - Icono
     - Imagen
     - Icono de la categoría en el mapa y las listas.

A.5.2 Base y jornada
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Punto de inicio / Punto de fin
     - Relación con Contacto
     - Dónde empieza y termina el recorrido de un vehículo de esta categoría (la base, el hub). El
       optimizador y la secuenciación arrancan y cierran ahí. Así se llaman los dos campos en la
       interfaz.
   * - Intervalo Inicio Ruta / Intervalo Ruta Fin
     - Hora
     - Franja horaria en la que puede salir y debe volver.
   * - Máxima Distancia (Km) de Ruta
     - Número
     - Kilómetros máximos de un Viaje. Restricción del optimizador.
   * - Paradas Máxima
     - Número
     - Número máximo de Paradas por Viaje.
   * - Horas de Conducción
     - Relación con Horas de conducción
     - El perfil de jornada que se envía a PTV cuando el Viaje no viene de una franja del Plan de
       disponibilidad.

A.5.3 Parámetros del optimizador
--------------------------------

Los campos de la pestaña Optimización: los costes y límites que el optimizador tiene en cuenta al
decidir qué vehículos usar y cómo llenarlos.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Coste fijo, por hora, por km, por parada, sin usar
     - Importe
     - Costes que el optimizador minimiza al decidir qué vehículos usar y cómo llenarlos. «Sin usar»
       es lo que cuesta tener el vehículo disponible y dejarlo parado.
   * - Duración máxima de ruta (h) / Conducción máxima (h)
     - Número
     - Límites de la jornada de un Viaje de esta categoría, en horas.
   * - Compacidad / Equilibrio de duración
     - Número de 0 a 1
     - Cuánto prefiere el optimizador Viajes geográficamente compactos y cuánto iguala la duración
       entre vehículos.
   * - Factor de velocidad / Modo de tráfico
     - Número / Selección (Media, Realista)
     - Ajuste sobre el perfil de velocidad de PTV y si se usa tráfico histórico realista.
   * - Permitir violaciones de ruta
     - Sí/No
     - Deja que el optimizador atraviese restricciones que el perfil del vehículo prohibiría.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_2_logistic-configuration`.
