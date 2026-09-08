3.3 Modelo de planificación
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planificación (Plan Disponibilidad Conductores, Optimizador de Paradas)

El modelo de planificación agrupa las herramientas que permiten organizar la ejecución de
los servicios de transporte teniendo en cuenta restricciones operativas, disponibilidad
de recursos y objetivos de optimización. Su principio es coherente con el modelo
conceptual: se planifican **Paradas** (``tms.stop``), eventos físicos con coordenada,
ventana horaria y tiempo de servicio, y el resultado se consolida en **Viajes**
(``tms.trip``).

.. _disponibilidad-recursos:

3.3.1 Disponibilidad de recursos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planificación › Plan Disponibilidad Conductores

La planificación parte de declarar **qué recursos están disponibles y cuándo**. Esto se
gestiona en el :term:`Plan de disponibilidad de conductores`, una **vista Gantt** por
fechas en la que cada **franja** reserva un recurso para una ventana temporal y concentra
los datos que la optimización necesita para trabajar sobre recursos reales:

- el **conductor** y el **vehículo** (y, en su caso, el **transportista**),
- la **tarifa de compra** aplicable,
- el **Planning** al que pertenece, que segmenta y filtra qué paradas y áreas son
  compatibles.

Los :term:`planes de transporte <Plan de transporte>` enmarcan esa disponibilidad dentro de
la red territorial del proyecto. Estas franjas son, además, lo que consume el Optimizador
en su **modo por franja** (ver :ref:`optimizador-paradas`).

.. CAPTURA: 3_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_3_planning-model_02_plan-disponibilidad.png
      :alt: Plan de disponibilidad de conductores (Gantt de franjas)

      Plan de disponibilidad de conductores: vista Gantt de franjas.

.. _optimizador-paradas:

3.3.2 Optimización: el Optimizador de Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planificación › Optimizador de Paradas

El :term:`Optimizador de Paradas` (``tms.optimizator``) es la herramienta visual de
planificación del TMS: reúne las **Paradas pendientes** de una fecha y las muestra sobre un
**mapa** (con trazado de ruta) para construir o mejorar los Viajes apoyándose en el motor
**PTV**. Opera en los tres niveles descritos en
:ref:`17.0/1_introduction/1_4_technological-architecture:1.4.2 Servicios de PTV`:
**cálculo de ruta** (enriquecer una ruta existente), **secuenciación** (ordenar las Paradas
de un Viaje) y **optimización completa** (proponer la asignación y secuenciación de Paradas
a Viajes). El planificador lanza la optimización, revisa la propuesta y la confirma o la
ajusta a mano.

La optimización puede trabajar de dos formas:

3.3.2.1 Modo por franja
^^^^^^^^^^^^^^^^^^^^^^^

El sistema optimiza sobre **recursos ya definidos** en las franjas del Plan de
disponibilidad de conductores (conductor, vehículo, transportista, tarifa de compra y
disponibilidad temporal). Es la opción para planificar sobre recursos reales ya reservados;
el resultado deja cada Viaje con su conductor y su vehículo asignados.

3.3.2.2 Modo por categoría
^^^^^^^^^^^^^^^^^^^^^^^^^^

El sistema optimiza según la **capacidad disponible por categoría de vehículo**, sin fijar
aún un recurso concreto. El operador asigna después conductor y vehículo a cada Viaje
propuesto.

3.3.2.3 Requisitos previos
^^^^^^^^^^^^^^^^^^^^^^^^^^

Para que la optimización produzca rutas viables deben cumplirse algunas condiciones:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Requisito
     - Descripción
   * - Token PTV
     - Configurado en la compañía (ver el cap. 1).
   * - Geocodificación
     - Coordenadas válidas en las localizaciones de las paradas.
   * - Paradas pendientes
     - Operaciones disponibles para planificar en la fecha.
   * - Ventanas horarias coherentes
     - Restricciones temporales consistentes entre paradas y recursos.
   * - Planning, franjas o categorías
     - Contexto operativo correctamente configurado.
   * - Capacidades y restricciones
     - Equipamientos, carga y límites parametrizados en las categorías de vehículo.

Tras recibir la respuesta de PTV, el Optimizador crea **Viajes en borrador** con sus
Paradas asignadas y **secuenciadas**, y enriquece la ruta con las horas estimadas de
llegada (ETA), las distancias y los tiempos de conducción, además del **trazado** que se
ve en el mapa y que sirve también de apoyo a la app móvil. El paso a paso de esta
generación, y las alternativas manual y por fichero, están en
:doc:`/17.0/5_operational-flows/5_2_trip-generation`.

3.3.3 Resultado
~~~~~~~~~~~~~~~

El resultado de la planificación es un conjunto de Viajes coherentes con el modelo
estructural: cada Parada conserva su vínculo con el Tramo y la Orden de origen, de modo
que la reorganización de la ejecución nunca rompe la trazabilidad ni la dimensión
económica.

.. figure:: /_static/img/3_functional-architecture/3_3_planning-model_01_optimizador.png
   :alt: Optimizador de Paradas en Odoo

   Optimizador de Paradas en Odoo.
