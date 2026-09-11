Integraciones
-------------

Pocas empresas de transporte teclean sus Órdenes. Llegan del sistema del cliente, de un
fichero que alguien manda cada mañana o de una plataforma de comercio electrónico. Y el
cliente quiere de vuelta el estado de cada Orden y la prueba de entrega (POD), en su sistema,
sin llamar. Guraify TMS está construido para eso.

Cómo entran los datos
~~~~~~~~~~~~~~~~~~~~~

**Por fichero.** El cliente envía un Excel o un CSV con su formato. En el TMS se define una
vez cómo leer ese fichero: qué columna es qué, cómo se transforma cada dato (fechas, teléfonos,
referencias, códigos de barras) y qué hacer con lo que falta. A partir de ahí, cada fichero se
importa en un Manifiesto, se revisa, se normalizan las direcciones y se convierte en Órdenes
con un botón. Hay un catálogo de transformaciones listas para usar; si un cliente necesita una
que no exista, se añade durante la implantación.

**Por API.** El sistema del cliente envía las Órdenes directamente. Cada petición entra en una
Bandeja de entrada API, donde queda registrada tal cual llegó, se valida y se agrupa en un
Manifiesto. Lo que no es válido se ve, con su motivo, para corregirlo o reclamárselo al
cliente. Para los sistemas externos hay una pasarela de API con documentación para sus
técnicos, autenticación y registro de cada llamada.

**Por webhook.** El cliente notifica eventos (una Orden nueva, una cancelación, un cambio de
dirección) a una dirección propia del TMS protegida con clave. Qué hace el TMS con cada aviso
se define en la configuración de ese cliente.

**A mano.** Siempre queda el formulario de Odoo para la Orden puntual o la corrección.

Cómo salen los datos
~~~~~~~~~~~~~~~~~~~~

**Estados y POD hacia el cliente.** Cuando una Parada cambia de estado, cuando se entrega,
cuando hay una incidencia o cuando se firma, el TMS puede enviarlo al sistema del cliente en
el formato que ese sistema espere. Cada cliente tiene su propia configuración de envío: qué
eventos, con qué formato, a qué dirección, uno a uno o por lotes.

**Consulta de seguimiento.** El cliente puede preguntar por una referencia suya y recibir el
estado, el histórico de eventos, los Bultos y los documentos adjuntos.

Además, el portal estándar de Odoo puede habilitarse para que el cliente consulte sus Órdenes
y sus facturas.

Qué queda registrado
~~~~~~~~~~~~~~~~~~~~

Toda llamada que entra o sale queda en un registro de actividad con fecha, origen o destino,
contenido, respuesta y resultado. Cuando un cliente dice que envió algo y no aparece, se busca
ahí. Cuando el TMS envió algo y el sistema del cliente no lo aceptó, también.

.. seealso::

   La :doc:`Guía del integrador </17.0/7_edi-integrations/index>` explica cómo se configura
   cada canal y cómo fluyen los datos. Los contratos de la API (formatos, ejemplos, códigos de
   error) los facilita Guraify junto con la pasarela de API.
