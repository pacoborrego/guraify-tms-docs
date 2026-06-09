3.2.4 API Inbox
===============

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Bandeja de entrada API

La Bandeja de Entrada API (``tms_int.api.inbox``) es el punto de recepción de la demanda
que llega por API REST. Funciona como una bandeja por proyecto en la que cada pedido
entrante se deposita como una línea (``tms_int.api.inbox.line``) antes de vincularse a un
Manifiesto y materializarse.

3.2.4.1 Funcionamiento
----------------------

Cada línea de la bandeja atraviesa una secuencia de estados que permite separar la
recepción de la materialización:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado de la línea
     - Significado
   * - Recibido (``received``)
     - El pedido ha entrado en la bandeja y está pendiente de tratamiento.
   * - Inválido (``invalid``)
     - No supera la validación; queda señalado para su revisión.
   * - Vinculado a Manifiesto (``linked``)
     - La línea se ha asociado a un Manifiesto para su procesamiento.

La cabecera de la bandeja lleva contadores (recibidos, inválidos, vinculados y número de
manifiestos) que dan una visión inmediata del estado de la cola, y permite abrir
directamente los Manifiestos generados a partir de sus líneas.

3.2.4.2 Relación con el Manifiesto
----------------------------------

La Bandeja de Entrada API no crea Órdenes directamente: agrupa sus líneas en un
Manifiesto (``tms.edi.manifest``), que es quien, al cerrarse, materializa la estructura
operativa (ver :doc:`3_2_3_manifests`). De este modo, la ingesta por API comparte el
mismo punto de validación y materialización que el resto de canales, manteniendo la
coherencia del modelo. Los contratos REST concretos de esta recepción se documentan en el
*gateway* y en :doc:`/17.0/7_edi-integrations/7_3_api-integrations`.

.. CAPTURA: 3_2_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_4_api-inbox_01_inbox.png
      :alt: Bandeja de Entrada API con sus líneas y estados

      Bandeja de Entrada API (``tms_int.api.inbox``) con sus líneas y estados.
