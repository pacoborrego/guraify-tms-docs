8.8 Control y reporting
-----------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Transacciones (Líneas de Orden de Venta, Líneas de Orden de Compra,
   Lista de facturas) · TMS › Administración › Opciones de Tarifa › Diagnóstico de tarifa de
   órdenes y de viajes · TMS › Métricas › KPIs · TMS › Operaciones › Tableros.

El control económico se hace con cuatro herramientas, de lo más detallado a lo más agregado.

8.8.1 Transacciones
~~~~~~~~~~~~~~~~~~~

Las tres listas de **Transacciones** son la vista por líneas: todas las **líneas de venta** de las
Órdenes, con su Tramo o Parada, la tarifa y el detalle que las generó, su Viaje y su estado de
factura; todas las **líneas de compra** de los Viajes, con su Parada y su estado; y la **lista de
facturas** de cliente, con sus rectificativas. Desde las dos primeras se factura por líneas y se
abona, como se describe en :doc:`/17.0/5_operational-flows/5_7_invoicing`. Son las pantallas del
cierre económico: filtrar lo pendiente de facturar por cliente o por transportista, agrupar por
producto o por zona, exportar.

8.8.2 Diagnósticos de tarifa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada Orden lleva un diagnóstico de tarifa de venta y cada Viaje uno de compra, con un motivo
cuando el cálculo no pudo hacerse. Las listas **Diagnóstico de tarifa de órdenes** y
**Diagnóstico de tarifa de viajes** reúnen lo pendiente, y los botones de cada registro llevan a
la corrección (ver :doc:`/17.0/5_operational-flows/5_6_settlement`). Revisarlas antes de facturar
es la primera comprobación del cierre: un diagnóstico pendiente es una operación sin precio o
sin coste.

8.8.3 Indicadores
~~~~~~~~~~~~~~~~~

.. CAPTURA: 8_8_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/8_economic-administration/8_8_control-reporting_01_kpis.png
      :alt: Lista de indicadores configurables del motor de indicadores

      El motor de indicadores: cada indicador con su sección, formato, audiencia y objetivo.

El TMS tiene un **motor de indicadores** (``tms.kpi``) compartido por todos los módulos. Cada
**indicador configurable** es un registro con su cálculo, su formato (número, porcentaje,
moneda, duración, tendencia), su sección (tablero, operativa, administrativa), su objetivo y el
sentido en que mejora, y a qué **audiencias** se muestra. Las audiencias dicen quién ve cada
indicador dentro de Odoo y con qué alcance: el mismo indicador, calculado para un usuario de
cliente, solo cuenta sus operaciones; para uno de transportista, solo las suyas; para el equipo
interno, todo. Al pulsarlo abre la lista de registros que lo componen.

Los indicadores operativos del núcleo son la entrega a tiempo, la tasa de retraso, la entrega
al primer intento, las fallidas, el tiempo medio de entrega y el volumen; los de mantenimiento
se describen en :doc:`/17.0/6_resources/6_7_kpis`. Se administran en TMS › Métricas › KPIs.

8.8.4 Tableros
~~~~~~~~~~~~~~

.. CAPTURA: 8_8_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/8_economic-administration/8_8_control-reporting_02_tablero.png
      :alt: Tablero de facturación pendiente

      El tablero de facturación pendiente.

Los **tableros** son hojas de cálculo de Odoo con tablas dinámicas sobre los datos vivos,
agrupadas en TMS › Operaciones › Tableros. Vienen tres con el módulo, cuyos nombres en la
interfaz son «Operations KPI», con los indicadores operativos del periodo; «Stops Operations»,
con las Paradas por estado, puntualidad y zona; y «Pending Invoicing», con lo ejecutado y no
facturado por cliente y por transportista. Funcionan en cualquier compañía y cualquier base, y
el cliente puede duplicarlos y adaptarlos desde la propia hoja.
