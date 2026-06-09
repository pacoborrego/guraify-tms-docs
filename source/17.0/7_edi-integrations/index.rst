7 EDI e Integraciones
=====================

Este capítulo describe cómo Guraify TMS intercambia información con sistemas
externos: la ingesta de pedidos y eventos desde ficheros (XLSX/CSV), API REST
(JSON) y webhooks; el mapeo y la transformación de los datos hacia el modelo
interno; y la trazabilidad de cada intercambio.

El módulo responsable es ``tms_int`` (Integraciones), apoyado en los modelos de
EDI del núcleo (``tms.edi.file``, ``tms.edi.manifest``, ``tms.edi.field.mapping``)
y en el registro de actividad ``tms.api.log``.

.. admonition:: Alcance vs. contratos de API
   :class: important

   Aquí se documenta la **arquitectura funcional** de las integraciones (cómo se
   configuran y cómo fluyen los datos). Los **contratos de la API REST pública**
   (payloads, ejemplos y códigos de error) viven en la documentación del *gateway*
   (``/api/docs``) y **no** se duplican en este manual.

.. toctree::
   :maxdepth: 2

   7_1_integration-strategy
   7_2_file-import
   7_3_api-integrations
   7_4_endpoint-configuration
   7_5_webhooks
   7_6_automated-actions
   7_7_integration-best-practices
