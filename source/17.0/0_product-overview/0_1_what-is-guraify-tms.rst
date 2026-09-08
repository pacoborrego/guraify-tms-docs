Qué es Guraify TMS
------------------

Guraify TMS es la aplicación de transporte de Odoo 17. No es un programa aparte que se conecta
con el ERP: **es un módulo más de Odoo**, como Ventas o Contabilidad, y se instala sobre la
misma base de datos. Quien lo usa entra en Odoo y encuentra un menú nuevo, TMS, con todo lo
que necesita para gestionar el transporte.

Cubre el ciclo completo de un servicio de transporte:

1. **Recibir el encargo.** El cliente pide un transporte: a mano, por un fichero, por una
   integración con su sistema o desde un portal. En el TMS eso es una :term:`Orden`.
2. **Convertirlo en trabajo real.** La Orden se descompone en movimientos (:term:`Tramo`) y
   cada movimiento en los puntos físicos donde hay que hacer algo (:term:`Parada`): cargar,
   descargar, pasar por un hub.
3. **Planificar.** Las Paradas se agrupan en :term:`Viajes <Viaje>` y se asignan a un
   conductor y un vehículo, propios o de un transportista. Se puede hacer a mano, con ayuda del
   mapa, o dejar que el optimizador proponga los viajes.
4. **Ejecutar.** El conductor lleva el viaje en la app del móvil: ve sus paradas, escanea
   bultos, recoge la firma o la foto del albarán, cobra reembolsos y registra incidencias. Cada
   acción llega al backoffice al momento.
5. **Cerrar y cobrar.** Al terminar el viaje, el sistema calcula el coste del transportista y
   genera su orden de compra, y la Orden queda lista para facturar al cliente con la tarifa que
   le corresponde.

Qué lo hace distinto
~~~~~~~~~~~~~~~~~~~~

**Está dentro del ERP.** Los clientes, los transportistas, los vehículos, las tarifas, las
facturas y la contabilidad son los de Odoo. No hay dos fichas de cliente ni hay que
sincronizar nada: la factura del transporte es una factura de Odoo, y el coste del viaje es
una orden de compra de Odoo.

**Separa lo que se vende de lo que se ejecuta.** El encargo del cliente (la Orden) y la
ejecución física (el Viaje) son dos cosas distintas y así se guardan. Una Orden puede
ejecutarse en varios viajes y un viaje puede llevar órdenes de muchos clientes. Eso es lo que
permite grupaje, distribución multicliente y reorganizar la operación sin tocar lo que se
factura. Y es lo que permite saber el margen de cada orden, de cada viaje y de cada cliente
sin cuadrar hojas de cálculo.

**Planifica sobre puntos reales.** La unidad de planificación no es el pedido, es la Parada:
un lugar con coordenadas, una ventana horaria y un tiempo de servicio. Por eso el optimizador
trabaja con datos físicos y por eso la app puede decir dónde está cada cosa.

**Trazabilidad de fábrica.** Cada estado, cada escaneo, cada firma y cada incidencia queda
registrada con fecha, autor y origen, desde el bulto hasta la factura. No hay que activarla:
es la consecuencia de trabajar con el sistema.

Qué necesita para funcionar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una instalación de Odoo 17 y el propio Guraify TMS. Para la planificación automática y las
horas estimadas de llegada se usa el motor cartográfico de PTV, que requiere un contrato
propio; sin él, el sistema funciona con planificación manual y mapa de OpenStreetMap. Para los
conductores, un móvil Android o iPhone con la app. Los detalles comerciales, de licencia y de
despliegue se consultan con Guraify.
