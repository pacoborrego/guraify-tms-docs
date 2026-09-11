8.3 División de costes
----------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Campo **Modo División Viaje** del Planning (TMS › Configuración › Ajustes › Datos auxiliares ›
   Plannings); campo **Factor División** en el Viaje y en cada Parada.

El coste de un Viaje (``tms.trip``) es uno: lo que dice su orden de compra. Pero el Viaje sirve
a muchas Paradas (``tms.stop``), de muchas Órdenes y a veces de muchos clientes, y para saber
qué margen deja cada una hay que repartir ese coste. La **división de costes** lo hace con un
**factor de división por Parada**, que sale del **Modo División Viaje** del Planning, con los
mismos modos que la división de ventas: una magnitud (peso, volumen, bultos, palés, cantidad,
metros), lineal, o la magnitud por los kilómetros hasta la Parada.

El Viaje suma los factores de las Paradas que entran en el cálculo del pasivo (las que tienen la
marca Tarifa pasiva) en su **Factor División**, que es la base del reparto, y cada Parada recibe
la parte del coste que le corresponde: las líneas de compra que la tarifa generó para ella y, de
la parte fija de la orden de compra (las líneas sin Parada), su factor sobre la base.

Dos matices vienen de la operativa real. Las **Paradas de hub** no reciben coste: el paso por el
hub es infraestructura, y el coste del Viaje se imputa a las Paradas de cliente. Y en los Viajes
de **reparto desde hub**, las Paradas de carga tampoco reciben coste, porque lo que cuesta el
Viaje es la distribución; en los Viajes **directos** (origen a destino sin hub), la carga y la
descarga se reparten el coste entre ambas.

Del pasivo de las Paradas sube el de los Tramos con el porcentaje de división de
:doc:`8_2_sales-split`, y la Orden suma el de sus Tramos. Con esto se cierra el círculo: el
margen existe en los cuatro niveles y cuadra entre ellos. Campos en
:doc:`/17.0/annexes/A_21_economico`.
