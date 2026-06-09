7.7 Buenas Prácticas de Integración
===================================

Una integración robusta no depende solo de una configuración correcta, sino de hábitos
de trazabilidad, validación y seguridad sostenidos en el tiempo. Esta sección reúne las
recomendaciones que conviene aplicar en cualquier despliegue.

Trazabilidad y observabilidad
-----------------------------

El registro ``tms.api.log`` es la pieza central de la observabilidad: recoge cada
intercambio —de entrada y de salida— con sus cabeceras, *payloads*, estado, código HTTP
y el modelo y registro afectados. Revisar este registro de forma periódica permite
detectar patrones de error y, ante llamadas fallidas, reintentarlas sin perder la
trazabilidad de los intentos previos.

.. CAPTURA: 7_7_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_7_integration-best-practices_01_api-log.png
      :alt: Registro de actividad de las APIs

      Registro de actividad de las APIs (``tms.api.log``).

EDI: ficheros y manifiestos
---------------------------

En los flujos EDI, conviene apoyarse en los dos niveles previstos: el contenedor de
configuración ``tms.edi.file``, que agrupa los mapeos aplicables, y el Manifiesto
``tms.edi.manifest``, que actúa como paso intermedio antes de materializar la estructura
operativa. Mantener esta separación facilita validar y corregir un intercambio sin
afectar a los registros operativos ya creados.

Auditoría de transferencias de agencia
---------------------------------------

Las transferencias de agencia (``tms.agency.transfer.snapshot``) conservan el estado
anterior y posterior a los *splits* y reasignaciones, lo que permite auditar qué cambió
y revertir la operación si fuera necesario. Es la salvaguarda ante reasignaciones
erróneas en la subcontratación.

Seguridad
---------

Como medidas de seguridad básicas: emplear siempre el secreto en los webhooks (ver
:doc:`7_5_webhooks`), gestionar el *token* de API por proyecto y respetar el control de
acceso por *tenant* en la descarga de adjuntos, de modo que cada cliente acceda
únicamente a su propia información.

Recomendaciones operativas
--------------------------

Por último, conviene diseñar las integraciones de forma idempotente, apoyándose en
referencias externas únicas (``external_ref``) para no duplicar registros ante reenvíos;
validar los datos antes de materializarlos (ver :doc:`7_2_1_field-mapping`); controlar los
límites de lote en los envíos salientes (ver :doc:`7_4_endpoint-configuration`); y revisar
los logs con regularidad como práctica habitual de mantenimiento.
