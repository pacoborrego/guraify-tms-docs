7.3 Integraciones API
=====================

La integración por API REST en formato JSON es el canal en tiempo real del TMS: permite
recibir pedidos y eventos de los sistemas de cliente y consultar información de
seguimiento sin intervención manual. Esta sección describe la orquestación común del
camino de integración (API REST y webhooks) y la mecánica propia de las APIs.

Orquestación
------------

Cada conexión con un sistema externo se define mediante la Integración
(``tms_int.integration``) y sus líneas (``tms_int.integration.line``). Cada línea
representa un canal concreto con sus credenciales y parámetros, y se asocia a uno o
varios clientes y a un proyecto. Esta estructura permite que un mismo cliente disponga
de varios canales activos y que la configuración de cada uno quede aislada del resto.

Para los flujos de salida, los patrones (``tms_int.pattern`` y sus líneas
``tms_int.pattern.line`` / ``tms_int.pattern.line.field``) describen cómo construir el
*payload* que se remite a los sistemas remotos (ver :doc:`7_4_endpoint-configuration`).

Configuración de la conexión
----------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Integraciones API

.. CAPTURA: 7_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_3_api-integrations_01_integracion.png
      :alt: Configuración de una integración API y su autenticación

      Configuración de una integración API y su autenticación.

La conexión HTTP se define en la Integración API (``tms_int.api.integration``), que
declara la URL base y el método de autenticación. Se admiten cinco modalidades: sin
autenticación (``none``), autenticación básica (``basic``), *bearer token* (``bearer``),
clave de API (``api_key``) y JWT dinámico (``jwt_dynamic``). En esta última, el sistema
solicita el *token* con usuario y contraseña, lo cachea y lo refresca automáticamente
cuando expira, evitando renovaciones innecesarias. La configuración incluye además una
prueba de credenciales para validar la conexión antes de ponerla en producción.

Almacenamiento intermedio y materialización
--------------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Bandeja de entrada API

.. CAPTURA: 7_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_3_api-integrations_02_inbox.png
      :alt: Bandeja de Entrada API con los estados de las líneas

      Bandeja de Entrada API con los estados de las líneas.

Los datos que llegan por API no se convierten directamente en registros operativos.
Primero se depositan en la Bandeja de Entrada API (``tms_int.api.inbox``) y sus líneas
(``tms_int.api.inbox.line``), organizadas por proyecto. Cada línea atraviesa una
secuencia de estados —recibido, inválido y vinculado— y se agrupa en un Manifiesto
(``tms.edi.manifest``) junto con sus *preview packs*. Los datos maestros que acompañan
a la recepción se gestionan mediante los lotes de bandeja (``tms_int.api.inbox.batch``).

Solo tras la validación y el cierre del Manifiesto se materializa la estructura
operativa: la Orden (``sale.order``), el Tramo (``tms.shipment.leg``), la Parada
(``tms.stop``) y el Viaje (``tms.trip``).

Ingesta de datos
----------------

La entrada de datos se canaliza a través de ``tms_int.api.post.import.data``, que crea
las líneas de bandeja y los *preview packs* asociados a un *token* de etiqueta, **sin
crear todavía la Orden**. La materialización en ``sale.order`` se produce en una fase
posterior, una vez validados y agrupados los datos, manteniendo así separadas la
recepción y la creación de registros operativos.

APIs de lectura
---------------

Además de la ingesta, la integración expone consultas de solo lectura: la API de
seguimiento (``tms_int.api.get.tracking``), que devuelve el estado de las expediciones,
y la descarga de adjuntos (``tms_int.api.get.attachment``), que aplica control de acceso
por proyecto para que cada cliente solo acceda a su propia documentación.

.. admonition:: Contratos REST en el *gateway*
   :class: important

   La estructura concreta de las peticiones y respuestas REST (campos de cada
   *payload*, ejemplos y códigos de error) se documenta en el *gateway* (``/api/docs``).
   Aquí se describe únicamente el comportamiento funcional de la integración.
