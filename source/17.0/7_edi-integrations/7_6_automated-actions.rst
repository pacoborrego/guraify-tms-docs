7.6 Acciones automáticas
========================

Buena parte de la integración funciona sin intervención manual, mediante procesos
programados y reglas que reaccionan a los cambios en los datos. Esta automatización es
la que sostiene la operativa continua: los datos entran, se procesan y se notifican sin
que nadie tenga que lanzar cada paso.

7.6.1 Tareas programadas
------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Ajustes › Técnico › Automatización › Acciones planificadas

.. CAPTURA: 7_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_6_automated-actions_01_crons.png
      :alt: Tareas programadas que orquestan las integraciones

      Tareas programadas que orquestan las integraciones.

El módulo de integraciones instala cuatro tareas programadas (``ir.cron``), todas con
cadencia de cinco minutos, que encadenan la entrada de datos con su tratamiento
económico. En el orden en que actúan sobre un intercambio:

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Tarea
     - Qué hace
   * - ``Compute File Imports in Queue``
     - Recoge los ficheros que el asistente de importación (``tms_int.file.wizard``) dejó
       en cola, los valida contra su Definición de fichero y devuelve su Manifiesto al
       estado abierto para que pueda revisarse y cerrarse (ver :doc:`7_2_file-import`).
   * - ``Compute Close Manifest``
     - Procesa los Manifiestos (``tms.edi.manifest``) marcados para cerrar: los pasa a
       *procesando*, materializa sus Órdenes, Tramos y Paradas y los deja *cerrados*.
   * - ``Compute Sale Orders for TMS Shipments``
     - Tarifica y confirma las Órdenes (``sale.order``) marcadas para recalcular su
       tarifa o pendientes de confirmación tras el cierre desde la app, en lotes acotados
       por tiempo y por tamaño para no bloquear el servidor.
   * - ``Compute Tariff for TMS Trips``
     - Tarifica los Viajes (``tms.trip``) marcados para recalcular su coste, con los mismos
       topes de lote y de tiempo.

Las dos últimas son la tarea de tarificación que el Manual de implantación describe en
:doc:`/17.0/5_operational-flows/5_6_settlement`; aquí interesa saber que existen porque
explican por qué una Orden recién importada tarda unos minutos en aparecer tarificada.

7.6.2 Reglas y programación de los endpoints
--------------------------------------------

Los flujos de salida se automatizan desde el propio endpoint, que genera sus reglas
automáticas (``base.automation`` con disparo ``on_write``) y sus tareas programadas
(``ir.cron``) sin que haya que crearlas a mano. Los dos disparadores y su filtro se
describen en :doc:`7_4_endpoint-configuration`. El conjunto de tareas y reglas se
encadena con la importación de ficheros y el despacho por Proyecto para cubrir el ciclo
completo de entrada y salida de datos.
