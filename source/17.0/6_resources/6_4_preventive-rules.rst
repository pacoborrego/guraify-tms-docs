6.4 Reglas de preventivo y control de service
---------------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Mantenimiento › Reglas de preventivo y Control de service.

Odoo sabe repetir un mantenimiento cada tantos días, pero en ningún módulo sabe hacerlo cada
tantos **kilómetros**. Eso es lo que añade la :term:`Regla de preventivo`
(``tms.maintenance.rule``): para un vehículo y un trabajo, cada cuántos kilómetros o días toca,
y a partir del último realizado y del kilometraje actual, en qué estado está. El cliente de
referencia tiene setecientas cuarenta reglas sobre cuarenta y nueve unidades.

6.4.1 La regla
~~~~~~~~~~~~~~

.. CAPTURA: 6_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_4_preventive-rules_01_reglas.png
      :alt: Lista de Reglas de preventivo con su semáforo

      Las reglas de preventivo con su estado, lo consumido, lo restante y la confianza.

Una regla une un **vehículo** y un **trabajo**, y dice el **intervalo** y su **tipo**: kilómetros,
días o «no lleva» (el trabajo existe en el catálogo pero no aplica a esa unidad). Al elegir el
trabajo, la regla toma su tarea, su material y su intervalo por defecto, que se pueden cambiar.
Un vehículo no puede tener dos reglas activas para el mismo trabajo.

El resto de la regla lo calcula el motor: la fecha y el kilometraje del **último realizado**,
lo **consumido** desde entonces, lo **restante**, el **progreso**, el **estado** y la
**confianza**. Y cuando la regla no se puede evaluar, el **motivo**.

6.4.2 Cómo se evalúa
~~~~~~~~~~~~~~~~~~~~

Para una regla por **kilómetros**, el motor toma el kilometraje actual del vehículo y busca la
última orden de trabajo cerrada de ese trabajo en esa unidad. Si la orden trae el kilometraje
real, lo usa y la confianza es **alta**; si no lo trae (una orden histórica), lo **estima** con
la serie del odómetro en la fecha del trabajo y la confianza es **media**. Lo consumido es la
diferencia con el kilometraje actual; el progreso, lo consumido sobre el intervalo. Para una
regla por **días**, lo consumido son los días desde la fecha de cierre y la confianza es siempre
alta, porque las fechas no se estiman.

Los umbrales son los del prototipo del cliente y no se cambian: **al día** por debajo del 85 %,
**por vencer** entre el 85 % y el 100 %, **vencido** desde el 100 %. Lo restante es negativo
cuando la regla está vencida.

Una regla que no se puede evaluar queda **No evaluada**, y nunca se esconde: lleva su motivo a
la vista para que alguien lo resuelva.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Motivo
     - Qué significa
   * - No aplica a esta unidad
     - El intervalo es «no lleva».
   * - Sin historial
     - Nunca se ha cerrado una orden de ese trabajo en esa unidad. La regla no inventa un estado:
       si el trabajo toca, se carga como pendiente y a partir de ahí el motor tiene desde dónde
       contar.
   * - Falta captura de odómetro
     - La unidad no tiene ninguna lectura válida.
   * - Serie insuficiente para estimar
     - No hay lecturas con las que estimar el kilometraje del último trabajo.
   * - Dato incoherente
     - El kilometraje estimado del último trabajo supera al actual en más de 2.000 km. El dato
       no es creíble y la regla se aparta en vez de mostrar un vencido falso. Registrar el
       kilometraje real lo resuelve.

6.4.3 Cuándo se recalcula y cuándo genera pendientes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El motor no está calculando todo el tiempo: se dispara cuando algo cambia. Al crear, modificar o
cerrar una orden de trabajo se recalculan las reglas de ese vehículo; al registrar o validar una
lectura de odómetro, sus reglas por kilómetros y su control de service; al editar una regla,
esa regla. Una **tarea programada diaria** recalcula todas las reglas activas (las de días
avanzan con el calendario sin que nadie toque nada), refresca el control de service de toda la
flota y **genera los pendientes por kilómetros**: por cada regla por kilómetros que esté por
vencer o vencida, y no tenga ya una orden abierta para ese trabajo en esa unidad, crea una
orden de trabajo preventiva en Pendiente, con el material y lo que falta en la descripción.

Esa comprobación de «ya hay una abierta» es lo que evita que la tarea, al correr cada día,
duplique los pendientes. Y por eso el pendiente de una regla que cruza el umbral aparece con la
siguiente pasada de la tarea, no en el acto.

Las reglas por **días** no generan sus pendientes aquí: usan la **recurrencia nativa** de Odoo.
Al cerrar una orden preventiva recurrente, Odoo crea la siguiente con la fecha desplazada
según el intervalo. El motor sólo pinta el semáforo.

6.4.4 Control de service a dos niveles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_4_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_4_preventive-rules_02_control-service.png
      :alt: Pantalla Control de service

      El control de service por unidad: km actual, último service y los dos niveles.

Además de las reglas, cada vehículo lleva el :term:`Control de service`: dos niveles sobre el
kilometraje del último service registrado. El **service de combustible** toca cada 15.000 km y
el **service completo** cada 30.000, con un margen de aviso de 1.500 km; los tres umbrales se
configuran por compañía (ver :doc:`6_8_configuration`). Para cada nivel, lo restante es el
intervalo menos lo recorrido desde el último service: **vencido** si es negativo, **por vencer**
dentro del margen, **al día** en otro caso.

Si el vehículo no tiene kilometraje o no tiene kilometraje de último service, el estado es
**Sin datos**, no vencido. Es una decisión deliberada: la hoja de cálculo del cliente pintaba
como vencidas las unidades cuyo último service se desconocía, y eso es un falso vencido que el
sistema no reproduce. La pantalla **Control de service** lista toda la flota con los dos niveles
y las órdenes abiertas. Campos en :doc:`/17.0/annexes/A_20_mantenimiento`.
