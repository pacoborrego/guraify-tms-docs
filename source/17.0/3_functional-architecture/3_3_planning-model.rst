3.3 Modelo de planificación
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Planificación (Plan Disponibilidad Conductores, Optimizador de Paradas)

El modelo de planificación agrupa las herramientas que permiten organizar la ejecución de
los servicios de transporte teniendo en cuenta restricciones operativas, disponibilidad
de recursos y objetivos de optimización. Su principio es coherente con el modelo
conceptual: se planifican **Paradas** (``tms.stop``) —eventos físicos con coordenada,
ventana horaria y tiempo de servicio— y el resultado se consolida en **Viajes**
(``tms.trip``).

3.3.1 Disponibilidad de recursos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La planificación parte de la disponibilidad de conductores y vehículos. El Plan de
disponibilidad de conductores permite declarar qué recursos están disponibles en cada
ventana temporal, de modo que la asignación y la optimización trabajen solo sobre
recursos realmente operables. Los planes de transporte (``tms.transport.plan``) enmarcan
esa disponibilidad dentro de la estructura de planificación del proyecto.

3.3.2 Optimización
~~~~~~~~~~~~~~~~~~~

El Optimizador de Paradas (``tms.optimizator``) construye o mejora los Viajes a partir de
las Paradas pendientes, apoyándose en el motor PTV. Opera en los tres niveles descritos
en :doc:`/17.0/1_introduction/1_4_technological-architecture`: *routing* (enriquecer una
ruta existente), secuenciación (ordenar las Paradas de un Viaje) y optimización completa
(proponer la asignación y secuenciación de Paradas a Viajes). El planificador define el
objetivo de optimización —minimizar distancia, tiempo o incumplimiento de ventanas— y
revisa la propuesta antes de confirmarla.

3.3.3 Resultado
~~~~~~~~~~~~~~~

El resultado de la planificación es un conjunto de Viajes coherentes con el modelo
estructural: cada Parada conserva su vínculo con el Tramo y la Orden de origen, de modo
que la reorganización de la ejecución nunca rompe la trazabilidad ni la dimensión
económica.

.. CAPTURA: 3_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_3_planning-model_01_optimizador.png
      :alt: Optimizador de Paradas en Odoo

      Optimizador de Paradas (``tms.optimizator``) en Odoo.
