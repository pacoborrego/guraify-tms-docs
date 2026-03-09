2.4 Modelo Económico Vinculado
----------------------------------

Uno de los elementos diferenciales de Guraify TMS es que la dimensión económica no se gestiona como una capa externa al TMS, sino como una consecuencia directa de la estructura operativa. El sistema no obliga a reconciliar después lo que se ejecuta con lo que se factura; ambas dimensiones están integradas desde el diseño conceptual.

La arquitectura separa claramente ingreso y coste, pero los mantiene vinculados estructuralmente a las entidades que los generan. Esto elimina duplicidades, reduce conciliaciones manuales y permite que el análisis económico se construya sobre datos operativos reales.

.. note::

   En Guraify TMS la economía no es un proceso posterior.

   Es una propiedad estructural del modelo operativo.

2.4.1 Ingreso (Activo)
~~~~~~~~~~~~~~~~~~~~~~~~~~

El ingreso nace en la Orden, ya que es la entidad que representa el compromiso contractual con el cliente. El cálculo puede realizarse automáticamente mediante reglas de tarifa configuradas en el sistema o aplicando condiciones económicas pactadas previamente. En ambos casos, el importe no es un valor aislado, sino el resultado de la estructura logística definida.

Cuando la operativa lo requiere, el ingreso puede segmentarse por Tramo, permitiendo que distintas fases del servicio tengan impacto económico diferenciado. Cada línea económica generada queda vinculada al contexto operativo que la origina —orden, tramo, servicio, producto— lo que garantiza trazabilidad financiera completa.

De esta forma, el ingreso no es un dato agregado al final del proceso, sino una consecuencia directa de la configuración operativa.

2.4.2 Coste (Pasivo)
~~~~~~~~~~~~~~~~~~~~~~~~

El coste, por su parte, se genera en el Viaje, ya que este representa la ejecución real asignada a un recurso. El Viaje actúa como unidad de coste porque es la entidad que materializa la prestación efectiva del servicio, ya sea mediante flota propia o transportistas externos.

En caso de colaboradores externos, el Viaje genera automáticamente la orden de compra correspondiente y activa el proceso de liquidación. Cuando el modelo operativo lo requiere, el coste puede dividirse entre las distintas paradas que componen el viaje, según el criterio de reparto configurado.

Esta separación estructural permite analizar de forma clara qué se factura al cliente y qué se paga por ejecutar el servicio, sin mezclar ambas dimensiones.

.. _section-15:

2.4.3 Imputación prorrateada multidimensional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aquí reside uno de los mayores diferenciales del sistema. Guraify TMS no limita el análisis económico al nivel agregado de Orden o Viaje, sino que permite imputar tanto el ingreso como el coste en cualquier nivel estructural del modelo: Orden, Tramo, Parada o Viaje.

Esto significa que el ingreso generado por una Orden puede distribuirse proporcionalmente entre sus tramos, y que el coste generado por un Viaje puede dividirse entre sus paradas. Como resultado, el margen puede calcularse no solo a nivel global, sino en micro-unidades operativas.

La imputación puede realizarse según criterios configurables adaptados a la realidad del negocio: peso, volumen, número de bultos, pallets, metros lineales, kilómetros recorridos o combinaciones de estas variables. También es posible aplicar una distribución lineal cuando la operativa lo requiera.

.. important::

   El margen no se calcula únicamente por cliente o por viaje.

   Puede analizarse en cualquier dimensión estructural del sistema.

2.4.4 Resultado: análisis avanzado de margen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gracias a esta arquitectura económica desacoplada y prorrateada, el sistema permite calcular margen no solo por Orden o por Viaje, sino también por Tramo, Parada, Proyecto, Cliente, Planning, Zona geográfica, Tipo de servicio o cualquier dimensión analítica configurada.

Esto abre un campo de análisis estratégico que va más allá de la simple facturación. Permite identificar qué zonas son realmente rentables, qué servicios generan mayor margen real, qué clientes aportan volumen pero reducen rentabilidad, qué paradas penalizan la operación o qué transportistas optimizan mejor el coste por kilómetro o por unidad transportada.

La combinación de operativa estructurada, tarificación automática e imputación prorrateada convierte al sistema no solo en un TMS de ejecución, sino en una herramienta avanzada de análisis de rentabilidad operativa basada en datos reales y coherentes con la ejecución física del transporte.

Sobre esta base económica se apoyan posteriormente los mecanismos de control analítico, reporting y toma de decisiones estratégicas del sistema.

.. _section-16:

.. _section-17:

.. _section-18:

.. _section-19:

.. _section-20:

.. _section-21:

.. _section-22:

