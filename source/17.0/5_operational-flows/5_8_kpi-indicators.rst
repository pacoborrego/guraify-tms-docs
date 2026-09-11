5.8 Indicadores visuales (KPI)
------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Columna KPI en las listas de TMS › Operaciones › Tráfico › Órdenes y de TMS › Operaciones ›
   Maestros › Paradas.

Esta sección no es un paso del flujo: es una ayuda para leer los anteriores. Para que el
departamento de tráfico pueda ver el estado de la operativa de un vistazo, las listas de
Paradas y de Órdenes incluyen un :term:`indicador KPI <Indicador KPI>`: un pequeño gráfico que
se calcula automáticamente a partir del estado de cada registro. No es un dato editable, sino
un resumen visual que se regenera cuando cambian los estados subyacentes. No confundirlo con
los :term:`indicadores configurables <Indicador configurable>` del motor de indicadores
(:doc:`/17.0/8_economic-administration/8_8_control-reporting`).

5.8.1 Indicador de Parada
~~~~~~~~~~~~~~~~~~~~~~~~~

El indicador de la Parada (``tms.stop``) condensa cuatro informaciones en un mismo gráfico:

- **Tipo de Parada y flujo**: representado con triángulos según sea recogida, entrega, paso por
  hub, recogida a domicilio o recogida o entrega directa.
- **Estado de la Parada**: por el color del triángulo. Gris para los estados abiertos
  (borrador, en proceso, procesada y los intermedios de la app); verde para **Completada**;
  rojo para **Fallida**, **Devuelta** y **Cancelada**; amarillo para **Con reservas** y
  **Reprogramada** (ver :term:`Estados de la Parada`).
- **Puntualidad**: una barra de color que compara la hora real con la prevista: verde si la
  Parada se ejecutó a tiempo, roja si con retraso y azul si con adelanto, con una etiqueta que
  resume el desvío en minutos.
- **Secuencia**: un número con la posición de la Parada dentro del Viaje.

Las Paradas de inicio y fin que genera el optimizador se muestran con un único icono de
información («i»), porque no son eventos ejecutables.

5.8.2 Indicador de Orden
~~~~~~~~~~~~~~~~~~~~~~~~

El indicador de la Orden (``sale.order``) se construye a partir del de su Parada activa (ver
:doc:`/17.0/3_functional-architecture/3_2_5_active-leg`) y le añade, a la derecha, iconos
propios del nivel de Orden:

- **Validación**: si la Orden no ha superado la validación, se muestra solo un aviso rojo; el
  resto de iconos no aparece hasta que la Orden es válida.
- **Facturación y bloqueo**: si la Orden está **facturada**, un icono de factura verde. Si no
  lo está, un **candado** cuyo color refleja el estado administrativo: verde y cerrado si está
  confirmada o bloqueada, rojo si está cancelada, turquesa y abierto si está en borrador, y
  amarillo y abierto cuando no tiene importe de venta pero sí Tramos facturables, que es una
  situación a revisar.
- **Reclamación de POD físico**: si procede reclamar la :term:`prueba de entrega (POD) <POD>`
  física, un icono rojo de reclamación.

Los estados de la Orden que el indicador refleja se describen en
:doc:`/17.0/3_functional-architecture/3_2_1_orders`.

.. figure:: /_static/img/5_operational-flows/5_8_kpi-indicators_01_kpi-parada.png
   :alt: Indicador KPI en la lista de Paradas

   Indicador KPI en la lista de Paradas (triángulos de estado, barra de puntualidad y secuencia).

.. figure:: /_static/img/5_operational-flows/5_8_kpi-indicators_02_kpi-orden.png
   :alt: Indicador KPI en la lista de Órdenes

   Indicador KPI en la lista de Órdenes (parada activa + validación, factura/candado y POD).

5.8.3 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Campo
   * - Indicador KPI de la Parada
     - ``tms.stop.stop_kpi_badge``
   * - Indicador KPI de la Orden
     - ``sale.order.so_kpi_badge``
   * - Orden pendiente de validación
     - ``sale.order.show_validation``
   * - Reclamar POD físico
     - ``sale.order.claim_pod``
