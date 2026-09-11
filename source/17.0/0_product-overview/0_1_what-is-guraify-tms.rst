Qué es Guraify TMS
------------------

Guraify TMS es una aplicación de gestión del transporte para Odoo 17. No es un programa aparte
que se conecta con el sistema de gestión de la empresa (el ERP): **se instala dentro de
Odoo**, como Ventas o Contabilidad, sobre la misma base de datos. Quien lo usa entra en Odoo y
encuentra un menú nuevo, TMS, con todo lo que necesita para gestionar el transporte.

Cubre el ciclo completo de un servicio de transporte: recibir el encargo del cliente (la
:term:`Orden`), convertirlo en los puntos físicos donde hay que hacer algo (las
:term:`Paradas <Parada>`), agrupar las Paradas en :term:`Viajes <Viaje>` y asignarles conductor
y vehículo, ejecutar cada Viaje con la app del móvil y, al terminar, liquidar al transportista
y facturar al cliente. Cada paso está contado en :doc:`Cómo funciona <0_3_how-it-works>`.

Qué lo hace distinto
~~~~~~~~~~~~~~~~~~~~

**Está dentro del ERP.** Los clientes, los transportistas, los vehículos, las tarifas, las
facturas y la contabilidad son los de Odoo. No hay dos fichas de cliente ni hay que
sincronizar nada: la factura del transporte es una factura de Odoo, y el coste de un Viaje
subcontratado es una orden de compra de Odoo.

**Separa lo que se vende de lo que se ejecuta.** El encargo del cliente (la Orden) y la
ejecución física (el Viaje) son dos cosas distintas y así se guardan. Eso es lo que permite el
grupaje, la distribución multicliente y reorganizar la operación sin tocar lo que se factura,
y lo que hace que el margen salga solo. El porqué está en
:doc:`Cómo funciona <0_3_how-it-works>`.

**Planifica sobre puntos reales.** La unidad de planificación no es la Orden, es la Parada:
un lugar concreto, con coordenadas. Por eso el optimizador trabaja con datos físicos y por eso
la app puede decir dónde está cada cosa.

**Trazabilidad de fábrica.** Cada estado, cada escaneo, cada firma y cada incidencia queda
registrada con fecha, autor y origen, desde el Bulto hasta la factura. No hay que activarla:
es la consecuencia de trabajar con el sistema.

Qué necesita para funcionar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Necesita una instalación de Odoo 17 y los módulos de Guraify TMS. Para la planificación
automática y las horas estimadas de llegada usa los servicios de PTV, un proveedor de
cartografía y de cálculo de rutas para el transporte profesional, que se contratan aparte; sin
ellos, el sistema funciona con planificación manual (ver :doc:`Qué incluye
<0_4_what-it-includes>`). Para los conductores, un móvil Android o iPhone con la app.
