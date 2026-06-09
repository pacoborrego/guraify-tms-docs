7.5 Webhooks
============

Los webhooks permiten que sistemas externos notifiquen eventos al TMS de forma activa,
sin que este tenga que consultarlos. Son el canal idóneo para actualizaciones de estado
que se producen en origen y deben reflejarse en el TMS de inmediato.

Ruta de recepción
-----------------

Las notificaciones se reciben en la ruta pública ``/tms_int/webhook/<route_code>``, que
acepta peticiones POST, GET, PUT y DELETE. El segmento ``route_code`` identifica el
webhook concreto que debe atender la petición.

Configuración
-------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Endpoints API

.. CAPTURA: 7_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_5_webhooks_01_endpoint-webhook.png
      :alt: Endpoint configurado como webhook

      Endpoint configurado como webhook.

Un webhook se configura sobre un Endpoint (``tms_int.api.endpoint``) marcado como tal.
Tres campos lo definen: ``is_webhook``, que lo habilita; ``webhook_route``, el
identificador único que aparece en la ruta; y ``webhook_secret``, el secreto compartido
que autentica al emisor.

Procesamiento
-------------

Al recibir una petición, el sistema localiza el endpoint por su ``webhook_route`` y
valida el secreto, que el emisor envía en la cabecera ``X-Webhook-Secret`` o como
parámetro. Si la validación es correcta, parsea el JSON recibido y el tratamiento
depende del contenido del evento: si corresponde a una **Orden**, se encamina a la
Bandeja de Entrada (``tms_int.api.inbox``) y sigue el mismo circuito de validación y
materialización que la ingesta API (ver :doc:`7_3_api-integrations`); en el resto de
casos, ejecuta ``response_mapper_code`` para crear o actualizar los registros
correspondientes, con la misma mecánica de mapeo de respuesta empleada en los
endpoints salientes (ver :doc:`7_4_endpoint-configuration`).

Trazabilidad y códigos de respuesta
------------------------------------

Cada recepción se registra en ``tms.api.log`` con ``api_type = in_api``, guardando las
cabeceras, los *payloads*, el código HTTP devuelto y la IP de origen. El servicio
responde con códigos HTTP estándar según el resultado: ``200`` cuando el procesamiento
es correcto, ``401`` si el secreto no es válido, ``404`` si la ruta no existe o está
inactiva, ``400`` ante una petición mal formada y ``500`` ante un error interno.
