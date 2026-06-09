2.5 Separación estructural entre ingreso y coste
------------------------------------------------

El siguiente diagrama resume la columna vertebral del modelo: la cadena estructural
Orden → Tramo → Parada → Viaje, con el ingreso anclado en la Orden (``sale.order``) y el
coste en el Viaje (``tms.trip``). Sobre esa misma cadena, tanto el ingreso como el coste
pueden imputarse de forma prorrateada y multidimensional en cualquier nivel intermedio.

.. mermaid::

   flowchart TB
       O["Orden (sale.order)<br/>— Ingreso —"]:::ing --> T["Tramo (tms.shipment.leg)"]
       T -->|1:N| P["Parada (tms.stop)"]
       O -->|1:N| T
       P -->|N:1| V["Viaje (tms.trip)<br/>— Coste —"]:::cost
       classDef ing fill:#d7f0ff,stroke:#5a9;
       classDef cost fill:#ffe0e0,stroke:#c77;
