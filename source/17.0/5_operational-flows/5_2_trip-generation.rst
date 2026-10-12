5.2 Generación de Viajes
------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes · botón **Asignar** de la lista de Órdenes ·
   **Acciones operativas › Asignar a viaje** en la lista de Paradas · TMS › Operaciones ›
   Planning › Optimizador de Paradas

.. figure:: /_static/img/5_operational-flows/5_2_trip-generation_01_generacion-viajes.png
   :alt: Optimizador de Paradas

   El Optimizador de Paradas: Viajes propuestos, mapa y Paradas pendientes.

Con las Órdenes validadas, sus Paradas están pendientes de planificar. Generar un Viaje
(``tms.trip``) es agrupar esas Paradas en una salida que ejecutará un conductor con un vehículo
en una fecha. Hay tres maneras de hacerlo, y las tres producen el mismo resultado: un Viaje
**planificado** con sus Paradas en orden, al que después se asignan o confirman los recursos
(:doc:`5_3_resource-assignment`) y que no sale a la calle hasta que alguien lo despacha
(:doc:`5_4_app-execution`). La excepción es el Viaje que nace al enviar Paradas a una
agencia, que puede quedar ya despachado si la agencia recibe las instrucciones por API o el
Proyecto lo pide (ver :doc:`5_4_app-execution`).

5.2.1 Qué contiene un Viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un Viaje reúne la fecha y las horas previstas de inicio y fin; el Planning y, si procede, la
franja del Plan de disponibilidad de la que sale; los recursos y la tarifa de compra o el
precio cerrado con que se liquidará; las Paradas en su orden, con los Tramos, los Bultos y los
Reembolsos que arrastran; y los datos del cálculo de ruta. Su estructura, sus estados y los
botones de su cabecera (Despachar, Validar y sus vueltas atrás) están en
:doc:`/17.0/3_functional-architecture/3_2_2_trips`.

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

5.2.3 Con el asistente Asignar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El asistente **Asignar** es la única puerta de la planificación manual y de la optimización: el
planificador elige Paradas y decide si van a un Viaje nuevo, a uno que ya existe o a los que
proponga el motor de optimización. Se abre de dos maneras:

- Desde la lista de **Órdenes**, seleccionando varias y pulsando **Asignar**. El asistente trabaja
  con la Parada activa de cada Orden (ver :doc:`/17.0/3_functional-architecture/3_2_5_active-leg`);
  las Órdenes sin validar no se admiten.
- Desde la lista de **Paradas**, seleccionando varias y abriendo **Acciones operativas**, con la
  acción **Asignar a viaje**. El mismo menú ofrece **Reprogramar parada**
  (:doc:`5_5_trip-closing`), **Establecer evento** (cerrar una Parada desde la oficina,
  :doc:`5_4_app-execution`) y **Enviar por API**.

.. mermaid::

   flowchart TB
       A["Asistente Asignar<br/>(Paradas elegidas)"] --> M{"Modo"}
       M -->|"Nuevo"| N["Un Viaje nuevo:<br/>fecha, recursos, Planning"]
       M -->|"Existente"| E["Un Viaje de esas fechas,<br/>elegido en la lista o en el mapa"]
       M -->|"Optimización"| O["El motor propone los Viajes:<br/>por franja o por categoría"]
       N & E --> G{"¿Enviar a agencia?<br/>¿Transferencia hub?"}
       G -->|"no"| V["Viaje planificado"]
       G -->|"sí"| T["Arrastre a agencia<br/>o a un hub propio (3.2.6.3)"]
       O --> P["Plan que espera<br/>«Aplicar plan»"]

**Qué Paradas admite.** Las de ruta y las de servicio directo (las de hub las genera el propio
Viaje), **que nadie haya reportado**: la regla es por Parada, no por Viaje. Una Parada sin Viaje
entra siempre; una Parada planificada o incluso despachada también, siempre que ni ella ni sus
Tramos tengan un evento del conductor (cargada, en curso, completada, con reservas, fallida…).
Así, la ruta que se avería a media mañana se puede repartir: salen las Paradas pendientes y las
entregadas se quedan en su Viaje. Lo único que no se mueve es una Parada de un arrastre a
agencia: ahí se saca del Viaje de la agencia (lo que revierte el envío) y se asigna después. El
Viaje que pierde una Parada queda pendiente de reenviar y, si aún no ha empezado, se vuelve a
secuenciar y a enrutar por sí solo; si ya ha empezado, solo se le recalcula el ETA.

**Nuevo.** Crea un Viaje con lo que se indique. Lo único obligatorio es la **categoría de
vehículo** (con ella el motor sabe capacidades y perfil), el **Planning** y los **servicios**; lo
demás lo completa el Proyecto. Elegir el **conductor** rellena en cascada lo que se deduce de él:
su transportista, su vehículo (si tiene varios, la lista se limita a ellos; si no tiene ninguno, a
los del transportista), la categoría del vehículo y la tarifa de compra del transportista en la
compañía (ninguna si es flota propia). Se puede fijar un **precio cerrado** en vez de tarifa, y
los **hubs** del Viaje se proponen desde las Paradas y el Proyecto. Si alguna Parada no tiene hub,
antes de ejecutar se abre **Paradas sin hub**, con **Aplicar a todas** y **Guardar y continuar**.

**Existente.** Añade las Paradas al final de un Viaje que ya existe. La lista ofrece los Viajes
**de las fechas de las Paradas** que no estén cerrados, y el mapa de la derecha dibuja la ruta de
cada uno; pulsar una ruta o uno de sus puntos abre su ficha (conductor, vehículo, horas, Paradas,
km) con **Elegir este viaje**. Un Viaje despachado admite Paradas (se despachan con él); uno que
ya ha empezado también, con un aviso: el conductor recibirá la ruta modificada. Si el Viaje es de
una agencia o un arrastre, el asistente adopta su rama por sí solo. El botón **Buscar la mejor
ruta** abre, con las mismas Órdenes, el asistente **Encontrar ruta**, que pregunta al motor en
qué ruta existente cabe cada una y a qué coste.

**Optimización.** El tercer modo lanza el motor de optimización sobre las Paradas elegidas y es
el mismo que el del Optimizador de Paradas; se describe en :ref:`la sección siguiente
<generacion-optimizador>`.

**Enviar a agencia y transferencia hub.** Bajo los campos, un bloque decide si las Paradas se
traspasan. **Enviar a agencia** aparece cuando el transportista elegido es una agencia con la
que hay integración (la propia compañía nunca lo es, aunque esté marcada como agencia) y manda la
agencia al asistente: el Viaje nace como traslado a la agencia y, si recibe las instrucciones por
API, queda despachado en el acto (:doc:`5_4_app-execution`). **Crear transferencia hub** lo
enciende el Proyecto y crea el arrastre con su expedición propia; con **Dejar la última milla sin
planificar** el destino es un hub propio y las Paradas del cliente quedan libres para optimizarlas
desde allí. Qué forma tiene ese arrastre y cómo se deshace está en
:doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`. El arrastre a hub propio solo admite
Paradas sin Viaje; si alguna lo tiene, el asistente lo dice y ofrece **Desasignar y continuar**.

Al pulsar **Ejecutar**, el asistente comprueba hubs, obligatorios y coordenadas (avisa de las
Paradas que el motor dejaría fuera por estar en otro país o demasiado lejos del hub, sin impedir
la asignación), y abre un diálogo de progreso mientras asigna y enruta. Cada Parada pasa al Viaje
con el siguiente número de secuencia y toma su Planning; sus Tramos quedan vinculados al Viaje y
sus Reembolsos, disponibles para la liquidación. Al terminar, **Abrir viaje** lleva a la ficha.

Sobre el Viaje resultante, tres botones ajustan el recorrido cuando hace falta: **Secuenciar
Viaje** pide a PTV la :term:`secuenciación <Secuenciación>` de las Paradas, **Enrutar Viaje**
lanza el :term:`cálculo de ruta <Cálculo de ruta>` con el orden actual (trazado, distancias y
horas estimadas), y **Actualizar** regenera las Paradas de hub cuando se han añadido o quitado
Tramos. En el mapa del Optimizador de Paradas las Paradas también se pueden reordenar y mover
entre Viajes arrastrándolas; cada cambio relanza el cálculo de ruta.

.. CAPTURA: 5_2_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_2_trip-generation_02_asignar-nuevo.png
      :alt: Asistente Asignar en modo Nuevo con el mapa de las Paradas

      El asistente Asignar en modo Nuevo: los campos a la izquierda, las Paradas y el mapa a la
      derecha.

.. CAPTURA: 5_2_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_2_trip-generation_03_asignar-existente.png
      :alt: Asistente Asignar en modo Existente con la ficha de un Viaje en el mapa

      Modo Existente: los Viajes de esas fechas sobre el mapa y la ficha de uno con «Elegir este
      viaje».

.. CAPTURA: 5_2_04 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_2_trip-generation_04_paradas-sin-hub.png
      :alt: Diálogo Paradas sin hub

      Paradas sin hub: el hub se asigna a cada una o a todas antes de seguir.

.. _generacion-optimizador:

5.2.4 Con el Optimizador
~~~~~~~~~~~~~~~~~~~~~~~~

La generación automática deja que el motor de optimización proponga qué Viajes crear y cómo
llenarlos. Se lanza desde el asistente Asignar en modo **Optimización**, o desde el
:term:`Optimizador de Paradas`, que abre el mismo asistente sobre las Paradas del mapa. Los pasos:

#. **Elegir las Paradas** pendientes de una fecha y un Planning. Deben tener coordenadas
   válidas y ventanas horarias coherentes; las de un Viaje despachado no se mueven.
#. **Elegir el modo.** En el **modo por franja** se seleccionan
   las franjas del :term:`Plan de disponibilidad de conductores` que van a trabajar ese día;
   cada una aporta conductor, vehículo y transportista. En el **modo por categoría de
   vehículo** («Por Categoría») se indica cuántos vehículos de cada categoría hay disponibles,
   con su hub y su ventana de salida, sin decir cuáles.
#. **Lanzar la optimización.** El sistema envía al motor las Paradas, los vehículos con sus
   capacidades y los conductores con su perfil de jornada, y sigue el progreso en un diálogo.
   El resultado **no se aplica solo**: el diálogo enseña las Paradas por estado de ventana, las
   que quedan fuera y las violaciones, y espera a **Aplicar plan**. Al aplicarlo se crean los
   **Viajes planificados** con sus Paradas asignadas y secuenciadas, sus horas estimadas y su
   trazado; **Revertir** deshace el plan entero.
#. **Revisar la propuesta** sobre el mapa: mover Paradas entre Viajes, reordenarlas, quitar las
   que no procedan. En el modo por categoría, asignar después conductor y vehículo a cada
   Viaje (:doc:`5_3_resource-assignment`).

La herramienta, sus requisitos y lo que envía y recibe de PTV están en
:ref:`optimizador-paradas`.

.. CAPTURA: 5_2_05 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_2_trip-generation_05_asignar-optimizacion.png
      :alt: Asistente Asignar en modo Optimización

      Modo Optimización: las categorías de vehículo disponibles y el bloque del motor.
