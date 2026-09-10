6.6 Salidas de taller
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Botones **Print Work Order** y **Copy Workshop Status** en la pestaña Maintenance (TMS) del
   vehículo; Gestión de Recursos › Mantenimiento › Rankings de objetivos.

El taller no trabaja mirando Odoo: trabaja con una hoja impresa en el capó y con mensajes de
WhatsApp en el grupo. Las tres salidas de esta sección reproducen **al carácter** los formatos
que el taller ya usaba antes del TMS, porque cualquier cambio de formato es una regresión para
quien los lee cada día.

6.6.1 La orden de trabajo impresa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_6_outputs_01_orden-impresa.png
      :alt: Orden de trabajo impresa

      La orden de trabajo impresa: unidad, controles, trabajos con su estado y firmas.

Desde la ficha del vehículo, **Print Work Order** genera el PDF que el mecánico se lleva al
taller. Lleva la fecha y un hueco para el número; el recuadro de la unidad (matrícula, tipo y
configuración, chofer, kilometraje al ingreso y fecha de la última lectura); la tabla de
**controles de gomería y lavado** con los cuatro objetivos (última vez, días, objetivo y si está
fuera de objetivo); la tabla de **trabajos a realizar**, con las reglas de preventivo ordenadas
por urgencia (vencidas, próximas, sin registro, sin kilometraje, al día, no aplica) y su estado
en palabras («⚠ VENCIDO · pasado 36.660 km», «Al día · faltan 23.340 km»), seguidas de las
órdenes correctivas abiertas; cuatro filas en blanco para anotar a mano; un recuadro de
observaciones y repuestos; y las tres firmas: jefe de taller, mecánico responsable y conforme
del chofer.

6.6.2 El estado de la unidad para WhatsApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_6_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_6_outputs_02_copiar-estado.png
      :alt: Ventana con el texto de estado de la unidad para WhatsApp

      El texto de estado de la unidad, listo para copiar y pegar en el grupo del taller.

**Copy Workshop Status** abre una ventana con el texto del estado de la unidad en formato
WhatsApp, con negritas y cursivas, y un botón para copiarlo. El texto lleva la cabecera con la
matrícula y el tipo, el chofer, el kilometraje actual y hace cuántos días se leyó; el bloque
**SERVICE** con los dos niveles y lo que les falta o sobra; el bloque **GOMERÍA / OBJETIVOS**
con los días desde la última calibración, relevamiento, lavado y engrase; el bloque
**PREVENTIVO A ATENDER** con los trabajos vencidos y por vencer (hasta diez) y su diferencia en
kilómetros o días; el bloque **PENDIENTES DE TALLER** con las órdenes abiertas (hasta quince); y
el pie en cursiva con la firma de la compañía y la fecha. Los separadores de miles van con
punto, los vencidos en negativo y cada bloque con su contador entre paréntesis.

6.6.3 Los rankings de objetivos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_6_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_6_outputs_03_rankings.png
      :alt: Asistente de rankings de objetivos

      El ranking de lavados de la semana, con los diez primeros numerados y las unidades sin
      registro.

Los cuatro **objetivos periódicos** (lavado y engrase cada 30 días, calibración y relevamiento de
cubiertas cada 90) son trabajos del catálogo cuyo intervalo es el objetivo. El asistente
**Rankings de objetivos** elige el objetivo, la fecha de la semana, el tipo de unidad, el tope
de unidades y si se listan sólo las atrasadas, y compone el texto: el título con el icono del
objetivo y la semana, el subtítulo «ranking por días sin lavar», las unidades ordenadas de más a
menos días con los emojis del uno al diez y luego numeradas, la línea **Sin registro** con las
unidades que nunca lo hicieron, y el pie con el objetivo en días. Cada objetivo cuenta los días
desde la última orden cerrada de ese trabajo en cada unidad, así que registrar un lavado es
cerrar una orden de trabajo de lavado, a mano o en la carga masiva. Los objetivos se ajustan en
:doc:`6_8_configuration`.
