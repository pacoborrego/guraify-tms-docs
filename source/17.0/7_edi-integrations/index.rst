7 Guía del integrador: EDI e integraciones
==========================================

Esta es la **Guía del integrador** de Guraify TMS. Explica cómo entran y salen los datos del
sistema: la carga de Órdenes desde ficheros (XLSX, XLS y CSV), por API REST (JSON) y por
webhooks; el mapeo y la transformación de esos datos hacia el modelo interno; el envío de
estados y documentos hacia los sistemas de los clientes; y la trazabilidad de cada intercambio.
Está escrita para el técnico que va a conectar un sistema externo con el TMS, y a diferencia
del Manual de implantación sí lleva código, cabeceras HTTP y nombres de campos.

**Qué necesitas saber antes.** El modelo de datos del TMS, al menos las cuatro entidades y su
relación (Orden, Tramo, Parada, Viaje), que están en el
:doc:`Modelo conceptual </17.0/2_conceptual-model/index>`; cómo entra una Orden por Manifiesto y
por Bandeja de entrada API (:doc:`/17.0/3_functional-architecture/3_2_3_manifests` y
:doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`); el encuadre general de las
integraciones (:doc:`/17.0/3_functional-architecture/3_5_integration-model`); y qué decide el
Proyecto del cliente sobre la importación
(:doc:`/17.0/4_parametrization/4_5_project-configuration`). Conviene tener Odoo delante con
permisos de administrador del TMS, porque la configuración se hace en TMS › Configuración › EDI.

El módulo responsable es ``tms_int`` (Integraciones), apoyado en los modelos de EDI del núcleo
(``tms.edi.file``, ``tms.edi.manifest``, ``tms.edi.field.mapping``) y en el registro de
actividad ``tms.api.log``.

.. admonition:: Contratos de la API: en la pasarela
   :class: important

   Esta guía documenta la **arquitectura funcional** de las integraciones: cómo se configuran
   y cómo fluyen los datos. Los **contratos de la API REST pública** (direcciones, cuerpos de
   petición y respuesta, ejemplos y códigos de error) viven en la documentación interactiva
   de la pasarela de API, en ``/api/docs`` de cada instalación, y **no** se duplican aquí. Pide
   a Guraify la dirección y las credenciales de la pasarela de tu instalación. La única
   excepción es el webhook entrante (:doc:`7_5_webhooks`), que atiende Odoo directamente.

.. toctree::
   :maxdepth: 2

   7_1_integration-strategy
   7_2_file-import
   7_3_api-integrations
   7_4_endpoint-configuration
   7_5_webhooks
   7_6_automated-actions
   7_7_integration-best-practices
