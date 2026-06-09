3.2.3 Manifiestos
=================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Manifiestos

El Manifiesto EDI (``tms.edi.manifest``) es la entidad intermedia entre la ingesta de
demanda y la estructura operativa. Agrupa los datos recibidos —de un fichero o de la
Bandeja de Entrada API— y los mantiene en un área de trabajo donde se validan y se
revisan antes de convertirse en Órdenes.

3.2.3.1 Origen
--------------

Un Manifiesto se origina al ingerir demanda por cualquiera de los canales descritos en
el capítulo 7: la importación de ficheros y la recepción por API depositan sus datos en
un Manifiesto, junto con sus *preview packs*. El Manifiesto conserva así la trazabilidad
del intercambio original, con independencia del canal de entrada.

3.2.3.2 Estados y cierre
------------------------

El Manifiesto recorre cuatro estados:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Abierto (``open``)
     - Recibiendo y acumulando datos; admite revisión.
   * - En cola (``in_queue``)
     - Marcado para procesarse por la tarea programada.
   * - Procesando (``processing``)
     - El sistema está materializando su contenido.
   * - Cerrado (``closed``)
     - Procesado: su contenido se ha convertido en estructura operativa.

El **cierre** es el momento clave: al cerrarse, el Manifiesto materializa su contenido en
la estructura operativa —Orden (``sale.order``), Tramos (``tms.shipment.leg``) y Paradas
(``tms.stop``)—. Este paso lo dispara habitualmente una tarea programada (ver
:doc:`/17.0/7_edi-integrations/7_6_automated-actions`), no una acción manual.

3.2.3.3 Validaciones
--------------------

Antes del cierre, el Manifiesto valida los datos contra el esquema y los mapeos
configurados, de modo que solo se materializan los registros coherentes; las incidencias
se reportan sin bloquear el resto. Esta validación previa es la que evita que datos
externos defectuosos contaminen la operativa real.

.. CAPTURA: 3_2_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_01_manifiesto.png
      :alt: Formulario de un Manifiesto EDI con su estado

      Formulario de un Manifiesto EDI (``tms.edi.manifest``) y su estado.
