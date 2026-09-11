3.2.4 Bandeja de entrada API
----------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Bandeja de entrada API

La :term:`Bandeja de entrada API` (``tms_int.api.inbox``) es el punto de recepción de la
demanda que llega por API REST. Hay una bandeja por Proyecto, y en ella cada Orden entrante se
deposita como una línea antes de vincularse a un Manifiesto y materializarse.

3.2.4.1 Funcionamiento
~~~~~~~~~~~~~~~~~~~~~~

Cada línea de la bandeja atraviesa una secuencia de estados que permite separar la recepción de
la materialización:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado de la línea
     - Significado
   * - Recibido
     - La Orden ha entrado en la bandeja y está pendiente de tratamiento.
   * - No válido
     - No supera la validación; queda señalada para su revisión, con el motivo.
   * - Vinculado a manifiesto
     - La línea se ha asociado a un Manifiesto para su procesamiento.

Cada envío del sistema externo queda registrado además como un **lote**, que conserva el
mensaje completo tal como llegó, el número de Órdenes que traía y los bloques que no son
Órdenes (clientes, transportistas, conductores, vehículos y viajes) para poder revisarlos o
reprocesarlos. Las líneas se cuentan y se tratan una a una; el lote es el registro de soporte
de la recepción.

La cabecera de la bandeja lleva cuatro botones inteligentes con contadores, **Recibido**, **No
válido**, **Manifiestos** e **Histórico** (las líneas que ya no están ni en recibidas ni en no
válidas), que dan una visión inmediata del estado de la cola y abren directamente las líneas de
cada grupo o los Manifiestos generados a partir de ellas.

3.2.4.2 Relación con el Manifiesto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La Bandeja de entrada API no crea Órdenes directamente: agrupa sus líneas en un Manifiesto con
el botón **Crear manifiesto**, y es el Manifiesto quien, al cerrarse, materializa la estructura
operativa (ver :doc:`3_2_3_manifests`). De este modo, la ingesta por API comparte el mismo
punto de validación y materialización que el resto de canales, manteniendo la coherencia del
modelo. Los contratos REST concretos de esta recepción se documentan en la pasarela de API y en
:doc:`/17.0/7_edi-integrations/7_3_api-integrations`.

.. figure:: /_static/img/3_functional-architecture/3_2_4_api-inbox_01_inbox.png
   :alt: Bandeja de entrada API con sus líneas y estados

   Bandeja de entrada API con sus líneas y estados.
