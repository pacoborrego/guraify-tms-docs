7.2 Importación de ficheros
===========================

La importación de ficheros es el canal de ingesta empleado para cargas manuales o
periódicas de Órdenes y datos maestros. Está pensada tanto para la puesta en marcha
inicial de un cliente como para los intercambios recurrentes en los que el sistema de
origen no dispone de API.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Definición de Fichero

.. toctree::
   :maxdepth: 1

   7_2_1_field-mapping
   7_2_2_python-transformations

7.2.3 Asistente de importación
------------------------------

.. CAPTURA: 7_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_file-import_01_asistente.png
      :alt: Asistente de importación de fichero

      Asistente de importación de fichero.

El proceso se gobierna desde el asistente de importación (``tms_int.file.wizard``), que
cubre la subida del fichero y el seguimiento de su tratamiento a través de una secuencia
de estados (borrador, procesando, validado e importado) y emite un informe de
validación con los errores y advertencias detectados antes de materializar nada.

7.2.4 Formatos y normalización
------------------------------

Se admiten ficheros **XLSX, XLS y CSV**. El formato se declara en la Definición de fichero
y el asistente comprueba que la extensión del fichero subido coincide con él; en CSV, el
delimitador de columna, la fila de cabecera y la fila de inicio son configurables. Tras el
parseo, el contenido se normaliza a una representación JSON **interna** que preserva la
estructura del intercambio (Órdenes, clientes, transportistas, conductores, vehículos y
Viajes). Esa representación es la que alimenta el resto del flujo, de modo que el mapeo y
la validación operan siempre sobre la misma estructura con independencia del formato del
fichero de partida.

.. note::

   El JSON como formato de **entrada** pertenece al camino de integración (API REST y
   webhooks, ver :doc:`7_3_api-integrations`); en la importación de ficheros el JSON es
   solo la forma normalizada interna tras el parseo.

7.2.5 Del fichero a la Orden
----------------------------

El recorrido completo es: parseo a la representación interna, validación contra el
esquema y los mapeos configurados, creación del Manifiesto (``tms.edi.manifest``) y
materialización final de la Orden (``sale.order``) a través de
``tms_int.sale.order.import``. La Definición de fichero (``tms.edi.file``) actúa como
contenedor de los mapeos de columnas aplicables a cada tipo de fichero. La
correspondencia entre las columnas del fichero y los campos del TMS se explica en
:doc:`7_2_1_field-mapping`, y las transformaciones que puede aplicar cada mapeo, en
:doc:`7_2_2_python-transformations`.

7.2.6 Procesamiento diferido y errores
--------------------------------------

Las filas pendientes no se procesan necesariamente en el momento de la subida: una
tarea programada las recoge periódicamente y completa su tratamiento (ver
:doc:`7_6_automated-actions`). Las incidencias de validación, por ejemplo un valor de
fecha y hora sin un formato reconocible, se recogen en el informe de validación sin
interrumpir el procesamiento de las filas correctas.

.. figure:: /_static/img/7_edi-integrations/7_2_file-import_02_validacion.png
   :alt: Informe de validación del fichero importado

   Informe de validación del fichero importado.
