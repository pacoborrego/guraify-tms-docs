11 Avisos al Destinatario
=========================

Este capítulo describe los **avisos al Destinatario**: los mensajes que el TMS envía solo, por
correo, SMS o WhatsApp, a quien recibe una entrega (o al cliente que la encargó) cuando pasa algo
que le interesa: que su envío está planificado, que es la siguiente entrega, que se ha entregado,
que no se ha podido. Es un módulo opcional, que se instala y se configura sin programar: cada
aviso es un **flujo** que dice cuándo, a quién, por qué canal y con qué plantilla.

La tesis es la de siempre: no inventar lo que Odoo ya tiene. Las plantillas son las de correo, SMS
y WhatsApp de Odoo; los envíos pasan por los canales de Odoo; el consentimiento y la lista negra
de teléfonos, también. Lo que añade el TMS es saber **cuándo** avisar (los quince momentos de una
entrega), **a quién** (el Destinatario de la Parada) y **cuándo no** (sin consentimiento, de
noche, si ya se le dijo).

.. mermaid::

   flowchart LR
       E["Pasa algo en la Parada<br/>o llega la hora"] --> F["Flujo de aviso<br/>¿aplica? ¿a quién?"]
       F --> C{"Consentimiento,<br/>no repetir,<br/>horario de silencio"}
       C -->|"sí"| Q["Mensaje en cola"]
       C -->|"no"| S["Mensaje omitido<br/>con su motivo"]
       Q -->|"tarea programada,<br/>cada minuto"| K["Correo · SMS · WhatsApp"]
       K --> O["Pestaña Avisos<br/>de la Orden"]
       S --> O

.. toctree::
   :maxdepth: 1

   11_1_what-it-is
   11_2_channels
   11_3_workflows
   11_4_recipient
   11_5_following
   11_6_go-live
   11_7_reference
