5.2 Generación de Viajes
------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planificación (Optimizador de Paradas) y TMS › Operaciones › Tráfico › Viajes (``tms.trip``).

.. CAPTURA: 5_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_2_trip-generation_01_generacion-viajes.png
      :alt: Generación de viajes

      Generación de Viajes (``tms.trip``): asistente manual u optimizador PTV.

El Viaje agrupa las paradas que serán ejecutadas por un conductor, vehículo o transportista en una fecha determinada.

Es la entidad que concentra:

- planificación de ruta
- asignación de recursos
- tiempos y distancias
- trazabilidad agregada
- liquidación económica de compra

Un viaje puede originarse por distintos mecanismos:

- nombre de viaje recibido en importación
- creación manual desde órdenes o paradas
- optimización automática con PTV
- generación automática por configuración de proyecto

En todos los casos, el viaje termina vinculando:

- paradas
- tramos
- bultos
- reembolsos asociados



5.2.1 Información principal del viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Fecha y horarios
     - Inicio y fin previstos de ejecución.
   * - Planning y slot
     - Contexto operativo de planificación.
   * - Agencia y hubs
     - Referencias territoriales del viaje.
   * - Recursos asignados
     - Transportista, conductor, vehículo y remolques.
   * - Tarifa de compra
     - Base económica de liquidación.
   * - Paradas y tramos
     - Operaciones incluidas en la ruta.
   * - Métricas agregadas
     - Peso, volumen, pallets, distancia, tiempos, etc.
   * - Datos de optimización
     - Polilínea, respuesta cartográfica y secuencias calculadas.



5.2.2 Generación por importación de fichero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando las órdenes entran por fichero, el propio fichero puede traer ya la **asignación a
viajes**. En la configuración del **Fichero EDI** (``tms.edi.file``) se mapean los campos
que indican **a qué Viaje va cada expedición** (nombre de viaje) y, opcionalmente, la
**secuencia** de las paradas dentro del viaje (campos ``TripName`` y ``Sequence`` del
mapeo; ver :doc:`/17.0/7_edi-integrations/7_2_1_field-mapping`).

Al **cerrar el Manifiesto** (ver :doc:`/17.0/3_functional-architecture/3_2_3_manifests`),
el sistema crea los Viajes (``tms.trip``) con la información del fichero y les asigna sus
paradas. El enriquecimiento de la ruta depende de si el fichero trae o no la secuencia:

- **Con secuencia informada en el fichero.** El sistema respeta ese orden y calcula el
  **routing** con PTV —distancias, tiempos, ETA, peajes, etc.— (ver
  :doc:`/17.0/1_introduction/1_4_technological-architecture` y
  :doc:`/17.0/3_functional-architecture/3_3_planning-model`).
- **Sin secuencia.** El comportamiento depende de la **configuración del Proyecto** (ver
  :doc:`/17.0/4_parametrization/4_5_project-configuration`):

  - Si el proyecto tiene activada la **autosecuenciación**, el sistema primero
    **secuencia automáticamente** las paradas (secuenciación PTV) y después calcula el
    **routing**.
  - Si **no** está activada, las paradas se asignan al viaje **en el orden en que vienen en
    el fichero** y el viaje **no se enriquece** con datos de routing: no tendrá kilómetros,
    tiempos, ETA ni cálculo de peajes.

.. note::

   Sin secuencia ni autosecuenciación, el viaje queda creado y operativo pero "plano",
   sin métricas de ruta. Si la operación necesita ETAs, distancias o costes de ruta, el
   fichero debe venir secuenciado o el Proyecto debe tener activada la autosecuenciación.

5.2.3 Generación Manual
~~~~~~~~~~~~~~~~~~~~~~~

La generación manual se utiliza cuando el operador decide explícitamente qué paradas deben formar parte de un viaje.

Es habitual en escenarios como:

- bajo volumen
- rutas fijas
- ajustes manuales
- correcciones operativas
- planificación dirigida por operador

Normalmente parte de una selección de:

- órdenes
- paradas pendientes

y abre un asistente de asignación.

El asistente permite dos modos:

- viaje nuevo
- viaje existente

En modo viaje nuevo pueden configurarse:

- proyecto
- fecha
- ventana horaria
- conductor
- vehículo
- categoría
- transportista
- tarifa de compra
- servicios
- planning
- tipo de transportista
- tipo de destinatario
- precio cerrado (cuando aplique)

En modo viaje existente:

- se selecciona una ruta abierta
- se incorporan nuevas paradas

Al completar la asignación:

- la parada se vincula mediante ``trip_id``
- los tramos quedan asociados al viaje
- los reembolsos quedan disponibles para liquidación

Si el proyecto tiene secuenciación automática activa:

- el sistema puede reordenar la ruta automáticamente

5.2.4 Generación Automática con PTV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La generación automática se ejecuta desde el **Optimizador de Paradas**: reúne las paradas
pendientes y, con el motor PTV, propone los Viajes (asignación, secuencia y enriquecimiento
de ruta). Funciona en **modo por slot** —recursos ya definidos en el Plan de Disponibilidad
de Conductores— o en **modo por categoría** —capacidad por categoría de vehículo—.

El detalle de la herramienta (los dos modos, los requisitos previos, el mapa y lo que
devuelve: viajes en borrador, ETAs, distancias, polilínea, etc.) se describe en
:ref:`optimizador-paradas`.
