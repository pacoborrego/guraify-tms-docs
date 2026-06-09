3.5 Modelo de integración
-------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI

El modelo de integración define los mecanismos mediante los cuales el TMS intercambia
información con sistemas externos. Estas integraciones permiten automatizar la entrada de
demanda, sincronizar información con otros sistemas empresariales y facilitar la
interoperabilidad con plataformas logísticas, transformando los datos externos
directamente en entidades nativas del sistema (Orden, Tramo, Parada, Viaje) sin crear
estructuras paralelas.

El sistema soporta varios mecanismos, gestionados por el módulo de integraciones
(``tms_int``):

- Definición de ficheros estructurados (``tms.edi.file``) para la importación.
- Integraciones API REST (``tms_int.api.integration``) y su Bandeja de Entrada
  (``tms_int.api.inbox``).
- Endpoints de servicio salientes (``tms_int.api.endpoint``).
- Webhooks entrantes sobre esos mismos endpoints.
- Automatizaciones programadas (``ir.cron``) que orquestan el flujo.

.. admonition:: Dónde se detalla
   :class: important

   Este apartado es solo el encuadre arquitectónico. El funcionamiento completo de cada
   mecanismo —configuración, mapeo, transformaciones, webhooks, acciones automáticas y
   buenas prácticas— se desarrolla en el :doc:`capítulo 7, EDI e Integraciones
   </17.0/7_edi-integrations/index>`. Los contratos de la API REST pública viven en el
   *gateway* (``/api/docs``) y no se duplican aquí.
