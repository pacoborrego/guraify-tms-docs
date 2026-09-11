1.5 Filosofía operativa del sistema
-----------------------------------

La filosofía operativa de Guraify TMS no parte de la herramienta, sino del modelo. El sistema
está diseñado sobre una premisa clara: el transporte debe representarse de forma estructural,
desacoplada y trazable en todas sus dimensiones.

Tres principios articulan esta filosofía.

El primero es la **separación estructural entre ingreso y coste**: la Orden y el Viaje son
entidades distintas, y eso permite reorganizar la ejecución sin alterar el contrato. El capítulo 2
lo desarrolla en :doc:`/17.0/2_conceptual-model/2_1_structural-logic`.

El segundo principio es la **planificación basada en eventos físicos**. El sistema no planifica
Órdenes abstractas, sino Paradas geolocalizadas, con coordenada, franja horaria y tiempo de
servicio. Así la optimización trabaja sobre entidades físicas concretas y la ejecución, a través
de la aplicación móvil, actualiza el modelo en tiempo real con hechos y no con estimaciones.

El tercer principio es la **integración nativa entre operativa y economía**. La tarificación no
es un cálculo externo; nace de la estructura operativa. La liquidación no es un proceso
posterior; se genera en la ejecución. El reparto del ingreso y del coste entre Tramos y Paradas no
es un informe adicional; es una consecuencia del modelo relacional. Esto convierte al sistema en
una herramienta de control de rentabilidad basada en datos coherentes con la realidad operativa.

Desde esta perspectiva, las tecnologías descritas en
:doc:`1_4_technological-architecture` (Odoo como base, PTV como motor cartográfico y
matemático, Scandit como acelerador de captura, la geocodificación con control de calidad y
el modelo de punto y polígono) no son piezas aisladas. Todas responden a una misma lógica:
que cada decisión operativa tenga una representación estructural precisa y trazable.

El sistema no está concebido como un simple planificador de Viajes ni como un generador de
albaranes, sino como una arquitectura desacoplada capaz de:

- Adaptarse a distintos modelos de negocio sin alterar su núcleo.
- Escalar en volumen sin perder coherencia estructural.
- Integrarse con terceros sin duplicar modelos.
- Analizar la rentabilidad en las dimensiones operativas más pequeñas.
- Mantener la trazabilidad completa desde el Bulto hasta el margen final.

En definitiva, la filosofía operativa de Guraify TMS consiste en transformar la complejidad
logística en una estructura formal coherente, donde cada evento físico, cada coordenada, cada
escaneo y cada optimización se traduce en información analizable y económicamente relevante.
Sobre ella se construyen los capítulos siguientes.
