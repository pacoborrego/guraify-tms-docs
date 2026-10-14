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

.. figure:: /_static/img/8_economic-administration/8_8_control-reporting_01_kpis.png
   :alt: Lista de indicadores configurables del motor de indicadores

   El motor de indicadores: cada indicador con su sección, formato, audiencia y objetivo.

El TMS tiene un **motor de indicadores** (``tms.kpi``) compartido por todos los módulos. Cada
**indicador configurable** es un registro con su título, su cálculo, su formato (número,
porcentaje, moneda, duración, tendencia), su sección (tablero, operativa, administrativa), su
posición, su icono y a qué **audiencias** se dirige (equipo interno, cliente, transportista).

Lo que se configura es la presentación; el **cálculo** se elige de una lista de cálculos que
trae cada módulo. Un indicador nuevo que mida algo que ningún cálculo mide hoy es un desarrollo:
se añade el cálculo al módulo y, a partir de ahí, se configura como los demás.

TMS › Métricas › KPIs abre un **mosaico**: una tarjeta por indicador con su valor de los últimos
30 días para el equipo interno. Si el indicador tiene **Aplicar objetivo** marcado, la tarjeta se
colorea en verde o en rojo según el **Objetivo** y la **Dirección** (mejor cuanto más alto o
cuanto más bajo); sin esa casilla queda neutra. La casilla existe porque cero es un objetivo
válido (cero Viajes por validar, cero vencidos) y no se distinguiría de «sin objetivo». Una
tarjeta que dice **Sin datos** no ha encontrado nada que contar en el periodo, que no es lo mismo
que un cero; si el cálculo falla, la tarjeta muestra el error en lugar del valor. Al pulsarla se
abre la lista de los registros que cuenta, cuando el cálculo la tiene.

El botón **Probar** de la ficha calcula el indicador para una audiencia, un cliente o
transportista concreto y unas fechas, y enseña el resultado: el mismo indicador, calculado para
un cliente, solo cuenta sus operaciones; para un transportista, solo las suyas. Es la forma de
comprobar el alcance, porque **hoy no hay una pantalla en la que el cliente o el transportista
vean sus indicadores**: las audiencias de cliente y de transportista están preparadas para
cuando la haya. El menú solo lo ven los responsables del TMS.

Los indicadores operativos del núcleo son la entrega a tiempo, la tasa de retraso, la entrega
al primer intento, las fallidas, el tiempo medio de entrega y el volumen; a ellos se suma, solo
para el equipo interno, **Viajes por validar** (objetivo cero: si nadie valida, nadie factura;
ver :doc:`/17.0/5_operational-flows/5_5_trip-closing`). Los de mantenimiento se describen en
:doc:`/17.0/6_resources/6_7_kpis`. Se administran en TMS › Métricas › KPIs.

8.8.4 Tableros
~~~~~~~~~~~~~~

.. figure:: /_static/img/8_economic-administration/8_8_control-reporting_02_tablero.png
   :alt: Tablero de facturación pendiente

   El tablero de facturación pendiente.

Los **tableros** son hojas de cálculo de Odoo con tablas dinámicas sobre los datos vivos,
agrupadas en TMS › Operaciones › Tableros. Vienen tres con el módulo, cuyos nombres en la
interfaz son «Operations KPI», con los indicadores operativos del periodo; «Stops Operations»,
con las Paradas por estado, puntualidad y zona; y «Pending Invoicing», con lo ejecutado y no
facturado por cliente y por transportista. Funcionan en cualquier compañía y cualquier base, y
el cliente puede duplicarlos y adaptarlos desde la propia hoja.

Tres detalles del TMS sobre los tableros de Odoo:

- El filtro de fecha en **Periodo relativo** tiene, además de los periodos de Odoo, días sueltos
  hacia delante: **Hoy**, **Mañana**, **Mañana +1**, **Mañana +2** y **Mañana +3**. Cada uno filtra
  un solo día y se mueve con la fecha: «Mañana» es siempre mañana. Sirven para mirar la carga de
  trabajo de los próximos días.
- **Ver registros** en una celda de una tabla abre las Órdenes, las líneas de venta y las líneas de
  compra en las pantallas del TMS, no en las de Ventas o Compras de Odoo.
- TMS › Operaciones › Tableros enseña solo los grupos de tableros marcados como **Tablero TMS**
  (casilla de la ficha del grupo, en la configuración de los tableros de Odoo). Un grupo propio del
  cliente sale en el menú marcando esa casilla.

Cómo se lleva un tablero de una base a otra sin que se rompa está en la
:doc:`Guía del integrador </17.0/7_edi-integrations/7_10_kpis-dashboards>`.
