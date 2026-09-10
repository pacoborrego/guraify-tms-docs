8.2 División de ventas
----------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Campo **Modo de División** del Proyecto (TMS › Configuración › Proyectos › pestaña TMS ›
   Administración); campos **Factor División** y porcentajes en el Tramo.

Una Orden con un solo Tramo no necesita repartir nada. Pero la mayoría de las operativas tienen
Órdenes de dos o más Tramos (recogida al hub, hub a destino, y una devolución si falla), y el
precio que paga el cliente es uno. La **división de ventas** decide qué parte de ese importe
corresponde a cada Tramo, y por tanto a cada Parada y a cada Viaje que lo ejecuta. Sin ella no
hay margen por Viaje: un viaje de reparto no sabría cuánto ingreso lleva encima.

El reparto se hace con un **factor de división** por Tramo, que sale del **Modo de División**
del Proyecto:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Modo
     - Factor del Tramo
   * - Peso, Volumen, Bulto, Pallets, Cantidad, Metros
     - La magnitud del Tramo: cada tramo recibe la parte proporcional a lo que mueve.
   * - Lineal
     - Uno por tramo: todos los tramos reciben lo mismo.
   * - Km y Peso (por defecto), Km y Volumen, Km y Bulto, Km y Pallets, Km y Cantidad, Km y
       Metros, Km y Lineal
     - La magnitud multiplicada por los kilómetros del Tramo: los tramos largos y cargados pesan
       más. Es el modo natural cuando el coste depende de la distancia.

El **porcentaje de división** de cada Tramo es su factor sobre la suma de los factores de los
Tramos de la Orden que participan, y su activo es ese porcentaje del importe de las líneas de
venta de ámbito Orden. Las líneas de tarifa de ámbito Tramo o Parada no se reparten: van
directamente al tramo o la parada que las generó.

Dentro del Tramo hay un segundo reparto: el **tipo de orden** dice qué porcentaje del activo
del tramo corresponde a la **carga** y cuál a la **descarga** (por ejemplo, 30 y 70). Con eso, la
parada de carga y la de descarga reciben cada una su parte, y el hub, que carga y descarga
tramos distintos, suma lo que le toca de cada uno.

Elegir el modo es una decisión del cliente que conviene tomar mirando su tarifa: si cobra por
kilo, repartir por peso; si por bulto, por bultos; si sus costes van por distancia, combinar
con kilómetros. Cambiar el modo recalcula los repartos de las Órdenes no facturadas; las
facturadas quedan como estaban. Campos en :doc:`/17.0/annexes/A_21_economico`.
