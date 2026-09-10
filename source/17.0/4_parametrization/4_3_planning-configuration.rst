4.3 Configuración de planificación
----------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración: Planes de Transporte y Zonas Geográficas. TMS › Configuración ›
   Ajustes: Planificaciones y Franjas Horarias en **Datos auxiliares**; Operación de tiempos de
   servicio y Horas de Conducción en **Optimización de ruta**. Los Tiempos de Servicio tienen
   su propio menú en TMS › Configuración.

La configuración de planificación define cómo se agrupan las operaciones, sobre qué
territorio, con qué horarios y cuánto duran. Son los seis maestros con los que las Paradas se
convierten en Viajes planificables: el Planning, los Planes de transporte, las Áreas
geográficas, las Franjas horarias, los Tiempos de servicio y las Horas de conducción. La lista
completa de campos de cada uno está en el :doc:`anexo A </17.0/annexes/index>`.

4.3.1 Planning
~~~~~~~~~~~~~~

.. CAPTURA: 4_3_04 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_04_planning.png
      :alt: Formulario de un Planning

      Un Planning: su plan de transporte, sus tiempos de servicio y su modo de división.

El :term:`Planning` (``tms.planning``) es la segmentación operativa del sistema: agrupa las
Órdenes que comparten una misma lógica de transporte, como última milla, recogidas,
distribución urbana, rutas con hub o larga distancia. No es un viaje ni un calendario; es la
dimensión que dice «estas operaciones se planifican juntas y así». Se escribe siempre
Planning, sin traducir, para no confundirlo con la actividad de planificar; en la interfaz de
Odoo el campo se llama todavía «Planificación».

El Planning se hereda del Proyecto y se propaga a la Orden, a sus Tramos, a las Paradas y al
Viaje. Por eso una elección equivocada se nota en todas partes: en cómo se agrupan las
paradas, en qué franjas del Plan de disponibilidad son compatibles, en qué precios aplican.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Plan de transporte
     - La red territorial del Planning. Cuando el sistema resuelve la zona operativa de una
       dirección, sólo busca en las áreas de esta red.
   * - Tiempos de recogida y de entrega
     - Los segundos que se añaden a cada recogida y a cada entrega al enviar el Planning al
       optimizador, además del tiempo propio de la parada. Mal calibrados, el optimizador
       propone rutas que caben en el papel y no en el día.
   * - Modo de división de viaje
     - Cómo se reparte el coste de un Viaje entre sus paradas: por peso, volumen, bultos, palés,
       cantidad, metros lineales, o cada uno combinado con los kilómetros. Tiene efecto
       económico, no sólo operativo: decide cómo se imputa el coste a cada Orden.

El Planning interviene en cinco momentos. Al **generar Paradas**, forma parte de la clave de
agrupación: dos operaciones en la misma dirección y franja no se juntan si son de Plannings
distintos. Al **crear Viajes**, es obligatorio y filtra qué franjas del Plan de disponibilidad
sirven para esa fecha. Al **optimizar**, aporta sus tiempos de servicio. Al **tarificar**, las
líneas de tarifa pueden limitarse a uno o varios Plannings, de modo que reparto, recogida o
urgente tengan precios distintos. Y en las **importaciones**, el fichero puede traer el
Planning del viaje; si no existe, algunos flujos lo crean con una configuración mínima, así que
conviene tener los maestros definidos antes.

El modo de división más adecuado depende de la operativa: en distribución ligera, por bultos o
por kilómetros y bultos; en paletería, por palés; en carga voluminosa, por metros o volumen.
Campos en :doc:`/17.0/annexes/A_07_planning`.

4.3.2 Planes de transporte
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_01_planes-transporte.png
      :alt: Configuración de un Plan de Transporte

      Un Plan de Transporte con su agencia y sus áreas sobre el mapa.

El :term:`Plan de transporte` (``tms.transport.plan``) es la red territorial de una operativa:
el conjunto de áreas geográficas por las que circula, y la agencia responsable. No es una ruta
ni una tarifa. Delimita qué polígonos forman una red y qué agencia y hub debe heredar una
dirección que caiga dentro de uno de ellos.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Áreas
     - Las áreas de tipo Plan de Transporte que forman la red. Una dirección fuera de todas
       ellas queda sin zona operativa, salvo que el Proyecto pida asignar la más cercana.
   * - Agencia
     - La agencia responsable, que heredan los tramos de la red cuando su área no tiene otra.

El plan se vincula al Planning, y a través de él llega a Tramos y Paradas: al recalcular la
zona operativa de una carga o descarga, el sistema toma el plan del Planning y compara las
coordenadas con sus polígonos. También filtra las áreas que se pueden elegir en una franja del
Plan de disponibilidad, para no asignar recursos de una red a otra. La vista de mapa del
propio plan permite comprobar la red antes de usarla. Campos en
:doc:`/17.0/annexes/A_08_planes-transporte`.

4.3.3 Áreas geográficas
~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_02_areas-geograficas.png
      :alt: Configuración de un Área Geográfica

      Un Área Geográfica con su polígono dibujado sobre el mapa.

El :term:`Área geográfica` (``tms.area``) es un polígono con significado. La misma entidad
sirve para cinco cosas, que distingue su tipo: área operativa de un plan de transporte, zona
de tarifa, área extra de precio, elemento de operación y zona de bajas emisiones. Cómo se
dibujan, se importan de OpenStreetMap y se comprueba la pertenencia de una coordenada está en
:ref:`17.0/1_introduction/1_4_technological-architecture:Áreas geográficas`. Aquí, lo que se
decide al configurarlas:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Tipo
     - Para qué sirve el área. Un mismo territorio puede existir dos veces con dos tipos, una
       para operar y otra para tarificar, y evolucionar por separado.
   * - Agencia y hub
     - Lo que heredan los tramos cuya dirección cae en el área.
   * - Días disponibles
     - Los días de la semana en que la zona operativa admite servicio. Una carga o descarga
       fuera de ellos se avisa antes de planificar.
   * - Franjas horarias
     - Las ventanas válidas en el área, como referencia para el planificador.

En el flujo operativo, las áreas de tipo Plan de Transporte etiquetan cada carga y descarga
con su zona operativa; el sistema no las recalcula en operaciones cerradas o facturadas. En el
flujo económico, las de tipo Zona Tarifa deciden qué detalle de tarifa aplica, y las de tipo
Tarifa Extra permiten suplementos por entrar en un territorio concreto. Campos en
:doc:`/17.0/annexes/A_09_areas-geograficas`.

4.3.4 Franjas horarias
~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_3_05 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_05_franjas-horarias.png
      :alt: Lista de Franjas Horarias

      Franjas Horarias: ventanas de servicio reutilizables.

La :term:`Franja horaria` (``tms.time.zone``) es una ventana de servicio con nombre, de una
hora de inicio a una de fin, que se elige en lugar de teclear las horas en cada operación. El
nombre se compone solo, con el formato de las dos horas.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué franjas existen
     - Las ventanas estándar de la operativa (mañana, tarde, 8 a 14). Al elegir una en la
       carga o la descarga de un Tramo, el sistema copia sus horas a la operación.
   * - Tipos de servicio
     - Con qué servicios se puede usar cada franja.

Si en una operación se escribe una franja personalizada en vez de elegir una del catálogo, el
sistema avisa de que puede tener coste adicional: así se separa la ventana estándar de la
excepción. Cuando el Proyecto no recibe horarios informados, las horas salen del contacto o de
las predeterminadas del proyecto, y la franja permite ajustarlas de forma controlada. Campos
en :doc:`/17.0/annexes/A_10_franjas-horarias`.

4.3.5 Tiempos de servicio
~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_3_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_03_tiempos-servicio.png
      :alt: Configuración de Tiempos de Servicio

      Un esquema de Tiempos de Servicio con sus líneas y su matriz.

El :term:`Tiempo de servicio` (``tms.service.time``) calcula cuánto dura una parada más allá
de la conducción: aparcar, bajar la mercancía, subirla a un piso, esperar en un muelle. Sin él,
la duración de las rutas y las horas estimadas de llegada dependerían sólo de los kilómetros.
Un esquema se compone de líneas, y cada línea de una operación y una matriz de detalles.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Las operaciones del esquema
     - Qué suma tiempo en una parada. Cada línea es de un tipo: **Dificultad** (según la
       dificultad de aparcamiento del contacto), **Niveles** (según los pisos y si hay ascensor)
       o **Fijo** (siempre el mismo tiempo).
   * - Por tramo o por parada
     - Si la operación se cuenta una vez por parada o una vez por cada tramo que se entrega en
       ella. Descargar cuatro tramos en un mismo muelle suma cuatro veces el tiempo por tramo
       y una sola vez el tiempo por parada.
   * - Por operación o por kilos
     - Si el tiempo es fijo por operación o proporcional al peso.
   * - Los kilos por defecto
     - El peso que se asume en planta baja y en pisos cuando la línea no trae peso.

El Proyecto elige un esquema. Al calcular una parada, el sistema evalúa cada línea contra los
datos del contacto (dificultad de aparcamiento, ascensor, pisos) y el peso de la parada, elige
la celda de la matriz que corresponde y suma los segundos. El resultado se guarda en la parada
y lo consumen el optimizador, la secuenciación, el cálculo de ruta y la ETA. Campos del esquema,
las líneas, los detalles y las operaciones en :doc:`/17.0/annexes/A_11_tiempos-servicio`.

4.3.6 Horas de conducción
~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_3_06 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_06_horas-conduccion.png
      :alt: Formulario de un preset de Horas de Conducción

      Un preset de Horas de Conducción con sus ajustes para PTV.

Las Horas de conducción (``tms.driver.working.hours``) son los presets de jornada y regulación
que se envían a PTV. No calculan nada por sí mismas: dicen qué restricción de tiempo de
conducción debe respetar el optimizador, la secuenciación y el cálculo de ruta. El catálogo
viene con el reglamento europeo 561/2006 configurado.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Ajuste de secuenciación y ajustes de optimización
     - Los dos presets de PTV, uno por servicio: las regulaciones europea y americana en sus
       variantes de un día, día largo o varios días.
   * - Pausas de trabajo y de conducción
     - Las pausas explícitas (cuánto se puede trabajar o conducir seguido y cuánto dura la
       pausa), que usará el optimizador OptiFlow.
   * - Duración máxima de ruta
     - El tope de horas de una ruta bajo esta regla, si la categoría de vehículo no fija el suyo.

El preset llega a PTV desde la categoría de vehículo, cuando el viaje se optimiza sin franja,
o desde la plantilla de la franja del :term:`Plan de disponibilidad de conductores`, cuando
la hay. Una regulación mal elegida produce rutas válidas en el papel e imposibles dentro de la
jornada permitida. Campos en :doc:`/17.0/annexes/A_12_horas-conduccion`.
