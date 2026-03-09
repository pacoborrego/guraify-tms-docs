2.1 Lógica estructural del sistema
--------------------------------------

La lógica estructural de Guraify TMS se fundamenta en una decisión arquitectónica deliberada: separar de forma explícita el encargo comercial del cliente de su ejecución operativa y de su impacto económico. Esta separación no es únicamente conceptual, sino que determina la estructura del modelo de datos, la organización funcional del sistema y la propia metodología de implantación.

Desde el punto de vista del negocio, todo comienza con la necesidad de representar digitalmente un servicio solicitado por un cliente. Esa representación es la Orden. La Orden formaliza el compromiso contractual: define qué servicio debe prestarse y bajo qué condiciones se facturará. En ella nace el ingreso y desde ella se articula el resto de la estructura operativa.

Sin embargo, una Orden no describe la ejecución física del transporte. Para ello se introduce el Tramo, que permite descomponer el compromiso comercial en movimientos logísticos concretos entre un origen y un destino. Esta descomposición es lo que permite modelar tanto un servicio simple puerta a puerta como operativas complejas con múltiples fases, arrastres entre hubs o escenarios de reagenda, sin romper la coherencia administrativa.

Cuando una Orden se valida, el sistema traduce su estructura lógica en eventos físicos reales mediante la generación automática de Paradas. La Parada representa el punto operativo trazable: recogida, entrega, entrada en hub o cualquier evento intermedio necesario. Desde el punto de vista de planificación, la Parada es la unidad mínima operativa, ya que es sobre ella donde trabajan los algoritmos de optimización y las herramientas de planificación.

Finalmente, las Paradas se agrupan en Viajes, que representan la ejecución real asignada a un recurso. El Viaje consolida paradas en una ruta ejecutable, genera la orden de compra correspondiente al transportista y materializa el coste de la operación.

.. important::

   La Orden representa el ingreso.

   El Viaje representa el coste.

Esta separación estructural es el principio clave que permite analizar la rentabilidad en múltiples dimensiones sin mezclar ejecución y facturación.

Gracias a este diseño, una misma Orden puede ejecutarse en varios Viajes y un mismo Viaje puede contener paradas procedentes de distintas Órdenes. Este desacoplamiento es el que permite soportar operativas de grupaje, distribución multicliente y modelos de última milla sin alterar la lógica base del sistema.

El flujo estructural puede entenderse como una progresión lógica: se crea la Orden, se descompone en Tramos, se generan Paradas al validar y posteriormente estas se agrupan en Viajes. No obstante, lo verdaderamente relevante no es la secuencia, sino la independencia entre las capas comercial, operativa y económica, que permite reorganizar la ejecución sin modificar el compromiso contractual original.

Esta lógica conceptual no es abstracta ni teórica. Se refleja directamente en la estructura funcional del sistema, organizada en los bloques de Operaciones, Administración, Maestros y Configuración , donde cada sección materializa una dimensión distinta del modelo. Del mismo modo, el propio programa de implantación parte de la comprensión de esta estructura base —Orden, Tramo, Parada y Viaje— como primer paso antes de entrar en parametrización avanzada , lo que confirma que el modelo conceptual es la base real sobre la que se construye cualquier proyecto.

En consecuencia, la lógica estructural de Guraify TMS no consiste únicamente en definir entidades relacionadas, sino en establecer una arquitectura desacoplada que permita escalabilidad, optimización avanzada, integración masiva y análisis económico granular. Sobre este principio se construye toda la arquitectura funcional y técnica del sistema.

.. _section-12:

2.1.1 La Orden
------------------

La Orden es la entidad que representa digitalmente el encargo del cliente dentro de Guraify TMS. Constituye el punto de partida estructural del sistema y el eje sobre el que se articula toda la operativa posterior. Desde una perspectiva conceptual, la Orden responde a una pregunta sencilla pero fundamental: qué servicio debemos ejecutar y posteriormente facturar.

En términos funcionales, la Orden formaliza el compromiso contractual con el cliente. Contiene la información administrativa y comercial necesaria para definir el servicio, determina la lógica de facturación y establece el marco económico bajo el cual se desarrollará la operación. No describe la ejecución física del transporte, sino el acuerdo que da origen a dicha ejecución.

Cada Orden está obligatoriamente vinculada a un cliente y a un proyecto. El proyecto actúa como contenedor de configuración y permite que la Orden herede automáticamente parámetros críticos como la tarifa aplicable, el modo de división de ventas, el planning asociado, los tipos de servicio permitidos y otras restricciones operativas. Esta herencia garantiza coherencia entre configuración estratégica y ejecución diaria, evitando configuraciones manuales repetitivas y reduciendo riesgos de error.

Desde el punto de vista del modelo de datos, la Orden puede contener uno o varios Tramos. Esta capacidad de descomposición permite representar desde un servicio simple de origen a destino hasta estructuras más complejas en las que una misma relación contractual se materializa en múltiples fases logísticas. A pesar de esta posible complejidad operativa, la Orden mantiene siempre su unidad económica y administrativa.

La Orden es también el origen del ingreso. En ella se generan las líneas de venta y se activan las reglas de tasación configuradas en el sistema. El cálculo económico no se realiza de forma externa ni posterior, sino que forma parte del propio diseño estructural del modelo.

.. important::

   Una Orden no es una ruta ni una planificación física.

   Es un compromiso de servicio con impacto económico.

Esta diferenciación es clave para entender la arquitectura completa del sistema. Gracias a ella, la ejecución puede reorganizarse —mediante distintos Viajes o recursos— sin alterar la naturaleza contractual del servicio ni su lógica de facturación.

En definitiva, la Orden debe entenderse como la unidad contractual y económica del TMS. Es el objeto que conecta cliente, proyecto, tarificación y estructura operativa, y sobre ella se construye todo el desarrollo logístico posterior.

2.1.2 El Tramo
------------------

El Tramo es la unidad operativa contenida dentro de una Orden. Si la Orden define el compromiso comercial —qué servicio se debe prestar—, el Tramo concreta cómo se materializa ese compromiso desde el punto de vista logístico. En términos simples, el Tramo responde a la pregunta: desde dónde hasta dónde se presta el servicio.

Cada tramo define un movimiento específico entre un punto de carga y un punto de descarga. En él se registran los datos esenciales que permiten ejecutar y valorar ese desplazamiento: localizaciones, información de mercancía, parámetros temporales y las reglas de tasación que puedan aplicarse a esa fase concreta del servicio. Esto significa que la dimensión económica no se calcula únicamente a nivel global de la Orden, sino que puede vincularse a cada tramo cuando la operativa lo requiere.

La función principal del Tramo es permitir la descomposición controlada de una Orden en operaciones logísticas independientes sin perder la unidad contractual. Gracias a esta estructura, el sistema puede modelar con coherencia escenarios muy distintos: un servicio puerta a puerta se representará mediante un único tramo, mientras que un arrastre entre hubs podrá estructurarse en dos o más tramos dentro de la misma Orden. Del mismo modo, en operativas de última milla masiva o en casos de reagenda, basta con añadir tramos adicionales sin necesidad de crear nuevas órdenes ni alterar la lógica administrativa original.

Esta capacidad de segmentación aporta flexibilidad sin introducir fragmentación económica. La Orden sigue siendo el marco contractual, pero el Tramo permite adaptar la ejecución a la realidad operativa.

.. important::

   El Tramo es la entidad que da origen a las Paradas.

   Sin tramo no existe evento físico planificable.

Desde el punto de vista estructural, el Tramo actúa como puente entre la dimensión comercial (Orden) y la dimensión física (Paradas). Es la pieza que traduce el compromiso contractual en movimientos logísticos concretos sobre los que posteriormente se construirá la planificación y la ejecución real.

2.1.3 La Parada
-------------------

La Parada representa el evento físico real dentro de la operativa del transporte. Si el Tramo define un movimiento lógico entre un origen y un destino, la Parada es el punto concreto donde ocurre una acción trazable: una recogida, una entrega, una entrada o salida de hub, una parada técnica o cualquier otro evento que deba registrarse en el flujo operativo.

Desde el punto de vista del sistema, la Parada no se introduce manualmente en condiciones normales. Su generación forma parte del comportamiento estructural del modelo. Cuando una Orden se valida, el sistema analiza los tramos que la componen y genera automáticamente todas las paradas necesarias, vinculándolas al tramo correspondiente y conservando la coherencia jerárquica entre entidades. Este mecanismo garantiza que la representación física de la operación sea siempre consistente con la estructura contractual definida previamente.

En escenarios de importación masiva, el comportamiento es aún más sofisticado. El sistema es capaz de consolidar en una única parada aquellos tramos que comparten cliente, localización y una ventana horaria compatible. Esta lógica reduce la fragmentación innecesaria y prepara la información de forma óptima para la fase de planificación, especialmente en operativas de alta densidad como la última milla o el grupaje urbano.

La relevancia de la Parada no es únicamente operativa, sino también estratégica dentro del modelo de planificación.

.. important::

   La Parada es la unidad mínima de planificación.

   El optimizador no trabaja sobre Órdenes ni sobre Tramos, sino sobre Paradas.

Esta decisión arquitectónica permite que la planificación sea completamente flexible. Las órdenes pueden reorganizarse, agruparse o dividirse sin alterar su dimensión contractual, porque la lógica de optimización se basa exclusivamente en eventos físicos con coordenadas, ventanas horarias y tiempos de servicio asociados.

En consecuencia, la Parada actúa como el punto de convergencia entre estructura lógica y ejecución real. Es donde la operación deja de ser un compromiso abstracto y se convierte en un evento planificable, trazable y medible dentro del sistema.

2.1.4 El Viaje
------------------

El Viaje es la entidad que representa la ejecución real del transporte. Si la Orden formaliza el compromiso con el cliente y el Tramo estructura el movimiento logístico, el Viaje responde a una pregunta operativa concreta: qué conjunto de paradas ejecuta un recurso en una ruta real.

Desde el punto de vista funcional, el Viaje agrupa paradas para construir una ruta ejecutable. En él se asigna el recurso —propio o externo— que realizará el servicio, se consolidan los tiempos y distancias previstos y se genera la correspondiente orden de compra cuando interviene un transportista colaborador. Por tanto, el Viaje no es solo una estructura de planificación, sino también la unidad que activa la liquidación económica del servicio hacia el proveedor.

Su creación puede realizarse de forma manual, utilizando herramientas de filtrado y agrupación que permiten seleccionar paradas según múltiples criterios operativos, o de forma automática mediante el optimizador integrado con PTV, que construye rutas considerando restricciones horarias, tiempos de servicio, capacidades del vehículo, normativas de conducción y otros parámetros configurados en el sistema. En ambos casos, el resultado es una estructura coherente que traduce eventos físicos individuales en una secuencia operativa ejecutable.

Desde el punto de vista arquitectónico, el Viaje introduce la dimensión del coste dentro del modelo. Mientras que la Orden mantiene la unidad contractual y el ingreso asociado al cliente, el Viaje materializa el gasto derivado de la ejecución.

.. important::

   La Orden representa el ingreso.
   El Viaje representa el coste.

Esta separación estructural permite que una misma Orden pueda ejecutarse en varios Viajes distintos o que un Viaje agrupe paradas procedentes de múltiples Órdenes, algo habitual en operativas de grupaje y distribución multicliente. Gracias a este desacoplamiento, el sistema puede reorganizar la ejecución sin alterar la lógica comercial, manteniendo trazabilidad completa y control económico en todas las dimensiones.

El Viaje, por tanto, es la unidad de ejecución y coste del sistema, y cierra el ciclo iniciado por la Orden dentro del modelo estructural del TMS.

