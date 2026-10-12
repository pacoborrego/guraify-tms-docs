9.3 Obligación y exenciones
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Pestaña **DeCA** del Tramo (grupos Obligación, Transporte y Exenciones) · TMS › Operaciones ›
   DeCA › **Tramos sin DeCA**

Cada Tramo de una compañía con el DeCA activo lleva tres datos: si **requiere DeCA**, el
**motivo** y, si no lo requiere, la **exención** que lo libra. Los calcula el sistema, nadie los
teclea, y el usuario los ve en la pestaña DeCA del Tramo junto al cargador, el transportista, las
matrículas y el caso con que se resolvió.

9.3.1 El orden de las reglas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El motor evalúa las exenciones en un orden fijo y se detiene en la primera que se cumple; si
ninguna se cumple, el Tramo está obligado.

#. La **compañía** tiene el DeCA apagado: nada que evaluar.
#. **Exención manual** del Tramo: un Usuario DeCA la marca en el Tramo con su motivo, para el
   caso suelto que las reglas no contemplan.
#. **Exención fija del Proyecto** (ficha DeCA): internacional, sin licencia o manual.
#. **Transporte privado complementario**: cargador y transportista son los dos la propia
   compañía. Transportar con flota propia para un cliente externo **no** es privado.
#. **Internacional**: el origen o el destino no están en España; vale la carta de porte
   internacional (CMR).
#. **Vehículo sin autorización de transporte**: la masa máxima autorizada del vehículo es de
   2.000 kg o menos. Un vehículo sin ese dato cargado no está exento.
#. **Mudanza** o **vehículo averiado**: la operación del Tramo así lo dice.
#. **Paquetería** (art. 2.1.d), si la compañía o el Proyecto piden evaluarla.

9.3.2 Paquetería según el Ministerio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La exención de paquetería no es «este Proyecto es de paquetería»: es un criterio por Tramo,
fijado por la Subdirección General de Inspección de Transporte (respuesta del 3-oct-2026, citada
en el ``README`` del módulo), con **dos condiciones a la vez**:

#. La expedición es pequeña: bultos **y** palés por debajo o igual a los umbrales (y, si se fija,
   un peso por bulto por debajo del máximo).
#. Se puede manipular con lo que lleva el vehículo: **no hay palés**, o los hay y el vehículo
   del Viaje lleva un equipamiento de la lista de medios de manipulación (una transpaleta).

Las dos se evalúan igual para entregas, recogidas y servicios directos, y el motivo del Tramo
lleva las cifras («3 bultos ≤ 10, 0 palés ≤ 2»). Los umbrales salen de la ficha del Proyecto si
tiene los suyos; si no, de la compañía si tiene la casilla activa; **sin umbrales no hay
exención**. Un vehículo ajeno a la flota aporta sus medios de manipulación desde los equipos
externos anotados en el Viaje.

9.3.3 Qué pasa al cambiar la configuración
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cambiar un ajuste de la compañía, una ficha de Proyecto, la marca de flota propia de un
transportista, el país de un contacto o los equipos de un vehículo recalcula la obligación de los
**Tramos abiertos**: los no iniciados, sin facturar, sin DeCA emitido y de los últimos 90 días.
Un Tramo con DeCA emitido o facturado **conserva la obligación con la que se emitió**: es la
evidencia. Lo que se enseña en la lista **Tramos sin DeCA**, lo que se genera al despachar y la
alerta diaria no leen ese dato guardado sino que **evalúan en vivo**, así que un Tramo antiguo sale
bien aunque su campo no se haya recalculado.

Un Tramo cuenta como «sin DeCA» cuando está obligado y no tiene documento vigente, o cuando lo
tiene pero está **desactualizado**: el Tramo ya no va en el Viaje con que se emitió, o ese Viaje
cambió de transportista o de vehículo. En ese caso toca anular y emitir uno nuevo
(:doc:`9_4_lifecycle`).
