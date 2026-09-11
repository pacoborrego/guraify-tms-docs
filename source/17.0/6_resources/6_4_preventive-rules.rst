6.4 Reglas de preventivo y control de revisiones
------------------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Mantenimiento › Reglas de preventivo y «Control de service».

Odoo sabe repetir un mantenimiento cada tantos días, pero en ningún módulo sabe hacerlo cada
tantos **kilómetros**. Eso es lo que añade la :term:`Regla de preventivo`
(``tms.maintenance.rule``): para un vehículo y un trabajo, cada cuántos kilómetros o días toca,
y a partir del último realizado y del kilometraje actual, en qué estado está.

6.4.1 La regla
~~~~~~~~~~~~~~

.. CAPTURA: 6_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_4_preventive-rules_01_reglas.png
      :alt: Lista de Reglas de preventivo con su semáforo

      Las reglas de preventivo con su estado, lo consumido, lo restante y la confianza.

Una regla une un **vehículo** y un **trabajo**, y dice el **intervalo** y su **tipo**: kilómetros,
días o «no lleva» (el trabajo existe en el catálogo pero no aplica a ese vehículo). Al elegir el
trabajo, la regla toma su tarea, su material y su intervalo por defecto, que se pueden cambiar.
Un vehículo no puede tener dos reglas activas para el mismo trabajo.

El resto de la regla lo calcula el motor: la fecha y el kilometraje del **último realizado**,
lo **consumido** desde entonces, lo **restante**, el **progreso**, el **estado** y la
**confianza**. Y cuando la regla no se puede evaluar, el **motivo**.

6.4.2 Cómo se evalúa
~~~~~~~~~~~~~~~~~~~~

Para una regla por **kilómetros**, el motor toma el kilometraje actual del vehículo y busca la
última orden de trabajo cerrada de ese trabajo en ese vehículo. Si la orden trae el kilometraje
real, lo usa y la confianza es **alta**; si no lo trae (una orden histórica), lo **estima** con
la serie del odómetro en la fecha del trabajo y la confianza es **media**. Lo consumido es la
diferencia con el kilometraje actual; el progreso, lo consumido sobre el intervalo. Para una
regla por **días**, lo consumido son los días desde la fecha de cierre y la confianza es siempre
alta, porque las fechas no se estiman.

Los umbrales son fijos: **al día** por debajo del 85 % del intervalo, **por vencer** entre el
85 % y el 100 %, **vencido** desde el 100 %. Lo restante es negativo cuando la regla está
vencida.

Una regla que no se puede evaluar queda **No evaluada**, y nunca se esconde: lleva su motivo a
la vista para que alguien lo resuelva.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Motivo
     - Qué significa
   * - No aplica a este vehículo
     - El intervalo es «no lleva».
   * - Sin historial
     - Nunca se ha cerrado una orden de ese trabajo en ese vehículo. La regla no inventa un
       estado: si el trabajo toca, se carga como pendiente y a partir de ahí el motor tiene
       desde dónde contar.
   * - Falta captura de odómetro
     - El vehículo no tiene ninguna lectura válida.
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
lectura de odómetro, sus reglas por kilómetros y su control de revisiones; al editar una regla,
esa regla. Un **proceso diario** recalcula todas las reglas activas (las de días avanzan con el
calendario sin que nadie toque nada), refresca el control de revisiones de toda la flota y
**genera los pendientes por kilómetros**: por cada regla por kilómetros que esté por vencer o
vencida, y no tenga ya una orden abierta para ese trabajo en ese vehículo, crea una orden de
trabajo preventiva en Pendiente, con el material y lo que falta en la descripción.

Esa comprobación de «ya hay una abierta» es lo que evita que el proceso, al correr cada día,
duplique los pendientes. Y por eso el pendiente de una regla que cruza el umbral aparece con la
siguiente pasada del proceso, no en el acto.

Las reglas por **días** no generan sus pendientes aquí: usan la **recurrencia nativa** de Odoo.
Al cerrar una orden preventiva recurrente, Odoo crea la siguiente con la fecha desplazada
según el intervalo. El motor solo pinta el semáforo.

6.4.4 Control de revisiones a dos niveles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_4_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_4_preventive-rules_02_control-service.png
      :alt: Pantalla de control de revisiones

      El control de revisiones por vehículo: km actual, última revisión y los dos niveles.

Además de las reglas, cada vehículo lleva un control de revisiones (en la interfaz, «Control de
service»): dos niveles sobre el kilometraje de la última revisión registrada. La **revisión de
combustible** toca cada 15.000 km y la **revisión completa** cada 30.000, con un margen de aviso
de 1.500 km; los tres umbrales se configuran por compañía (ver :doc:`6_8_configuration`). Para
cada nivel, lo restante es el intervalo menos lo recorrido desde la última revisión: **vencido**
si es negativo, **por vencer** dentro del margen, **al día** en otro caso.

Si el vehículo no tiene kilometraje o no tiene kilometraje de última revisión, el estado es
**Sin datos**, no vencido. Es una decisión deliberada: una última revisión desconocida no es una
revisión vencida, y pintarla así sería un falso vencido. La pantalla «Control de service» lista
toda la flota con los dos niveles y las órdenes abiertas. Campos en
:doc:`/17.0/annexes/A_20_mantenimiento`.

6.4.5 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

Los estados y motivos de la regla, con la etiqueta que muestra hoy la interfaz.

.. list-table::
   :header-rows: 1
   :widths: 22 30 48

   * - Concepto
     - Etiqueta en la interfaz
     - Valor
   * - Estado de la regla
     - «OK», «Due Soon», «Overdue», «Not Evaluated»
     - ``status``: ``ok``, ``due_soon``, ``overdue``, ``not_evaluated``
   * - Confianza
     - «High», «Medium»
     - ``confidence``: ``high``, ``medium``
   * - Tipo de intervalo
     - «Kilometres», «Days», «Not Applicable»
     - ``interval_type``: ``km``, ``days``, ``na``
   * - Motivo de exclusión
     - «Does not apply to this unit», «No history: load it as a pending job», «Odometer capture
       missing», «Odometer series too thin to estimate», «Inconsistent data; register the real
       km»
     - ``exclusion_reason``: ``interval_na``, ``no_history``, ``no_odometer``,
       ``cannot_estimate``, ``estimate_inconsistent``
   * - Estado del control de revisiones
     - «OK», «Due Soon», «Overdue», «No Data»
     - ``tms_service_fuel_status`` y ``tms_service_full_status`` de ``fleet.vehicle``
   * - Proceso diario
     - «TMS: Recompute Preventive Maintenance»
     - Acción planificada (``ir.cron``) que ejecuta ``_cron_recompute_maintenance``
