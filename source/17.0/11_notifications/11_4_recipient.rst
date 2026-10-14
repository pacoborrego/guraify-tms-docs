11.4 El Destinatario: datos y consentimiento
--------------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Contacto › pestaña **Propiedades TMS** › grupo **AVISOS**

.. CAPTURA: 11_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/11_notifications/11_4_recipient_01_avisos.png
      :alt: Grupo AVISOS de un contacto con canal preferido, idioma y consentimientos

      El grupo AVISOS de un contacto: canal preferido, idioma y consentimientos.

Un aviso va a un contacto de Odoo. Con el rol **Destinatario**, es el contacto de la Parada (el de
carga o descarga que trae la Orden): es el que tiene el móvil de quien recibe. Si ese contacto no
tiene móvil, teléfono ni correo, el aviso va al contacto de entrega de la Orden. Lo que el aviso
necesita del contacto:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Dato
     - Para qué
   * - Móvil (o teléfono)
     - SMS y WhatsApp. Para WhatsApp, en formato internacional (+34 600 000 000) y con el **país**
       del contacto puesto: sin país, Odoo no sabe darle formato y el WhatsApp no sale.
   * - Correo
     - El canal de correo.
   * - Zona horaria
     - El horario de silencio se mide en la del contacto; sin ella, en la de la entrega.
   * - **Canal preferido**
     - El que se prueba primero si el flujo deja elegir. **No avisar** hace que no reciba
       ningún aviso, de ningún flujo.
   * - **Idioma de los avisos**
     - El formato de fechas y horas de los avisos; vacío, el idioma del contacto y después el de
       la compañía.
   * - **Consentimiento WhatsApp**
     - **Obligatorio**: sin él no sale ningún WhatsApp. Al marcarlo se guardan solas la fecha y
       el origen (a mano, una respuesta del Destinatario, la importación o la API), que es la
       prueba que pide la protección de datos.
   * - **Consentimiento SMS**
     - Marcado por defecto: un aviso operativo sobre un envío que el cliente encargó no necesita
       consentimiento previo. Desmarcarlo es dar de baja al contacto de los SMS.

Además, el aviso respeta la **lista negra de teléfonos** de Odoo: un número en ella no recibe SMS
ni WhatsApp. Cuando el aviso no puede salir, la fila de la Orden lo dice: **Sin destinatario**,
**Sin teléfono ni correo**, **Ningún canal utilizable**, **Sin consentimiento**, **Número en lista
negra** o **Baja voluntaria**.

Los contactos de entrega llegan casi siempre por importación o por API. Lo que haya que hacer
para que traigan móvil, país y, si se va a usar WhatsApp, el consentimiento, se decide con el
cliente al configurar la integración (:doc:`/17.0/7_edi-integrations/index`).
