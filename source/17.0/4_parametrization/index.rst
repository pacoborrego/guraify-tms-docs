4. Parametrización del sistema 
==============================

Este capítulo describe cómo se configura Guraify TMS para adaptarse a la operativa de una empresa de transporte. A diferencia de los capítulos anteriores —donde se ha explicado el modelo conceptual y la arquitectura funcional— aquí se documentan los elementos de parametrización que permiten que el sistema reproduzca el comportamiento real del negocio.

La parametrización no consiste únicamente en introducir datos en tablas de configuración. Cada elemento definido en este capítulo influye directamente en el funcionamiento de los algoritmos de planificación, en el cálculo económico de los servicios y en la lógica de ejecución operativa.

Por este motivo, la configuración se organiza en distintos bloques que reflejan las dimensiones fundamentales del sistema:

- configuración operativa

- configuración logística

- configuración de planificación

- configuración económica

- configuración de proyectos

Cada bloque agrupa registros maestros que definen reglas estructurales del sistema y que posteriormente serán utilizados por los procesos automáticos de generación de paradas, planificación de viajes, cálculo de tarifas y ejecución operativa.

Es importante entender que estas configuraciones no actúan de forma aislada. La mayoría de ellas se vinculan posteriormente dentro del Proyecto, que actúa como contenedor de configuración para cada operativa o cliente.

.. toctree::
   :maxdepth: 1

   4_1_operational-configuration
   4_2_logistic-configuration
   4_3_planning-configuration
   4_4_economic-configuration
   4_5_project-configuration
