7.1 Estrategia de Integración
=============================

Guraify TMS está concebido para operar en un ecosistema heterogéneo: clientes que
remiten pedidos por API, plataformas que depositan ficheros y sistemas que notifican
eventos mediante *webhooks*. La estrategia de integración parte de un principio único:
con independencia del canal de entrada, todos los datos externos se normalizan hacia la
misma estructura interna antes de materializarse en el modelo operativo.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI

.. CAPTURA: 7_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_1_integration-strategy_01_menu-edi.png
      :alt: Menú de configuración EDI en Odoo

      Menú de configuración EDI en Odoo.

Canales de entrada
------------------

El sistema admite cuatro vías de ingesta, todas ellas equivalentes en su destino final:

- **Importación de fichero**, para cargas manuales o periódicas de pedidos y datos
  maestros en formato XLSX o CSV (ver :doc:`7_2_file-import`).
- **API REST** en formato JSON, para integraciones en tiempo real con sistemas de
  cliente (ver :doc:`7_3_api-integrations`).
- **Webhooks entrantes**, para que sistemas externos notifiquen eventos al TMS
  (ver :doc:`7_5_webhooks`).
- **Alta manual**, creando la Orden (``sale.order``) directamente en Odoo, sin
  intermediación de ninguna integración.

Dos caminos hacia el modelo operativo
-------------------------------------

Dejando aparte el alta manual, los datos externos llegan por uno de **dos caminos**
diferenciados, cada uno con su propia mecánica:

- El **camino de fichero**: el contenido se sube mediante el asistente de importación,
  se parsea, se mapea y se valida antes de materializarse. Su configuración —mapeo de
  columnas y transformaciones— se documenta junto a la importación
  (:doc:`7_2_file-import`).
- El **camino de integración**, con dos variantes: **API REST**, donde el sistema
  externo llama a las APIs del TMS (o el TMS a las del sistema remoto), y **webhooks**,
  donde el sistema externo notifica eventos a una ruta pública del TMS. La
  orquestación, el almacenamiento intermedio y la materialización de este camino se
  describen en :doc:`7_3_api-integrations`.

El siguiente diagrama resume los canales y su convergencia en la estructura operativa:

.. mermaid::

   flowchart LR
       F[Fichero XLSX/CSV]:::ch --> FW[Asistente de importación<br/>tms_int.file.wizard]
       A[API REST JSON]:::ch --> I[Bandeja de Entrada<br/>tms_int.api.inbox]
       W[Webhook evento]:::ch --> EP[Endpoint webhook<br/>tms_int.api.endpoint]
       EP --> D{¿Orden?}
       D -->|Sí| I
       D -->|No| R[Creación / actualización<br/>de registros]
       U[Alta manual en Odoo]:::ch --> O
       FW --> M[Manifiesto EDI<br/>tms.edi.manifest]
       I --> M
       M --> O[Orden<br/>sale.order]
       O --> L[Tramo<br/>tms.shipment.leg]
       L --> C[Cerrar Manifiesto<br/>o Validar Orden]
       C --> S[Parada<br/>tms.stop]
       S --> T[Viaje<br/>tms.trip]
       classDef ch fill:#eef,stroke:#88a;

.. admonition:: Frontera con el *gateway*
   :class: important

   Este capítulo describe la **arquitectura funcional** de las integraciones. Los
   **contratos de la API REST pública** (estructura de *payloads*, ejemplos y códigos
   de error) se documentan en el *gateway* (``/api/docs``) y no se reproducen aquí.
