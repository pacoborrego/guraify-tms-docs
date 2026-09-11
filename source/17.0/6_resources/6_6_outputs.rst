6.6 Salidas de taller
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Botones «Print Work Order» y «Copy Workshop Status» en la pestaña de mantenimiento del
   vehículo; Gestión de Recursos › Mantenimiento › Rankings de objetivos.

El taller no trabaja mirando Odoo: trabaja con una hoja impresa en el capó y con mensajes de
WhatsApp en el grupo. Las tres salidas de esta sección tienen un formato fijo, pensado para
leerse en papel o en el móvil, que el sistema reproduce siempre igual.

6.6.1 La orden de trabajo impresa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_6_outputs_01_orden-impresa.png
      :alt: Orden de trabajo impresa

      La orden de trabajo impresa: vehículo, controles, trabajos con su estado y firmas.

Desde la ficha del vehículo, el botón de imprimir («Print Work Order») genera el PDF que el
mecánico se lleva al taller. Lleva la fecha y un hueco para el número; el recuadro del vehículo
(matrícula, tipo y configuración, conductor, kilometraje al ingreso y fecha de la última
lectura); la tabla de **controles** con los cuatro objetivos periódicos (última vez, días,
objetivo y si está fuera de objetivo); la tabla de **trabajos a realizar**, con las reglas de
preventivo ordenadas por urgencia (vencidas, por vencer, no evaluadas por falta de historial o
de odómetro, al día y no aplica; la hoja las escribe como «⚠ VENCIDO», «Próximo», «Sin
registro», «Falta odómetro», «Al día» y «No aplica») y su diferencia en palabras («⚠ VENCIDO ·
pasado 5.000 km», «Al día · faltan 10.000 km»), seguidas de las órdenes correctivas abiertas;
cuatro filas en blanco para anotar a mano; un recuadro de observaciones y repuestos; y las tres
firmas: jefe de taller, mecánico responsable y conforme del conductor.

6.6.2 El estado del vehículo para WhatsApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_6_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_6_outputs_02_copiar-estado.png
      :alt: Ventana con el texto de estado del vehículo para WhatsApp

      El texto de estado del vehículo, listo para copiar y pegar en el grupo del taller.

El botón de copiar estado («Copy Workshop Status») abre una ventana con el texto del estado del
vehículo en formato WhatsApp, con negritas y cursivas, y un botón para copiarlo. El texto lleva
la cabecera con la matrícula y el tipo, el conductor (la línea se titula «Chofer»), el
kilometraje actual y hace cuántos días se leyó; el bloque **SERVICE** con los dos niveles del
control de revisiones y lo que les falta o sobra; el bloque de objetivos (titulado «GOMERÍA /
OBJETIVOS») con los días desde la última calibración, revisión de neumáticos, lavado y engrase;
el bloque **PREVENTIVO A ATENDER** con los trabajos vencidos y por vencer (hasta diez) y su
diferencia en kilómetros o días; el bloque **PENDIENTES DE TALLER** con las órdenes abiertas
(hasta quince); y el pie en cursiva con la firma de la compañía y la fecha. Los separadores de
miles van con punto, los vencidos en negativo y cada bloque con su contador entre paréntesis.

6.6.3 Los rankings de objetivos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_6_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_6_outputs_03_rankings.png
      :alt: Asistente de rankings de objetivos

      El ranking de lavados de la semana, con los diez primeros numerados y los vehículos sin
      registro.

Los rankings miden los cuatro objetivos periódicos (ver :doc:`6_3_maintenance-model`). El
asistente **Rankings de objetivos** elige el objetivo, la fecha de la semana, la categoría de
vehículo, el tope de vehículos y si se listan solo los atrasados, y compone el texto: el título
con el icono del objetivo y la semana, el subtítulo «Ranking por días sin lavar», los vehículos
ordenados de más a menos días con los emojis del uno al diez y luego numerados, la línea **Sin
registro** con los vehículos que nunca lo hicieron, y el pie con el objetivo en días. Cada
objetivo cuenta los días desde la última orden cerrada de ese trabajo en cada vehículo, así que
registrar un lavado es cerrar una orden de trabajo de lavado, a mano o en la carga masiva. Los
objetivos se ajustan en :doc:`6_8_configuration`.
