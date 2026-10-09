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
     - Estado de ejecución del Viaje, **calculado a partir de sus Paradas de ruta** y de la
       marca de despacho: **Sin Paradas** (etiqueta *Borrador*: no tiene ninguna Parada de ruta),
       **Planificado** (tiene Paradas y nadie lo ha despachado), **Despachado** (se ha enviado
       al conductor o a la agencia), **En curso** (el conductor o la agencia han actuado sobre
       alguna Parada), **Por validar** (todas las Paradas cerradas en un Proyecto que exige
       revisar el Viaje antes de facturar), **Completado** (todas cerradas) o **Fallido** (todas
       fallidas). La escalera completa, con lo que mueve cada peldaño, está en
       :ref:`ciclo-estados`.
   * - Compra (OC)
     - Estado de la orden de compra asociada, con las etiquetas de Odoo 17: SdP (solicitud de
       presupuesto), SdP enviada, A aprobar, Pedido de compra, Bloqueada o Cancelado. Refleja
       el ciclo de contratación del transportista: la SdP nace al planificar, se marca enviada
       al despachar y se confirma y bloquea al completar el Viaje.
   * - Facturación
     - Estado de facturación de la OC: Nada a facturar, Facturas en espera o Totalmente
       facturado.

Esta separación permite, por ejemplo, que un Viaje esté operativamente completado pero aún
pendiente de facturar, o que la OC esté confirmada antes de iniciar la ejecución, sin que un
estado contamine al otro.

Dos marcas acompañan al estado operativo. Un Viaje **repartido** (sus Paradas pendientes se han
llevado a otras rutas con *Repartir este viaje*, ver
:doc:`/17.0/5_operational-flows/5_2_trip-generation`) se queda en *En curso* con lo que ya
entregó hasta que alguien lo cierra con **Cerrar viaje repartido**, se revierte el reparto o
termina su día. Y un Viaje **cerrado por migración** es uno anterior al ciclo de despacho que la
actualización cerró sin tarificar ni bloquear su OC; su estado ya no se recalcula.

.. _viaje-validacion:

3.2.2.4 Despacho, validación y reversiones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La cabecera del Viaje muestra en cada estado **solo los botones que se pueden pulsar**, y cada
paso que se da a mano tiene su vuelta atrás.

.. list-table::
   :header-rows: 1
   :widths: 22 16 62

   * - Botón
     - Cuándo se ve
     - Qué hace
   * - **Despachar**
     - Planificado
     - Envía el Viaje a quien lo va a ejecutar (la app del conductor, la agencia por API, o el
       sistema de seguimiento externo mientras siga en medio) y deja Viaje, Paradas, Tramos y
       Órdenes en **Despachado**. Es el único camino a ese estado. El paso a paso, los canales y
       lo que pasa si falla están en :doc:`/17.0/5_operational-flows/5_4_app-execution`.
   * - **Reenviar**
     - Despachado, En curso
     - Vuelve a enviar las instrucciones al mismo destino, por ejemplo tras cambiar una Parada.
       Un reenvío que falla deja el error anotado y no deshace el despacho anterior.
   * - **Revertir despacho**
     - Despachado
     - Devuelve el Viaje a Planificado, sus Paradas a Planificada y sus Tramos a Validado, y pone
       la OC otra vez en borrador. Si el Viaje era de una agencia por API, antes le avisa con sus
       llamadas de cancelación; si la agencia no lo acepta, no se revierte. No existe en *En
       curso*: el conductor ya ha actuado.
   * - **Cancelar viaje**
     - Despachado, En curso
     - Saca del Viaje las Paradas que nadie ha servido, que vuelven a Sin planificar con sus
       Tramos en Validado (en agencia, con la cancelación correspondiente). Si no se sirvió
       ninguna, el Viaje y su OC desaparecen; si alguna se sirvió, el Viaje se queda con ellas y
       cierra con ellas, porque eso se paga. No hay un estado «cancelado».
   * - **Validar**
     - Por validar (y Completado con la OC sin confirmar)
     - Da por buena la ejecución: tarifica el coste, confirma y bloquea la OC, deja el Viaje en
       Completado y marca sus Órdenes para que la tarea programada las confirme. Exige el permiso
       **Validador de viajes**. Si el Proyecto exige prueba de entrega y alguna Orden no tiene
       firma ni albarán escaneado (una foto no cuenta), un validador recibe el error con las
       Órdenes que faltan y solo un responsable puede validar, dejando el motivo en el chatter.
   * - **Rechazar**
     - Por validar
     - Deja el Viaje marcado como rechazado, con el motivo en el chatter y un aviso en la ficha;
       opcionalmente avisa al transportista por correo a la dirección que se indique. No cambia
       el estado: el Viaje sigue Por validar hasta que se corrija y se valide.
   * - **Revertir validación**
     - Completado con la OC confirmada y sin facturar
     - Deshace la validación: la OC vuelve a solicitud de presupuesto con sus cantidades a cero y
       el Viaje vuelve a Por validar (o se reabre, si el Proyecto no pide revisión). Las Órdenes
       ya confirmadas no vuelven atrás. Es lo que antes hacía **Desbloquear**.
   * - **Cerrar viaje repartido**
     - Viaje repartido
     - Cierra el Viaje con lo que entregó: el cierre normal, con su tarificación y su OC.

Los botones **Bloquear**, **Desbloquear** y **Pasar a borrador** ya no están en la cabecera:
Validar y Revertir validación hacen su trabajo con el estado delante, y volver a borrador queda
como acción de servidor para responsables.

**Quién puede validar.** Los permisos del TMS forman una escalera: Usuario < **Validador de
viajes** < Responsable. El validador ve el menú **Tráfico › Viajes por validar**, una lista con
los Viajes en Por validar, la más antigua primero y en rojo a partir de tres días, y la pestaña
**Revisión** de la ficha, con la validación, el rechazo y las Órdenes sin prueba de entrega. El
indicador **Viajes por validar** del motor de indicadores (:doc:`/17.0/8_economic-administration/8_8_control-reporting`)
enseña cuántos esperan: si nadie valida, nadie factura.

**Qué pide revisión.** Lo decide el Proyecto, con los interruptores **Los viajes requieren
validación** y **La validación exige prueba de entrega** de
:doc:`/17.0/4_parametrization/4_5_project-configuration`. Activarlos afecta a los Viajes que
cierren a partir de ese momento; los ya cerrados no se recalculan. Sin el primero, el Viaje pasa
de En curso a Completado por sí solo, con la cadena de :doc:`/17.0/5_operational-flows/5_5_trip-closing`.

**Recursos bloqueados.** Desde que el Viaje se despacha, conductor, vehículo, remolques,
transportista y agencia pasan a solo lectura: son lo que se le ha dicho a la app, a la agencia y
al DeCA. Para cambiarlos en un Viaje despachado hay que revertir el despacho; en uno en curso o
cerrado solo puede un responsable, y el cambio queda anotado en el historial.

**Protección.** Un Viaje cuya OC esté **facturada** no se revierte, no se recalcula ni se borra.
Y si la OC está *Bloqueada* o *Cancelada*, el sistema la considera intocable e impide pasarla a
borrador; cuando eso afecta a la tarificación, el diagnóstico de tarifa del Viaje lo indica con
el motivo «Orden de compra bloqueada».

.. figure:: /_static/img/3_functional-architecture/3_2_2_trips_01_viaje.png
   :alt: Formulario de un Viaje con sus tres estados

   Formulario de un Viaje con sus estados operativo, de compra y de facturación.

.. CAPTURA: 3_2_2_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_2_trips_02_viajes-por-validar.png
      :alt: Lista Viajes por validar

      Tráfico › Viajes por validar: los Viajes que esperan revisión, la más antigua primero.

.. CAPTURA: 3_2_2_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_2_trips_03_revision.png
      :alt: Pestaña Revisión de un Viaje por validar

      Pestaña Revisión: validación, rechazo y Órdenes sin prueba de entrega.

3.2.2.5 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Campo de ``tms.trip``
   * - Estado operativo
     - ``state`` (``draft`` Sin Paradas, ``in_process`` Planificado, ``processed`` Despachado,
       ``running`` En curso, ``to_validate`` Por validar, ``completed``, ``failed``)
   * - Despacho
     - ``dispatch_date``, ``dispatch_channel`` (``app``, ``axylog``, ``agency_api``,
       ``manual``), ``dispatch_state`` (``sent``, ``error``), ``dispatch_error``;
       ``trip_sended`` indica si las instrucciones enviadas están al día
   * - Validación
     - ``requires_validation`` (del Proyecto), ``to_validate_since``, ``validation_date``,
       ``validated_by_id``, ``validation_rejected``, ``validation_reject_reason``,
       ``pod_missing_order_ids``
   * - Recursos bloqueados
     - ``resources_locked`` (calculado; solo en pantalla)
   * - Viaje repartido · cerrado por migración
     - ``tms_split_pending`` · ``tms_closed_by_migration``
   * - Permiso de validación
     - grupo ``tms.group_tms_trip_validator``
   * - Orden de compra vinculada
     - ``purchase_order_id``
   * - Estado de compra
     - ``po_state`` (el ``state`` de la OC: ``draft``, ``sent``, ``to approve``, ``purchase``,
       ``done``, ``cancel``)
   * - Estado de facturación
     - ``invoice_status`` (el de la OC: ``no``, ``to invoice``, ``invoiced``)
   * - Motivo «Orden de compra bloqueada»
     - valor ``purchase_order_blocked`` del diagnóstico de tarifa del Viaje (no es un campo)
