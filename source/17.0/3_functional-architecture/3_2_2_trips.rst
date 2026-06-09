3.2.2 Viajes
============

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes

El Viaje (``tms.trip``) es la unidad de ejecución y de coste. Agrupa Paradas
(``tms.stop``) en una ruta ejecutable asignada a un recurso y, cuando interviene un
transportista externo, genera la orden de compra (``purchase.order``) que materializa el
coste y habilita la liquidación.

3.2.2.1 Creación, secuenciación y routing
-----------------------------------------

Un Viaje puede crearse de forma **manual** —filtrando y agrupando Paradas según criterios
operativos— o de forma **automática** mediante el optimizador integrado con PTV. Sobre
esa estructura, PTV interviene en dos planos descritos en :doc:`3_3_planning-model`: la
**secuenciación** (ordenar las Paradas ya asignadas al Viaje) y el **routing**
(enriquecer la ruta con distancias, tiempos, ETAs y costes de la red viaria real). En
todos los casos, la entidad planificable sigue siendo la Parada y la unidad de ejecución
el Viaje; PTV aporta la inteligencia matemática, no sustituye el modelo.

3.2.2.2 Relación con la orden de compra
---------------------------------------

Cuando el Viaje se ejecuta con un transportista colaborador, el sistema crea y vincula
una orden de compra (``purchase.order``, campo ``purchase_order_id``). Esa OC es la que
traslada el coste del Viaje al circuito de compras y facturación de proveedores de Odoo,
y la que activa el proceso de liquidación al transportista.

3.2.2.3 Estados en tres dimensiones
-----------------------------------

El Viaje no tiene un único estado, sino **tres dimensiones de estado independientes**,
que reflejan que un mismo viaje avanza a la vez en lo operativo, en lo contractual con el
proveedor y en lo económico:

.. list-table::
   :header-rows: 1
   :widths: 24 18 58

   * - Dimensión
     - Campo
     - Significado
   * - Operativa
     - ``state``
     - Estado de ejecución del viaje, **calculado a partir de sus Paradas**: borrador
       (``draft``), en proceso (``in_process``), procesado (``processed``), completado
       (``completed``) o fallido (``failed``).
   * - Compra (OC)
     - ``po_state``
     - Estado de la orden de compra asociada (``purchase_order_id.state``): borrador,
       enviada, por aprobar, confirmada, hecha o cancelada. Refleja el ciclo de
       contratación del transportista.
   * - Facturación
     - ``invoice_status``
     - Estado de facturación de la OC (``purchase_order_id.invoice_status``): refleja si
       el coste está pendiente de factura, facturado o sin factura.

Esta separación permite, por ejemplo, que un Viaje esté operativamente completado pero
aún pendiente de facturar, o que la OC esté confirmada antes de iniciar la ejecución, sin
que un estado contamine al otro.

3.2.2.4 Bloqueo y desbloqueo
----------------------------

En el Viaje, el "bloqueo" no actúa sobre el viaje en sí, sino sobre su **orden de compra**
(``purchase.order``), que es donde reside el coste. Equivale a los botones **Bloquear** y
**Desbloquear** del ciclo de compra de Odoo:

- **Bloquear** confirma la OC (``button_confirm`` → ``po_state`` = *confirmada*) y fija
  las cantidades recibidas y a facturar, dejando el coste listo para la liquidación.
- **Desbloquear** (``button_unlock``) devuelve la OC a borrador y **revierte a cero** las
  cantidades recibidas y a facturar, permitiendo recomponer el viaje.

La interacción con los estados es automática y sigue al estado de las Paradas:

- **Bloqueo automático al completar.** Cuando todas las Paradas del Viaje alcanzan un
  estado de cierre, el sistema tarifica el coste (tarifa pasiva), ejecuta ``button_done``
  sobre la OC y marca el Viaje como **completado**.
- **Desbloqueo automático al reabrir.** Si el Viaje deja de tener todas sus Paradas
  cerradas y su OC estaba confirmada (``po_state`` = *purchase*), el sistema ejecuta
  ``button_unlock`` y devuelve el Viaje a **procesado**.
- **Protección.** Un Viaje cuya OC esté **facturada** no puede revertirse; y si la OC está
  en estado *hecha* o *cancelada*, el sistema la considera **bloqueada** e impide pasarla a
  borrador. Estas situaciones se reflejan, cuando afectan a la tarificación, en el
  diagnóstico de tarifa del Viaje (``purchase_order_blocked``).

De este modo, bloquear un Viaje equivale a "cerrar el coste" del transportista, y
desbloquearlo a reabrirlo para corregirlo, siempre que no se haya facturado todavía.

.. CAPTURA: 3_2_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_2_trips_01_viaje.png
      :alt: Formulario de un Viaje con sus tres estados

      Formulario de un Viaje (``tms.trip``) con sus estados operativo, de compra y de facturación.
