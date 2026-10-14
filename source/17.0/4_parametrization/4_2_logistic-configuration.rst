4.2 Configuración logística
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes, bloque **Optimización de ruta** (Equipamientos, Categoría de
   Carga) y bloque **Datos auxiliares** (Regla de tarifa, Tipos de Bulto). Las categorías y los
   modelos de vehículo están en TMS › Maestros › Equipos.

La configuración logística describe la mercancía y los vehículos: qué se transporta, cómo se
mide, qué necesita el vehículo para llevarlo y cuánto cabe en cada tipo de vehículo. Son cinco
maestros pequeños, pero de ellos dependen tres cosas grandes: que el optimizador solo proponga
vehículos capaces de llevar la carga, que las líneas de mercancía se midan igual en toda la
casa, y que las capacidades con las que se planifica sean las reales.

Cada maestro se describe aquí por lo que decide el cliente. La lista completa de campos de
cada pantalla está en el :doc:`anexo A </17.0/annexes/index>`.

4.2.1 Equipamientos
~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_2_logistic-configuration_01_equipamientos.png
   :alt: Lista de Equipamientos

   Equipamientos: lo que un vehículo lleva instalado.

Un Equipamiento (``tms.equipment``) es algo que un vehículo lleva o puede ofrecer: plataforma
elevadora, equipo de frío, homologación ADR, jaula, transpaleta, doble tripulación. El maestro
no dice qué vehículos lo tienen; eso se marca en cada categoría de vehículo y, si hace falta,
en el vehículo concreto. Lo que hace es dar nombre a la capacidad para que la mercancía pueda
exigirla y el optimizador pueda comprobarla.

El cliente decide poco al crearlos:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué equipamientos existen
     - Solo se pueden exigir capacidades que estén en el catálogo. Conviene crear los que de
       verdad condicionan la asignación, no un inventario exhaustivo del vehículo.
   * - El código
     - Es la clave con la que el optimizador empareja lo que exige la carga con lo que tiene el
       vehículo. El nombre se traduce y el código no: una vez en uso, no se cambia.

Los equipamientos se exigen desde tres sitios: la categoría de carga (una carga refrigerada
exige frío), el tipo de bulto y el Proyecto (toda la operativa del proyecto exige plataforma).
Al planificar, el Tramo exige la unión de todos ellos y el optimizador descarta los vehículos
que no los tengan. Cómo se aplica en la práctica está en
:doc:`/17.0/5_operational-flows/5_2_trip-generation`; los campos, en
:doc:`/17.0/annexes/A_01_equipamientos`.

4.2.2 Categorías de carga
~~~~~~~~~~~~~~~~~~~~~~~~~

Una Categoría de carga (``tms.load.category``) clasifica la naturaleza logística de la
mercancía: refrigerada, seca, paletizada, frágil, ADR, voluminosa. No dice qué es el bulto
(eso es el tipo de bulto) ni cómo se mide (eso es la regla de tarifa): dice cómo hay que
tratarla y con qué puede viajar.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Equipamiento requerido
     - Qué debe llevar el vehículo para transportar esta carga. Es la forma normal de exigir
       equipamiento: se declara una vez en la categoría y la heredan todos los tramos que la
       lleven.
   * - Equipamiento incompatible
     - Qué no puede llevar el vehículo que transporte esta carga (un equipo de frío encendido
       con mercancía que no admite frío, por ejemplo). No se puede exigir y excluir lo mismo.
   * - Incompatible con
     - Qué categorías no pueden ir juntas en el mismo vehículo a la vez (alimentación y
       productos químicos, por ejemplo). Basta declararlo en una de las dos.

Las categorías se asignan en el Proyecto, como lo que la operativa mueve, y en la categoría de
vehículo, como lo que el vehículo admite. **La que manda al planificar es la del Tramo**, que la
hereda de la Orden y del Proyecto: los servicios de PTV leen de ella el equipamiento exigido y el
excluido, y un Tramo cuyo vehículo no cumple queda fuera del plan o marcado (ver
:ref:`que-restringe`). Campos en :doc:`/17.0/annexes/A_02_categorias-carga`.

4.2.3 Reglas de tarifa: la unidad de medida
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_2_logistic-configuration_03_reglas-tarifa.png
   :alt: Lista de Reglas de tarifa

   Las Reglas de tarifa: qué se mide en cada una (bultos, cantidad, metros, palés) y sus medidas
   por defecto..

La :term:`Regla de tarifa` (``tms.pricelist.rule``) define **cómo se mide** una línea de
mercancía dentro de una Orden: por bultos, por palés, por cantidad o por metros lineales. A
pesar del nombre, este maestro **no lleva precios**: qué magnitud se cobra lo dice la
:term:`Tarifa base` y cuánto vale, las :term:`Líneas de tarifa <Línea de tarifa>`; la
diferencia entre las tres se explica al inicio de :doc:`4_4_economic-configuration`. Aquí se
decide qué magnitudes existen y qué implica cada una.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Físico o no
     - Una regla física genera un Bulto por unidad, con su código de barras: se etiqueta, se
       escanea y se traza. Una regla no física (cantidad, metros) es un dato de la línea: no hay
       bultos que escanear.
   * - Qué magnitudes pide
     - Bultos, Cantidad, Metros o Palés, solas o combinadas. Una
       regla de palés que también
       pide bultos permite declarar «3 palés con 40 bultos».
   * - Dimensiones y peso por defecto
     - Cuando la línea no trae medidas, el sistema calcula el volumen y el peso con estos
       valores. En operativas de bulto estándar evitan teclear las medidas en cada orden.
   * - Cliente
     - Una regla puede ser exclusiva de un cliente que mide su mercancía a su manera.

Las reglas más habituales son cuatro. **Bultos**: la unidad es el bulto individual; el sistema
pide el número de unidades, calcula el volumen, genera un registro por bulto y permite el
escaneo. **Palés**: igual, con el palé como unidad. **Cantidad**: unidades que no se trazan
una a una; no hay bultos ni códigos. **Metros**: metros lineales de ocupación.

Cada línea de mercancía lleva una regla de tarifa y un tipo de bulto, y los dos son
complementarios: la regla dice cómo se mide y el tipo qué es. En el Proyecto, las líneas por
defecto fijan la regla con la que se crean las líneas cuando el fichero no las trae. Campos en
:doc:`/17.0/annexes/A_03_reglas-tarifa`.

4.2.4 Tipos de bulto
~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_2_logistic-configuration_04_tipos-bulto.png
   :alt: Lista de Tipos de Bulto

   Tipos de Bulto: qué mercancía se transporta.

El Tipo de Bulto (``tms.temperature``) responde a **qué mercancía** se transporta: seco,
refrigerado, congelado, frágil, textil, alimentación. En la interfaz aparece siempre como
Tipos de Bulto.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Rango de temperatura
     - En los tipos de temperatura controlada, los grados mínimo y máximo. Una lectura fuera
       del rango es una excursión. Un tipo con los dos a cero no tiene rango y no se controla.
   * - Equipamientos
     - Lo que el vehículo necesita para llevar este tipo (frío, por ejemplo).
   * - Imagen
     - El icono que ven el conductor en la app y el operario en las etiquetas.

El tipo de bulto viaja en cada línea de mercancía junto a la regla de tarifa, llega por fichero
y por API, y el Proyecto activa cuáles admite y cuál propone por defecto. Campos en
:doc:`/17.0/annexes/A_04_tipos-bulto`.

4.2.5 Categorías y modelos de vehículo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_2_logistic-configuration_02_vehiculos.png
   :alt: Categoría de vehículo con sus capacidades

   Una categoría de vehículo: perfil de PTV, capacidades y equipamientos.

La Flota de Odoo organiza los vehículos en marcas, modelos y categorías de modelo. El TMS
planifica con la **categoría** (``fleet.vehicle.model.category``): tráiler, camión de 12
toneladas, furgoneta. El **modelo** (``fleet.vehicle.model``) aporta los datos técnicos del
vehículo concreto, y el TMS lo extiende con lo que PTV necesita para el cálculo de ruta, los
peajes y las emisiones.

Lo que el cliente decide en la categoría es lo que el optimizador va a respetar:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Perfil Vehículo
     - El perfil de red viaria de PTV (tráiler, camión pesado, camión ligero, furgoneta; los
       perfiles exactos están en el anexo).
       Determina por dónde puede circular el vehículo y a qué velocidad: es el dato que más
       cambia distancias y tiempos.
   * - Las seis capacidades
     - Peso, volumen, bultos, palés, cantidad y metros máximos. El optimizador no llena un
       vehículo por encima de ninguna de ellas. Un vehículo concreto puede tener las suyas.
   * - Equipamientos y categorías de carga
     - Lo que llevan y lo que admiten los vehículos de la categoría. Es la otra mitad de la
       compatibilidad con la mercancía.
   * - Inicio, fin y límites del Viaje
     - Dónde arranca y termina el Viaje (la base, el hub), en qué franja horaria, y los
       kilómetros y las Paradas máximos por Viaje.
   * - Horas de conducción
     - El :term:`perfil de jornada <Perfil de jornada>` que se envía a PTV cuando el Viaje no
       viene de una franja del Plan de disponibilidad (ver
       :ref:`17.0/4_parametrization/4_3_planning-configuration:4.3.6 Horas de conducción`).
   * - Costes por hora, por kilómetro y por parada
     - Lo que cuesta mover un vehículo de la categoría. Son lo que el motor de optimización
       minimiza y lo que decide la mejor candidata en Encontrar ruta; el vehículo concreto los
       hereda mientras no tenga los suyos. Los valores de serie (21,26 €/h, 0,103 €/km,
       1,60 €/parada) son un punto de partida: una furgoneta y un carrozado no cuestan lo mismo.
   * - Modelo de referencia
     - El modelo de vehículo con el que se calcula la ruta cuando el Viaje aún no tiene vehículo
       concreto: de él salen pesos, dimensiones, motor, clase Euro y distintivo DGT. Sin modelo
       de referencia, el Viaje sin vehículo se enruta con el perfil genérico.
   * - Zonas operativas permitidas
     - A qué áreas de la red puede ir un vehículo de la categoría (el vehículo concreto puede
       tener las suyas). Sin ninguna, sirve a todas. Solo cuentan si la optimización se lanza
       con **Respetar zonas operativas**.

**El vehículo concreto.** Cada vehículo tiene, en su pestaña **Parámetros de optimización**,
los mismos datos que su categoría: capacidades, equipamientos, inicio y fin, límites de ruta y el
grupo **Optimizador** (duraciones máximas, compacidad, equilibrio, factor de velocidad, tráfico).
Al darle o cambiarle la categoría en la ficha, todos esos valores **se sobrescriben** con los de
la categoría nueva, también los que se habían ajustado a mano: después se corrigen las
excepciones. Los cuatro costes son la excepción: no se copian, el vehículo usa los de su
categoría mientras los suyos estén vacíos, así que cambiar un coste en la categoría llega a todos
los vehículos que no tengan uno propio. Casi todo el grupo Optimizador solo lo usa PTV OptiFlow
(ver :ref:`17.0/1_introduction/1_4_technological-architecture:1.4.2.1 Dos motores de optimización`).

En el modelo, los datos que importan son los físicos y ambientales: pesos autorizados y en
vacío, ejes y neumáticos, dimensiones exteriores e interiores, tipo de motor, combustible y
consumos, clase Euro, el **distintivo DGT** (B, C, ECO o 0 emisiones) y las **autorizaciones de
zonas de bajas emisiones** (las ZBE concretas en las que el modelo puede entrar aunque su
distintivo no llegue al mínimo). Con ellos PTV aplica las restricciones viarias, calcula los
peajes y las emisiones de cada Viaje con el vehículo real y decide qué vehículo puede entrar en
cada :term:`ZBE <Zona de bajas emisiones>`. **Antes de dar de alta la primera ZBE hay que
rellenar el distintivo de los modelos**: un vehículo sin distintivo ni autorización no recibe
ninguna Parada dentro de una.

La categoría es el criterio de asignación por excelencia: el Optimizador de Paradas en modo
por categoría pregunta cuántos vehículos de cada una hay disponibles, el Proyecto activa las
que admite, y las tarifas pueden fijar precios distintos por categoría. Campos en
:doc:`/17.0/annexes/A_05_categorias-vehiculo` y :doc:`/17.0/annexes/A_06_modelos-vehiculo`.

.. _que-restringe:

4.2.6 Qué restringe a qué
~~~~~~~~~~~~~~~~~~~~~~~~~

Los maestros de este capítulo y los del siguiente se cruzan en el momento de planificar. Esta
tabla resume qué compara el sistema y qué hace cuando no encaja; es la que hay que tener delante
cuando una Parada «no entra» en ningún Viaje.

.. list-table::
   :header-rows: 1
   :widths: 22 30 24 24

   * - La mercancía (el Tramo)
     - El vehículo (o su categoría)
     - Cómo se comprueba
     - Si no encaja
   * - Equipamiento exigido y excluido por su categoría de carga
     - Sus equipamientos
     - Siempre, por el código del equipamiento
     - La optimización no le asigna ese vehículo; una secuenciación marca ``EQUIPMENT``
   * - Categorías de carga incompatibles entre sí
     - —
     - En la optimización
     - Los dos Tramos no comparten vehículo
   * - Peso, volumen, bultos, palés, cantidad y metros
     - Sus seis capacidades
     - Siempre (en Encontrar ruta, contra la capacidad que le queda a la ruta)
     - La Parada queda fuera del plan; «Secuenciar todo» la marca ``CAPACITY``
   * - Zona operativa de la Parada (el área de la red en que cae)
     - Sus zonas operativas permitidas
     - Solo con **Respetar zonas operativas** (Estricto o Preferido); sin zonas permitidas, el
       vehículo sirve a todas
     - Estricto: fuera del plan. Preferido: entra, con un coste que el preset fija. Secuenciación:
       marca ``ZONE``
   * - Zona de bajas emisiones en que cae la Parada
     - Distintivo DGT de su modelo y autorizaciones de ZBE
     - Siempre, en toda optimización de la compañía con ZBE dibujadas; el distintivo alcanza el
       mínimo del área **o** el área está autorizada
     - Fuera del plan; secuenciación y cálculo de ruta marcan ``LEZ``
   * - Franja horaria de la Parada
     - Jornada y horario de salida del vehículo y del conductor
     - Siempre, ampliada con la tolerancia si se aplica
     - Fuera del plan o, con «Sacar todo como sea», dentro con la ventana violada y el estado
       *Fuera de ventana*
   * - Coordenadas de la Parada
     - Hub de salida
     - Control previo: país distinto o más lejos que la distancia máxima
     - No se envía: ``GEO_SUSPECT``
