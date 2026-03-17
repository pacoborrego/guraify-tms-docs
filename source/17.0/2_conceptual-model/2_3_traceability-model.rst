Modelo de Trazabilidad
----------------------

La trazabilidad en Guraify TMS es una consecuencia directa de su arquitectura desacoplada. Al estructurar el sistema en Orden, Tramo, Parada y Viaje, cada transición operativa queda registrada como parte natural del modelo, permitiendo reconstruir el recorrido completo de un servicio sin depender de procesos externos.

El sistema articula la trazabilidad en tres capas complementarias. La primera es la trazabilidad de mercancía, que opera a nivel de bultos o unidades transportadas. Cada bulto se vincula estructuralmente a un tramo y, a través de este, a sus paradas y viajes asociados. Esto permite seguir el recorrido físico de la mercancía dentro de la red logística, incluso cuando intervienen múltiples hubs o recursos.

La segunda capa es la trazabilidad de eventos, basada en las Paradas. Cada parada constituye un evento operativo concreto y registra estados, fechas previstas y reales, tiempos de servicio y cualquier modificación relevante. Dado que la Parada es la unidad mínima de planificación, también es la unidad mínima de trazabilidad temporal.

La tercera capa es la trazabilidad documental, donde se integran pruebas de entrega (POD), incidencias, fotografías, firmas digitales y cualquier documentación generada durante la ejecución.

Lo verdaderamente relevante es que esta información no se actualiza de forma manual posterior, sino que se alimenta automáticamente desde los puntos de ejecución del sistema.

La app móvil utilizada por conductores y personal de almacén actualiza en tiempo real los estados de las paradas, registra firmas, captura fotografías, declara incidencias y confirma tiempos efectivos de servicio. Cada acción genera un cambio de estado que queda persistido en el histórico de la entidad correspondiente. Del mismo modo, el equipo de operaciones puede actualizar eventos desde el backend cuando la operativa lo requiere, manteniendo coherencia entre planificación y realidad ejecutada. En escenarios integrados, los sistemas externos también pueden alimentar estados mediante API o procesos EDI.

.. note::

   La trazabilidad no es declarativa.

   Se construye automáticamente a partir de la ejecución real registrada en la app, el backoffice y las integraciones.

Gracias a este diseño, cada entidad conserva un histórico completo y auditable. En cualquier momento es posible conocer dónde se encuentra la mercancía, en qué estado operativo está, qué recurso la transporta o la ha transportado y qué incidencias han afectado al servicio. La trazabilidad no es una capa añadida, sino una propiedad emergente del propio modelo estructural del TMS.

Este enfoque garantiza visibilidad operativa en tiempo real y, al mismo tiempo, una base sólida para análisis de calidad, control de servicio y gestión de responsabilidades dentro de la cadena logística.
