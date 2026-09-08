Casos de uso
------------

Cuatro operativas reales, contadas de principio a fin, para ver cómo encajan las piezas. Los
datos están simplificados y las empresas no se nombran.

Distribución capilar con agencias y hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un operador regional recibe cada mañana de sus grandes clientes un fichero con las entregas
del día. Cada cliente tiene su formato, definido una vez en el TMS. Los ficheros se importan
en manifiestos, el sistema geolocaliza las direcciones y marca las dudosas para que tráfico
las corrija antes de cerrar.

Al cerrar cada manifiesto nacen las Órdenes con dos tramos: del hub central a la agencia de
la zona y de la agencia al destinatario. El primer tramo se agrupa en viajes de arrastre por
agencia; el segundo, en las rutas de reparto de cada agencia, que el optimizador propone
teniendo en cuenta franjas horarias y capacidad de las furgonetas.

Los conductores de cada agencia entregan con la app: escanean, firman, cobran reembolsos y
reportan ausentes. Al cerrar el día, cada viaje genera la orden de compra a la agencia o al
autónomo que lo ha hecho, con la tarifa de compra pactada, y las Órdenes se facturan a cada
cliente con su tarifa de venta. Dirección ve en el tablero el volumen, la puntualidad y el
margen por agencia.

Última milla con pedidos por API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una empresa de reparto trabaja para una plataforma de venta en línea. La plataforma envía
cada pedido por API en el momento en que se confirma. Los pedidos entran en la Bandeja de
entrada API del proyecto de ese cliente, se validan y se agrupan en un manifiesto que se
cierra varias veces al día.

Antes de la salida, el planificador abre el optimizador con las paradas pendientes de la
tarde y las franjas de disponibilidad de los conductores. El optimizador propone las rutas,
el planificador ajusta dos paradas a mano y confirma. Cada conductor recibe su viaje en la app.

En cada entrega el conductor escanea el bulto y recoge la firma. En ese instante el TMS envía
a la plataforma el estado "entregado" con la firma adjunta, y la plataforma se lo muestra a su
comprador. Si el destinatario no está, el conductor lo reporta, la parada queda fallida y la
plataforma recibe el motivo. Al día siguiente, la Orden lleva un tramo nuevo para el segundo
intento, sin que nadie cree otra orden.

Carga completa con transportista externo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un operador logístico organiza cargas completas para clientes industriales y las subcontrata
a transportistas de confianza. Cada servicio es una Orden con un tramo de origen a destino y
un viaje con esa única orden, asignado al transportista.

Lo que aporta el TMS es el control económico. La tarifa de venta del cliente y la tarifa de
compra del transportista están configuradas por zonas y tipo de vehículo, así que al validar
la Orden el precio de venta ya está calculado y al asignar el transportista también el coste.
El planificador ve el margen antes de confirmar. Al cerrar el viaje, el sistema genera la
orden de compra al transportista; administración la convierte en factura de compra cuando
llega la del transportista y factura al cliente con un clic. El diagnóstico de tarifa explica
cualquier importe que no cuadre.

Recogidas programadas en fábrica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un fabricante organiza con el TMS las recogidas de sus expediciones en planta. Cada recogida
tiene una hora de convocatoria única: no una franja, una hora. El transportista debe estar
allí a esa hora y la puntualidad se mide contra ella, con una tolerancia que fija el proyecto.

El conductor del transportista marca la llegada en la app, la planta carga, el conductor
escanea los bultos y confirma la salida. El indicador de puntualidad de la parada queda
registrado y el fabricante lo ve por transportista, por semana y por planta en sus tableros.
Cuando llega el momento de renegociar con un transportista, el dato de cumplimiento está en el
mismo sistema que sus facturas.
