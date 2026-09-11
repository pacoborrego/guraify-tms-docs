1.1 Propósito de este manual
----------------------------

Este es el **Manual de implantación** de Guraify TMS. Explica cómo está construido el sistema y
cómo se configura: el modelo conceptual sobre el que se apoya todo (capítulo 2), la
organización funcional y sus entidades (capítulo 3), la parametrización (capítulo 4), los
flujos operativos completos, de la Orden a la liquidación (capítulo 5), la gestión de recursos,
con el odómetro único y el mantenimiento de la flota (capítulo 6), y la administración y el
control económico (capítulo 8). Está escrito para quien va a poner el sistema en marcha en una
empresa de transporte o va a adaptarlo a una operativa nueva, y para el cliente que quiere
entender lo que hay detrás de las pantallas.

Su objetivo es que el comportamiento del sistema se pueda entender y configurar sin leer el
código fuente. Por eso describe la lógica, no la implementación: cuando cita una entidad de
Odoo lo hace una sola vez y entre paréntesis, y los nombres de menús y campos van en los
avisos «Ruta en Odoo» y en las tablas de referencia, no en el texto.

Este manual es uno de los cuatro recorridos de la documentación. Si lo que buscas es otra
cosa:

- Una visión general del producto, sin tecnicismos, está en
  :doc:`Conocer Guraify TMS </17.0/0_product-overview/index>`. Conviene leerla antes que este
  manual si es la primera vez que te acercas al sistema.
- Cómo entran y salen los datos (ficheros, API, webhooks) está en la
  :doc:`Guía del integrador </17.0/7_edi-integrations/index>`.
- Cómo usar la app está en el :doc:`Manual del conductor </17.0/10_manual_app/index>`.
- Cada término del producto, con su definición y los sinónimos que no se usan, está en el
  :doc:`glosario </17.0/glossary>`.
