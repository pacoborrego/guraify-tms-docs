7.2 Importación de Ficheros
===========================

La importación de ficheros es el canal de ingesta empleado para cargas manuales o
periódicas de pedidos y datos maestros. Está pensada tanto para la puesta en marcha
inicial de un cliente como para los intercambios recurrentes en los que el sistema de
origen no dispone de API.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Definición de Fichero

Asistente de importación
------------------------

.. CAPTURA: 7_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_file-import_01_asistente.png
      :alt: Asistente de importación de fichero

      Asistente de importación de fichero.

El proceso se gobierna desde el asistente de importación (``tms_int.file.wizard``), que
cubre la subida del fichero y el seguimiento de su tratamiento a través de una secuencia
de estados —borrador, procesando, validado e importado— y emite un reporte de
validación con los errores y advertencias detectados antes de materializar nada.

Formatos y normalización
------------------------

Se admiten ficheros **XLSX/XLS y CSV** (en CSV, con delimitador de columna, fila de
cabecera y fila de inicio configurables). Tras el parseo, el contenido se normaliza a
una representación JSON **interna** que preserva la estructura del intercambio
(pedidos, clientes, transportistas, conductores, vehículos y viajes). Esa
representación es la que alimenta el resto del flujo, de modo que el mapeo y la
validación operan siempre sobre la misma estructura con independencia del formato del
fichero de partida.

.. note::

   El JSON como formato de **entrada** pertenece al camino de integración (API REST y
   webhooks, ver :doc:`7_3_api-integrations`); en la importación de ficheros el JSON es
   solo la forma normalizada interna tras el parseo.

Del fichero a la Orden
----------------------

El recorrido completo es: parseo a la representación interna, validación contra el
esquema y los mapeos configurados, creación del Manifiesto (``tms.edi.manifest``) y de
sus *preview packs*, y materialización final de la Orden (``sale.order``) a través de
``tms_int.sale.order.import``. La configuración de fichero EDI (``tms.edi.file``) actúa
como contenedor de los mapeos de columnas aplicables a cada tipo de fichero (ver
:doc:`7_2_1_field-mapping`).

Procesamiento diferido y errores
--------------------------------

Las filas pendientes no se procesan necesariamente en el momento de la subida: una
tarea programada las recoge periódicamente y completa su tratamiento (ver
:doc:`7_6_automated-actions`). Los tipos de dato no admitidos —como los valores de
fecha y hora sin un formato reconocible— y el resto de incidencias se recogen en el
reporte de validación, sin interrumpir el procesamiento de las filas correctas.

.. CAPTURA: 7_2_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_file-import_02_validacion.png
      :alt: Reporte de validación del fichero importado

      Reporte de validación del fichero importado.

Configuración del mapeo
-----------------------

La correspondencia entre las columnas del fichero y los campos de Odoo, y las
transformaciones aplicables a cada campo, se detallan en las dos subsecciones
siguientes:

.. toctree::
   :maxdepth: 1

   7_2_1_field-mapping
   7_2_2_python-transformations
