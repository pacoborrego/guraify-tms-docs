7.4 Configuración de Endpoints
==============================

Los endpoints definen las llamadas HTTP **salientes** del TMS hacia sistemas remotos: la
contrapartida de la recepción descrita en :doc:`7_3_api-integrations`. Describen qué se
envía, cómo se construye y cuándo se dispara.

Definición del endpoint
-----------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Endpoints API

.. CAPTURA: 7_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_4_endpoint-configuration_01_endpoint.png
      :alt: Configuración de un endpoint saliente

      Configuración de un endpoint saliente.

Cada endpoint (``tms_int.api.endpoint``) declara el método HTTP y la ruta relativa sobre
la URL base de su Integración API, y construye las cabeceras, el cuerpo y la
*query string* mediante plantillas Jinja. La respuesta del sistema remoto se procesa con
``response_mapper_code``, que mapea los datos devueltos sobre los registros de Odoo. El
envío puede ser individual o por lotes según ``send_mode``: en modo *single* se emite
una llamada por registro y en modo *batch* se agrupan hasta ``max_batch_size`` registros
por llamada. La autenticación es la definida en la Integración API asociada.

Disparadores
------------

Un endpoint puede ejecutarse de dos formas. La primera, mediante reglas automáticas
(``base.automation`` con disparo ``on_write``) que se generan desde la propia
configuración del endpoint y reaccionan a cambios en los registros. La segunda, mediante
tareas programadas (``ir.cron``) que lo invocan periódicamente. En ambos casos,
``filter_domain`` permite condicionar la ejecución a los registros que cumplen un criterio
determinado, evitando envíos innecesarios.

El siguiente diagrama resume el flujo saliente:

.. mermaid::

   flowchart LR
       D{Disparador}
       A[Regla on_write<br/>base.automation]:::tr --> D
       C[Tarea programada<br/>ir.cron]:::tr --> D
       D -->|filter_domain| P[Patrón / plantilla Jinja<br/>tms_int.pattern]
       P --> B[Construcción del payload]
       B --> H[Llamada HTTP<br/>tms_int.api.endpoint]
       H --> R[Sistema remoto]
       R --> RM[response_mapper_code]
       RM --> U[Actualización de registros<br/>en Odoo]
       H --> G[Traza<br/>tms.api.log]
       classDef tr fill:#efe,stroke:#8a8;

Despacho por proyecto
---------------------

Para los flujos de subcontratación, los endpoints de despacho por proyecto
(``tms_int.project.dispatch.endpoint``) determinan qué endpoints se ejecutan al asignar
paradas a una agencia. Cada uno se declara con un propósito —``dispatch`` para notificar
la asignación o ``cancel`` para revertirla—, de modo que la comunicación con la agencia
queda alineada con el ciclo de vida de la asignación.

Trazabilidad
------------

Cada ejecución de un endpoint queda registrada en ``tms.api.log``, con sus cabeceras,
*payloads* y código de respuesta. El tratamiento de estas trazas y las recomendaciones
de reintento se detallan en :doc:`7_7_integration-best-practices`.
