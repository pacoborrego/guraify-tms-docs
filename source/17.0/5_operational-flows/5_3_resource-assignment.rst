5.3 Asignación de Recursos
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes (cabecera del formulario del Viaje)

.. CAPTURA: 5_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_3_resource-assignment_01_recursos.png
      :alt: Asignación de recursos a un viaje

      Viaje con conductor, vehículo y transportista asignados.

Un Viaje (``tms.trip``) está listo para ejecutarse cuando tiene quién lo hace y cuánto cuesta:
el **transportista**, el **conductor**, el **vehículo** (y su remolque, si lo hay) y la **tarifa
de compra** o el **precio cerrado** con que se liquidará. Estos datos pueden llegar por cuatro
caminos, y el planificador puede corregirlos en cualquier momento antes del cierre:

- **Del fichero**, si la :term:`Definición de fichero` mapea el transportista, su Proyecto o la
  tarifa de compra.
- **De la franja** del :term:`Plan de disponibilidad de conductores`: cuando el Viaje está
  ligado a una franja, su conductor, su transportista y su vehículo se copian de ella y se
  mantienen sincronizados.
- **Del Optimizador** en el modo por franja, que asigna a cada Viaje la franja con la que lo
  ha construido. En el modo por categoría de vehículo, el Viaje nace con la categoría y el
  recurso concreto se asigna después.
- **A mano**, en el formulario del Viaje o en el asistente **Asignar a viaje** al crearlo.

5.3.1 Los recursos y su efecto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Recurso
     - Qué determina
   * - Transportista
     - Quién ejecuta el Viaje: un transportista externo, una agencia o la flota propia. Es el
       proveedor de la :term:`Orden de compra`.
   * - Tarifa de compra o precio cerrado
     - Cómo se calcula el coste: con las líneas de la tarifa del transportista o con un importe
       fijo para todo el Viaje.
   * - Conductor
     - Quién ve el Viaje en la app. Sin conductor, el Viaje no se puede enviar a la app.
   * - Vehículo y remolque
     - Con qué se ejecuta. El vehículo aporta la categoría, y con ella el perfil de PTV, las
       capacidades y las horas de conducción del cálculo de ruta.
   * - Categoría de vehículo
     - Capacidades y restricciones cuando aún no hay vehículo concreto.

Con transportista y tarifa de compra (o precio cerrado), la siguiente tarificación crea la
Orden de compra del Viaje; sin uno de los dos, el Viaje no tiene coste. Cómo nace y se
actualiza la Orden de compra está en :doc:`/17.0/8_economic-administration/8_4_purchase-orders`;
el caso del transportista de **flota propia**, que no genera Orden de compra, en
:doc:`/17.0/8_economic-administration/8_1_active-passive-margin`.

5.3.2 Propagación a las Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los recursos no se quedan en el Viaje. Cada Parada toma su transportista, su conductor y su
vehículo del Viaje al que pertenece, de modo que la app del conductor, los informes, la
trazabilidad y la liquidación leen los mismos datos. Cambiar el conductor de un Viaje cambia el
conductor de todas sus Paradas, sin más intervención.
