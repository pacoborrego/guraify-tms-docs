7.4 Configuración de endpoints
==============================

Los endpoints definen las llamadas HTTP **salientes** del TMS hacia sistemas remotos: la
contrapartida de la recepción descrita en :doc:`7_3_api-integrations`. Describen qué se
envía, cómo se construye y cuándo se dispara.

7.4.1 Definición del endpoint
-----------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Endpoints API

.. figure:: /_static/img/7_edi-integrations/7_4_endpoint-configuration_01_endpoint.png
   :alt: Configuración de un endpoint saliente

   Configuración de un endpoint saliente.

Cada endpoint (``tms_int.api.endpoint``) declara el método HTTP y la dirección relativa
sobre la URL base de su Integración API, y construye las cabeceras, el cuerpo y la
*query string* mediante plantillas Jinja. La respuesta del sistema remoto se procesa con
``response_mapper_code``, que mapea los datos devueltos sobre los registros de Odoo. El
envío puede ser individual o por lotes según ``send_mode``: en modo *single* se emite
una llamada por registro y en modo *batch* se agrupan hasta ``max_batch_size`` registros
por llamada. La autenticación es la definida en la Integración API asociada.

7.4.2 Disparadores
------------------

Un endpoint puede ejecutarse de dos formas, y las dos se configuran desde el propio
endpoint, sin tocar a mano las herramientas técnicas de Odoo:

- **Al cambiar un registro**: una regla automática (``base.automation`` con disparo
  ``on_write``) que el endpoint genera desde su configuración y que lo ejecuta cuando
  cambia un registro del modelo. Es la forma de notificar un evento en cuanto ocurre.
- **Periódicamente**: una tarea programada (``ir.cron``), también generada desde el
  endpoint, que lo invoca con la cadencia indicada. Es la forma de enviar por lotes o de
  sincronizar a intervalos.

En ambos casos, ``filter_domain`` permite condicionar la ejecución a los registros que
cumplen un criterio determinado, evitando envíos innecesarios. El siguiente diagrama
resume el flujo saliente:

.. mermaid::

   flowchart LR
       D{Disparador}
       A[Regla on_write<br/>base.automation]:::tr --> D
       C[Tarea programada<br/>ir.cron]:::tr --> D
       D -->|filter_domain| P[Patrón / plantilla Jinja<br/>tms_int.pattern]
       P --> B[Construcción del cuerpo]
       B --> H[Llamada HTTP<br/>tms_int.api.endpoint]
       H --> R[Sistema remoto]
       R --> RM[response_mapper_code]
       RM --> U[Actualización de registros<br/>en Odoo]
       H --> G[Traza<br/>tms.api.log]
       classDef tr fill:#efe,stroke:#8a8;

7.4.3 Despacho por Proyecto
---------------------------

Para los flujos de subcontratación, los endpoints de despacho por Proyecto
(``tms_int.project.dispatch.endpoint``) determinan qué endpoints se ejecutan al asignar
Paradas a una Agencia. Cada uno se declara con un propósito, ``dispatch`` para notificar
la asignación o ``cancel`` para revertirla, de modo que la comunicación con la Agencia
queda alineada con el ciclo de vida de la asignación.

7.4.4 Trazabilidad
------------------

Cada ejecución de un endpoint queda registrada en el registro de actividad de las APIs,
que se describe en :doc:`7_7_integration-best-practices`.
