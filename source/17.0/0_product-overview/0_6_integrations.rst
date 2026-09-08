Integraciones
-------------

Pocas empresas de transporte teclean sus órdenes. Llegan del sistema del cliente, de un
fichero que alguien manda cada mañana o de una plataforma de comercio electrónico. Y el
cliente quiere de vuelta el estado de cada envío y la prueba de entrega, en su sistema, sin
llamar. Guraify TMS está construido para eso.

Cómo entran los datos
~~~~~~~~~~~~~~~~~~~~~

**Por fichero.** El cliente envía un Excel o un CSV con su formato. En el TMS se define una
vez cómo leer ese fichero: qué columna es qué, cómo se transforma cada dato (fechas, teléfonos,
referencias, códigos de barras) y qué hacer con lo que falta. A partir de ahí, cada fichero se
importa en un Manifiesto, se revisa, se normalizan las direcciones y se convierte en Órdenes
con un botón. Hay un catálogo de transformaciones listas para usar y se pueden añadir otras.

**Por API.** El sistema del cliente envía las órdenes directamente. Cada envío entra en una
Bandeja de entrada API, donde queda registrado tal cual llegó, se valida y se agrupa en un
Manifiesto. Lo que no es válido se ve, con su motivo, y se puede corregir o devolver al
cliente. Para los sistemas externos hay una pasarela de API con documentación interactiva,
autenticación y registro de cada llamada.

**Por webhook.** El cliente notifica eventos (una orden nueva, una cancelación, un cambio de
dirección) a una dirección propia del TMS protegida con clave. El TMS decide qué hacer con
cada uno según cómo se haya configurado.

**A mano.** Siempre queda el formulario de Odoo para la orden puntual o la corrección.

Cómo salen los datos
~~~~~~~~~~~~~~~~~~~~

**Estados y prueba de entrega hacia el cliente.** Cuando una parada cambia de estado, cuando
se entrega, cuando hay una incidencia o cuando se firma, el TMS puede enviarlo al sistema del
cliente en el formato que ese sistema espere. Cada cliente tiene su propia configuración de
envío: qué eventos, con qué formato, a qué dirección, uno a uno o por lotes.

**Consulta de seguimiento.** El cliente puede preguntar por una referencia suya y recibir el
estado, el histórico de eventos, los bultos y los documentos adjuntos.

**Portal del cliente.** Sin integración, el cliente entra con su usuario y ve lo que ha enviado
por API: qué se ha recibido, qué se ha rechazado y por qué, y en qué manifiesto ha quedado.

.. CAPTURA: 0_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/0_product-overview/0_6_integrations_01_portal.png
      :alt: Portal del cliente con sus envíos recibidos por API

      El portal del cliente: envíos recibidos, rechazados y su manifiesto.

Qué queda registrado
~~~~~~~~~~~~~~~~~~~~

Toda llamada que entra o sale queda en un registro de actividad con fecha, dirección,
contenido, respuesta y resultado. Cuando un cliente dice que envió algo y no aparece, se busca
ahí. Cuando el TMS envió algo y el sistema del cliente no lo aceptó, también.

.. seealso::

   La :doc:`Guía del integrador </17.0/7_edi-integrations/index>` explica cómo se configura
   cada canal y cómo fluyen los datos. Los contratos de la API (formatos, ejemplos, códigos de
   error) están en la documentación de la pasarela de API.
