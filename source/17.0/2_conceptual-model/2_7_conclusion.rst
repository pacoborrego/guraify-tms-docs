2.7 Conclusión del modelo conceptual
------------------------------------

El modelo conceptual de Guraify TMS se sostiene sobre cuatro entidades —Orden
(``sale.order``), Tramo (``tms.shipment.leg``), Parada (``tms.stop``) y Viaje
(``tms.trip``)— y, sobre todo, sobre la forma en que se relacionan: dependencias
estructurales fuertes entre Orden, Tramo y Parada, y una asignación operativa débil
entre Parada y Viaje. De esa asimetría nace la propiedad central del sistema: el encargo
comercial y su ejecución permanecen desacoplados.

Ese desacoplamiento no es un detalle técnico, sino lo que habilita la operativa real:
una Orden puede ejecutarse en varios Viajes y un Viaje puede agrupar Paradas de distintas
Órdenes, sin romper la coherencia contractual ni la trazabilidad. Sobre la misma
estructura se apoya el modelo económico, que imputa ingreso y coste de forma prorrateada
y multidimensional, y la trazabilidad, que emerge automáticamente de la ejecución
registrada en la app, el backoffice y las integraciones.

En definitiva, el modelo conceptual es la base real del producto: no describe una teoría,
sino el comportamiento del sistema. Sobre él se construyen la arquitectura funcional
(capítulo 3), la parametrización (capítulo 4) y los flujos operativos (capítulo 5) que se
detallan a continuación.
