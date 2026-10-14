11.6 Pruebas y puesta en marcha
-------------------------------

Un aviso mal configurado no se nota en la oficina: lo nota un Destinatario que recibe un mensaje
que no debía, o a las tres de la mañana. Por eso los avisos se prueban antes, y casi siempre sobre
una **copia de la base de producción**, que tiene los contactos reales con sus móviles reales.
Este apartado es la receta para que esa prueba no se convierta en un envío masivo.

11.6.1 Probar sobre una copia de producción
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Neutralizar la copia antes de arrancar Odoo sobre ella** (``odoo-bin neutralize``). La
   neutralización desactiva los servidores de correo y las tareas programadas y anula el token de
   WhatsApp, pero **no vacía las colas**: los correos, SMS y WhatsApp que estuvieran pendientes de
   salir en producción siguen ahí, y saldrían a clientes reales en cuanto se rearme un canal.
#. **Vaciar las colas heredadas**: cancelar los correos, SMS y mensajes de WhatsApp pendientes de
   envío.
#. **Poner la lista blanca de pruebas** (parámetro del sistema ``tms_notify.allowlist``) **antes
   de crear el primer flujo**: los móviles y correos de prueba, separados por comas. Con la lista
   puesta, solo se avisa a quien esté en ella; el resto queda omitido con **No está en la lista
   blanca de pruebas**. Los números se comparan por sus últimas nueve cifras, así que da igual
   escribirlos con prefijo o sin él.
#. Rearmar **solo** lo necesario: un servidor de correo propio, las credenciales del canal que se
   pruebe y las dos tareas programadas de los avisos.
#. Crear el flujo **acotado a un Proyecto de prueba** y una Orden de prueba cuyo Destinatario sea
   alguien de la lista, con su móvil, su país y, para WhatsApp, su consentimiento.
#. Cerrar la Parada de prueba (desde la oficina, con Establecer evento) y mirar la pestaña Avisos
   de la Orden. Un segundo cierre dentro del tiempo de no repetir tiene que quedar **Ya avisado**.

.. warning::

   En las copias de producción de E-Transport hay más de 22.000 móviles reales. Sin la lista
   blanca, el primer flujo activo avisa a todos los Destinatarios que cumplan su disparador.

11.6.2 Poner en marcha en producción
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Instalar ``tms_notify`` y, según los canales, ``sms_esendex`` y (Enterprise) ``whatsapp`` y
   ``tms_notify_whatsapp``.
#. Completar la **Marca de la compañía**: el nombre del remitente y el dominio del enlace
   (:ref:`17.0/4_parametrization/4_1_operational-configuration:4.1.7 Marca de la compañía`).
#. Configurar los canales (:doc:`11_2_channels`) y, en WhatsApp, esperar a que Meta apruebe las
   plantillas.
#. Revisar y adaptar las plantillas; quitar el enlace de seguimiento mientras su página no
   exista.
#. Comprobar que los contactos de entrega traen móvil y país, y decidir con el cliente cómo se
   recoge el consentimiento de WhatsApp.
#. Crear los flujos, empezando por uno o dos (entregado, entrega no realizada) en un Proyecto, y
   ampliar después.
#. Activar las tareas programadas «TMS: send the notification queue» y «TMS: dispatch the
   time-based notifications», y vigilar el indicador **Avisos atascados en cola**.

Las dos tareas programadas no recuperan lo atrasado al reactivarse: si han estado paradas, no
salen de golpe todos los avisos que no salieron.
