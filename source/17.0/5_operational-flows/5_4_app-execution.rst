5.4 Ejecución desde la app
--------------------------

.. admonition:: Dónde ocurre
   :class: tip

   En la **app móvil del conductor**, no en el backend de Odoo. Las pantallas y el uso paso a
   paso están en el :doc:`Manual del conductor </17.0/10_manual_app/index>`; aquí se explica
   qué le llega al conductor y qué hace cada evento suyo en el TMS.

5.4.1 Enviar el Viaje a la app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El conductor no ve todos los Viajes que tiene asignados, sino los que el planificador ha
**enviado**. El botón **Enviar a la app** del Viaje (``tms.trip``) exige que tenga conductor,
pasa el Viaje a **Procesado** y lo comunica al sistema de seguimiento externo configurado
para la compañía; sin ese punto de conexión el envío no se completa. La app, al iniciar sesión
o al refrescar, carga el
Viaje **procesado más reciente** del conductor con todo lo que necesita para trabajar sin
conexión: las Paradas en orden con sus Tramos, líneas, Bultos y Reembolsos; los perfiles de la
app y sus motivos de incidencia (ver :doc:`/17.0/4_parametrization/4_5_project-configuration`);
las coordenadas y el trazado; y las métricas del recorrido.

5.4.2 El ciclo de una Parada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El conductor avanza Parada a Parada. En cada una, la app registra el mismo ciclo: la Parada
está en espera, el conductor indica que va en camino, al llegar la pone en curso y, al
terminar, registra el **resultado**. Estos pasos intermedios son los estados de la app, que se
listan en la tabla de 5.4.4. El resultado depende de lo que se hace en la Parada:

- En una **carga** (recogida, recogida a domicilio o paso por hub), la mercancía queda cargada,
  cargada con reservas o no cargada (tabla de 5.4.4). Los Bultos se comprueban escaneando (ver
  :doc:`/17.0/1_introduction/1_4_technological-architecture`).
- En una **entrega**, la Parada queda **Completada**, **Con reservas** o **Fallida** (ver
  :term:`Estados de la Parada`). La app pide la :term:`prueba de entrega (POD) <POD>` (firma en
  pantalla o foto del albarán firmado), el motivo cuando hay reservas o la entrega falla, el
  cobro del Reembolso si lo hay, y permite comentarios y fotos.
- En una **Parada de hub**, se registra la entrada o la salida de la mercancía del hub.

Una Parada puede agrupar Tramos de varias Órdenes. El resultado se aplica a la Parada y, salvo
que el conductor lo indique Tramo a Tramo, a todos sus Tramos que no estuvieran ya cerrados.

5.4.3 Qué hace cada evento en el TMS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada evento de la app llega a Odoo y se guarda como un apunte de :term:`Trazabilidad` sobre la
entidad afectada (Parada, Tramo, Bulto o reembolso) con todo su contexto: fecha y hora,
conductor, coordenadas y precisión del GPS, dispositivo y sistema operativo, batería, tipo de
red, motivo, comentario, importe cobrado y adjuntos. A partir de ese apunte el sistema
actualiza la estructura, en este orden:

#. La **Parada** toma el estado que corresponde al evento y lo hereda cada uno de sus **Tramos**
   que no estuviera ya en un estado de cierre.
#. La **Orden** refleja el estado de su tramo activo (ver
   :doc:`/17.0/3_functional-architecture/3_2_5_active-leg`): el planificador ve avanzar la
   Orden sin que nadie la toque.
#. El **Viaje** recalcula su estado a partir de sus Paradas; cuando la última se cierra, arranca
   el cierre (:doc:`5_5_trip-closing`).
#. Si hay integraciones de salida configuradas, el evento se envía al sistema del cliente
   (:doc:`Guía del integrador </17.0/7_edi-integrations/index>`).

Si el mismo evento llega dos veces (la app reintenta cuando no tiene cobertura), se procesa
una sola. Si Odoo rechaza un evento por una regla de negocio, la app se lo dice al conductor
en el momento.

.. CAPTURA: 5_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_4_app-execution_01_paradas-estado-app.png
      :alt: Lista de Paradas con el estado que envía la app

      Las Paradas, en el backend de Odoo, con el estado que llega desde la app.

5.4.4 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

La Parada tiene dos campos de estado. El **estado de la Parada** (``state`` de ``tms.stop``) es
el del glosario: los estados abiertos y los seis de cierre, que se describen en
:doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`. El **estado de la app**
(``app_state``) registra el paso en que está el conductor dentro de la Parada y el resultado
que ha reportado; es el que llega con cada evento y del que el sistema deriva el estado de la
Parada. Estos son los estados de la app y cómo se nombran en esta documentación:

.. list-table::
   :header-rows: 1
   :widths: 22 30 48

   * - Código
     - Etiqueta en Odoo
     - Nombre en la documentación
   * - ``standby``
     - Modo de espera
     - En espera
   * - ``on_way``
     - En camino
     - En camino
   * - ``running``
     - En curso
     - En curso
   * - ``lo_ok``
     - Cargado
     - Cargada
   * - ``lo_ok_reserve``
     - Reserva cargada
     - Cargada con reservas
   * - ``lo_failed``
     - No cargado
     - No cargada
   * - ``ok``
     - Completada
     - Completada
   * - ``ok_reserve``
     - Con reservas
     - Con reservas
   * - ``failed``
     - Fallida
     - Fallida
