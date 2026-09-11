7.1 Estrategia de integración
=============================

Guraify TMS está concebido para operar en un ecosistema heterogéneo: clientes que
remiten Órdenes por API, plataformas que depositan ficheros y sistemas que notifican
eventos mediante webhooks. La estrategia de integración parte de un principio único:
con independencia del canal de entrada, todos los datos externos se normalizan hacia la
misma estructura interna antes de materializarse en el modelo operativo.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI

.. figure:: /_static/img/7_edi-integrations/7_1_integration-strategy_01_menu-edi.png
   :alt: Menú de configuración EDI en Odoo

   Menú de configuración EDI en Odoo.

7.1.1 Canales de entrada y convergencia
---------------------------------------

Los canales de entrada y su encaje en el modelo del TMS están descritos en el Manual de
implantación (:doc:`/17.0/3_functional-architecture/3_5_integration-model`); aquí interesa
cómo se recorren. Dejando aparte el alta manual de la Orden en Odoo, los datos externos
llegan por uno de **dos caminos**, cada uno con su propia mecánica:

- El **camino de fichero** (XLSX, XLS o CSV): el contenido se sube mediante el asistente de
  importación, se parsea, se mapea y se valida antes de materializarse. Su configuración,
  mapeo de columnas y transformaciones, se documenta junto a la importación
  (:doc:`7_2_file-import`).
- El **camino de integración**, con dos variantes: **API REST** en JSON, donde el sistema
  externo llama a las APIs del TMS (o el TMS a las del sistema remoto), y **webhooks**,
  donde el sistema externo notifica eventos a una dirección pública del TMS. La
  orquestación, el almacenamiento intermedio y la materialización de este camino se
  describen en :doc:`7_3_api-integrations` y :doc:`7_5_webhooks`.

Los dos caminos desembocan en el mismo punto, el Manifiesto, y a partir de ahí la
materialización en Orden, Tramo, Parada y Viaje es idéntica. El siguiente diagrama resume
los canales y su convergencia:

.. mermaid::

   flowchart LR
       F[Fichero XLSX/XLS/CSV]:::ch --> FW[Asistente de importación<br/>tms_int.file.wizard]
       A[API REST JSON]:::ch --> I[Bandeja de entrada API<br/>tms_int.api.inbox]
       W[Webhook evento]:::ch --> EP[Endpoint webhook<br/>tms_int.api.endpoint]
       EP --> D{¿Orden?}
       D -->|Sí| I
       D -->|No| R[Creación / actualización<br/>de registros]
       U[Alta manual en Odoo]:::ch --> O
       FW --> M[Manifiesto<br/>tms.edi.manifest]
       I --> M
       M --> O[Orden<br/>sale.order]
       O --> L[Tramo<br/>tms.shipment.leg]
       L --> C[Cerrar Manifiesto<br/>o Validar Orden]
       C --> S[Parada<br/>tms.stop]
       S --> T[Viaje<br/>tms.trip]
       classDef ch fill:#eef,stroke:#88a;
