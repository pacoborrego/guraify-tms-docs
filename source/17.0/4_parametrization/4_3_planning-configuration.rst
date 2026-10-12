4.3 Configuración de planificación
----------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración: Planes de Transporte, Áreas Geográficas y Tiempos de Servicio. TMS ›
   Configuración › Ajustes: «Plannings» y Franjas Horarias en **Datos auxiliares**; Operación
   de tiempos de servicio y Horas de Conducción en **Optimización de ruta**.

La configuración de planificación define cómo se agrupan las operaciones, sobre qué
territorio, con qué horarios y cuánto duran. Son los seis maestros con los que las Paradas se
convierten en Viajes planificables: el Planning, los Planes de transporte, las Áreas
geográficas, las Franjas horarias, los Tiempos de servicio y las Horas de conducción. La lista
completa de campos de cada uno está en el :doc:`anexo A </17.0/annexes/index>`.

4.3.1 Planning
~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_3_planning-configuration_04_planning.png
   :alt: Lista de Plannings

   Los Plannings, cada uno con su plan de transporte y su modo de división.

El :term:`Planning` (``tms.planning``) es la segmentación operativa del sistema: agrupa las
Órdenes que comparten una misma lógica de transporte, como última milla, recogidas,
distribución urbana, reparto con hub o larga distancia. No es un Viaje ni un calendario; es la
dimensión que dice «estas operaciones se planifican juntas y así».

El Planning se hereda del Proyecto y se propaga a la Orden, a sus Tramos, a las Paradas y al
Viaje. Por eso una elección equivocada se nota en todas partes: en cómo se agrupan las
Paradas, en qué franjas del Plan de disponibilidad son compatibles, en qué precios aplican.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Plan de transporte
     - La red territorial del Planning. Cuando el sistema resuelve la zona operativa de una
       dirección, solo busca en las áreas de esta red.
   * - Tiempos de recogida y de entrega
     - Los segundos fijos que el Planning añade a cada recogida y a cada entrega cuando sus
       Paradas se envían al optimizador, además del tiempo de servicio calculado para cada
       Parada (ver 4.3.5). Mal calibrados, el optimizador propone Viajes que caben en el papel
       y no en el día.
   * - Modo División Viaje
     - Cómo se reparte el coste de un Viaje entre sus Paradas: por peso, volumen, bultos, palés,
       cantidad, metros lineales, o cada uno combinado con los kilómetros. Es la
       :term:`División de costes`, que se explica en
       :doc:`/17.0/8_economic-administration/8_3_cost-split`.
   * - Aplicar tolerancia y minutos antes / después
     - Si las franjas horarias de las Paradas se envían a PTV **ampliadas** unos minutos por
       cada lado (:term:`Tolerancia de ventana`), y cuántos. Es lo que propone el asistente al
       optimizar y lo que usan Secuenciar Viaje y el cálculo de ruta de los Viajes de este
       Planning. Con la casilla marcada y sin minutos, cada Parada toma los de su zona
       operativa. Una Parada que solo cabe gracias a la tolerancia queda *En tolerancia*, no
       *Fuera de ventana*.

El Planning interviene en cinco momentos. Al **generar Paradas**, forma parte de la clave de
agrupación: dos operaciones en la misma dirección y franja no se juntan si son de Plannings
distintos. Al **crear Viajes**, es obligatorio y filtra qué franjas del Plan de disponibilidad
sirven para esa fecha. Al **optimizar**, aporta sus tiempos de recogida y de entrega. Al
**tarificar**, las Líneas de tarifa pueden limitarse a uno o varios Plannings, de modo que
reparto, recogida o urgente tengan precios distintos. Y en las **importaciones**, el fichero
puede traer el Planning de cada Viaje. Su plan de transporte aporta además las **zonas
operativas** que los motores comparan con las permitidas a cada vehículo (ver
:ref:`que-restringe`). Campos en :doc:`/17.0/annexes/A_07_planning`.

4.3.2 Planes de transporte
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_3_planning-configuration_01_planes-transporte.png
   :alt: Lista de Planes de Transporte

   Los Planes de Transporte, cada uno con su agencia.

El :term:`Plan de transporte` (``tms.transport.plan``) es la red territorial de una operativa:
el conjunto de áreas geográficas por las que circula, y la agencia responsable. No es un Viaje
ni una tarifa. Delimita qué polígonos forman una red y qué agencia y hub debe heredar una
dirección que caiga dentro de uno de ellos.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Áreas
     - Las áreas de tipo «Plan de Transporte» que forman la red. Una dirección fuera de todas
       ellas queda sin zona operativa, salvo que el Proyecto pida asignar la más cercana (ver
       :doc:`4_5_project-configuration`).
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

.. figure:: /_static/img/4_parametrization/4_3_planning-configuration_02_areas-geograficas.png
   :alt: Lista de Áreas Geográficas

   Las Áreas Geográficas: su tipo (plan de transporte, zona de tarifa, extra), su agencia, su hub
   y sus franjas.

El :term:`Área geográfica` (``tms.area``) es un polígono, o un multipolígono, dibujado sobre el
mapa con un uso asignado. La misma entidad sirve para cinco cosas, que distingue su tipo:
«Plan de Transporte» (área operativa de una red), «Zona Tarifa», «Tarifa Extra» (suplemento por
entrar en un territorio), «Operación Artículo» y «Bajas emisiones». Cómo se dibujan, se
importan de OpenStreetMap y se comprueba la pertenencia de una coordenada está en
:doc:`/17.0/1_introduction/1_4_technological-architecture`. Aquí, lo que se decide al
configurarlas:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Tipo
     - Para qué sirve el área. Un mismo territorio puede existir dos veces con dos tipos, una
       para operar y otra para tarificar, y evolucionar por separado.
   * - Código
     - La clave con la que los motores de optimización nombran la zona (se genera del nombre si
       se deja vacío; único por compañía). Como el código de un equipamiento, una vez en uso no
       se cambia.
   * - Agencia y hub
     - Lo que heredan los tramos cuya dirección cae en el área.
   * - Tolerancia antes / después (min)
     - Los minutos de :term:`tolerancia <Tolerancia de ventana>` propios de esta zona operativa,
       que se aplican a sus Paradas cuando el Planning pide tolerancia sin fijar los suyos. Una
       zona de polígonos industriales puede admitir más margen que un centro urbano.
   * - Distintivo DGT mínimo (solo Bajas emisiones)
     - El distintivo (B, C, ECO o 0 emisiones) que un vehículo necesita para entrar en esta
       :term:`ZBE <Zona de bajas emisiones>`. Un vehículo entra si el distintivo de su modelo lo
       alcanza o si tiene el área entre sus autorizaciones; sin mínimo, solo entran los
       autorizados. Es obligatorio en un área de bajas emisiones.
   * - Días disponibles
     - Los días de la semana en que la zona operativa admite servicio. Una carga o descarga
       fuera de ellos se avisa antes de planificar.
   * - Franjas horarias
     - Las ventanas válidas en el área, como referencia para el planificador.

En el flujo operativo, las áreas de tipo «Plan de Transporte» etiquetan cada carga y descarga
con su zona operativa; el sistema no las recalcula en operaciones cerradas o facturadas. En el
flujo económico, las de tipo «Zona Tarifa» deciden qué detalle de tarifa aplica, y las de tipo
«Tarifa Extra» permiten suplementos por entrar en un territorio concreto. Las de tipo **«Bajas
emisiones»** con polígono cuentan para **toda** optimización de la compañía, siempre de forma
estricta y sin casilla que las apague: ningún motor asigna una Parada dentro de una ZBE a un
vehículo que no puede entrar, y el cálculo de ruta marca las Paradas que la cruzan. Por eso, antes
de dibujar la primera, los modelos de vehículo tienen que llevar su distintivo
(:doc:`4_2_logistic-configuration`). Las zonas de tipo «Plan de Transporte» son, además, las
**zonas operativas** que el motor compara con las permitidas a cada vehículo cuando se le pide
**Respetar zonas operativas**. Campos en :doc:`/17.0/annexes/A_09_areas-geograficas`.

.. CAPTURA: 4_3_06 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_06_zbe.png
      :alt: Área geográfica de tipo Bajas emisiones con su distintivo DGT mínimo

      Un área de bajas emisiones: polígono, código y distintivo DGT mínimo.

4.3.4 Franjas horarias
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_3_planning-configuration_05_franjas-horarias.png
   :alt: Lista de Franjas Horarias

   Franjas Horarias: ventanas de servicio reutilizables.

La :term:`Franja horaria` (``tms.time.zone``) es una ventana de servicio con nombre, de una
hora de inicio a una de fin, que se elige en lugar de teclear las horas en cada operación. El
nombre se compone automáticamente con las dos horas («09:00 - 14:00»).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué franjas existen
     - Las ventanas estándar de la operativa (de 9 a 14, de 15 a 19). Al elegir una en la
       carga o la descarga de un Tramo, el sistema copia sus horas a la operación.
   * - Tipos de servicio
     - Con qué servicios se puede usar cada franja.

Si en una operación se escribe una franja personalizada en vez de elegir una del catálogo, el
sistema avisa de que puede tener coste adicional: así se separa la ventana estándar de la
excepción. Qué horas se aplican cuando la Orden no trae horario lo decide el Proyecto (ver
:doc:`4_5_project-configuration`). Campos en :doc:`/17.0/annexes/A_10_franjas-horarias`.

4.3.5 Tiempos de servicio
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_3_planning-configuration_03_tiempos-servicio.png
   :alt: Lista de esquemas de Tiempos de Servicio

   Los esquemas de Tiempos de Servicio con sus kilos por defecto.

El :term:`Tiempo de servicio` (``tms.service.time``) calcula cuánto dura una Parada más allá
de la conducción: aparcar, bajar la mercancía, subirla a un piso, esperar en un muelle. Sin él,
la duración de los Viajes y las horas estimadas de llegada dependerían solo de los kilómetros.
El maestro es el **esquema** de tiempos de servicio, que el Proyecto elige; un esquema se
compone de líneas, y cada línea de una operación y de una matriz de detalles.

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

.. figure:: /_static/img/4_parametrization/4_3_planning-configuration_06_horas-conduccion.png
   :alt: Formulario de un perfil de jornada (Horas de Conducción)

   Un perfil de jornada con sus ajustes para PTV.

Las Horas de conducción (``tms.driver.working.hours``) son los :term:`perfiles de jornada
<Perfil de jornada>` que se envían a PTV. No calculan nada por sí mismas: dicen qué regulación
de tiempos de conducción y de trabajo debe respetar el optimizador, la secuenciación y el
cálculo de ruta. El catálogo viene con el reglamento europeo 561/2006 configurado.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Ajuste de secuenciación y ajuste de optimización
     - Los dos ajustes de PTV, uno para la secuenciación y otro para la optimización completa:
       la regulación europea de tiempos de conducción, la directiva europea de tiempo de
       trabajo o la regulación estadounidense, en sus variantes de un día, día largo, varios
       días y conducción en equipo. Los códigos exactos están en el anexo.
   * - Pausas de trabajo y de conducción
     - Las pausas explícitas (cuánto se puede trabajar o conducir seguido y cuánto dura la
       pausa), que se declaran aquí para los servicios de optimización que las admiten.
   * - Duración máxima del Viaje
     - El tope de horas de un Viaje bajo esta regla, si la categoría de vehículo no fija el
       suyo.

El perfil llega a PTV desde la franja del :term:`Plan de disponibilidad de conductores`,
cuando el Viaje sale de una, y si no desde la categoría del vehículo. Una regulación mal
elegida produce Viajes válidos en el papel e imposibles dentro de la jornada permitida. Campos
en :doc:`/17.0/annexes/A_12_horas-conduccion`.

.. _presets-optimizacion:

4.3.7 Presets de optimización
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Presets de optimización (solo responsables)

.. CAPTURA: 4_3_07 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_3_planning-configuration_07_presets.png
      :alt: Lista de Presets de optimización

      Los cuatro presets de serie, con las casillas que marcan por defecto.

Un :term:`Preset de optimización` (``tms.ptv.preset``) dice **para qué se optimiza**: qué
persigue el motor cuando construye los Viajes y qué está dispuesto a sacrificar. Antes el TMS
enviaba siempre lo mismo; ahora el planificador elige el preset al lanzar la optimización
(asistente Asignar en modo Optimización, Encontrar ruta) y el preset rellena las casillas de lo
que se permite violar, que el planificador puede cambiar en ese momento. Vienen cuatro de serie:

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Preset
     - Qué hace
   * - **Máxima calidad**
     - El mejor plan que el motor encuentra respetando todos los límites: la búsqueda más larga,
       la calidad alta y los costes reales de cada vehículo. Es el punto de partida.
   * - **Máxima rentabilidad**
     - Solo planifica una Orden si su importe paga lo que añade a la ruta; el resto queda fuera.
       Necesita los costes de los vehículos y el importe de los Tramos. Hoy, con los importes de
       Tramo que se envían, no llega a planificar nada: está pendiente de decidir de dónde sale
       el ingreso.
   * - **Balancear vehículos**
     - Reparte el trabajo: duraciones de ruta parecidas, sin coste fijo por usar un vehículo
       más y con un coste por dejar uno parado. En la práctica consigue que salgan todos los
       vehículos, pero no iguala las rutas.
   * - **Sacar todo como sea**
     - Planifica todas las Órdenes cueste lo que cueste: aplica la tolerancia de ventanas y
       convierte jornada, kilómetros, Paradas y carga en costes en vez de límites. Solo la
       conducción máxima sigue siendo un límite duro, porque es ley. Es la última herramienta,
       no la primera: enseña lo que no cabe.

Cada preset fija, además, el **motor** al que se aplica, la duración de la búsqueda, la
compacidad, la preferencia por equilibrar, el uso de los costes del vehículo o de los suyos
propios, los límites blandos y su coste, y las **casillas que marca por defecto**: aplicar
tolerancia, permitir violar restricciones de vía, permitir violar jornada, km, Paradas y carga,
respetar zonas operativas (y el coste de no respetarlas en modo Preferido). Un preset es por
compañía; crear uno nuevo es copiar el que más se parece y ajustar. Campos en
:doc:`/17.0/annexes/A_29_presets-optimizacion`.
