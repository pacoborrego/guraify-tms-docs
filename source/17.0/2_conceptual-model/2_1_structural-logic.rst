2.1 Lógica estructural del sistema
----------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › **Órdenes** y **Viajes** para las dos entidades con menú propio.
   Los Tramos y las Paradas se consultan dentro de la Orden y del Viaje, y también en
   TMS › Operaciones › Maestros › **Tramos** y **Paradas**.

La lógica estructural de Guraify TMS parte de una decisión de diseño: separar el encargo comercial
del Cliente de su ejecución operativa y de su resultado económico. Esa separación no es solo
conceptual. Determina el modelo de datos, la organización de los menús y el propio orden de una
implantación, que empieza siempre por entender estas cuatro entidades antes de entrar en la
parametrización.

El encargo se representa con la Orden (``sale.order``), que formaliza el compromiso con el Cliente:
qué servicio se presta y en qué condiciones se factura. La Orden no describe la ejecución física;
para eso se descompone en Tramos (``tms.shipment.leg``), cada uno un movimiento entre un punto de
carga y otro de descarga. Al validar la Orden, el sistema traduce sus Tramos en Paradas
(``tms.stop``), los eventos físicos sobre los que se planifica. Y las Paradas se agrupan en Viajes
(``tms.trip``), que asignan la ejecución a un conductor y un vehículo.

En corto: la Orden es el origen del ingreso y el Viaje el del coste, y la diferencia entre ambos es
el margen. El capítulo 8 desarrolla esa dimensión económica
(:doc:`/17.0/8_economic-administration/8_1_active-passive-margin`); aquí basta con retener que una
misma Orden puede ejecutarse en varios Viajes y que un Viaje puede llevar Paradas de muchas
Órdenes. Ese desacoplamiento es el que permite soportar grupaje, distribución multicliente y
última milla sin cambiar la lógica base del sistema.

2.1.1 La Orden
~~~~~~~~~~~~~~

.. figure:: /_static/img/2_conceptual-model/2_1_structural-logic_01_orden.png
   :alt: Formulario de una Orden en Odoo

   Formulario de una Orden en Odoo.

La Orden representa el encargo del Cliente y responde a una pregunta sencilla: qué servicio hay
que ejecutar y facturar. Contiene la información administrativa y comercial que define el
servicio y el marco económico en el que se desarrollará. No describe cómo se ejecuta el
transporte, sino el acuerdo que le da origen.

Toda Orden pertenece a un Cliente y a un Proyecto. El Proyecto actúa como contenedor de
configuración: de él hereda la Orden la Tarifa aplicable, el modo de división de ventas, el
Planning, los Tipos de Servicio permitidos y el resto de parámetros operativos. Esa herencia
mantiene coherentes la configuración y el trabajo diario, y evita repetir ajustes a mano en cada
encargo.

Una Orden puede tener uno o varios Tramos y, por compleja que sea su ejecución, conserva siempre su
unidad económica y administrativa: en ella se generan las líneas de venta y se aplica la
tarificación. La ejecución puede reorganizarse en distintos Viajes o recursos sin alterar el
compromiso contractual ni su facturación. La Orden no es una planificación física; es un
compromiso de servicio con impacto económico.

2.1.2 El Tramo
~~~~~~~~~~~~~~

El Tramo es la unidad operativa contenida en la Orden. Si la Orden dice qué servicio se presta, el
Tramo dice desde dónde hasta dónde: un movimiento concreto entre un punto de carga y un punto de
descarga, con sus localizaciones, su mercancía, sus fechas y franjas horarias y, cuando la
operativa lo pide, su propia valoración económica. El ingreso de la Orden puede así repartirse
entre sus Tramos (:doc:`/17.0/8_economic-administration/8_2_sales-split`).

Su función es permitir que una Orden se descomponga en movimientos independientes sin perder la
unidad contractual. Un servicio puerta a puerta es un Tramo; un servicio con paso por Hub son dos
o más Tramos dentro de la misma Orden; y una reprogramación o una devolución se resuelven
añadiendo Tramos, no creando Órdenes nuevas. El Tramo es la pieza que traduce el compromiso
comercial en movimientos concretos y la que da origen a las Paradas: sin Tramo no hay evento
físico que planificar.

2.1.3 La Parada
~~~~~~~~~~~~~~~

La Parada es el evento físico: el punto donde ocurre una acción trazable, sea una carga, una
descarga o un paso por Hub, con coordenadas, franja horaria y tiempo de servicio. En condiciones
normales no se crea a mano. Al validar la Orden, o al cerrar el Manifiesto que la trae, el sistema
recorre sus Tramos y genera las Paradas necesarias, vinculadas a los Tramos que las originan.

Varios Tramos pueden compartir una misma Parada. Al generarlas, el sistema agrupa los Tramos que
coinciden en el tipo de evento (carga o descarga, según el tipo de Tramo), en el contacto de la
dirección, en el Planning y el Proyecto y, si viene informado, en el nombre de Viaje del fichero,
y cuyas franjas horarias se solapan al menos una hora; la Parada resultante toma la franja común.
Los Tramos directos solo se consolidan dentro de su propia Orden; los demás pueden hacerlo entre
Órdenes distintas cuando llegan juntas en un Manifiesto. Si ya existe una Parada compatible, del
mismo tipo, en el mismo contacto, el mismo día y el mismo nombre de Viaje, cuya franja contiene la
del Tramo, este se añade a ella en lugar de crear otra. Esta consolidación evita Paradas duplicadas
en operativas densas, como la última milla o el grupaje urbano, y es la razón de que un Viaje
tenga menos Paradas que Tramos.

La Parada es la unidad mínima de planificación: el Optimizador de Paradas y las herramientas
manuales trabajan sobre Paradas, no sobre Órdenes ni Tramos. Por eso las Órdenes pueden
reorganizarse, agruparse o dividirse sin tocar su dimensión contractual: la planificación solo ve
eventos físicos con coordenadas, franjas horarias y tiempos de servicio. La Parada es donde la
operación deja de ser un compromiso abstracto y se convierte en un evento planificable, trazable y
medible.

2.1.4 El Viaje
~~~~~~~~~~~~~~

.. figure:: /_static/img/2_conceptual-model/2_1_structural-logic_02_viaje.png
   :alt: Formulario de un Viaje en Odoo

   Formulario de un Viaje en Odoo.

El Viaje es la ejecución: el conjunto de Paradas que un recurso, conductor y vehículo, realiza en
una salida, en una secuencia ejecutable y con los tiempos y distancias previstos. Se crea a mano,
filtrando y agrupando Paradas por los criterios que convengan, o con el Optimizador de Paradas
apoyado en PTV, que tiene en cuenta franjas horarias, tiempos de servicio, capacidades del
vehículo y jornada del conductor (:doc:`/17.0/1_introduction/1_4_technological-architecture`). En
ambos casos el resultado es el mismo: eventos físicos individuales convertidos en una secuencia
operativa ejecutable.

El Viaje introduce el coste en el modelo. Cuando lo ejecuta un Transportista, genera la Orden de
compra de la que saldrá su factura y activa la liquidación
(:doc:`/17.0/8_economic-administration/8_4_purchase-orders`). Es la unidad de ejecución y de coste
del sistema, y cierra el ciclo que abrió la Orden.

2.1.5 Relaciones entre entidades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El flujo es una progresión: se crea la Orden, se descompone en Tramos, al validarla se generan las
Paradas y estas se agrupan en Viajes, a mano o con el optimizador; el Viaje se asigna a un recurso,
se ejecuta y, al cerrarse, dispara la liquidación y la facturación. Pero lo relevante no es la
secuencia, sino que cada entidad ocupa una capa distinta. La Orden es el compromiso comercial y el
ingreso; el Tramo estructura la operación y aporta trazabilidad dentro del servicio; la Parada
materializa el evento físico y es la base de la planificación; el Viaje agrupa Paradas y genera el
coste.

El modelo no funde ingreso y ejecución en una sola entidad. Gracias a eso se puede reorganizar la
ejecución sin tocar la facturación, agrupar Órdenes de varios Clientes en un Viaje, repartir una
Orden entre varios recursos y analizar márgenes por cualquier dimensión sin conciliaciones
posteriores. Las cardinalidades exactas y la naturaleza de cada dependencia se formalizan en
:doc:`2_4_relational-model`.
