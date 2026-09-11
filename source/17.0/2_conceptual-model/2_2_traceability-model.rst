2.2 Modelo de Trazabilidad
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Trazabilidad

.. figure:: /_static/img/2_conceptual-model/2_3_traceability-model_01_trazabilidad.png
   :alt: Vista de Trazabilidad en Odoo

   Vista de Trazabilidad en Odoo.

La trazabilidad (``tms.traceability``) en Guraify TMS es una consecuencia directa de su
arquitectura desacoplada. Al estructurar el sistema en Orden, Tramo, Parada y Viaje, cada
transición operativa queda registrada como parte natural del modelo, y el recorrido completo de un
servicio se puede reconstruir sin depender de procesos externos.

El sistema articula la trazabilidad en tres capas complementarias. La primera es la **trazabilidad
de mercancía**, al nivel del Bulto. Cada Bulto se vincula a un Tramo y, a través de él, a sus
Paradas y Viajes, lo que permite seguir el recorrido físico de la mercancía dentro de la red aunque
intervengan varios Hubs o recursos.

La segunda capa es la **trazabilidad de eventos**, basada en las Paradas. Cada Parada es un evento
operativo concreto y registra estados, fechas previstas y reales, tiempos de servicio y cualquier
modificación relevante. Como la Parada es la unidad mínima de planificación, es también la unidad
mínima de trazabilidad temporal.

La tercera capa es la **trazabilidad documental**: las pruebas de entrega (POD), las incidencias,
las fotografías, las firmas digitales y cualquier documento generado durante la ejecución.

Esta información no se actualiza a mano y a posteriori: se alimenta desde los puntos donde ocurre
la ejecución. La app del conductor actualiza en tiempo real el estado de las Paradas, registra
firmas, captura fotografías, declara incidencias y confirma los tiempos efectivos de servicio.
Cada acción genera un cambio de estado que queda en el histórico de la entidad correspondiente. El
equipo de operaciones puede actualizar eventos desde el backend de Odoo cuando la operativa lo
requiere, y los sistemas externos pueden alimentar estados por API o por importación de ficheros.

.. note::

   La trazabilidad no es declarativa. Se construye a partir de la ejecución real registrada en la
   app, en el backend de Odoo y en las integraciones.

Gracias a este diseño, cada entidad conserva un histórico completo y auditable. En cualquier
momento es posible saber dónde está la mercancía, en qué estado operativo se encuentra, qué
recurso la transporta o la ha transportado y qué incidencias han afectado al servicio. Eso da
visibilidad operativa en tiempo real y, al mismo tiempo, una base sólida para el análisis de
calidad, el control del servicio y la gestión de responsabilidades en la cadena logística.
