Casos de uso
------------

Cuatro operativas inspiradas en casos reales, contadas de principio a fin, para ver cómo
encajan las piezas. Los datos están simplificados y las empresas no se nombran.

Distribución capilar con agencias y hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un operador regional recibe cada mañana de sus grandes clientes un fichero con las entregas
del día. Cada cliente tiene su formato, definido una vez en el TMS. Los ficheros se importan
en Manifiestos, el sistema geolocaliza las direcciones y marca las dudosas para que tráfico
las corrija antes de cerrar.

Al cerrar cada Manifiesto nacen las Órdenes con dos Tramos: del Hub central, donde los
clientes dejan la mercancía, a la Agencia de la zona, y de la Agencia al destinatario. El
primer Tramo se agrupa en Viajes de arrastre (los que llevan la mercancía del Hub a cada
Agencia); el segundo, en los Viajes de reparto de cada Agencia, que el optimizador propone
teniendo en cuenta franjas horarias y capacidad de las furgonetas.

Los conductores de cada Agencia entregan con la app: escanean, firman, cobran reembolsos y
reportan ausentes. Al cerrar el día, cada Viaje genera la orden de compra al transportista que
lo ha hecho, con la tarifa de compra pactada, y las Órdenes se facturan a cada cliente con su
tarifa de venta. Dirección ve en los tableros el volumen y la puntualidad por cliente,
Planning y conductor, filtrando por transportista si quiere; el margen, en cada Orden y en
cada Viaje.

Última milla con Órdenes por API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una empresa de reparto trabaja para una plataforma de venta en línea. Cada pedido de la
tienda llega por API como una Orden en el momento en que se confirma. Las Órdenes entran en
la Bandeja de entrada API del Proyecto de ese cliente, se validan y se agrupan en un
Manifiesto que se cierra varias veces al día.

Antes de la salida, el planificador abre el optimizador con las Paradas pendientes de la
tarde y las franjas de disponibilidad de los conductores. El optimizador propone los Viajes,
el planificador ajusta dos Paradas a mano y confirma. Cada conductor recibe su Viaje en la
app.

En cada entrega el conductor escanea el Bulto y recoge la firma. En ese instante el TMS envía
a la plataforma el estado «entregado», tal como lo espera su sistema, con la firma adjunta, y
la plataforma se lo muestra a su comprador. Si el destinatario no está, el conductor lo
reporta, la Parada queda Fallida y la plataforma recibe el motivo. Al reprogramar la entrega
para el día siguiente, la Orden recibe un Tramo nuevo para el segundo intento, sin que nadie
cree otra Orden.

Carga completa con transportista externo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un operador logístico organiza cargas completas para clientes industriales y las subcontrata
a transportistas de confianza. Cada servicio es una Orden con un Tramo de origen a destino y
un Viaje con esa única Orden, asignado al transportista.

Lo que aporta el TMS es el control económico. La tarifa de venta del cliente y la tarifa de
compra del transportista están configuradas por zonas y tipo de vehículo, así que al validar
la Orden el precio de venta ya está calculado y al asignar el transportista también el coste.
El planificador ve el margen antes de confirmar. Al cerrar el Viaje, el sistema genera la
orden de compra al transportista; administración la convierte en factura de compra cuando
llega la del transportista y factura al cliente desde la propia lista de Órdenes. El
diagnóstico de tarifa explica cualquier importe que no cuadre.

Recogidas programadas en fábrica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un fabricante organiza con el TMS las recogidas de sus cargas en planta. Cada recogida tiene
una hora de convocatoria única: no una franja, una hora. El transportista debe estar allí a
esa hora y la puntualidad se mide contra ella, con una tolerancia que fija el Proyecto.

El conductor del transportista marca la llegada en la app, la planta carga, el conductor
escanea los Bultos y confirma la salida. La puntualidad de la Parada queda registrada y el
fabricante la consulta en sus tableros filtrando por transportista y periodo. Cuando llega el
momento de renegociar con un transportista, el dato de cumplimiento está en el mismo sistema
que sus facturas.
