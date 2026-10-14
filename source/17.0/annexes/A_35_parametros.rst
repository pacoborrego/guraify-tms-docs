A.35 Parámetros del sistema
===========================

.. admonition:: Ruta en Odoo
   :class: tip

   Ajustes › Técnico › Parámetros del sistema (modo desarrollador; solo administradores)

Los parámetros del sistema son ajustes de la base que no tienen pantalla propia: se crean o se
cambian en la lista de parámetros, con su clave y su valor, y valen para toda la base. Si un
parámetro no existe, se usa el valor por defecto de la tabla. Se tocan poco y con conocimiento:
la mayoría son frenos de rendimiento o interruptores de transición.

.. list-table::
   :header-rows: 1
   :widths: 36 14 50

   * - Clave
     - Por defecto
     - Qué cambia
   * - ``tms_app.enforce_token``
     - ``0``
     - Con ``1``, la app no puede llamar a Odoo sin el token de su dispositivo
       (:ref:`17.0/4_parametrization/4_1_operational-configuration:4.1.9 Conductores y acceso a la app`).
       Se activa cuando todos los teléfonos tienen una versión que lo envía.
   * - ``tms_app.partial_delivery_guard_enabled``
     - ``1``
     - Que un Tramo con Bultos sin reportar no se cierre como entregado sino con reservas
       (:doc:`/17.0/5_operational-flows/5_4_app-execution`). ``0`` lo apaga.
   * - ``tms_app.partial_delivery_reason_id``
     - motivo A17
     - El motivo (su id) que se pone en ese caso.
   * - ``tms_app.trip_slim_min_version``
     - ``1.9``
     - Desde qué versión de la app se envía el Viaje en el formato ligero; las anteriores siguen
       recibiendo el completo.
   * - ``tms_app.tower_platforms``, ``tms_app.tower_outcome_guard_enabled``,
       ``tms_app.tower_outcome_dedup_minutes``
     - ``Axylog``, ``1``, ``15``
     - Protección contra los resultados que una torre de control externa (Axylog) vuelve a
       reportar sobre lo que el TMS ya le envió: no se duplican dentro de esos minutos.
   * - ``tms_notify.allowlist``
     - vacío
     - Lista blanca de pruebas de los avisos: con valor, solo se avisa a esos móviles y correos
       (:doc:`/17.0/11_notifications/11_6_go-live`).
   * - ``tms_int.telematics_position_min_gap_s``
     - ``120``
     - Segundos mínimos entre dos posiciones aceptadas del mismo Viaje (:doc:`/17.0/7_edi-integrations/7_8_telematics`).
   * - ``tms_int.telematics_retention_days``
     - ``90``
     - Días que se guardan las lecturas de telemática.
   * - ``tms.tacho_freshness_minutes``
     - ``60``
     - Antigüedad máxima del dato de tacógrafo para usarlo al planificar las pausas.
   * - ``tms.eta_history_retention_days``
     - ``180``
     - Días que se guarda el histórico de ETA de las Paradas.
   * - ``tms.portal_audience_months``
     - ``24``
     - Meses hacia atrás que cuentan para que una empresa sea transportista
       (:doc:`/17.0/7_edi-integrations/7_9_external-access`).
   * - ``tms_maintenance.odometer_stale_days``
     - ``30``
     - Días sin lectura de odómetro a partir de los cuales una unidad cuenta como «sin lectura
       reciente» (:doc:`/17.0/6_resources/6_7_kpis`).
   * - ``tms.tariff_cron_batch_limit``, ``tms.tariff_cron_time_budget``
     - ``40``, ``120``
     - Cuántas Órdenes o Viajes tarifica cada pasada de la tarea de tarificación y cuántos
       segundos puede durar (:doc:`/17.0/7_edi-integrations/7_6_automated-actions`).
   * - ``tms.label_batch_chunk``
     - ``50``
     - Cuántas etiquetas se generan en cada bloque al imprimir un lote grande
       (:doc:`/17.0/5_operational-flows/5_9_labels`).
   * - ``tms_int.tracking.api_log_enabled``, ``tms_int.tracking.api_log_max_chars``
     - ``1``, ``20000``
     - Si las consultas de seguimiento por API quedan en el registro de actividad, y cuántos
       caracteres de la respuesta se guardan.
   * - ``tms_deca.allow_insecure_url``
     - vacío
     - Permite emitir DeCA en una base sin https. Solo para copias locales y pruebas, nunca en
       producción.
   * - ``tms_map.token_ptv``
     - vacío
     - Token de PTV de respaldo para las compañías que no tienen el suyo
       (:doc:`/17.0/1_introduction/1_4_technological-architecture`). Lo normal es el de la
       compañía.
