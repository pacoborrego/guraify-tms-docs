Arquitectura tecnológica
--------------------------------

Guraify TMS está construido sobre una arquitectura modular y desacoplada que separa claramente la capa de datos, la lógica de negocio y la capa de presentación, siguiendo las buenas prácticas del framework Odoo y principios de diseño orientados a escalabilidad.

El sistema no es una aplicación monolítica, sino un ecosistema compuesto por varios bloques tecnológicos que interactúan entre sí de forma controlada: la plataforma ERP base, el módulo TMS, el motor de optimización, la capa de integración externa y la aplicación móvil operativa.

Esta arquitectura permite evolucionar cada componente sin comprometer la estabilidad del núcleo funcional.

Plataforma base Odoo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El núcleo del sistema es Odoo, que proporciona la infraestructura ORM, el modelo de seguridad por roles, la capa de vistas, el motor de automatizaciones y la integración nativa con módulos financieros y analíticos.

El módulo Guraify TMS se implementa como extensión sobre esta base, reutilizando:

- Gestión contable y facturación.

- Gestión de empleados y contactos.

- Gestión de flota.

- Proyectos.

- CRM.

- Gestión documental.

- Acciones automáticas y programadas.

Esta decisión permite que el TMS no sea un sistema aislado, sino una especialización logística dentro de un ERP horizontal.

Integración con PTV 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La integración con PTV en Guraify TMS se articula en tres niveles de uso progresivos: Routing, Secuenciación y Optimización completa con OptiFlow. Todos ellos se apoyan en la misma base: la entidad planificable sigue siendo la Parada y la unidad de ejecución el Viaje; PTV aporta la inteligencia matemática sobre esta estructura, no la sustituye.

Routing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En el nivel de Routing, el Viaje ya existe en el TMS (paradas asignadas y recurso definido) y lo que se hace es enriquecerlo con la red viaria profesional de PTV, utilizando la Routing API. Esta API trabaja con waypoints (los puntos del viaje), parámetros de vehículo y contexto temporal para calcular distancias, tiempos, ETAs, peajes, costes y emisiones.

**Parámetros que se toman de los maestros del TMS**

Desde Guraify se construye la petición a PTV a partir de:

- Maestro de localizaciones y de paradas: coordenadas geográficas de cada parada, orden actual, tipo de parada (recogida, entrega, hub) y, cuando aplica, ventanas horarias y tiempos de servicio configurados por tipo de cliente o tipo de operación. Estas ventanas y tiempos se trasladan a PTV como *opening intervals* y *service times* para que el cálculo respete la realidad operativa.

- Maestro de vehículos: perfil de vehículo (camión rígido, tráiler, furgoneta, eléctrico), dimensiones y capacidades (peso máximo, volumen, ejes, altura), restricciones de mercancías peligrosas o refrigeradas y, cuando aplica, costes asociados al vehículo (coste por km, por hora, etc.), que se mapean con los *vehicle parameters* y la lógica de *monetary costs* de la API.

- Maestro de calendarios y planificación: fecha y hora de salida previstas del viaje, zona horaria y, opcionalmente, reglas de horas de conducción y descanso del conductor, que se trasladan a PTV a través de los parámetros de *date and time* y *drivers’ working hours*.

**Resultados que vuelven y se exponen en el TMS**

La respuesta de Routing se vuelca de nuevo en el Viaje y en sus Paradas:

- Geometría de ruta (polilínea) asociada al Viaje, para representación en mapa.

- Distancia total y por segmento entre paradas, tiempo de conducción y de servicio, y tiempo total de ruta.

- ETA calculada por parada, indispensable tanto en planificación como en seguimiento en ejecución.

- Información de peajes y costes cuando se activan las opciones de *toll* y *monetary costs*, y, si se configura, emisiones estimadas (CO₂, etc.) usando la funcionalidad de *emissions*.

En operativa, esto permite recalcular la ETA durante la ejecución, combinando la ruta planificada de PTV con la posición real del conductor obtenida desde la app móvil, de modo que el Viaje en Guraify se convierte en un objeto dinámico que refleja la situación real y no solo el plan teórico.

Secuenciación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En el nivel de Secuenciación, las paradas ya están asignadas a un Viaje, pero su orden no es óptimo. Aquí se usa la Sequence Optimization API, que trabaja con el concepto de *locations, transports and stops*, vehículo y conductor, tiempos de servicio, ventanas horarias y prioridades de transporte para devolver el mejor orden posible de ejecución.

.. _parámetros-que-se-toman-de-los-maestros-del-tms-1:


'''''''''''''''''''''''''''''''''''''''''''''''''''

La petición a PTV se construye con:

- Las Paradas del Viaje como *stops*, cada una con su localización, tiempo de servicio, ventana horaria y, cuando aplica, prioridad (por ejemplo, entregas urgentes o condicionadas a cut-off horarios).

- El Vehículo asignado al Viaje como *vehicle*, incluyendo capacidades básicas (peso, volumen, pallets) y restricciones (ADR, refrigerado, etc.), así como el perfil de conducción.

- El Conductor o recurso humano, a través de parámetros de jornada máxima, pausas y reglas de horas de trabajo, reutilizando las reglas internas del TMS y mapeándolas a los parámetros de *drivers’ working hours*.

A nivel de configuración, el planificador puede definir el objetivo de optimización (minimizar distancia, tiempo, retrasos respecto a ventanas, etc.), que se mapea a la configuración de *objective of optimization* de PTV.

.. _resultados-que-vuelven-y-se-exponen-en-el-tms-1:


'''''''''''''''''''''''''''''''''''''''''''''''''

La secuenciación devuelve:

- Un nuevo orden de paradas dentro del Viaje, con su posición en ruta.

- Horarios previstos de llegada y salida por parada, ya ajustados a ventanas horarias y tiempos de servicio.

- Indicaciones de posibles violaciones (ventana no cumplible, jornada de conductor excedida) cuando la secuenciación no puede respetar todas las restricciones, apoyándose en la lógica de *drivers’ working hours* y *violations*.

En Guraify, esto se traduce en una reordenación de las Paradas del Viaje, con actualización de ETAs y KPIs de ruta (km, duración, nivel de servicio), manteniendo la vinculación de cada parada con su Tramo y su Orden para no romper el modelo estructural.

Optimización completa
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El nivel más avanzado utiliza Route Optimization OptiFlow API. Aquí ya no hablamos solo de ordenar paradas dentro de un viaje existente, sino de dejar que PTV proponga el plan completo de asignación y secuenciación de las paradas a viajes, en base a órdenes, vehículos, depósitos y un conjunto rico de reglas y restricciones.

OptiFlow trabaja con el concepto de Orders, que en su terminología representan peticiones de transporte o servicio (pickup, delivery, pickup–delivery o servicio puro), con cargas, categorías, ventanas horarias, tiempos de servicio y parámetros económicos como *outsourcing cost* e *insourcing revenue* para ayudar a decidir qué pedidos merece la pena planificar o dejar fuera.

.. _parámetros-que-se-toman-de-los-maestros-del-tms-2:

**Parámetros que se toman de los maestros del TMS**


En este caso, el mapeo desde Guraify hacia OptiFlow es más rico:

- Las Órdenes / Paradas del TMS se transforman en Orders y Tasks de OptiFlow: para un simple reparto desde hub serán típicamente *delivery orders*; para un transporte origen–destino, *pickup-delivery orders*; para ciertos servicios de solo visita, *service orders*. Cada task incorpora localización, ventanas horarias y tiempo de servicio.

- Las cargas (peso, volumen, pallets, metros lineales, etc.) se toman de las líneas o de los bultos asociados en Guraify y se mapean a los *loads* del order para controlar capacidades de los vehículos.

- Las categorías de pedido (temperatura controlada, ADR, requisitos de equipamiento) se mapean a *order categories*, que luego se cruzan con las categorías de vehículos, depósitos y recursos para asegurar compatibilidad.

- Los Vehículos del maestro de flota se convierten en *vehicles/resources* de OptiFlow, con sus capacidades, costes, restricciones, equipamientos y, si se quiere, perfiles de coste horario y por kilómetro.

- Los Depósitos / Hubs definidos en Guraify se mapean a *depots*, con sus localizaciones, horarios y, en su caso, perfiles de servicio específicos.

- Opcionalmente, se pueden utilizar parámetros económicos de cada pedido para alimentar los campos de *outsourcing cost* e *insourcing revenue*, de forma que el optimizador pueda decidir dejar fuera pedidos poco rentables o priorizar aquellos que aportan mayor margen, de acuerdo a la definición de la propia API.

.. _resultados-que-vuelven-y-se-exponen-en-el-tms-2:

**Resultados que vuelven y se exponen en el TMS**


OptiFlow devuelve un plan de rutas completo: listado de rutas con sus vehículos asignados, secuencias de órdenes/paradas, horarios, ocupación de capacidades y métricas globales de coste y rendimiento.

En Guraify, ese plan se traduce en:

- Creación o actualización de Viajes propuestos, con sus Paradas ya asignadas y secuenciadas.

- Asignación automática de recursos (vehículo y, cuando corresponda, conductor).

- Cálculo de distancias, tiempos y niveles de ocupación por viaje y por tramo.

- Identificación de órdenes no planificadas, junto con la razón (incompatibilidades, sobrecoste, falta de recursos), alineado con la lógica de órdenes “outsourced” que describe OptiFlow.

El usuario del TMS no ve el detalle técnico de la API, sino una propuesta de planificación coherente con el modelo Orden–Tramo–Parada–Viaje. Puede aceptarla tal cual, ajustarla manualmente o combinarla con reglas de negocio propias de la compañía.

.. tip::

   Routing enriquece Viajes existentes.

   Secuenciación optimiza el orden de Paradas.

   OptiFlow propone directamente qué Viajes crear y cómo llenarlos.

   Toda la parametrización nace de los maestros del TMS.

Capa de integración 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El sistema incorpora una capa de integración que permite intercambiar información estructurada con sistemas externos mediante:

- Ficheros CSV o Excel.

- API REST.

- Webhooks.

- Automatizaciones programadas.

Las integraciones no crean estructuras paralelas, sino que alimentan directamente las entidades nativas del modelo (Orden, Tramo, Parada, Viaje). Esto garantiza coherencia entre datos importados y ejecución real.

.. _section-1:

Arquitectura móvil y tecnologías embarcadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La aplicación móvil de Guraify TMS es una extensión operativa del backend. No es únicamente una interfaz de confirmación de entregas, sino un punto activo de generación de datos estructurales que alimentan la trazabilidad en tiempo real,

Es la responsable de actualizar estados, registrar incidencias, capturar POD digitales y sincronizar eventos operativos con el backend en tiempo real

La aplicación móvil de Guraify TMS integra el Scandit Barcode Scanner SDK como motor de captura inteligente de códigos de barras. La tecnología no se utiliza de una única forma, sino que se estructura en tres modos operativos distintos: escaneo simple, escaneo masivo y escaneo en vídeo continuo. Cada uno responde a una necesidad diferente dentro del flujo logístico.

Cada escaneo actualiza automáticamente la trazabilidad y puede activar eventos posteriores como desbloqueo de facturación o liquidación, recalculos de ETA o envío de alertas.

.. _section-2:

.. _section-3:

Tipologías de escaneo
^^^^^^^^^^^^^^^^^^^^^^^^^

Escaneo simple 
''''''''''''''''''''''''''''''''

Es el modo clásico de lectura individual. El usuario enfoca un único código y el sistema lo identifica inmediatamente.

Este tipo de escaneo se caracteriza por:

- Lectura rápida y precisa de un único código.

- Confirmación inmediata.

- Validación directa contra el modelo de datos (bulto, parada, viaje).

- Registro automático del evento en la trazabilidad.

Es el modo más controlado y se utiliza cuando se requiere precisión individual en la validación de mercancía.

Escaneo masivo
'''''''''''''''''''''

El escaneo masivo permite capturar múltiples códigos de forma consecutiva en una misma sesión, validándolos contra el conjunto esperado de bultos asociados a un Viaje o Parada.

A diferencia del modo simple, aquí el objetivo no es validar una unidad concreta, sino verificar el conjunto completo.

El sistema:

- Compara los bultos escaneados con los asignados.

- Detecta faltantes.

- Detecta duplicados.

- Impide validar el proceso si existen inconsistencias.

Este modo actúa como mecanismo de control y verificación global antes de cerrar una fase operativa.

Escaneo en vídeo 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Es el modo más avanzado y diferencial. Utiliza la cámara en modo continuo para detectar múltiples códigos simultáneamente en tiempo real.

El sistema analiza constantemente la imagen capturada y superpone información visual en pantalla:

- Indicador verde si el bulto pertenece al Viaje o Parada.

- Indicador rojo si no corresponde.

- Confirmación inmediata sin necesidad de lectura individualizada.

Este modo permite interacción dinámica y reduce drásticamente el tiempo operativo en escenarios de alto volumen.

.. note::

   El escaneo en vídeo no es una lectura rápida.

   Es validación contextual en tiempo real contra la estructura del Viaje.

Uso dentro del flujo operativo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una vez definidos los modos de escaneo, su aplicación dentro del flujo logístico es la siguiente:

Entrada de mercancía en almacén
'''''''''''''''''''''''''''''''''''

Se utiliza el escaneo simple. Cada bulto que entra en el sistema —ya sea por primera vez o en procesos de devolución— se identifica individualmente, activando su trazabilidad. Aquí prima la precisión individual.

Proceso de removido en hub
''''''''''''''''''''''''''''''

Se utiliza el escaneo en vídeo. El conductor o el operario enfoca las etiquetas y el sistema indica visualmente si cada bulto pertenece o no a su ruta. Esto permite separar rápidamente mercancía correcta de mercancía incorrecta sin validaciones manuales adicionales. Aquí prima la velocidad con validación contextual.

Verificación completa antes de carga
''''''''''''''''''''''''''''''''''''''''

Se utiliza el escaneo masivo. Una vez que el conductor considera que tiene toda la mercancía preparada, el sistema verifica que el conjunto de bultos escaneados coincide exactamente con los asignados al Viaje. Si falta alguno, no se permite validar la salida. Aquí prima el control de coherencia total.

.. important::

   El escaneo masivo es un punto de control previo a la ejecución del Viaje.

Localización de bultos durante el reparto
'''''''''''''''''''''''''''''''''''''''''''''

Durante la ejecución, el conductor puede utilizar el escaneo en vídeo para localizar mercancía dentro del vehículo.

Simplemente enfocando las etiquetas, el sistema le indica si ese bulto corresponde a la parada actual o a una parada posterior. Esto reduce errores de entrega y evita búsquedas manuales innecesarias dentro del vehículo. Aquí prima la asistencia operativa en tiempo real.

.. _section-4:

Confirmación en entrega o recogida
''''''''''''''''''''''''''''''''''''''

Se utiliza principalmente el escaneo masivo, asegurando que:

- Se entregan exactamente los bultos asignados.

- No quedan bultos pendientes.

- Las recogidas se vinculan correctamente a la parada correspondiente.

.. _section-5:

Impacto estructural
^^^^^^^^^^^^^^^^^^^^^^^

En todos los casos, el escaneo no es una acción aislada. Cada lectura genera:

- Actualización de estado del Bulto.

- Registro en el histórico de la Parada.

- Impacto en el estado del Viaje.

- Evidencia operativa trazable.

La tecnología de Scandit actúa como acelerador operativo, pero el resultado siempre es estructural: el modelo de datos se actualiza en tiempo real y mantiene coherencia entre ejecución física y representación digital.

Modelo de geolocalización y normalización de coordenadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Guraify TMS se basa en la geolocalización como fundamento estructural para múltiples procesos: asignación automática a áreas operativas, cálculo de rutas, segmentación tarifaria y planificación por zonas.

Para comprender correctamente este modelo, es necesario distinguir tres conceptos geométricos fundamentales que se utilizan de forma recurrente dentro del sistema:

- Coordenada (punto)

- Polígono (superficie)

- Polilínea (trayectoria)

Estos tres elementos constituyen la base geométrica sobre la que se construyen muchas de las funciones del TMS.

.. _section-6:

Coordenada: la representación puntual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toda entidad que represente una localización física dentro del sistema —punto de entrega, recogida, hub, almacén o cualquier dirección operativa— dispone de una coordenada geográfica compuesta por: Latitud (lat), Longitud (lon)

Esta pareja de valores numéricos define un punto exacto sobre la superficie terrestre. Desde el punto de vista matemático, una coordenada es una posición puntual sin superficie.

En el TMS, cada registro de localización almacena estas coordenadas como parte estructural de su modelo de datos. No se trata de un atributo accesorio; es el elemento que permite:

- Calcular distancias reales.

- Planificar rutas.

- Determinar pertenencia a áreas.

- Aplicar tarifas zonales.

- Evaluar restricciones geográficas.

.. warning::

   Sin coordenada válida no existe planificación fiable.

Polígono: la representación de superficie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mientras que una coordenada representa un punto, un polígono representa una superficie delimitada por un conjunto de vértices conectados.

En Guraify TMS, cualquier entidad que represente un área geográfica —zona operativa, área tarifaria, zona de bajas emisiones, región de planificación o segmento logístico— se modeliza mediante un polígono.

La información del polígono se almacena utilizando el estándar GeoJSON, un formato estructurado ampliamente utilizado para representar geometrías geográficas. Un polígono en GeoJSON está compuesto por una lista ordenada de coordenadas que definen su perímetro.

Este enfoque permite que el sistema pueda responder a preguntas como:

- ¿Esta entrega pertenece a la Zona Norte?

- ¿Este cliente está dentro de un área tarifaria específica?

- ¿Este destino se encuentra dentro de una ZBE (Zona de Bajas Emisiones)?

La lógica que se aplica es puramente geométrica: se comprueba si la coordenada (punto) cae dentro del polígono (superficie).

.. important::

   Una localización es un punto (lat, lon).

   Un área es una superficie (polígono GeoJSON).

   La pertenencia se calcula geométricamente.
.. _section-7:

Polilínea: la representación de una ruta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El tercer elemento geométrico utilizado en el sistema es la polilínea.

Una polilínea representa una trayectoria formada por una secuencia ordenada de coordenadas conectadas entre sí. A diferencia del polígono, no define una superficie cerrada, sino un recorrido.

En el contexto del TMS, las polilíneas se utilizan principalmente para representar la geometría de una ruta calculada por el motor de routing.

Cuando el sistema ejecuta un cálculo de ruta mediante la integración con PTV Routing, el servicio devuelve, entre otros datos:

- Distancia total

- Tiempo estimado

- Segmentos entre paradas

- Rutas alternativas

- Peajes y emisiones

Y también la polilínea de la ruta, que describe el recorrido exacto sobre la red viaria.

Esta polilínea permite:

- Representar gráficamente la ruta en el mapa.

- Visualizar el trayecto real entre paradas.

- Analizar desviaciones entre ruta planificada y ejecución real.

Desde el punto de vista técnico, la polilínea es una lista ordenada de coordenadas que describe el recorrido que debe seguir el vehículo entre origen y destino.

.. _section-8:

Proceso de geolocalización de coordenadas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para que este modelo funcione, cada dirección debe transformarse en una coordenada fiable. Este proceso se denomina geocodificación.

Guraify TMS utiliza un modelo jerárquico de geolocalización basado en dos proveedores: PTV y Google Maps, ambos configurables mediante token en la configuración del sistema Odoo.

El flujo de geocodificación es el siguiente:

1. Se intenta geolocalizar utilizando PTV como primera capa.

2. Se evalúa la calidad del resultado devuelto.

3. Si la calidad es inferior al 80 %, se realiza un segundo intento mediante Google Maps.

4. Si la calidad sigue siendo inferior al 80 %, se asigna automáticamente la coordenada del centroide del código postal o localidad.

En este último escenario, la localización queda marcada como “Normalizable”, lo que implica que la coordenada no es suficientemente precisa y requiere validación manual por parte del usuario antes de utilizarla en una expedición definitiva.

.. important::

   Una coordenada con calidad inferior al 80 % no se considera válida para planificación definitiva.

   Cuando un usuario intenta validar una expedición que utiliza una localización con baja calidad, el sistema obliga a realizar una normalización manual. Este mecanismo no es una excepción operativa, sino un control de calidad estructural que evita errores de planificación, desvíos innecesarios y problemas en la ETA.

   Más adelante en el manual se detallará el procedimiento paso a paso de normalización manual.
.. _section-9:

Gestión y creación de áreas geográficas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para la creación y mantenimiento de áreas (polígonos), el sistema integra servicios basados en OpenStreetMap, plataforma cartográfica de uso libre.

OpenStreetMap se utiliza para:

- Visualizar mapas base.

- Dibujar polígonos manualmente.

- Editar áreas existentes.

- Exportar e importar geometrías en formato GeoJSON.

El uso de OSM permite que la gestión de áreas sea independiente de proveedores propietarios y garantiza flexibilidad en la definición de superficies operativas.

.. _section-10:

Modelo conceptual de asignación geográfica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El funcionamiento interno puede representarse de forma simplificada mediante el siguiente esquema lógico:

.. note::

   Dirección (texto)

   ↓

   Proceso de geocodificación (PTV → Google → Centroide)

   ↓

   Coordenada válida (lat, lon)

   ↓

   Evaluación geométrica

   ¿La coordenada cae dentro de un polígono?

   ↓

   Asignación automática a Área

Desde el punto de vista matemático, el sistema realiza una operación conocida como Point-in-Polygon: se comprueba si un punto definido por latitud y longitud se encuentra dentro de la superficie delimitada por un conjunto de coordenadas que forman un polígono en formato GeoJSON.

Podemos visualizarlo conceptualmente así:

.. note::

   +---------------------------+
   | Área Operativa            |
   | (Polígono GeoJSON)        |
   |                           |
   | •                         |
   | (lat, lon)                |
   | Punto Localización        |
   +---------------------------+
   
   
Si el punto se encuentra dentro de los límites del polígono, la localización queda automáticamente asociada a esa área. Si no pertenece a ningún polígono definido, el sistema puede:

- Dejarla sin asignación.
- Asociarla al área más cercana.
- Requerir intervención manual según configuración.

.. important::

   La asignación a áreas no se basa en texto ni en códigos postales.
   Se basa en geometría real sobre coordenadas verificadas.

Implicaciones prácticas
^^^^^^^^^^^^^^^^^^^^^^^

Este modelo permite que:

- Una misma dirección cambie automáticamente de área si se corrige su coordenada.
- Las tarifas zonales se apliquen de forma automática y coherente.
- Las restricciones geográficas (ZBE, áreas restringidas) se validen antes de planificar.
- La planificación avanzada tenga información espacial fiable.

En definitiva, el sistema no interpreta “direcciones”, interpreta geometría. La dirección textual es solo el punto de partida; la coordenada validada es la base real de toda la lógica espacial del TMS.

.. _section-11:

Impacto arquitectónico
^^^^^^^^^^^^^^^^^^^^^^

La combinación de:

- Coordenadas precisas (lat, lon)
- Polígonos en formato GeoJSON
- Geocodificación jerárquica con control de calidad
- Normalización manual obligatoria cuando procede

permite que la asignación automática a áreas, la tarificación zonal y la planificación avanzada funcionen sobre bases geométricas fiables.

Este modelo convierte la geolocalización en un componente estructural del TMS, no en una funcionalidad accesoria. Sin precisión geográfica no hay planificación fiable, y sin áreas correctamente definidas no existe automatización tarifaria ni segmentación operativa coherente.