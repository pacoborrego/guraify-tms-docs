Para quién es
-------------

Guraify TMS está pensado para empresas que **organizan transporte de mercancía para
terceros**, con flota propia, con transportistas externos o con las dos cosas. El mismo
sistema sirve para operativas muy distintas porque la lógica es la misma: encargos que se
convierten en Paradas y Paradas que se agrupan en Viajes. Lo que cambia entre una operativa y
otra es la configuración, no el producto.

Operativas que cubre
~~~~~~~~~~~~~~~~~~~~

**Última milla.** Muchas entregas pequeñas al día, con franjas horarias, reembolsos y prueba
de entrega (POD). Las Órdenes entran por integración o por fichero, el optimizador las reparte
en Viajes y el conductor las entrega con la app. El cliente recibe el estado y la POD de cada
Bulto.

**Distribución capilar con red de agencias.** Un operador con delegaciones territoriales y
uno o varios Hubs de cruce. La mercancía entra en el Hub, se reparte por Agencias y cada
Agencia la entrega en su zona. El TMS modela Hubs y Agencias, encadena los Tramos entre ellos
y mantiene la trazabilidad de la Orden aunque la ejecuten tres Viajes distintos.

**Grupaje.** Varios clientes comparten vehículo. Cada Orden se factura a su cliente con su
tarifa, cada Viaje se liquida con su transportista y el coste del Viaje se reparte entre las
Órdenes que lleva, para saber el margen de cada una (ver :doc:`Cómo funciona
<0_3_how-it-works>`).

**Carga completa.** Un origen, un destino y un vehículo por servicio, normalmente con
transportista externo. Aquí el valor está en el control económico: tarifa de venta, coste de
compra, orden de compra automática al transportista y liquidación, con el margen a la vista
desde el primer día.

**Recogidas programadas y logística industrial.** Recogidas en fábrica o almacén con una hora
de convocatoria única (una hora concreta, no una franja) y medición de la puntualidad contra
esa hora. Sirve para fabricantes y distribuidores que exigen a sus transportistas cumplir
citas y quieren el dato de puntualidad en el mismo sistema que la factura.

Para quién dentro de la empresa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Tráfico y planificación**: crean y validan Órdenes, montan Viajes, asignan recursos y
  siguen la ejecución en tiempo real.
- **Conductores**: trabajan solo con la app del móvil, sin entrar en Odoo.
- **Administración**: liquida transportistas, factura clientes y controla márgenes con los
  datos que la operación ya ha generado.
- **Dirección**: consulta los tableros de operación, puntualidad y facturación pendiente.
- **Clientes**: reciben el estado de sus Órdenes y la POD en su propio sistema, por
  integración, o los consultan por su referencia a través de ella.

Para quién no es
~~~~~~~~~~~~~~~~

No es una herramienta de gestión de almacén ni de transporte de pasajeros. Tampoco es un
comparador de tarifas de paquetería: gestiona el transporte que la empresa organiza y
ejecuta, no la contratación de mensajerías de terceros. Y no funciona sin Odoo: quien no
quiera trabajar sobre Odoo necesita otra herramienta.
