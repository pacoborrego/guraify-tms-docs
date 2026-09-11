2.4 Modelo Relacional
---------------------

El modelo relacional formaliza cómo se vinculan las cuatro entidades definidas en
:doc:`2_1_structural-logic` desde el punto de vista lógico y de cardinalidad. No es una
representación teórica, sino la traducción estructural del comportamiento real del sistema, y
sobre ella se construye la arquitectura funcional del capítulo 3.

.. mermaid::

   flowchart LR
       O["Orden<br/>(sale.order)<br/>ingreso"]:::ing -->|1 : N| T["Tramo<br/>(tms.shipment.leg)"]
       T -->|N : M| P["Parada<br/>(tms.stop)"]
       P -->|N : 1| V["Viaje<br/>(tms.trip)<br/>coste"]:::cost
       O -.->|"N : M, indirecta a través de las Paradas"| V
       classDef ing fill:#d7f0ff,stroke:#5a9;
       classDef cost fill:#ffe0e0,stroke:#c77;

2.4.1 Orden y Tramo
~~~~~~~~~~~~~~~~~~~

La relación entre la Orden (``sale.order``) y el Tramo (``tms.shipment.leg``) es de uno a muchos.
Una Orden puede contener varios Tramos, pero cada Tramo pertenece a una única Orden. Es una
dependencia estructural fuerte: sin Orden, el Tramo carece de sentido.

2.4.2 Tramo y Parada
~~~~~~~~~~~~~~~~~~~~

Cada Tramo da lugar a dos Paradas (``tms.stop``), la de carga y la de descarga, y una Parada puede
agrupar varios Tramos que coinciden en tipo de evento, contacto y franja horaria, tal como se
explica en :doc:`2_1_structural-logic`. La relación es, por tanto, de muchos a muchos, pero la
dependencia sigue siendo fuerte: la Parada no existe sin al menos un Tramo que la origine, y se
genera al validar la Orden, no a mano.

2.4.3 Parada y Viaje
~~~~~~~~~~~~~~~~~~~~

La relación entre la Parada y el Viaje (``tms.trip``) es de otra naturaleza. Una Parada pertenece a
un único Viaje en un momento dado y un Viaje agrupa muchas Paradas. Aquí no hay dependencia
estructural, sino asignación operativa: la Parada existe antes de tener Viaje, se puede mover de
un Viaje a otro y sigue existiendo si el Viaje se deshace.

2.4.4 Orden y Viaje, una relación indirecta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No hay relación estructural directa entre la Orden y el Viaje: la conexión se produce a través de
las Paradas. Un Viaje puede llevar Paradas de muchas Órdenes y una Orden puede repartir sus
Paradas entre varios Viajes, lo que define una relación de muchos a muchos indirecta. Es lo
habitual en grupaje, última milla, entornos multicliente y redes con varios Hubs, donde la
ejecución real no coincide con la unidad contractual. Esa ausencia de dependencia directa es lo
que permite reorganizar la ejecución sin alterar el compromiso comercial.

2.4.5 Dependencias estructurales y operativas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El modelo distingue, pues, dos tipos de dependencia. Las estructurales son fuertes: el Tramo
depende de la Orden y la Parada del Tramo, y si desaparece la entidad padre las hijas pierden
sentido. Las operativas son débiles: la Parada se asigna a un Viaje, pero el Viaje no depende de
ninguna Orden concreta. De esa asimetría nace la propiedad central del sistema: el encargo
comercial y su ejecución permanecen desacoplados, y por eso se puede replanificar, reasignar y
optimizar sin tocar la facturación, y mantener separadas las dimensiones de ingreso y coste.

Ese desacoplamiento no es un detalle técnico, sino lo que habilita la operativa real, y sobre la
misma estructura se apoyan el modelo de trazabilidad, que emerge de la ejecución registrada, y el
modelo económico, que imputa ingreso y coste en cualquier nivel. El modelo conceptual no describe
una teoría, sino el comportamiento del sistema; sobre él se construyen la arquitectura funcional
(capítulo 3), la parametrización (capítulo 4), los flujos operativos (capítulo 5) y la
administración económica (capítulo 8).
