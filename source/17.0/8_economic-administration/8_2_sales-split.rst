8.2 División de ventas
----------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Campo **Modo de División** del Proyecto (TMS › Configuración › Proyectos › pestaña TMS ›
   Administración); campos **Factor División** y porcentajes en el Tramo.

Una Orden (``sale.order``) con un solo Tramo (``tms.shipment.leg``) no necesita repartir nada.
Pero la mayoría de las operativas tienen Órdenes de dos o más Tramos (recogida al hub, hub a
destino, y una devolución si falla), y el precio que paga el cliente es uno. La **división de
ventas** decide qué parte de ese importe corresponde a cada Tramo, y por tanto a cada Parada y a
cada Viaje que lo ejecuta. Sin ella no hay margen por Viaje: un Viaje de reparto no sabría cuánto
ingreso lleva encima.

El reparto se hace con un **factor de división** por Tramo, que sale del **Modo de División**
del Proyecto:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Modo
     - Factor del Tramo
   * - Peso, Volumen, Bulto, Palés, Cantidad, Metros
     - La magnitud del Tramo: cada Tramo recibe la parte proporcional a lo que mueve.
   * - Lineal
     - Uno por Tramo: todos los Tramos reciben lo mismo.
   * - Km y Peso (por defecto), Km y Volumen, Km y Bulto, Km y Pallets, Km y Cantidad, Km y
       Metros, Km y Lineal
     - La magnitud multiplicada por los kilómetros del Tramo: los Tramos largos y cargados pesan
       más. Es el modo natural cuando el coste depende de la distancia.

Del factor salen dos porcentajes por Tramo. El **porcentaje activo** es el factor del Tramo
sobre la suma de los factores de los Tramos facturables de la Orden, y con él se reparte entre
los Tramos el importe de las líneas de venta de ámbito Orden que comparten varios Tramos. El
**porcentaje de división** es el factor del Tramo sobre la suma de los factores de los Tramos de
la misma Orden que comparten su Parada de referencia (la de descarga en una entrega, la de carga
en una recogida), y es el que se usa para bajar el pasivo de la Parada al Tramo
(:doc:`8_3_cost-split`). Las líneas de tarifa de ámbito Tramo o Parada no se reparten: van
directamente al Tramo o la Parada que las generó.

Dentro del Tramo hay un segundo reparto: el **Tipo de Orden** dice qué porcentaje del activo
del Tramo corresponde a la **carga** y cuál a la **descarga** (por ejemplo, 30 y 70). Con eso, la
Parada de carga y la de descarga reciben cada una su parte, y el hub, que carga y descarga
Tramos distintos, suma lo que le toca de cada uno.

Elegir el modo es una decisión del cliente que conviene tomar mirando su tarifa: si cobra por
kilo, repartir por peso; si por bulto, por bultos; si sus costes van por distancia, combinar
con kilómetros. El modo se lee cada vez que se calcula el factor de un Tramo, así que un cambio
de modo se aplica a los Tramos cuyo factor vuelve a calcularse (al cambiar su mercancía o su
distancia); las Órdenes ya facturadas no cambian sus repartos. Campos en
:doc:`/17.0/annexes/A_21_economico`.
