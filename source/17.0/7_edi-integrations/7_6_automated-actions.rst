7.6 Acciones Automáticas
========================

Buena parte de la integración funciona sin intervención manual, mediante procesos
programados y reglas que reaccionan a los cambios en los datos. Esta automatización es
la que sostiene la operativa continua: los datos entran, se procesan y se notifican sin
que nadie tenga que lanzar cada paso.

Tareas programadas
------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Ajustes › Técnico › Automatización › Acciones planificadas

.. CAPTURA: 7_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_6_automated-actions_01_crons.png
      :alt: Tareas programadas que orquestan las integraciones

      Tareas programadas que orquestan las integraciones.

Varias tareas programadas (``ir.cron``) orquestan el flujo a intervalos de pocos
minutos. Entre ellas, el procesamiento de los ficheros en cola pendientes del asistente
de importación (``tms_int.file.wizard``), el cómputo de las Órdenes de venta
(``sale.order``) asociadas a las expediciones, el cálculo de la tarifa de los Viajes
(``tms.trip``) y el cierre de los Manifiestos (``tms.edi.manifest``). Este escalonamiento
permite que la ingesta (ver :doc:`7_2_file-import`) avance de forma diferida y ordenada.

Reglas automáticas dinámicas
----------------------------

Para los flujos de salida, las reglas automáticas (``base.automation``) con disparo
``on_write`` ejecutan un Endpoint saliente cuando cambia un registro. Estas reglas no se
configuran a mano: se generan desde la propia configuración del endpoint, de modo que
activar la notificación automática de un evento es una decisión que se toma en el mismo
endpoint (ver :doc:`7_4_endpoint-configuration`).

Programación de endpoints
-------------------------

De forma complementaria, un endpoint puede programarse para ejecutarse periódicamente
mediante tareas ``ir.cron`` generadas también desde su configuración. Así, el envío
saliente puede responder tanto a eventos (``on_write``) como a una cadencia temporal,
según convenga a cada integración. El conjunto de tareas y reglas se encadena con la
importación de ficheros y el despacho por proyecto para cubrir el ciclo completo de
entrada y salida de datos.
