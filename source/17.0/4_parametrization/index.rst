4 Parametrización del Sistema
=============================

Este capítulo describe cómo se configura Guraify TMS para que reproduzca la operativa real de
una empresa de transporte. Los capítulos anteriores explican el modelo conceptual y la
arquitectura funcional; aquí se documentan los maestros que hay que rellenar para que ese
modelo funcione con los datos de la casa.

Parametrizar no es solo introducir datos en tablas. Cada maestro de este capítulo influye en
los algoritmos de planificación, en el cálculo económico de los servicios o en la ejecución
operativa, y una configuración incompleta aparece después como incidencia de importación, de
planificación, de la app o de tarifa. Por eso la configuración se organiza en cinco bloques,
que son las cinco páginas del capítulo: la **configuración operativa** (los catálogos que
clasifican Órdenes, Paradas y participantes), la **logística** (la mercancía y los vehículos),
la de **planificación** (el territorio, los horarios y los tiempos), la **económica** (las
tarifas) y la de **Proyectos**.

Estos maestros no actúan aislados. Casi todos se vinculan después en el :term:`Proyecto`, que
es el contenedor de configuración de cada operativa o cliente y del que Órdenes, Tramos,
Paradas y Viajes heredan su comportamiento. El orden de las páginas es el orden razonable de
implantación: primero los catálogos, después la mercancía y la flota, luego el territorio y las
tarifas, y al final el Proyecto que los reúne.

.. toctree::
   :maxdepth: 1

   4_1_operational-configuration
   4_2_logistic-configuration
   4_3_planning-configuration
   4_4_economic-configuration
   4_5_project-configuration
