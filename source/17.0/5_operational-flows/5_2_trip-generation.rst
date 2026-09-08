5.2 Generación de Viajes
------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes · TMS › Operaciones › Planificación › Optimizador de
   Paradas · botones **Asignar** y **Optimiza** en la lista de Órdenes

.. CAPTURA: 5_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_2_trip-generation_01_generacion-viajes.png
      :alt: Generación de viajes

      Generación de Viajes: asistente manual u Optimizador de Paradas.

Con las Órdenes validadas, sus Paradas están pendientes de planificar. Generar un Viaje
(``tms.trip``) es agrupar esas Paradas en una salida que ejecutará un conductor con un vehículo
en una fecha. Hay tres maneras de hacerlo, y las tres producen el mismo resultado: un Viaje en
borrador con sus Paradas secuenciadas, al que después se asignan o confirman los recursos
(:doc:`5_3_resource-assignment`).

5.2.1 Qué contiene un Viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un Viaje reúne la fecha y las horas previstas de inicio y fin; el Planning y, si procede, la
franja del Plan de disponibilidad de la que sale; la agencia y los hubs de referencia; los
recursos (transportista, conductor, vehículo y remolque) y la tarifa de compra o el precio
cerrado con que se liquidará; las Paradas en su orden, con los Tramos, los Bultos y los
reembolsos que arrastran; las métricas agregadas (peso, volumen, palés, distancia, tiempos);
y los datos del cálculo de ruta (trazado y horas estimadas por parada). Qué son sus tres
estados y qué hacen Bloquear y Desbloquear está en
:doc:`/17.0/3_functional-architecture/3_2_2_trips`.

5.2.2 Desde el fichero del Manifiesto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando las Órdenes entran por fichero, el propio fichero puede traer ya la asignación a
viajes. En la :term:`Definición de fichero` se mapean el campo que dice **a qué Viaje va cada
Orden** (el nombre del viaje) y, opcionalmente, la **secuencia** de sus paradas dentro de él
(ver :doc:`/17.0/7_edi-integrations/7_2_1_field-mapping`). Al **cerrar el Manifiesto**, el
sistema crea los Viajes con esa información y les asigna sus Paradas. El enriquecimiento de
la ruta depende de si el fichero trae o no la secuencia:

- **Con secuencia.** El sistema respeta ese orden y lanza el :term:`cálculo de ruta <Cálculo de
  ruta>` con PTV: distancias, tiempos y horas estimadas de llegada por parada.
- **Sin secuencia**, depende del Proyecto (ver
  :doc:`/17.0/4_parametrization/4_5_project-configuration`). Si tiene activada la
  **autosecuenciación**, el sistema primero ordena las paradas con la secuenciación de PTV y
  después calcula la ruta. Si no, las paradas quedan en el orden del fichero y el Viaje no se
  enriquece: no tendrá kilómetros, tiempos ni horas estimadas.

.. note::

   Sin secuencia ni autosecuenciación, el Viaje queda creado y operativo pero "plano", sin
   métricas de ruta. Si la operación necesita horas estimadas o distancias, el fichero debe
   venir secuenciado o el Proyecto debe tener activada la autosecuenciación.

5.2.3 A mano, con el asistente Asignar a viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La generación manual es la habitual con poco volumen, rutas fijas o correcciones: el
planificador decide qué Paradas van a qué Viaje. Se hace con el asistente **Asignar a viaje**,
que se abre de dos maneras:

- Desde la lista de **Órdenes**, seleccionando varias y pulsando **Asignar**. El asistente
  trabaja con la parada activa de cada Orden; las Órdenes sin validar no se admiten.
- Desde la lista de **Paradas**, seleccionando varias y abriendo **Acciones operativas**, con la
  acción **Asignar a viaje**.

Sólo se pueden asignar Paradas **en borrador** y de tipo ruta o directas (recogida o entrega de
origen a destino); las paradas de hub las genera el propio Viaje. El asistente tiene dos modos:

- **Nuevo.** Se crea un Viaje con lo que se indique: Proyecto, fecha y franja horaria,
  conductor, vehículo o categoría de vehículo, transportista, tarifa de compra o precio
  cerrado, Planning y tipo de transportista. Lo que no se rellene lo completa el Proyecto: su
  tipo de servicio y, si no se ha elegido tarifa de compra, la suya.
- **Existente.** Se elige un Viaje abierto y las Paradas se añaden al final de su secuencia.

Al ejecutar, cada Parada pasa al Viaje con el siguiente número de secuencia y toma su Planning;
sus Tramos quedan vinculados al Viaje y sus reembolsos, disponibles para la liquidación. Si el
transportista elegido es una **agencia**, el asistente ofrece además el traspaso por hub, que
crea la parada de entrega en la agencia y divide los Tramos.

Sobre el Viaje resultante, tres botones ajustan la ruta cuando hace falta: **Secuenciar
Viaje** pide a PTV el mejor orden de las paradas, **Enrutar Viaje** recalcula el trazado y las
horas estimadas con el orden actual, y **Actualizar** regenera las paradas de hub cuando se han
añadido o quitado Tramos. En el mapa del Optimizador de Paradas las paradas también se pueden
reordenar y mover entre Viajes arrastrándolas; cada cambio relanza el cálculo de ruta.

5.2.4 Con el Optimizador de Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La generación automática deja que PTV proponga qué Viajes crear y cómo llenarlos. Se lanza
desde el :term:`Optimizador de Paradas`, o con **Optimiza** desde la lista de Órdenes, o con
**Acciones operativas › Optimizar con PTV** desde la lista de Paradas. Los pasos:

#. **Elegir las Paradas** pendientes de una fecha y un Planning. Todas deben tener coordenadas
   válidas y ventanas horarias coherentes.
#. **Elegir el modo.** **Por Turno**, seleccionando las franjas del Plan de disponibilidad de
   conductores que van a trabajar ese día (cada una aporta conductor, vehículo y
   transportista). O **Por Categoría**, indicando cuántos vehículos de cada categoría hay
   disponibles, sin decir cuáles.
#. **Lanzar la optimización.** El sistema envía a PTV las paradas, los vehículos con sus
   capacidades y los conductores con su jornada, espera el resultado y crea los **Viajes en
   borrador** con sus Paradas asignadas y secuenciadas, sus horas estimadas y su trazado. Si
   alguna parada no ha podido planificarse, lo dice con la lista.
#. **Revisar la propuesta** sobre el mapa: mover paradas entre viajes, reordenarlas, quitar las
   que no procedan. En el modo por categoría, asignar después conductor y vehículo a cada
   Viaje (:doc:`5_3_resource-assignment`).

La herramienta, sus requisitos y lo que envía y recibe de PTV están en
:ref:`optimizador-paradas` y en
:ref:`17.0/1_introduction/1_4_technological-architecture:1.4.2 Servicios de PTV`.
