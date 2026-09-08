Para quién es
-------------

Guraify TMS está pensado para empresas que **organizan transporte de mercancía para
terceros**, con flota propia, con transportistas colaboradores o con las dos cosas. El mismo
sistema sirve para operativas muy distintas porque el modelo de datos es el mismo: encargos
que se convierten en paradas y paradas que se agrupan en viajes. Lo que cambia entre una
operativa y otra es la configuración, no el producto.

Operativas que cubre
~~~~~~~~~~~~~~~~~~~~

**Última milla.** Cientos o miles de entregas pequeñas al día, con ventanas horarias,
reembolsos y prueba de entrega. Los pedidos entran por integración o por fichero, el
optimizador los reparte en rutas y el conductor los entrega con la app. El cliente que envía
recibe el estado y la prueba de entrega de cada bulto.

**Distribución capilar con red de agencias.** Un operador con delegaciones territoriales y
uno o varios hubs de cruce. La mercancía entra en el hub, se reparte por agencias y cada
agencia la entrega en su zona. El TMS modela hubs y agencias, mueve las paradas entre ellas y
mantiene la trazabilidad de la Orden aunque la ejecuten tres viajes distintos.

**Grupaje.** Varios clientes comparten vehículo. Cada Orden se factura a su cliente con su
tarifa y cada Viaje se liquida con su transportista, y el sistema reparte el coste del viaje
entre las órdenes para saber el margen de cada una.

**Carga completa.** Un origen, un destino y un vehículo por servicio, normalmente con
transportista externo. Lo que aporta el TMS aquí es el control económico: tarifa de venta,
coste de compra, orden de compra automática al transportista y liquidación, con el margen a la
vista desde el primer día.

**Recogidas programadas y logística industrial.** Recogidas en fábrica o almacén con una hora
de convocatoria única y medición de puntualidad contra esa hora. Sirve para cargadores que
exigen a sus transportistas cumplir citas y quieren el dato de puntualidad en el mismo sistema
que la factura.

Para quién dentro de la empresa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Tráfico y planificación**: crean y validan órdenes, montan viajes, asignan recursos y
  siguen la ejecución en tiempo real.
- **Conductores**: trabajan sólo con la app del móvil, sin entrar en Odoo.
- **Administración**: liquida transportistas, factura clientes y controla márgenes con los
  datos que la operación ya ha generado.
- **Dirección**: mira los tableros de operación, puntualidad, facturación pendiente y margen.
- **Clientes finales**: consultan el estado de sus envíos por integración o por el portal.

Para quién no es
~~~~~~~~~~~~~~~~

No es una herramienta de gestión de almacén ni de transporte de pasajeros. Tampoco es un
comparador de tarifas de paquetería: gestiona el transporte que la empresa organiza y
ejecuta, no la contratación de mensajerías de terceros. Y no es un producto para usar sin
Odoo: quien no quiera trabajar sobre Odoo necesita otra herramienta.
