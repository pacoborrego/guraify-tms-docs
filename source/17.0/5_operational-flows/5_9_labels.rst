5.9 Etiquetas
-------------

.. admonition:: Ruta en Odoo
   :class: tip

   Acción **Generar etiquetas** en las listas y fichas de Viajes, Manifiestos, Órdenes, Tramos,
   Paradas y Bultos · TMS › Administración › **Label Printers** y **Label Designs** (etiquetas en
   inglés en la interfaz) · ficha del Proyecto, grupo de etiquetas

Esta sección tampoco es un paso del flujo: la :term:`Etiqueta` acompaña al Bulto desde que
existe hasta que se entrega, y se imprime donde haga falta. Aquí está qué es, cómo se genera y
desde dónde se imprime; cómo se escanea está en :doc:`5_4_app-execution` y en el
:doc:`Manual del conductor </17.0/10_manual_app/index>`.

5.9.1 Qué es y cuándo existe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada :term:`Bulto` tiene una etiqueta propia con su código de barras, el destinatario y su
dirección, la referencia de la Orden, el cliente, la fecha, la franja y el número de Bulto
dentro de la Orden (2 de 5). Existe en dos formas: **PDF**, para cualquier impresora, y
**ZPL**, el lenguaje de las etiquetadoras térmicas (Zebra y compatibles), y en dos tamaños,
**10 × 6 cm** (horizontal) y **10 × 15 cm** (vertical, el de las agencias).

La etiqueta **no se crea con el Bulto**: se genera la primera vez que alguien la pide y se guarda
con el Bulto, de modo que la segunda vez no hay que calcularla. Si cambia lo que lleva impreso
(el destinatario, la fecha o el Planning del Tramo, el código del Bulto), la guardada se
descarta y la siguiente petición la regenera. Al **cerrar un Manifiesto**, el sistema genera de
una vez las etiquetas de todos sus Bultos de entrega, para que la impresión en el muelle no
espere: si esa generación falla, el cierre no se detiene y las etiquetas se harán al pedirlas.

En el camino API el Bulto existe antes que la Orden: es el :term:`Bulto previo`, que nace al
recibir la Orden en la Bandeja de entrada con su código y su **token de etiqueta**, con el que
el cliente descarga la etiqueta desde la pasarela antes incluso de que el Manifiesto se cierre.
Al cerrarse, el Bulto previo pasa a definitivo con el mismo código y la misma etiqueta. Si la
Orden llega sin la lista de Bultos y solo con cuántos son, el sistema crea un Bulto previo por
unidad. El contrato está en la :doc:`Guía del integrador </17.0/7_edi-integrations/index>`.

5.9.2 Generar etiquetas
~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 5_9_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_9_labels_01_generar-etiquetas.png
      :alt: Asistente Generar etiquetas abierto desde un Viaje

      Generar etiquetas desde un Viaje: formato de salida, tamaño, diseño y orden del lote.

La acción **Generar etiquetas** está en el menú de acciones de seis sitios y hace lo mismo en
todos: reúne los Bultos del registro (o de los registros seleccionados) y los saca en un solo
documento.

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Desde
     - Qué Bultos
   * - Viaje
     - Los de las entregas de todas sus Paradas, en el orden de la ruta. Es la impresión del
       muelle antes de cargar.
   * - Manifiesto
     - Los de todas sus Órdenes: la impresión en origen de un fichero recién cerrado.
   * - Orden, Tramo, Parada
     - Los suyos, para reponer una etiqueta o etiquetar una recogida.
   * - Bulto
     - Uno o varios Bultos elegidos en la lista.

El asistente enseña cuántos Bultos va a procesar y cuántos tienen ya la etiqueta guardada, y
pide:

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Decisión
     - Efecto
   * - Formato de salida
     - **PDF (descarga combinada)**: un solo PDF con una página por Bulto. **ZPL
       (concatenado)**: un fichero para enviar a la etiquetadora. **Listado de URL**: una página
       de índice con el enlace de descarga de cada etiqueta, para quien imprime desde otro
       sistema. **Imprimir directamente en etiquetadora**: el ZPL va por red a la impresora
       elegida, sin descargar nada.
   * - Tamaño de etiqueta
     - 10 × 6 o 10 × 15 cm. Se propone el del Proyecto o, al imprimir directamente, el de la
       impresora.
   * - Diseño
     - El diseño de etiqueta del lote (ver 5.9.3). Vacío, el estándar del tamaño.
   * - Impresora
     - Solo al imprimir directamente: una de las etiquetadoras configuradas.
   * - Orden de las etiquetas
     - Por qué campos se ordena el lote y en qué sentido (secuencia de la Parada, destinatario,
       código postal, referencia, cliente, fecha, tipo de bulto, zona operativa, origen…). Se
       propone el orden por defecto del Proyecto. Solo reordena la salida; no regenera nada.

Los Bultos sin etiqueta guardada se generan de una vez; los demás salen de lo guardado. **Generar
etiqueta ahora**, en la ficha del Bulto, fuerza la regeneración de uno solo.

5.9.3 Impresoras y diseños
~~~~~~~~~~~~~~~~~~~~~~~~~~

Dos maestros de Administración completan la configuración:

- Una **impresora de etiquetas** (``tms.label.printer``) es una etiquetadora térmica accesible
  por red: nombre, dirección IP y puerto (9100 por defecto), modelo (Zebra, Honeywell o
  genérica ZPL), tamaño de etiqueta que carga, ubicación y tiempo de espera. Puede limitarse a
  unos Proyectos, para que un cliente que imprime por API solo vea la suya. La ficha guarda la
  última vez que se usó y si respondió.
- Un **diseño de etiqueta** (``tms.label.design``) dice con qué plantilla se dibuja cada
  tamaño: el estándar del TMS o uno propio de un cliente (con su logotipo, sus campos o su
  distribución). El diseño se elige en el asistente o se fija por defecto en el Proyecto, junto
  con el tamaño y el orden habituales de sus etiquetas
  (:doc:`/17.0/4_parametrization/4_5_project-configuration`).

Las entradas antiguas del menú **Imprimir** (Transport Label 10x6, Transport Label 10x15 y la
descarga en ZIP del Viaje) han dejado de mostrarse: hacían lo mismo que Generar etiquetas sin
sus opciones. Si alguien las echa en falta, se pueden volver a activar desde el informe, pero el
camino es el asistente.

5.9.4 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Campo o modelo
   * - La etiqueta guardada del Bulto
     - ``tms.shipment.pack``: ``label_pdf``, ``label_zpl``, ``label_url`` (y
       ``label_pdf_filename``); se vacían al cambiar ``barcode``, ``barcode_external``,
       ``shipment_line_id``, ``active_leg_id`` o ``pricelist_rule_id`` del Bulto, o el
       destinatario, la fecha de descarga o el Planning del Tramo
   * - Bulto previo y token
     - ``tms.shipment.pack.is_preview``, ``api_label_token`` (``tms_int``)
   * - El asistente
     - ``tms.label.print.wizard`` (``output_format``, ``label_format``, ``design_id``,
       ``printer_id``, ``order_line_ids``), acciones de servidor en los seis modelos
   * - Informes de Bulto
     - ``tms.transport_label_10x6_pack``, ``…_10x6_pack_product_sequenced``,
       ``…_10x15_pack``, ``…_10x15_pack_product_sequenced``
   * - Impresoras y diseños
     - ``tms.label.printer``, ``tms.label.design`` (+ ``tms.label.design.format``)
   * - Defectos del Proyecto
     - ``project.project``: ``default_label_format``, ``default_label_design_id`` y las líneas
       de orden por defecto
   * - Descarga por API
     - ``GET /api/labels/<token>?format=pdf|zpl|url`` (pasarela)
