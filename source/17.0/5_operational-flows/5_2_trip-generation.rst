5.2 Generación de Viajes
------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes · TMS › Operaciones › Planning › Optimizador de
   Paradas · botones **Asignar** y **Optimiza** (así se llama en la interfaz) en la lista de
   Órdenes

.. CAPTURA: 5_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_2_trip-generation_01_generacion-viajes.png
      :alt: Generación de viajes

      Generación de Viajes: asistente manual u Optimizador de Paradas.

Con las Órdenes validadas, sus Paradas están pendientes de planificar. Generar un Viaje
(``tms.trip``) es agrupar esas Paradas en una salida que ejecutará un conductor con un vehículo
en una fecha. Hay tres maneras de hacerlo, y las tres producen el mismo resultado: un Viaje en
**borrador** con sus Paradas en orden, al que después se asignan o confirman los recursos
(:doc:`5_3_resource-assignment`). La excepción es el Viaje que nace al enviar Paradas a una
agencia, que puede crearse ya en Procesado si el Proyecto lo pide (ver
:doc:`/17.0/4_parametrization/4_5_project-configuration`).

5.2.1 Qué contiene un Viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un Viaje reúne la fecha y las horas previstas de inicio y fin; el Planning y, si procede, la
franja del Plan de disponibilidad de la que sale; los recursos y la tarifa de compra o el
precio cerrado con que se liquidará; las Paradas en su orden, con los Tramos, los Bultos y los
Reembolsos que arrastran; y los datos del cálculo de ruta. Su estructura, sus estados y los
botones Bloquear y Desbloquear están en :doc:`/17.0/3_functional-architecture/3_2_2_trips`.

5.2.2 Desde el fichero del Manifiesto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando las Órdenes entran por fichero, el propio fichero puede traer ya la asignación a
Viajes. En la :term:`Definición de fichero` se mapean el campo que dice **a qué Viaje va cada
Orden** (el nombre del viaje) y, opcionalmente, la **secuencia** de sus paradas dentro de él
(ver :doc:`/17.0/7_edi-integrations/7_2_1_field-mapping`). Al **cerrar el Manifiesto**, el
sistema crea los Viajes con esa información y les asigna sus Paradas. El enriquecimiento del
Viaje depende de si el fichero trae o no la secuencia:

- **Con secuencia.** El sistema respeta ese orden y lanza el :term:`cálculo de ruta <Cálculo de
  ruta>` con PTV: distancias, tiempos y horas estimadas de llegada por Parada.
- **Sin secuencia**, depende del Proyecto (ver
  :doc:`/17.0/4_parametrization/4_5_project-configuration`). Si tiene activado **Secuenciar
  Viaje**, el sistema primero ordena las Paradas con la :term:`secuenciación <Secuenciación>`
  de PTV y después lanza el cálculo de ruta. Si no, las Paradas quedan en el orden del fichero y el
  Viaje no se enriquece: no tendrá kilómetros, tiempos ni horas estimadas.

.. note::

   Sin secuencia en el fichero ni Secuenciar Viaje en el Proyecto, el Viaje queda creado y
   operativo pero «plano», sin métricas de recorrido. Si la operación necesita horas estimadas o
   distancias, el fichero debe venir secuenciado o el Proyecto debe tener activado Secuenciar
   Viaje.

5.2.3 A mano, con el asistente Asignar a viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La generación manual es la habitual con poco volumen, recorridos fijos o correcciones: el
planificador decide qué Paradas van a qué Viaje. Se hace con el asistente **Asignar a viaje**,
que se abre de dos maneras:

- Desde la lista de **Órdenes**, seleccionando varias y pulsando **Asignar**. El asistente
  trabaja con la Parada activa de cada Orden (ver
  :doc:`/17.0/3_functional-architecture/3_2_5_active-leg`); las Órdenes sin validar no se
  admiten.
- Desde la lista de **Paradas**, seleccionando varias y abriendo **Acciones operativas**, con la
  acción **Asignar a viaje**.

Solo se pueden asignar Paradas **en borrador** cuyo Tipo de Parada sea Parada de Ruta, Recogida
Directo o Entrega Directo; las de hub las genera el propio Viaje. El asistente tiene dos modos:

- **Nuevo.** Se crea un Viaje con lo que se indique: Proyecto, fecha y franja horaria, recursos
  (ver :doc:`5_3_resource-assignment`), Planning y Tipo de Transportista. Lo que no se rellene
  lo completa el Proyecto.
- **Existente.** Se elige un Viaje abierto y las Paradas se añaden al final de su secuencia.

Al ejecutar, cada Parada pasa al Viaje con el siguiente número de secuencia y toma su Planning;
sus Tramos quedan vinculados al Viaje y sus Reembolsos, disponibles para la liquidación. Si el
transportista elegido es una **agencia**, el asistente ofrece además el traslado a hub de
:doc:`/17.0/4_parametrization/4_5_project-configuration`.

Sobre el Viaje resultante, tres botones ajustan el recorrido cuando hace falta: **Secuenciar
Viaje** pide a PTV la :term:`secuenciación <Secuenciación>` de las Paradas, **Enrutar Viaje**
lanza el :term:`cálculo de ruta <Cálculo de ruta>` con el orden actual (trazado, distancias y
horas estimadas), y **Actualizar** regenera las Paradas de hub cuando se han añadido o quitado
Tramos. En el mapa del Optimizador de Paradas las Paradas también se pueden reordenar y mover
entre Viajes arrastrándolas; cada cambio relanza el cálculo de ruta.

5.2.4 Con el Optimizador de Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La generación automática deja que PTV proponga qué Viajes crear y cómo llenarlos. Se lanza
desde el :term:`Optimizador de Paradas`, o con **Optimiza** desde la lista de Órdenes, o con
**Acciones operativas › Optimizar con PTV** desde la lista de Paradas. Los pasos:

#. **Elegir las Paradas** pendientes de una fecha y un Planning. Todas deben tener coordenadas
   válidas y ventanas horarias coherentes.
#. **Elegir el modo.** En el **modo por franja** se seleccionan
   las franjas del :term:`Plan de disponibilidad de conductores` que van a trabajar ese día;
   cada una aporta conductor, vehículo y transportista. En el **modo por categoría de
   vehículo** («Por Categoría») se indica cuántos vehículos de cada categoría hay disponibles,
   sin decir cuáles.
#. **Lanzar la optimización.** El sistema envía a PTV las Paradas, los vehículos con sus
   capacidades y los conductores con su perfil de jornada, espera el resultado y crea los
   **Viajes en borrador** con sus Paradas asignadas y secuenciadas, sus horas estimadas y su
   trazado. Las Paradas que no han podido planificarse se muestran en una lista aparte.
#. **Revisar la propuesta** sobre el mapa: mover Paradas entre Viajes, reordenarlas, quitar las
   que no procedan. En el modo por categoría, asignar después conductor y vehículo a cada
   Viaje (:doc:`5_3_resource-assignment`).

La herramienta, sus requisitos y lo que envía y recibe de PTV están en
:ref:`optimizador-paradas`.
