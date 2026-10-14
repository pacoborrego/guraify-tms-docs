11.7 Referencia técnica
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Concepto
     - Modelo, campo o dato
   * - Módulos
     - ``tms_notify`` (depende de ``tms``, ``tms_kpi``, ``mail``, ``sms``): el motor y los canales
       de correo y SMS. ``tms_notify_whatsapp`` (depende de ``tms_notify`` y ``whatsapp``,
       Enterprise): el canal WhatsApp. ``sms_esendex`` (depende solo de ``sms``): Esendex como
       proveedor de SMS de toda la base
   * - Flujo de aviso
     - ``tms.notify.workflow``: ``trigger``, ``condition_domain``, ``recipient_role``,
       ``project_ids``, ``channel_policy``, ``sms_template_id``, ``mail_template_id``,
       ``wa_template_id`` (con WhatsApp), ``include_tracking_link``, ``dedupe_window_min``,
       ``quiet_hours_from``, ``quiet_hours_to``, ``quiet_hours_action``
   * - Aviso
     - ``tms.notify.message``: ``trigger``, ``channel``, ``stop_id``, ``sale_order_id``,
       ``trip_id``, ``partner_id``, ``to``, ``state``, ``skip_reason``, ``error``,
       ``scheduled_at``, ``sent_at``; en la Orden, ``tms_notify_message_ids``
   * - Enlace de seguimiento
     - ``tms.tracking.token``: ``token``, ``url`` (``https://<dominio de la marca>/t/<token>``),
       ``expires_at`` (30 días desde la fecha de la entrega), ``revoked``, ``access_count``,
       ``last_access_at``
   * - Contacto
     - ``res.partner``: ``tms_notify_channel_preferred``, ``tms_notify_lang``,
       ``tms_whatsapp_opt_in`` (+ ``_date``, ``_source``), ``tms_sms_opt_in``; lista negra nativa
       ``phone.blacklist``
   * - Campos para las plantillas
     - ``tms.stop``: ``notify_recipient_name``, ``notify_recipient_mobile``,
       ``notify_recipient_email``, ``notify_order_ref``, ``notify_eta_local``,
       ``notify_window_local``, ``notify_refund_amount_text``, ``notify_tracking_url``,
       ``notify_driver_first_name``, ``notify_company_brand_name`` (calculados, no se guardan)
   * - Lista blanca de pruebas
     - Parámetro del sistema ``tms_notify.allowlist``
   * - Tareas programadas
     - «TMS: send the notification queue» (cada minuto: envía la cola y libera lo retenido);
       «TMS: dispatch the time-based notifications» (cada 5 minutos: el día anterior, ETA dentro
       de N minutos, el lote de Viaje iniciado y el barrido de reembolsos); «Esendex: poll SMS
       delivery status» (cada 10 minutos)
   * - Indicadores
     - ``notify_queue_stuck`` (Avisos atascados en cola), ``notify_sent`` (Avisos enviados)
   * - Esendex
     - ``res.company``: ``sms_provider``, ``sms_esendex_account_reference``,
       ``sms_esendex_username``, ``sms_esendex_password`` (solo administradores del sistema),
       ``sms_esendex_sender``, ``sms_esendex_character_set``, ``sms_esendex_endpoint``; el
       identificador de cada SMS en Esendex se guarda en ``sms.tracker``
   * - Desactivar los avisos en un proceso
     - Contexto ``skip_tms_notify``

Campos y disparadores, uno a uno, en :doc:`/17.0/annexes/A_33_avisos`.
