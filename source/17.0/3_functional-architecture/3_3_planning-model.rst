3.3 Modelo de planificación
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planning (Plan Disponibilidad Conductores, Optimizador de Paradas)

El modelo de planificación agrupa las herramientas que permiten organizar la ejecución de los
servicios de transporte teniendo en cuenta restricciones operativas, disponibilidad de recursos
y objetivos de optimización. Su principio es coherente con el modelo conceptual: se planifican
**Paradas** (``tms.stop``), eventos físicos con coordenada, franja horaria y tiempo de servicio,
y el resultado se consolida en **Viajes** (``tms.trip``).

3.3.1 Disponibilidad de recursos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planning › Plan Disponibilidad Conductores

La planificación parte de declarar **qué recursos están disponibles y cuándo**. Esto se gestiona
en el :term:`Plan de disponibilidad de conductores`, una **vista Gantt** por fechas en la que
cada **franja** reserva un recurso para una ventana temporal y concentra los datos que la
optimización necesita para trabajar sobre recursos reales:

- el **conductor** y el **vehículo** (y, en su caso, el **transportista**),
- la **tarifa de compra** aplicable,
- el **Planning** al que pertenece, que segmenta y filtra qué paradas y áreas son compatibles.

El :term:`Plan de transporte` del Planning delimita esa disponibilidad: filtra las Áreas
geográficas que se pueden elegir en una franja, para no asignar recursos de una red a otra. Estas
franjas son, además, lo que consume el Optimizador en su **modo por franja** (ver
:ref:`optimizador-paradas`).

.. CAPTURA: 3_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_3_planning-model_02_plan-disponibilidad.png
      :alt: Plan de disponibilidad de conductores (Gantt de franjas)

      Plan de disponibilidad de conductores: vista Gantt de franjas.

.. _optimizador-paradas:

3.3.2 Optimización: el Optimizador de Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planning › Optimizador de Paradas

El :term:`Optimizador de Paradas` (``tms.optimizator``) es la herramienta visual de
planificación del TMS: reúne las **Paradas pendientes** de una fecha y las muestra sobre un
**mapa** (con el trazado del recorrido) para construir o mejorar los Viajes apoyándose en el motor
**PTV**. Desde él se lanzan los tres servicios de PTV (cálculo de ruta, secuenciación y
optimización completa) descritos en la sección 1.4.2 de
:doc:`/17.0/1_introduction/1_4_technological-architecture`. El planificador lanza la
optimización, revisa la propuesta y la confirma o la ajusta a mano.

La optimización completa puede trabajar de dos formas.

3.3.2.1 Modo por franja
^^^^^^^^^^^^^^^^^^^^^^^

El sistema optimiza sobre **recursos ya definidos** en las franjas del Plan de disponibilidad de
conductores (conductor, vehículo, transportista, tarifa de compra y disponibilidad temporal). Es
la opción para planificar sobre recursos reales ya reservados; el resultado deja cada Viaje con
su conductor y su vehículo asignados.

3.3.2.2 Modo por categoría de vehículo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El sistema optimiza según la **capacidad disponible por categoría de vehículo**, sin fijar aún
un recurso concreto. El operador asigna después conductor y vehículo a cada Viaje propuesto.

3.3.2.3 Requisitos previos
^^^^^^^^^^^^^^^^^^^^^^^^^^

Para que la optimización produzca Viajes viables deben cumplirse algunas condiciones:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Requisito
     - Descripción
   * - Token de PTV
     - Configurado en la compañía (ver la sección 1.4.2 de
       :doc:`/17.0/1_introduction/1_4_technological-architecture`).
   * - Geocodificación
     - Coordenadas válidas en las localizaciones de las Paradas: sin ellas la Parada no se puede
       situar en el mapa ni enviar a PTV.
   * - Paradas pendientes
     - Paradas sin asignar a un Viaje en la fecha elegida; el Optimizador abre por defecto las
       no programadas del día siguiente.
   * - Franjas horarias coherentes
     - Las ventanas de las Paradas y la disponibilidad de los recursos deben poder cumplirse a
       la vez; una Parada cuya franja no encaje queda en la lista de lo no planificado.
   * - Planning, franjas o categorías
     - En el modo por franja, franjas del Plan de disponibilidad para la fecha; en el modo por
       categoría, cuántos vehículos de cada categoría hay.
   * - Capacidades y restricciones
     - Pesos, volúmenes, equipamientos y distancia máxima parametrizados en las categorías de
       vehículo (:doc:`/17.0/4_parametrization/4_3_planning-configuration`).

El resultado es un conjunto de **Viajes en borrador** con sus Paradas asignadas y secuenciadas,
sus horas estimadas y su trazado. El paso a paso de esta generación, y las alternativas manual y
por fichero, están en :doc:`/17.0/5_operational-flows/5_2_trip-generation`.

3.3.3 Resultado
~~~~~~~~~~~~~~~

El resultado de la planificación es un conjunto de Viajes coherentes con el modelo estructural:
cada Parada conserva su vínculo con el Tramo y la Orden de origen, de modo que la reorganización
de la ejecución nunca rompe la trazabilidad ni la dimensión económica.

.. figure:: /_static/img/3_functional-architecture/3_3_planning-model_01_optimizador.png
   :alt: Optimizador de Paradas en Odoo

   Optimizador de Paradas en Odoo.
