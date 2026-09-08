Cómo funciona
-------------

Todo Guraify TMS se apoya en cuatro conceptos. Quien los entiende entiende el sistema; el
resto es configuración.

Los cuatro conceptos
~~~~~~~~~~~~~~~~~~~~

**La Orden es lo que pide el cliente.** Qué hay que transportar, para quién y en qué
condiciones se factura. Es el documento comercial, y por eso es donde nace el ingreso. Una
Orden pertenece siempre a un :term:`Proyecto`, que es donde se guarda la configuración de ese
cliente o de esa operativa: su tarifa, su forma de trabajar, lo que se le permite y lo que no.

**El Tramo es cada movimiento de la Orden.** Desde dónde hasta dónde. Un envío puerta a
puerta tiene un tramo. Uno que pasa por un hub tiene dos: del origen al hub y del hub al
destino. Si una entrega falla y hay que volver, se añade un tramo más, sin tocar la Orden ni
lo que se factura.

**La Parada es el punto físico donde ocurre algo.** Cargar, descargar, entrar en un hub. Se
genera automáticamente al validar la Orden, a partir de sus tramos, y lleva coordenadas,
ventana horaria y tiempo estimado. Es la pieza con la que trabaja el planificador y la que ve
el conductor en el móvil. Si varias órdenes van al mismo sitio a la misma hora, el sistema las
junta en una sola parada.

**El Viaje es lo que hace un conductor en una salida.** Un conjunto de paradas ordenadas,
asignadas a un conductor y a un vehículo. Es la ejecución física, y por eso es donde nace el
coste: cuando lo hace un transportista externo, el viaje genera su orden de compra.

.. important::

   La Orden es el ingreso. El Viaje es el coste. Como son cosas distintas, una Orden puede
   repartirse en varios viajes y un viaje puede llevar órdenes de varios clientes. Y el
   margen sale solo.

El ciclo completo
~~~~~~~~~~~~~~~~~

.. mermaid::

   flowchart LR
       A[Orden<br/>encargo del cliente] --> B[Tramos<br/>movimientos]
       B --> C[Paradas<br/>puntos físicos]
       C --> D[Viajes<br/>rutas asignadas]
       D --> E[Ejecución<br/>app del conductor]
       E --> F[Cierre<br/>estados finales]
       F --> G[Liquidación<br/>orden de compra al transportista]
       F --> H[Facturación<br/>factura al cliente]

1. **Entra la Orden.** A mano, por fichero, por API o por webhook. Si viene en lote, primero
   pasa por un :term:`Manifiesto`, que la revisa y normaliza las direcciones antes de crear
   nada.
2. **Se valida.** La validación genera las Paradas. A partir de aquí la Orden ya tiene una
   representación física.
3. **Se planifica.** Las Paradas pendientes se agrupan en Viajes: filtrando y seleccionando a
   mano, en el mapa, o con el optimizador, que propone viajes completos teniendo en cuenta
   ventanas horarias, capacidades, horas de conducción y disponibilidad de conductores.
4. **Se ejecuta.** El conductor ve el viaje en la app, va parada a parada, escanea, entrega,
   firma, cobra y reporta. Cada acción actualiza la Parada, el Tramo y la Orden al momento, y
   el backoffice lo ve en pantalla sin llamar a nadie.
5. **Se cierra.** Cuando todas las paradas tienen un estado final (completada, con reservas,
   fallida, reprogramada, devuelta o cancelada), el Viaje se cierra y la Orden se bloquea para
   que nadie cambie lo que ya se ha ejecutado.
6. **Se liquida y se factura.** El Viaje calcula el coste con la tarifa del transportista y
   genera su orden de compra. La Orden calcula el precio con la tarifa del cliente y queda
   lista para facturar. Las dos operaciones usan las mismas tarifas, zonas y reglas, y el
   margen queda calculado por orden, por viaje, por cliente y por transportista.

Lo que pasa por debajo sin que nadie lo pida
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Geolocalización de direcciones**, con control de calidad: una dirección mal ubicada se
  marca y no deja cerrar el manifiesto hasta que alguien la corrige.
- **Trazabilidad** de cada evento, con quién lo hizo y desde dónde.
- **Indicadores visuales** en las listas de órdenes y paradas: estado, puntualidad, si hay
  factura, si falta la prueba de entrega.
- **Documentos**: etiquetas de bultos, manifiesto de transporte, detalle de la orden y
  prueba de entrega, generados desde el propio registro.
