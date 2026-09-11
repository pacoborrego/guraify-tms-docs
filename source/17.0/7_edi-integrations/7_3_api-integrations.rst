7.3 Integraciones API
=====================

La integración por API REST en formato JSON es el canal en tiempo real del TMS: permite
recibir Órdenes y eventos de los sistemas de cliente y consultar información de
seguimiento sin intervención manual. Esta sección describe la orquestación común del
camino de integración (API REST y webhooks) y la mecánica propia de las APIs.

7.3.1 Orquestación
------------------

Dos registros distintos organizan una integración, y conviene no confundirlos. La
**Integración** (``tms_int.integration``) es la ficha de negocio: asocia uno o varios
clientes y un Proyecto, agrupa sus canales en líneas (``tms_int.integration.line``, cada
una de tipo API/webhook, importación de fichero o conexión a base de datos, con sus
credenciales y sus Definiciones de fichero) y designa el patrón de salida. La
**Integración API** (``tms_int.api.integration``) es la conexión HTTP concreta con un
sistema remoto, con su URL base y su autenticación, y de ella cuelgan los Endpoints
(:doc:`7_4_endpoint-configuration`). No están enlazadas por un campo: la primera dice
*con quién* y *por qué canales* se intercambian datos; la segunda, *cómo* se llama a un
sistema remoto.

Para los flujos de salida, los patrones (``tms_int.pattern`` y sus líneas
``tms_int.pattern.line`` / ``tms_int.pattern.line.field``) describen cómo construir el
cuerpo que se remite a los sistemas remotos (ver :doc:`7_4_endpoint-configuration`).

7.3.2 Configuración de la conexión
----------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Integraciones API

.. figure:: /_static/img/7_edi-integrations/7_3_api-integrations_01_integracion.png
   :alt: Configuración de una integración API y su autenticación

   Configuración de una integración API y su autenticación.

La Integración API declara la URL base y el método de autenticación. Se admiten cinco
modalidades: sin autenticación (``none``), autenticación básica (``basic``), *bearer
token* (``bearer``), clave de API (``api_key``) y JWT dinámico (``jwt_dynamic``). En esta
última, el sistema solicita el *token* con usuario y contraseña, lo guarda y lo refresca
automáticamente cuando expira, evitando renovaciones innecesarias. La configuración
incluye además una prueba de credenciales para validar la conexión antes de ponerla en
producción.

7.3.3 Almacenamiento intermedio y materialización
-------------------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Bandeja de entrada API

.. CAPTURA: 7_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_3_api-integrations_02_inbox.png
      :alt: Bandeja de entrada API con los estados de las líneas

      Bandeja de entrada API con los estados de las líneas.

Los datos que llegan por API no se convierten directamente en registros operativos:
primero se depositan en la Bandeja de entrada API, organizada por Proyecto, y solo tras
la validación y el cierre del Manifiesto se materializan la Orden, el Tramo, la Parada y
el Viaje. Los estados de las líneas y los lotes de datos maestros se describen en el
Manual de implantación (:doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`).

Lo que interesa al integrador es lo que ese paso intermedio le da: cada línea de la
bandeja conserva el mensaje recibido tal cual, se identifica por la referencia externa de
la Orden (``ExternalRef``, única por Proyecto, de modo que un reenvío actualiza la línea
en vez de duplicarla) y genera de inmediato los **bultos previos** (*preview packs*):
registros de Bulto (``tms.shipment.pack``) creados en modo previo, antes de que exista la
Orden, para que el cliente pueda disponer ya de sus etiquetas. Al cerrarse el Manifiesto
esos bultos previos se promueven a los Bultos definitivos de la Orden, conservando su
código de barras y su token de etiqueta.

7.3.4 Ingesta de datos
----------------------

La entrada de datos se canaliza a través de ``tms_int.api.post.import.data``, que crea
las líneas de bandeja y sus bultos previos **sin crear todavía la Orden**. Cada bulto
previo recibe un **token de etiqueta**: un identificador opaco (UUID) que el cliente
recibe en la respuesta y con el que puede descargar la etiqueta de ese bulto desde la
pasarela, tanto antes como después de que la Orden exista. La materialización en
``sale.order`` se produce en una fase posterior, una vez validados y agrupados los datos,
manteniendo así separadas la recepción y la creación de registros operativos.

7.3.5 APIs de lectura
---------------------

Además de la ingesta, la integración expone consultas de solo lectura: la API de
seguimiento (``tms_int.api.get.tracking``), que devuelve el estado de las Órdenes,
y la descarga de adjuntos (``tms_int.api.get.attachment``), que aplica control de acceso
por Proyecto para que cada cliente solo acceda a su propia documentación. Sus contratos
están en la pasarela (ver el índice del capítulo).
