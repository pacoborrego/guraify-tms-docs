5.6 Liquidación Económica
-------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Botón **Tarificar** en la Orden y en el Viaje · TMS › Administración › Opciones de Tarifa ›
   Diagnosis de tarifa de órdenes / Diagnosis de tarifa de viajes

.. CAPTURA: 5_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_6_settlement_01_liquidacion.png
      :alt: Liquidación económica

      Liquidación económica de venta (cliente) y de compra (transportista).

Liquidar es poner precio a lo ejecutado, en los dos lados a la vez: lo que se **cobra al
cliente** por cada Orden (``sale.order``) y lo que se **paga al transportista** por cada Viaje.
Los dos cálculos usan las mismas tarifas, zonas y reglas, pero son independientes: por eso el
margen sale por Orden, por Viaje, por Tramo o por Parada sin conciliaciones. Esta sección
cuenta cuándo se calcula cada lado y qué pasa cuando no se puede; la configuración de tarifas
está en :doc:`/17.0/4_parametrization/4_4_economic-configuration` y el modelo, en
:doc:`/17.0/3_functional-architecture/3_4_pricing-model`.

5.6.1 Cuándo se tarifica
~~~~~~~~~~~~~~~~~~~~~~~~

La tarificación no es un paso que el usuario tenga que recordar. El sistema marca la Orden o
el Viaje como **pendientes de tarificar** cada vez que cambia algo que afecta al precio, y una
**tarea programada** que corre cada cinco minutos los recoge y los calcula, por lotes y uno a
uno, para no cargar el servidor. Además, hay tres momentos en que el cálculo es inmediato:

- **Al validar la Orden**: se calculan sus líneas de venta y, si ya está en un Viaje, el coste
  de ese Viaje.
- **Al cerrar** el Viaje y la Orden (:doc:`5_5_trip-closing`): el coste se fija antes de
  bloquear la orden de compra y el precio se fija antes de confirmar la Orden.
- **Con el botón Tarificar**, en la Orden o en el Viaje, cuando el planificador quiere ver el
  resultado sin esperar.

Una Orden sólo se tarifica mientras está en *Presupuesto*; un Viaje, mientras su orden de
compra no está hecha ni cancelada y no se ha facturado. Volver a tarificar algo ya confirmado
exige pasarlo antes a borrador, a mano.

5.6.2 El lado de la venta
~~~~~~~~~~~~~~~~~~~~~~~~~

La Orden hereda la **tarifa de cliente** de su Proyecto. La tarificación recorre las
:term:`líneas de tarifa <Línea de tarifa>` aplicables, resuelve las :term:`zonas de tarifa <Zona
de tarifa>` de origen y destino a partir de las coordenadas de cada Tramo, mide lo que la
:term:`regla de tarifa <Regla de tarifa>` indique (peso, volumen, bultos, palés, metros,
kilómetros, paradas) y genera las **líneas de venta** de la Orden con su producto e importe.
Según la configuración del Proyecto, el importe se calcula para la Orden completa o se divide
por Tramo, de modo que cada fase del servicio tenga su precio. Los reembolsos cobrados en la
entrega se incorporan como conceptos propios.

5.6.3 El lado de la compra
~~~~~~~~~~~~~~~~~~~~~~~~~~

El Viaje se liquida con la **tarifa de compra** de su transportista, o con el **precio
cerrado** si se ha pactado un importe fijo. La primera tarificación con transportista y
tarifa crea la :term:`Orden de compra` y la vincula al Viaje; las siguientes actualizan sus
líneas. La orden de compra lleva una línea de sección con la descripción de la ruta, la fecha,
la distancia y los tiempos, y debajo los conceptos calculados. Cuando el transportista es
**flota propia** no hay orden de compra: el coste del conductor propio no se liquida por esta
vía.

5.6.4 Cuando el cálculo no puede hacerse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si la tarificación no encuentra cómo poner precio, no inventa un cero: deja un **diagnóstico
de tarifa** en la Orden o en el Viaje, visible en su formulario y en los menús **Diagnosis de
tarifa de órdenes** y **Diagnosis de tarifa de viajes**, que agrupan todo lo pendiente de
resolver. Los motivos habituales son una zona que no se resuelve para alguna dirección, un
trayecto entre zonas sin precio en la tarifa, una línea de tarifa cuyas condiciones no
coinciden con la Orden, una tarifa sin líneas, una orden de compra bloqueada o una
parametrización incompleta.

Dos botones ayudan a resolverlo sin salir del registro. **Resolver diagnosis** lleva al campo o
al registro que hay que corregir según el motivo. **Crear trayecto faltante** abre un asistente
que da de alta el precio entre las dos zonas que faltaban en la tarifa. Corregido el motivo, la
Orden o el Viaje vuelven a quedar pendientes de tarificar y la tarea programada los recalcula.

.. warning::

   Una Orden o un Viaje con diagnóstico de tarifa pendiente pueden cerrarse operativamente,
   pero no deben facturarse: el diagnóstico existe para que la incidencia se corrija antes de
   emitir el documento. La lista de diagnósticos pendientes es la primera revisión del cierre
   económico.
