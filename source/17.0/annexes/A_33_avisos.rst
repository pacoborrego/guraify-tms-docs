A.33 Avisos al Destinatario
===========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Avisos › Workflows · Mensajes enviados · Enlaces de seguimiento ·
   Ajustes › Ajustes generales › Contactos › Enviar SMS

Módulos ``tms_notify``, ``tms_notify_whatsapp`` y ``sms_esendex``. Cómo se usan:
:doc:`/17.0/11_notifications/index`.

A.33.1 Disparadores
-------------------

.. list-table::
   :header-rows: 1
   :widths: 26 22 52

   * - Disparador
     - Código
     - Qué lo lanza
   * - Orden recibida
     - ``order_received``
     - Se crea la Parada de la Orden.
   * - Planificado para una fecha
     - ``order_planned``
     - La Parada se crea dentro de un Viaje o se le asigna uno.
   * - Viaje iniciado
     - ``trip_started``
     - Lote diario a la hora del flujo sobre los Viajes despachados ese día, con repeticiones
       horarias; nadie recibe dos veces el aviso del mismo Viaje.
   * - Eres el siguiente
     - ``next_stop``
     - Se cierra una Parada: al Destinatario de la siguiente del Viaje.
   * - ETA dentro de N minutos
     - ``eta_within``
     - Cada 5 minutos, las Paradas abiertas cuyo ETA (no caducado) está a menos de N minutos.
   * - Vehículo llegado
     - ``arrived``
     - La Parada pasa a En curso.
   * - Entregado
     - ``delivered_ok``
     - La Parada se cierra completada.
   * - Entregado con reservas
     - ``delivered_reserve``
     - La Parada se cierra con reservas.
   * - Orden Fallida
     - ``failed``
     - La Parada se cierra fallida.
   * - Reprogramado
     - ``rescheduled``
     - La Parada se reprograma.
   * - Devuelto
     - ``returned``
     - La Parada se cierra devuelta.
   * - Dirección cambiada
     - ``address_changed``
     - Cambia el contacto (la dirección) de la Parada.
   * - El día anterior
     - ``day_before``
     - A la hora del flujo, las Paradas abiertas con fecha del día siguiente.
   * - Reembolso pendiente
     - ``refund_pending``
     - Barrido diario a la hora del flujo: Paradas abiertas cuyo Tramo lleva un Reembolso con
       importe sin cobrar.
   * - Prueba de entrega disponible
     - ``pod_available``
     - La app sube un adjunto de uno de los tipos del flujo (``PODSignature`` la firma,
       ``PODScanDoc`` el documento escaneado; ``PhotoModal`` es una foto y no cuenta).

Las horas de los disparadores por reloj se leen en la zona horaria de la compañía.

A.33.2 Flujo de aviso
---------------------

Modelo ``tms.notify.workflow``.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Cómo se llama el flujo, por ejemplo «Entregado: avisa al Destinatario».
   * - Disparador
     - Selección
     - Uno de los quince de A.33.1.
   * - ETA dentro de (min)
     - Número
     - Para ETA dentro de N minutos; 30 por defecto.
   * - El día anterior a las
     - Hora
     - Para El día anterior; 18:00 por defecto.
   * - Lote a las / Repeticiones cada hora
     - Hora / Número
     - Para Viaje iniciado; 20:00 y 2 por defecto (20:00, 21:00 y 22:00).
   * - Barrido de reembolsos a las
     - Hora
     - Para Reembolso pendiente; 9:00 por defecto.
   * - Tipos de POD
     - Texto
     - Para Prueba de entrega disponible: los tipos de adjunto que cuentan, separados por comas;
       ``PODSignature`` por defecto. El sistema rechaza un tipo que no existe.
   * - Condición
     - Filtro
     - Condición adicional sobre la Parada.
   * - Rol del destinatario
     - Selección
     - Destinatario, Cliente o Seguidores internos.
   * - Proyectos
     - Relación
     - Limita el flujo a las Órdenes de esos Proyectos; vacío, todos.
   * - Compañía
     - Relación
     - La compañía del flujo.
   * - Política de canal
     - Selección
     - El preferido y, si falla, el alternativo · Solo WhatsApp · Solo SMS · Solo correo ·
       Todos los canales disponibles.
   * - Plantilla de SMS / de correo / de WhatsApp
     - Relación
     - Una por canal, todas sobre la Parada. La de WhatsApp, solo con ``tms_notify_whatsapp``.
   * - Enlace de seguimiento
     - Sí/No
     - Si el aviso lleva el enlace personal de seguimiento; marcado por defecto.
   * - No repetir durante (min)
     - Número
     - 240 por defecto. Cuenta todos los canales.
   * - Silencio desde / Silencio hasta
     - Hora
     - 21:00 y 8:00 por defecto. Iguales, sin horario de silencio.
   * - Acción en horario de silencio
     - Selección
     - Retener hasta que cierre la ventana (por defecto) u Omitir el mensaje.
   * - Último despacho
     - Fecha (solo lectura)
     - La última vez que el flujo lanzó avisos.

A.33.3 Aviso (Mensajes enviados)
--------------------------------

Modelo ``tms.notify.message``.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Flujo, Disparador, Canal
     - Relación / Selección
     - De qué flujo sale, qué lo disparó y por qué canal (SMS, correo, WhatsApp).
   * - Contacto, Enviado a
     - Relación / Texto
     - A quién y a qué número o correo.
   * - Orden, Parada, Viaje
     - Relación
     - Sobre qué entrega.
   * - Estado
     - Selección
     - En cola, Retenido, Enviado, Entregado, Leído, Respondido, Fallido, Omitido.
   * - Motivo de omisión
     - Selección
     - Sin destinatario, Sin teléfono ni correo, Ningún canal utilizable, Sin consentimiento,
       Número en lista negra, Baja voluntaria, Ya avisado, Horario de silencio, Canal no
       instalado, No está en la lista blanca de pruebas, Error del canal.
   * - Error
     - Texto
     - Lo que respondió el canal cuando falló.
   * - Programado, Enviado
     - Fecha
     - Cuándo debe salir (los retenidos) y cuándo salió.

A.33.4 Contacto (grupo AVISOS)
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Canal preferido
     - Selección
     - WhatsApp, SMS, Correo o No avisar.
   * - Idioma de los avisos
     - Selección
     - Formato de fechas y horas de los avisos.
   * - Consentimiento WhatsApp
     - Sí/No
     - Obligatorio para recibir WhatsApp. Al marcarlo se guardan su **fecha** y su **origen**.
   * - Consentimiento SMS
     - Sí/No
     - Marcado por defecto; desmarcado, el contacto no recibe SMS.

A.33.5 Esendex (Ajustes › Enviar SMS)
-------------------------------------

Etiquetas en inglés en la interfaz.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - SMS Provider
     - Selección
     - Send via Odoo (el servicio de pago de Odoo) o Send via Esendex.
   * - Esendex Account Reference
     - Texto
     - La referencia de cuenta que da Esendex (EX0123456).
   * - Esendex User / Esendex API Password
     - Texto
     - Usuario y contraseña de la API (no la del portal web). La contraseña solo la ven los
       administradores del sistema.
   * - Esendex Sender
     - Texto
     - El remitente; con letras, 11 caracteres como mucho. Vacío, el de la cuenta.
   * - Esendex Character Set
     - Selección
     - Auto (recomendado), GSM o Unicode.
   * - Esendex Endpoint
     - Texto
     - La dirección de la API; solo se cambia si lo pide Esendex.
