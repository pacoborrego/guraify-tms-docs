2.3 Modelo Económico
--------------------

La dimensión económica de Guraify TMS no es una capa externa que haya que reconciliar después con
lo ejecutado: nace de la propia estructura operativa. Lo que se cobra al Cliente por una operación
es su **activo** y lo que se paga al Transportista es su **pasivo**; la diferencia es el
**margen**. En la prosa de esta documentación se habla de ingreso, coste y margen; la interfaz
llama a esos campos Activo, Pasivo y Beneficio (:term:`Activo y pasivo`).

El ingreso nace en la Orden, donde la tarificación aplica la Tarifa del Proyecto o el precio
pactado. El coste nace en el Viaje, que, cuando lo ejecuta un Transportista, genera la Orden de
compra y la liquidación. Ambos existen en los cuatro niveles del modelo: el ingreso de la Orden se
reparte entre sus Tramos y Paradas con la división de ventas, y el coste del Viaje entre sus
Paradas con la división de costes, según criterios configurables (peso, volumen, bultos, palés,
kilómetros o una distribución lineal). Así el margen se puede leer por Orden, Viaje, Tramo o
Parada y, agregando, por Cliente, Proyecto, Planning, Zona de tarifa o Tipo de Servicio.

El detalle está en el capítulo :doc:`8 Administración y Control Económico
</17.0/8_economic-administration/index>`: :doc:`8.1
</17.0/8_economic-administration/8_1_active-passive-margin>` para activo, pasivo y margen,
:doc:`8.2 </17.0/8_economic-administration/8_2_sales-split>` para la división de ventas y
:doc:`8.3 </17.0/8_economic-administration/8_3_cost-split>` para la división de costes.
