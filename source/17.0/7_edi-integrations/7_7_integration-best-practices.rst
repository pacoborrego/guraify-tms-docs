7.7 Buenas prácticas de integración
===================================

Una integración robusta no depende solo de una configuración correcta, sino de hábitos
de trazabilidad, validación y seguridad sostenidos en el tiempo. Esta sección reúne las
recomendaciones que conviene aplicar en cualquier despliegue.

7.7.1 Trazabilidad y observabilidad
-----------------------------------

El registro de actividad de las APIs (``tms.api.log``) es la pieza central de la
observabilidad: recoge cada intercambio, de entrada y de salida, con su tipo, sus
cabeceras, los cuerpos enviado y recibido, el estado, el código HTTP, el método y la
dirección, la IP de origen en las recepciones, el mensaje de error si lo hubo, y el
modelo y el registro de Odoo afectados. Cada ejecución de un endpoint saliente
(:doc:`7_4_endpoint-configuration`), cada webhook recibido (:doc:`7_5_webhooks`) y cada
consulta de seguimiento deja aquí su traza. Revisar este registro
de forma periódica permite detectar patrones de error y, ante llamadas fallidas,
reintentarlas sin perder la trazabilidad de los intentos previos.

.. CAPTURA: 7_7_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_7_integration-best-practices_01_api-log.png
      :alt: Registro de actividad de las APIs

      Registro de actividad de las APIs (``tms.api.log``).

7.7.2 EDI: Definiciones de fichero y Manifiestos
------------------------------------------------

En los flujos EDI, conviene apoyarse en los dos niveles previstos: la Definición de
fichero, que agrupa los mapeos aplicables, y el Manifiesto, que actúa como paso
intermedio antes de materializar la estructura operativa (ver :doc:`7_2_file-import`).
Mantener esta separación facilita validar y corregir un intercambio sin afectar a los
registros operativos ya creados.

7.7.3 Auditoría de transferencias de Agencia
--------------------------------------------

Las transferencias de Agencia (``tms.agency.transfer.snapshot``) conservan el estado
anterior y posterior a las divisiones de Tramos y a las reasignaciones, lo que permite
auditar qué cambió y revertir la operación si fuera necesario. Es la salvaguarda ante
reasignaciones erróneas en la subcontratación.

7.7.4 Seguridad
---------------

Como medidas de seguridad básicas: emplear siempre el secreto en los webhooks (ver
:doc:`7_5_webhooks`), gestionar el *token* de API por Proyecto y respetar el control de
acceso por Proyecto en la descarga de adjuntos, de modo que cada cliente acceda
únicamente a su propia información.

7.7.5 Recomendaciones operativas
--------------------------------

Por último, conviene diseñar las integraciones de forma idempotente, apoyándose en la
referencia externa única de cada Orden (el campo de mapeo ``ExternalRef``, que la Bandeja
de entrada API exige única por Proyecto) para no duplicar registros ante reenvíos;
validar los datos antes de materializarlos (ver :doc:`7_2_1_field-mapping`); controlar los
límites de lote en los envíos salientes (ver :doc:`7_4_endpoint-configuration`); y revisar
el registro de actividad con regularidad como práctica habitual de mantenimiento.
