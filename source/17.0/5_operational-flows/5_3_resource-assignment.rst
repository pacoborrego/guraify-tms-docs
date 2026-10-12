5.3 Asignación de Recursos
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes (cabecera del formulario del Viaje)

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
     - Quién ve el Viaje en la app. Sin conductor, el Viaje no se puede despachar al conductor (:doc:`5_4_app-execution`).
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

5.3.3 Historial del conductor y el vehículo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quién conduce qué no se declara: lo escriben los Viajes. Cuando un Viaje se **completa**, el
sistema anota el par conductor–vehículo en el **historial de conductores** del vehículo (el
nativo de Flota de Odoo). Si la línea abierta del vehículo ya es de ese conductor, el Viaje se
cuelga de ella; si era de otro, esa línea se cierra con la fecha del Viaje, se abre una para el
nuevo conductor y pasa a ser el titular del vehículo. Un Viaje antiguo de otro conductor que se
complete tarde deja una línea cerrada de su día, sin cambiar al titular; un Viaje sin conductor o
sin vehículo no anota nada. Si el Viaje se vuelve a completar con otro conductor u otro vehículo,
se recoloca y la línea que se queda sin Viajes desaparece (solo las que nacieron de un Viaje; las
escritas a mano no se tocan).

Cada línea acumula lo que sus Viajes recorrieron según el cálculo de ruta: Viajes, kilómetros,
horas de ruta, combustible, peajes y CO₂e. Son cifras de **ruta**, no del
:term:`odómetro <Odómetro único>`. Se consultan desde el botón **Drivers History** del vehículo
y desde el botón **Historial de vehículos** del conductor. El historial empieza a escribirse desde
que se activa: los Viajes anteriores no se cargan.
