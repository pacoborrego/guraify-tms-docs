11.2 Canales: correo, SMS y WhatsApp
------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Correo: Ajustes › Ajustes generales › servidores de correo saliente · SMS: Ajustes › Ajustes
   generales › bloque **Contactos** › **Enviar SMS** · WhatsApp: aplicación WhatsApp de Odoo
   (Enterprise)

Un flujo de aviso no envía por su cuenta: usa los canales de Odoo. Cada canal necesita su
configuración, que se hace una vez por compañía y que este apartado resume. Un canal que no está
listo no rompe nada: el aviso queda omitido con el motivo (**Canal no instalado**, **Ningún canal
utilizable**) y, si el flujo lo permite, sale por el siguiente.

11.2.1 Correo
~~~~~~~~~~~~~

El correo sale por el servidor de correo saliente de Odoo, como cualquier otro correo del sistema,
con las plantillas de correo del flujo. Es el canal que siempre existe, y por eso es el último que
se prueba cuando el flujo deja elegir. Necesita que el Destinatario tenga correo.

.. _sms-esendex:

11.2.2 SMS con Esendex
~~~~~~~~~~~~~~~~~~~~~~

Sin más, Odoo envía los SMS por su propio servicio de pago, que necesita crédito comprado a Odoo.
Para enviarlos por **Esendex** se instala el módulo ``sms_esendex``, que añade Esendex como
proveedor al bloque **Enviar SMS** de los Ajustes. Elegido Esendex para una compañía, **todo** SMS
de esa compañía sale por Esendex: los avisos y cualquier otro SMS de Odoo.

.. CAPTURA: 11_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/11_notifications/11_2_channels_01_esendex.png
      :alt: Bloque Enviar SMS de los Ajustes con Esendex como proveedor

      Enviar SMS con Esendex: cuenta, usuario, contraseña de la API, remitente y prueba de las
      credenciales.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Proveedor (**Send via Esendex**)
     - Que los SMS de la compañía salgan por Esendex y no por el servicio de Odoo.
   * - Referencia de cuenta, usuario y contraseña de la API
     - Los datos que da Esendex. La contraseña es **la de la API, no la del portal web**, y solo
       la ven los administradores del sistema.
   * - Remitente
     - Lo que el Destinatario ve como remitente. Un remitente con letras tiene como mucho 11
       caracteres y suele haber que registrarlo antes en Esendex; vacío, el de la cuenta.
   * - Juego de caracteres
     - Dejarlo en **Auto**: usa el juego normal salvo que el texto necesite Unicode, que reduce a
       la mitad los caracteres de cada SMS.

El botón **Test the credentials** comprueba usuario y contraseña con Esendex **sin enviar ni
gastar un mensaje**. Los acuses de entrega no llegan solos: la tarea programada «Esendex: poll SMS
delivery status» pregunta a Esendex cada 10 minutos por los SMS enviados y marca los entregados.
Estos campos salen en inglés en la interfaz.

``sms_esendex`` **no puede convivir con otro módulo de proveedor de SMS** (el de Twilio de Odoo):
los dos declaran el mismo selector de proveedor. Hay que elegir uno.

11.2.3 WhatsApp
~~~~~~~~~~~~~~~

WhatsApp es de **Odoo Enterprise**: necesita la aplicación WhatsApp de Odoo y el módulo
``tms_notify_whatsapp``. Sin ellos, el resto de los avisos funciona igual y un flujo puesto en
WhatsApp deja sus mensajes omitidos con **Canal no instalado**.

Lo que pide Meta, en orden:

#. Una **cuenta de WhatsApp Business** (WABA) de la compañía, con un **número registrado y
   verificado en ella**, y un **token permanente** de un usuario de sistema de Meta. Se dan de
   alta en la cuenta de WhatsApp de Odoo; su botón de probar la conexión comprueba que el número
   pertenece a la cuenta.
#. Las **plantillas aprobadas por Meta**. El módulo trae cuatro en borrador (envío planificado,
   es la siguiente entrega, entregado, entrega no realizada), con la categoría **utilidad**. Hay
   que enviarlas a aprobación desde Odoo; la aprobación tarda minutos. Una plantilla vive en una
   cuenta concreta: si se cambia de cuenta, hay que volver a aprobarlas.
#. El **consentimiento** de cada Destinatario (:doc:`11_4_recipient`): sin él no sale ningún
   WhatsApp.

Tres reglas de Meta que Odoo no comprueba y que solo aparecen al enviar a aprobación o al enviar:

- El texto de una plantilla **no puede empezar ni acabar en una variable**; un punto suelto
  después de la última no cuenta como texto. Hay que cerrar con palabras.
- La categoría tiene que ser **utilidad**: un aviso de entrega clasificado como marketing deja de
  entregarse.
- El número de pruebas de Meta solo escribe a **cinco números** dados de alta a mano en Meta.

Si una plantilla no está aprobada, el aviso falla con un error que dice qué plantilla y en qué
estado está. Las fechas y horas de la plantilla salen en la zona horaria de la entrega, no en la
de quien envía. Cuando el Destinatario **responde**, la respuesta se anota en la Orden y el aviso
pasa a **Respondido**; responder cuenta como consentimiento.

**Estado**: el circuito completo (envío, entrega, lectura, respuesta) se ha probado con la cuenta
de pruebas de Meta. La cuenta real de la compañía no tiene todavía número registrado: hasta
entonces, WhatsApp no está disponible en producción.
