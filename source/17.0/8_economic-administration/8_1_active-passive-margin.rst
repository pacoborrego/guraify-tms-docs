8.1 Activo, pasivo y margen
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Campos **Activo**, **Pasivo**, **Beneficio** y **Margen %** en las listas y formularios de
   Viajes, Paradas y Tramos (TMS › Operaciones).

.. CAPTURA: 8_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/8_economic-administration/8_1_active-passive-margin_01_viaje.png
      :alt: Lista de Viajes con activo, pasivo y margen

      Los Viajes con sus columnas Activo, Pasivo, Beneficio y Margen %.

El TMS llama **activo** a lo que se cobra al cliente y **pasivo** a lo que se paga al
transportista. Son los términos del sector para el ingreso y el coste de una operación, y
aparecen así en todas las pantallas. El **margen** (en la interfaz, Beneficio) es la diferencia,
y el **Margen %** la diferencia sobre el activo.

Lo distinto del TMS es que estas tres cifras no viven sólo en la Orden y el Viaje: existen en
los **cuatro niveles** del modelo, y cada nivel se calcula a partir de los demás.

.. list-table::
   :header-rows: 1
   :widths: 16 42 42

   * - Nivel
     - De dónde sale el activo
     - De dónde sale el pasivo
   * - Orden (``sale.order``)
     - Las líneas de venta que genera su tarifa: por Orden completa, por Tramo o por Parada,
       según el ámbito de cada línea de tarifa.
     - La suma del pasivo de sus Tramos.
   * - Tramo (``tms.shipment.leg``)
     - Su parte de las líneas de venta de la Orden, según la división de ventas (8.2). Se
       reparte a su vez entre la carga y la descarga con los porcentajes del tipo de orden.
     - El pasivo de sus paradas de carga y de descarga, ponderado por su porcentaje de división.
   * - Parada (``tms.stop``)
     - La suma de lo que le corresponde de cada Tramo que carga o descarga en ella, más su parte
       de la parte fija del Viaje.
     - Las líneas de la orden de compra que le corresponden, según la división de costes (8.3).
   * - Viaje (``tms.trip``)
     - Las líneas de venta ligadas al viaje o a sus paradas. La parte fija (líneas sin parada) se
       reparte entre las paradas.
     - El importe sin impuestos de su orden de compra. La parte fija son las líneas de compra
       sin parada.

Así, el margen de una Parada es real y no un prorrateo contable: tiene lo que el cliente paga
por lo que se entrega en ella y lo que cuesta al transportista pasar por ella. Agregado por
cliente, zona, transportista o Planning, es la base del análisis de rentabilidad.

8.1.1 Qué es facturable
~~~~~~~~~~~~~~~~~~~~~~~

Cada Viaje y cada Parada llevan dos marcas, **Tarifa activa** y **Tarifa pasiva**, activadas
por defecto. Quitar una excluye ese nivel del cálculo correspondiente: una parada de hub que no
se cobra al cliente, un viaje interno que no genera coste de transportista. Lo que no es
facturable no entra en la división ni en el margen, y el diagnóstico de tarifa lo indica con el
motivo «No facturable».

8.1.2 Precio cerrado y flota propia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un Viaje se paga normalmente con la **tarifa de compra** del transportista. Cuando se ha pactado
un importe fijo por el viaje, se informa el **Precio cerrado** y ese importe sustituye a la
tarifa en la orden de compra. Cuando el transportista está marcado como **flota propia**, el
conductor es un empleado que cobra por nómina: el Viaje no genera orden de compra ni pasivo, y
su margen es el activo entero. El coste real del conductor propio no se imputa por esta vía.

8.1.3 El viaje que factura al cliente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En las operativas de carga completa o de viajes dedicados, el precio al cliente no se fija por
Orden sino **por Viaje**. El Viaje puede llevar un cliente y una tarifa de cliente; al tarificar,
el sistema crea o actualiza una Orden propia del Viaje, con el Proyecto de ese cliente y esa
tarifa, y las líneas de venta se generan con el ámbito Viaje. Es el mismo modelo, con el Viaje
como origen del ingreso además del coste. Campos en
:doc:`/17.0/annexes/A_21_economico`.
