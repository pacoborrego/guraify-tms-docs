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
pasa el Viaje a **Procesado** y lo comunica al sistema de seguimiento externo configurado en la
compañía. La app, al iniciar sesión o al refrescar, carga el Viaje **procesado más reciente**
del conductor con todo lo que necesita para trabajar sin conexión: las Paradas en orden con
sus Tramos, líneas, Bultos y reembolsos; los perfiles de la app y los motivos de incidencia del
Proyecto; las coordenadas y el trazado; y las métricas de la ruta.

5.4.2 El ciclo de una Parada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El conductor avanza parada a parada. En cada una, la app registra el mismo ciclo: la parada
está **en espera**, el conductor indica que va **en camino**, al llegar la pone **en curso** y,
al terminar, registra el **resultado**. El resultado depende de lo que se hace en la parada:

- En una **carga** (recogida, recogida a domicilio o paso por hub), la mercancía queda
  **Cargada**, **Cargada con reservas** o **No cargada**. Los Bultos se comprueban escaneando
  (ver :ref:`17.0/1_introduction/1_4_technological-architecture:1.4.5 La app del conductor y el escaneo`).
- En una **entrega**, la parada queda **Completada**, **Con reservas** o **Fallida**. La app
  pide la prueba de entrega (firma en pantalla o foto del albarán firmado), el motivo cuando
  hay reservas o fallo, el cobro del reembolso si lo hay, y permite comentarios y fotos.
- En una **parada de hub**, se registra la entrada o la salida de la mercancía del hub.

Una parada puede agrupar Tramos de varias Órdenes. El resultado se aplica a la parada y, salvo
que el conductor lo indique tramo a tramo, a todos sus Tramos que no estuvieran ya cerrados.

5.4.3 Qué hace cada evento en el TMS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada evento de la app llega a Odoo y se guarda como un apunte de :term:`Trazabilidad` sobre la
entidad afectada (Parada, Tramo, Bulto o reembolso) con todo su contexto: fecha y hora,
conductor, coordenadas y precisión del GPS, dispositivo y sistema operativo, batería, tipo de
red, motivo, comentario, importe cobrado y adjuntos. A partir de ese apunte el sistema
actualiza la estructura, en este orden:

#. La **Parada** toma el estado que corresponde al evento y lo hereda cada uno de sus **Tramos**
   que no estuviera ya en un estado final.
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

.. figure:: /_static/img/5_operational-flows/5_8_kpi-indicators_01_kpi-parada.png
   :alt: Lista de Paradas con el estado que envía la app

   Las Paradas, en el backend, con el estado que llega desde la app.

5.4.4 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

Estados que la app envía a la Parada (campo ``app_state`` de ``tms.stop``) y cómo se nombran
en esta documentación:

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
     - Ok
     - Completada
   * - ``ok_reserve``
     - Reservista
     - Con reservas
   * - ``failed``
     - Fallo
     - Fallida
