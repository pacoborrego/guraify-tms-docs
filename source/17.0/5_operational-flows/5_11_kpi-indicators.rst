Indicadores visuales (KPI)
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Columna de KPI en las listas de TMS › Operaciones › Tráfico › Órdenes y de las Paradas
   (TMS › Operaciones › Maestros operativos › Paradas).

Para que el departamento de tráfico pueda leer el estado de la operativa de un vistazo,
las listas de Paradas y de Órdenes incluyen un **indicador KPI**: un pequeño gráfico SVG
(campos ``stop_kpi_badge`` en la Parada y ``so_kpi_badge`` en la Orden) que se **calcula
automáticamente** a partir del estado de cada registro. No es un dato editable, sino un
resumen visual que se regenera cuando cambian los estados subyacentes.

Indicador de Parada
~~~~~~~~~~~~~~~~~~~~

El KPI de la Parada (``tms.stop``) condensa cuatro informaciones en un mismo gráfico:

- **Tipo de parada / flujo**: representado con triángulos según sea recogida, entrega,
  paso por hub, recogida a domicilio o entrega/recogida directa.
- **Estado operativo**: por el color del triángulo — gris para los estados en curso
  (borrador, en proceso, procesada, cargada, en ruta), verde para *completada*, rojo para
  *fallida*, *devuelta* o *cancelada*, y amarillo para *reservas* o *reprogramada*.
- **Puntualidad**: una barra/etiqueta de color — verde si llega a tiempo (*on_time*), rojo
  si hay retraso (*delay*), azul si hay adelanto (*advance*)— con una etiqueta del desvío
  (``<15``, ``<30``, ``<60``, ``+60`` o los minutos con signo).
- **Secuencia**: un chip con el número de orden de la parada dentro del Viaje.

Las paradas sugeridas por el optimizador se muestran con un único icono de información
("i"), ya que aún no son eventos ejecutables.

Indicador de Orden
~~~~~~~~~~~~~~~~~~~

El KPI de la Orden (``sale.order``) **se construye a partir del KPI de su parada activa** y
le añade, a la derecha, iconos propios del nivel de pedido:

- **Validación**: si la Orden no ha superado la validación (``show_validation``), se
  muestra **solo** un aviso rojo de advertencia; el resto de iconos no aparecen hasta que
  la orden es válida.
- **Facturación y bloqueo**: si la Orden está **facturada**, un icono de **factura verde**.
  Si no lo está, un **candado** cuyo color refleja el estado administrativo: verde y
  cerrado si está confirmada/bloqueada, rojo si está cancelada, turquesa y abierto si está
  en borrador, y amarillo y abierto en el caso especial de no tener importe activo pero sí
  tramos facturables (atención).
- **Reclamación de POD físico**: si procede reclamar la prueba de entrega física
  (``claim_pod``), un icono rojo de reclamación.

De este modo, el KPI de la Orden resume en una sola celda el estado operativo (heredado de
la parada activa), la validación, la situación de facturación/bloqueo y la necesidad de
reclamar POD. Los estados que el indicador refleja se describen en
:doc:`/17.0/3_functional-architecture/3_2_1_orders` (Orden) y
:doc:`/17.0/3_functional-architecture/3_2_2_trips` (Viaje).

.. CAPTURA: 5_11_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_11_kpi-indicators_01_kpi-parada.png
      :alt: Indicador KPI en la lista de Paradas

      Indicador KPI en la lista de Paradas (triángulos de estado, barra de puntualidad y secuencia).

.. CAPTURA: 5_11_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_11_kpi-indicators_02_kpi-orden.png
      :alt: Indicador KPI en la lista de Órdenes

      Indicador KPI en la lista de Órdenes (parada activa + validación, factura/candado y POD).
