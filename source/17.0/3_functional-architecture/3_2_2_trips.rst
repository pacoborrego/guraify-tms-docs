3.2.2 Viajes
------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes

El :term:`Viaje` (``tms.trip``) es la unidad de ejecución y de coste. Agrupa Paradas en una
secuencia que ejecuta un recurso (conductor y vehículo) y, cuando interviene un transportista
externo, genera la :term:`Orden de compra` que materializa el coste y habilita la liquidación.

3.2.2.1 Creación, secuenciación y cálculo de ruta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un Viaje puede crearse de forma **manual**, filtrando y agrupando Paradas según criterios
operativos, de forma **automática** con el Optimizador de Paradas, o desde un **Manifiesto**
cuyo fichero ya trae la asignación a viajes. Sobre esa estructura, PTV ordena las Paradas
(:term:`secuenciación <Secuenciación>`) y enriquece el recorrido con distancias, tiempos y horas
estimadas de llegada (:term:`cálculo de ruta <Cálculo de ruta>`); los tres servicios de PTV y
cuándo se lanza cada uno están en
:doc:`/17.0/1_introduction/1_4_technological-architecture`. En todos los casos, la entidad
planificable sigue siendo la Parada y la unidad de ejecución el Viaje; PTV aporta el cálculo,
no sustituye el modelo. El paso a paso de cada forma de creación está en
:doc:`/17.0/5_operational-flows/5_2_trip-generation`.

3.2.2.2 Relación con la orden de compra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando el Viaje se ejecuta con un transportista, el sistema crea y vincula una orden de compra
(OC). Esa OC es la que traslada el coste del Viaje al circuito de compras y facturación de
proveedores de Odoo, y la que activa el proceso de liquidación al transportista. Si el
transportista es flota propia no hay orden de compra (ver
:doc:`/17.0/8_economic-administration/8_1_active-passive-margin`).

3.2.2.3 Estados en tres dimensiones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El Viaje no tiene un único estado, sino **tres dimensiones de estado independientes**, que
reflejan que un mismo viaje avanza a la vez en lo operativo, en lo contractual con el proveedor
y en lo económico:

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Dimensión
     - Significado
   * - Operativa
     - Estado de ejecución del Viaje, **calculado a partir de sus Paradas**, con cinco valores
       propios: borrador (todas sus Paradas en borrador), en proceso, procesado (hay Paradas
       sin cerrar), completado (todas cerradas) o fallido.
   * - Compra (OC)
     - Estado de la orden de compra asociada, con las etiquetas de Odoo 17: SdP (solicitud de
       presupuesto), SdP enviada, A aprobar, Pedido de compra, Bloqueada o Cancelado. Refleja
       el ciclo de contratación del transportista.
   * - Facturación
     - Estado de facturación de la OC: Nada a facturar, Facturas en espera o Totalmente
       facturado.

Esta separación permite, por ejemplo, que un Viaje esté operativamente completado pero aún
pendiente de facturar, o que la OC esté confirmada antes de iniciar la ejecución, sin que un
estado contamine al otro.

3.2.2.4 Bloqueo y desbloqueo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En el Viaje, el «bloqueo» no actúa sobre el viaje en sí, sino sobre su **orden de compra**, que
es donde reside el coste. La cabecera del Viaje ofrece dos botones:

- **Bloquear** confirma la OC y fija las cantidades recibidas y a facturar de sus líneas,
  dejando el coste listo para la liquidación. Antes comprueba que ninguna línea tenga cantidad
  o precio a cero; si los hay, avisa de que la OC no se podría facturar.
- **Desbloquear** devuelve la OC a borrador y **revierte a cero** las cantidades recibidas y a
  facturar, permitiendo recomponer el viaje. Requiere el permiso de responsable de compras.

La interacción con los estados es automática y sigue al estado de las Paradas:

- **Bloqueo automático al completar.** Cuando todas las Paradas del Viaje alcanzan un estado de
  cierre, el sistema tarifica el coste con la tarifa del transportista, bloquea la OC y marca el
  Viaje como **completado**.
- **Desbloqueo automático al reabrir.** Si el Viaje deja de tener todas sus Paradas cerradas y
  su OC estaba confirmada, el sistema la desbloquea y devuelve el Viaje a **procesado**.
- **Protección.** Un Viaje cuya OC esté **facturada** no puede revertirse. Y si la OC está
  *Bloqueada* o *Cancelada*, el sistema la considera intocable e impide pasarla a borrador;
  cuando eso afecta a la tarificación, el diagnóstico de tarifa del Viaje lo indica con el
  motivo «Orden de compra bloqueada».

De este modo, bloquear un Viaje equivale a «cerrar el coste» del transportista, y desbloquearlo
a reabrirlo para corregirlo, siempre que no se haya facturado todavía. El flujo completo de
cierre está en :doc:`/17.0/5_operational-flows/5_5_trip-closing`.

.. figure:: /_static/img/3_functional-architecture/3_2_2_trips_01_viaje.png
   :alt: Formulario de un Viaje con sus tres estados

   Formulario de un Viaje con sus estados operativo, de compra y de facturación.

3.2.2.5 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Campo de ``tms.trip``
   * - Estado operativo
     - ``state`` (``draft``, ``in_process``, ``processed``, ``completed``, ``failed``)
   * - Orden de compra vinculada
     - ``purchase_order_id``
   * - Estado de compra
     - ``po_state`` (el ``state`` de la OC: ``draft``, ``sent``, ``to approve``, ``purchase``,
       ``done``, ``cancel``)
   * - Estado de facturación
     - ``invoice_status`` (el de la OC: ``no``, ``to invoice``, ``invoiced``)
   * - Motivo «Orden de compra bloqueada»
     - valor ``purchase_order_blocked`` del diagnóstico de tarifa del Viaje (no es un campo)
