Relación entre entidades
--------------------------------

Una vez definidas las entidades principales —Orden, Tramo, Parada y Viaje—, es necesario entender cómo se relacionan entre sí dentro del flujo estructural del sistema. La potencia del modelo no reside únicamente en cada entidad por separado, sino en la forma en que se encadenan y, al mismo tiempo, permanecen desacopladas.

.. _section-13:

Flujo lógico estructural
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El flujo comienza cuando un cliente solicita un servicio. Ese compromiso se formaliza mediante la creación de una Orden, que actúa como unidad contractual y económica. A partir de ella se generan uno o varios Tramos que describen los movimientos logísticos necesarios para cumplir el servicio.

Cuando la Orden se valida, el sistema transforma la estructura lógica en eventos físicos reales generando automáticamente las Paradas asociadas a cada tramo. Estas paradas, que constituyen la unidad mínima planificable, se agrupan posteriormente en Viajes, ya sea manualmente o mediante optimización automática. Una vez creado el Viaje, se asigna a un recurso, se ejecuta la operación y finalmente se activan los procesos de liquidación y facturación correspondientes.

Este flujo no debe entenderse únicamente como una secuencia técnica, sino como una transición progresiva desde la dimensión comercial hasta la dimensión operativa y económica de la ejecución real.

.. _section-14:


Separación conceptual clave
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada entidad representa una capa distinta dentro del modelo y cumple un papel específico tanto operativo como económico. La Orden representa el ingreso y concentra el impacto en facturación; el Tramo estructura la operación logística y aporta trazabilidad dentro del servicio; la Parada materializa el evento físico y constituye la base de la planificación; el Viaje agrupa esas paradas en una ruta ejecutable y genera el coste asociado a su ejecución.

.. important::

   El modelo no fusiona ingreso y ejecución en una única entidad.

   Separa explícitamente compromiso comercial, operación logística y coste real.

Esta separación conceptual es lo que permite que el sistema escale sin perder coherencia. Gracias a ella, es posible reorganizar la ejecución sin alterar la facturación, agrupar múltiples órdenes en un mismo viaje, dividir una orden en distintos recursos o analizar márgenes en distintas dimensiones operativas.

En consecuencia, la arquitectura no solo facilita la planificación y la ejecución, sino que habilita flexibilidad operativa, optimización avanzada y un control económico real basado en la estructura misma del modelo, no en procesos externos de conciliación.
