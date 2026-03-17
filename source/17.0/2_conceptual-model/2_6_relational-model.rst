Modelo Relacional Conceptual Simplificado
-------------------------------------------------

El Modelo Relacional Conceptual formaliza las relaciones estructurales entre las entidades principales del sistema: Orden, Tramo, Parada y Viaje. Si en los apartados anteriores se ha explicado su función operativa y económica, aquí se define cómo se vinculan entre sí desde el punto de vista lógico y de cardinalidad.

Este modelo constituye la base sobre la que se construye la arquitectura técnica del sistema. No es una representación teórica, sino la traducción estructural del comportamiento real del TMS.

Entidades principales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La Orden representa el encargo comercial del cliente. Es la entidad contractual, genera el ingreso y puede contener múltiples tramos.

El Tramo es la unidad operativa dependiente de una Orden. Define un origen y un destino concretos y es el elemento que da lugar a la generación de paradas.

La Parada es el evento físico asociado a un tramo. Puede corresponder a una carga, descarga, entrada en hub u otro evento intermedio. Es la unidad mínima de planificación.

El Viaje es la unidad de ejecución operativa. Agrupa múltiples paradas en una ruta ejecutable y genera el coste asociado a dicha ejecución.

.. image:: /_static/images/modelo_relacional.png
   :align: center

Cardinalidades estructurales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Desde el punto de vista relacional, el modelo puede representarse de forma simplificada mediante las siguientes cardinalidades:

ORDEN (1) ──────── (N) TRAMO

TRAMO (1) ──────── (N) PARADA

PARADA (N) ──────── (1) VIAJE

La relación entre Orden y Tramo es de uno a muchos. Una Orden puede contener múltiples Tramos, pero cada Tramo pertenece exclusivamente a una única Orden. Se trata de una dependencia estructural fuerte: sin Orden, el Tramo carece de sentido lógico.

La relación entre Tramo y Parada también es de uno a muchos. Un Tramo genera al menos dos Paradas —carga y descarga— aunque en escenarios complejos puede generar más. De nuevo, es una dependencia fuerte: la Parada no puede existir sin un Tramo que la origine.

La relación entre Parada y Viaje es distinta. Una Parada pertenece a un único Viaje operativo en un momento dado, pero un Viaje puede agrupar múltiples Paradas. Aquí no hablamos de dependencia estructural, sino de asignación operativa.

.. note::

   Las relaciones Orden→Tramo y Tramo→Parada son dependencias estructurales fuertes.

   La relación Parada→Viaje es una asignación operativa.


Relación indirecta Orden ↔ Viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No existe una relación estructural directa entre Orden y Viaje. La conexión se produce de forma indirecta a través de las Paradas.

Esto implica que un Viaje puede contener Paradas procedentes de múltiples Órdenes, y que una Orden puede distribuir sus Paradas en distintos Viajes. Conceptualmente, esto genera una relación N:M indirecta entre Orden y Viaje.

Este comportamiento es especialmente relevante en operativas de grupaje, última milla, entornos multicliente o estructuras multihub, donde la ejecución real no coincide necesariamente con la unidad contractual.

Esta ausencia de dependencia directa es lo que permite reorganizar la ejecución sin alterar el compromiso comercial.

.. _section-24:

Dependencias funcionales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El modelo distingue claramente entre dependencias estructurales y dependencias operativas.

Las dependencias estructurales son fuertes: el Tramo depende de la Orden y la Parada depende del Tramo. Si se elimina la entidad padre, las hijas pierden sentido lógico dentro del modelo.

Las dependencias operativas son débiles: la Parada se asigna a un Viaje, pero el Viaje no depende estructuralmente de una Orden concreta. Esto permite replanificar, reasignar viajes, optimizar dinámicamente y mantener separadas las dimensiones de ingreso y coste.

Esta diferenciación es esencial para la escalabilidad del sistema.

Impacto en la arquitectura del sistema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La arquitectura relacional descrita no solo define relaciones técnicas; habilita comportamientos funcionales avanzados. Gracias a este modelo es posible agrupar múltiples órdenes en un mismo viaje, redistribuir paradas entre recursos, realizar imputación económica multidimensional y mantener independencia entre facturación y ejecución.

La separación estructural entre encargo comercial (Orden) y ejecución operativa (Viaje) solo es posible porque el modelo relacional evita una dependencia directa entre ambas entidades.

.. note::

   La independencia entre ingreso y ejecución no es una decisión funcional aislada.

   Es una consecuencia directa del modelo relacional.

En definitiva, el Modelo Relacional Conceptual es el fundamento lógico que permite que Guraify TMS sea escalable, flexible y económicamente analizable en múltiples dimensiones. Sobre esta base se construye la arquitectura técnica y funcional descrita en los capítulos siguientes.
