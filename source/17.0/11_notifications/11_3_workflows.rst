11.3 Flujos de aviso
--------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Avisos › **Workflows** (los crean y cambian los responsables; los
   usuarios del TMS los ven)

.. CAPTURA: 11_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/11_notifications/11_3_workflows_01_flujo.png
      :alt: Ficha de un flujo de aviso con sus grupos Cuándo, Quién, Cómo y Restricción

      Un flujo de aviso: cuándo, a quién, por qué canal y con qué límites.

Un :term:`Flujo de aviso` (``tms.notify.workflow``) es un aviso configurado: uno por cada cosa que
se quiere decir a alguien. «Entregado, al Destinatario, por WhatsApp o SMS» es un flujo; «el día
anterior, al Destinatario, por correo, solo en el Proyecto X» es otro. El módulo no trae ninguno
creado: el implantador crea los que el cliente quiera, con las plantillas de serie como ejemplo.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - **Cuándo**: Disparador
     - Cuál de los quince momentos lo lanza (:doc:`11_1_what-it-is`). Según el disparador
       aparecen sus ajustes: los minutos de **ETA dentro de (min)** (30), la hora de **El día
       anterior a las** (18:00), del **Lote a las** y las **Repeticiones cada hora** de Viaje
       iniciado (20:00 y dos más), del **Barrido de reembolsos a las** (9:00), o los **Tipos de
       POD** que cuentan como prueba de entrega (por defecto, solo la firma).
   * - **Cuándo**: Condición
     - Un filtro adicional sobre la Parada: solo entregas, solo con Reembolso, solo de un tipo de
       Orden. La Parada tiene que cumplirlo además del disparador.
   * - **Quién**: Rol del destinatario
     - **Destinatario** (el contacto de la Parada; si no tiene móvil, teléfono ni correo, el
       contacto de entrega de la Orden), **Cliente** (el que encargó la Orden) o **Seguidores
       internos** (los seguidores de la Parada).
   * - **Quién**: Proyectos
     - Solo las Órdenes de esos Proyectos. Vacío, todos. Es la forma de tener avisos distintos por
       cliente, y de probar un flujo nuevo en un solo Proyecto.
   * - **Cómo**: Política de canal
     - **El preferido y, si falla, el alternativo**: el canal preferido del contacto, si se puede
       usar; si no, el primero utilizable en este orden: WhatsApp, SMS, correo. Un solo mensaje.
       **Solo WhatsApp**, **Solo SMS**, **Solo correo**: ese canal o nada. **Todos los canales
       disponibles**: un mensaje por cada canal utilizable.
   * - **Cómo**: Plantillas de SMS, de correo y de WhatsApp
     - Una por canal. Un canal sin plantilla no se usa en este flujo.
   * - **Cómo**: Enlace de seguimiento
     - Si el aviso lleva el enlace personal de seguimiento. Hoy la página que abre no existe
       (:doc:`11_1_what-it-is`): mejor desmarcarlo.
   * - **Restricción**: No repetir durante (min)
     - El mismo disparador no se envía dos veces al mismo destinatario sobre la misma Parada en
       ese tiempo (240 minutos por defecto), sea por el canal que sea. Solo cuentan los avisos que
       salieron o están saliendo: uno que falló o se omitió no impide el siguiente. Para
       Reembolso pendiente, 1.440 minutos o más.
   * - **Restricción**: Silencio desde, Silencio hasta, y qué hacer
     - El horario en que no se molesta al Destinatario (de 21:00 a 8:00 por defecto), en **su**
       zona horaria. Lo que caiga dentro se **retiene hasta que cierre la ventana** o se
       **omite**. El lote de Viaje iniciado no lo respeta: sus horas las fija el propio flujo.

11.3.1 Las plantillas
~~~~~~~~~~~~~~~~~~~~~

Las plantillas son las de Odoo (SMS, correo, WhatsApp) sobre la **Parada**, porque desde la Parada
se llega a todo: la Orden, el Tramo, el Viaje, el ETA, la franja, el conductor y el Reembolso.
Para que no haya que saber cómo se llega, la Parada ofrece estos campos ya preparados:

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Campo
     - Qué pone
   * - ``notify_recipient_name``
     - El nombre del destinatario.
   * - ``notify_order_ref``
     - La referencia de la Orden.
   * - ``notify_eta_local``, ``notify_window_local``
     - El ETA y la franja de entrega, en la hora local de la entrega.
   * - ``notify_refund_amount_text``
     - El importe del Reembolso, con su moneda.
   * - ``notify_tracking_url``
     - El enlace de seguimiento.
   * - ``notify_driver_first_name``
     - El nombre de pila del conductor.
   * - ``notify_company_brand_name``
     - El nombre del remitente de la marca de la compañía
       (:ref:`17.0/4_parametrization/4_1_operational-configuration:4.1.7 Marca de la compañía`).

Vienen de serie cinco plantillas de SMS y cinco de correo (envío planificado, envío en ruta, es la
siguiente entrega, entregado, entrega no realizada) y cuatro de WhatsApp en borrador. Son un
ejemplo trabajado: se copian y se adaptan. **Una plantilla sirve para todos los idiomas**: su
texto se traduce como cualquier texto de Odoo y se elige al enviar según el idioma del contacto;
**Idioma de los avisos**, en el contacto, decide además el formato de las fechas y horas.
