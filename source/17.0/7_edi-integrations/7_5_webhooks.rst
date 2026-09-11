7.5 Webhooks
============

Los webhooks permiten que sistemas externos notifiquen eventos al TMS de forma activa,
sin que este tenga que consultarlos. Son el canal idóneo para actualizaciones de estado
que se producen en origen y deben reflejarse en el TMS de inmediato.

7.5.1 Dirección de recepción
----------------------------

Las notificaciones se reciben en la dirección pública ``/tms_int/webhook/<route_code>``,
que acepta peticiones POST, GET, PUT y DELETE. El segmento ``<route_code>`` es el valor
del campo de dirección del webhook (``webhook_route``, ver más abajo) del Endpoint que
debe atender la petición.

7.5.2 Configuración
-------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Endpoints API

.. CAPTURA: 7_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_5_webhooks_01_endpoint-webhook.png
      :alt: Endpoint configurado como webhook

      Endpoint configurado como webhook.

Un webhook se configura sobre un Endpoint (``tms_int.api.endpoint``) marcado como tal.
Tres campos lo definen: ``is_webhook``, que lo habilita; ``webhook_route``, el
identificador único que forma el último segmento de la dirección; y ``webhook_secret``,
el secreto compartido que autentica al emisor.

7.5.3 Procesamiento
-------------------

Al recibir una petición, el sistema localiza el Endpoint activo cuyo ``webhook_route``
coincide con el segmento de la dirección y valida el secreto, que el emisor envía en la
cabecera ``X-Webhook-Secret`` o como parámetro. Si la validación es correcta, parsea el
JSON recibido y el tratamiento depende del contenido del evento: si corresponde a una
**Orden**, se encamina a la Bandeja de entrada API y sigue el mismo circuito de validación
y materialización que la ingesta API (ver :doc:`7_3_api-integrations`); en el resto de
casos, ejecuta ``response_mapper_code`` para crear o actualizar los registros
correspondientes, con la misma mecánica de mapeo de respuesta empleada en los
endpoints salientes (ver :doc:`7_4_endpoint-configuration`).

7.5.4 Trazabilidad y códigos de respuesta
-----------------------------------------

Cada recepción se registra como entrada en el registro de actividad de las APIs
(:doc:`7_7_integration-best-practices`), con la IP de origen. Este punto de conexión lo
atiende Odoo directamente, no la pasarela, por eso su contrato va aquí: el servicio
responde con códigos HTTP estándar según el resultado, ``200`` cuando el procesamiento es
correcto, ``401`` si el secreto no es válido, ``404`` si la dirección no existe o está
inactiva, ``400`` ante una petición mal formada y ``500`` ante un error interno.
