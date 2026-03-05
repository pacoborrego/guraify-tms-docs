**1. INTRODUCCIÓN**
===================

**1.1 Objetivo del documento**
------------------------------

El presente documento tiene como finalidad describir la arquitectura funcional y técnica de Guraify TMS, módulo desarrollado sobre la plataforma Odoo ERP para la gestión integral de operaciones de transporte.

No se trata de un manual de usuario final, sino de un manual técnico-funcional orientado a consultores, integradores y perfiles técnicos que necesiten comprender el sistema desde su diseño estructural. El objetivo es proporcionar una visión clara del modelo conceptual, la organización funcional, la lógica económica y las dependencias técnicas, permitiendo entender el comportamiento del sistema sin necesidad de analizar directamente el código fuente.

Este documento sirve como referencia para proyectos de implantación, integración, parametrización avanzada y evolución futura del sistema.

**1.2 Alcance funcional del sistema**
-------------------------------------

Guraify TMS cubre de forma nativa el ciclo completo de gestión del transporte, desde la recepción del encargo del cliente hasta la liquidación económica y el análisis de rentabilidad.

El sistema permite:

- Representar digitalmente órdenes de transporte.

- Descomponerlas en estructuras operativas (tramos y paradas).

- Planificar y optimizar rutas mediante motor avanzado.

- Ejecutar servicios con soporte de aplicación móvil.

- Gestionar liquidaciones a transportistas.

- Automatizar tarificación y facturación.

- Integrarse con sistemas externos mediante API y EDI.

Su alcance funcional abarca tanto operativas de carga completa como grupaje, última milla, distribución capilar o entornos multihub. La arquitectura está diseñada para adaptarse a distintos modelos de negocio sin modificar la estructura base del sistema.

[IMPORTANT]

Guraify TMS no es únicamente una herramienta de planificación.

Es un sistema integral que conecta operativa, economía y análisis.

**1.3 Público objetivo**
------------------------

Este documento está dirigido a:

- Consultores funcionales responsables de implantación.

- Arquitectos de soluciones ERP.

- Equipos técnicos encargados de integraciones.

- Responsables de operaciones que necesiten comprender la lógica estructural.

- Equipos financieros que deban entender la vinculación entre operativa y rentabilidad.

Se presupone conocimiento básico del ecosistema Odoo y de los procesos habituales del sector transporte y logística.

**1.4 Arquitectura tecnológica**
--------------------------------

Guraify TMS está construido sobre una arquitectura modular y desacoplada que separa claramente la capa de datos, la lógica de negocio y la capa de presentación, siguiendo las buenas prácticas del framework Odoo y principios de diseño orientados a escalabilidad.

El sistema no es una aplicación monolítica, sino un ecosistema compuesto por varios bloques tecnológicos que interactúan entre sí de forma controlada: la plataforma ERP base, el módulo TMS, el motor de optimización, la capa de integración externa y la aplicación móvil operativa.

Esta arquitectura permite evolucionar cada componente sin comprometer la estabilidad del núcleo funcional.

**1.4.1 Plataforma base Odoo**
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

**1.4.2 Integración con PTV (detalle técnico)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La integración con PTV en Guraify TMS se articula en tres niveles de uso progresivos: Routing, Secuenciación y Optimización completa con OptiFlow. Todos ellos se apoyan en la misma base: la entidad planificable sigue siendo la Parada y la unidad de ejecución el Viaje; PTV aporta la inteligencia matemática sobre esta estructura, no la sustituye.

**Nivel 1 – Routing: enriquecimiento de Viaje y cálculo de ETA**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En el nivel de Routing, el Viaje ya existe en el TMS (paradas asignadas y recurso definido) y lo que se hace es enriquecerlo con la red viaria profesional de PTV, utilizando la Routing API. Esta API trabaja con waypoints (los puntos del viaje), parámetros de vehículo y contexto temporal para calcular distancias, tiempos, ETAs, peajes, costes y emisiones.

**Parámetros que se toman de los maestros del TMS**
'''''''''''''''''''''''''''''''''''''''''''''''''''

Desde Guraify se construye la petición a PTV a partir de:

- Maestro de localizaciones y de paradas: coordenadas geográficas de cada parada, orden actual, tipo de parada (recogida, entrega, hub) y, cuando aplica, ventanas horarias y tiempos de servicio configurados por tipo de cliente o tipo de operación. Estas ventanas y tiempos se trasladan a PTV como *opening intervals* y *service times* para que el cálculo respete la realidad operativa.

- Maestro de vehículos: perfil de vehículo (camión rígido, tráiler, furgoneta, eléctrico), dimensiones y capacidades (peso máximo, volumen, ejes, altura), restricciones de mercancías peligrosas o refrigeradas y, cuando aplica, costes asociados al vehículo (coste por km, por hora, etc.), que se mapean con los *vehicle parameters* y la lógica de *monetary costs* de la API.

- Maestro de calendarios y planificación: fecha y hora de salida previstas del viaje, zona horaria y, opcionalmente, reglas de horas de conducción y descanso del conductor, que se trasladan a PTV a través de los parámetros de *date and time* y *drivers’ working hours*.

**Resultados que vuelven y se exponen en el TMS**
'''''''''''''''''''''''''''''''''''''''''''''''''

La respuesta de Routing se vuelca de nuevo en el Viaje y en sus Paradas:

- Geometría de ruta (polilínea) asociada al Viaje, para representación en mapa.

- Distancia total y por segmento entre paradas, tiempo de conducción y de servicio, y tiempo total de ruta.

- ETA calculada por parada, indispensable tanto en planificación como en seguimiento en ejecución.

- Información de peajes y costes cuando se activan las opciones de *toll* y *monetary costs*, y, si se configura, emisiones estimadas (CO₂, etc.) usando la funcionalidad de *emissions*.

En operativa, esto permite recalcular la ETA durante la ejecución, combinando la ruta planificada de PTV con la posición real del conductor obtenida desde la app móvil, de modo que el Viaje en Guraify se convierte en un objeto dinámico que refleja la situación real y no solo el plan teórico.

**Nivel 2 – Secuenciación: ordenar paradas dentro de un Viaje**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En el nivel de Secuenciación, las paradas ya están asignadas a un Viaje, pero su orden no es óptimo. Aquí se usa la Sequence Optimization API, que trabaja con el concepto de *locations, transports and stops*, vehículo y conductor, tiempos de servicio, ventanas horarias y prioridades de transporte para devolver el mejor orden posible de ejecución.

.. _parámetros-que-se-toman-de-los-maestros-del-tms-1:

**Parámetros que se toman de los maestros del TMS**
'''''''''''''''''''''''''''''''''''''''''''''''''''

La petición a PTV se construye con:

- Las Paradas del Viaje como *stops*, cada una con su localización, tiempo de servicio, ventana horaria y, cuando aplica, prioridad (por ejemplo, entregas urgentes o condicionadas a cut-off horarios).

- El Vehículo asignado al Viaje como *vehicle*, incluyendo capacidades básicas (peso, volumen, pallets) y restricciones (ADR, refrigerado, etc.), así como el perfil de conducción.

- El Conductor o recurso humano, a través de parámetros de jornada máxima, pausas y reglas de horas de trabajo, reutilizando las reglas internas del TMS y mapeándolas a los parámetros de *drivers’ working hours*.

A nivel de configuración, el planificador puede definir el objetivo de optimización (minimizar distancia, tiempo, retrasos respecto a ventanas, etc.), que se mapea a la configuración de *objective of optimization* de PTV.

.. _resultados-que-vuelven-y-se-exponen-en-el-tms-1:

**Resultados que vuelven y se exponen en el TMS**
'''''''''''''''''''''''''''''''''''''''''''''''''

La secuenciación devuelve:

- Un nuevo orden de paradas dentro del Viaje, con su posición en ruta.

- Horarios previstos de llegada y salida por parada, ya ajustados a ventanas horarias y tiempos de servicio.

- Indicaciones de posibles violaciones (ventana no cumplible, jornada de conductor excedida) cuando la secuenciación no puede respetar todas las restricciones, apoyándose en la lógica de *drivers’ working hours* y *violations*.

En Guraify, esto se traduce en una reordenación de las Paradas del Viaje, con actualización de ETAs y KPIs de ruta (km, duración, nivel de servicio), manteniendo la vinculación de cada parada con su Tramo y su Orden para no romper el modelo estructural.

**Nivel 3 – Optimización completa: asignación y secuenciación con OptiFlow**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El nivel más avanzado utiliza Route Optimization OptiFlow API. Aquí ya no hablamos solo de ordenar paradas dentro de un viaje existente, sino de dejar que PTV proponga el plan completo de asignación y secuenciación de las paradas a viajes, en base a órdenes, vehículos, depósitos y un conjunto rico de reglas y restricciones.

OptiFlow trabaja con el concepto de Orders, que en su terminología representan peticiones de transporte o servicio (pickup, delivery, pickup–delivery o servicio puro), con cargas, categorías, ventanas horarias, tiempos de servicio y parámetros económicos como *outsourcing cost* e *insourcing revenue* para ayudar a decidir qué pedidos merece la pena planificar o dejar fuera.

.. _parámetros-que-se-toman-de-los-maestros-del-tms-2:

**Parámetros que se toman de los maestros del TMS**
'''''''''''''''''''''''''''''''''''''''''''''''''''

En este caso, el mapeo desde Guraify hacia OptiFlow es más rico:

- Las Órdenes / Paradas del TMS se transforman en Orders y Tasks de OptiFlow: para un simple reparto desde hub serán típicamente *delivery orders*; para un transporte origen–destino, *pickup-delivery orders*; para ciertos servicios de solo visita, *service orders*. Cada task incorpora localización, ventanas horarias y tiempo de servicio.

- Las cargas (peso, volumen, pallets, metros lineales, etc.) se toman de las líneas o de los bultos asociados en Guraify y se mapean a los *loads* del order para controlar capacidades de los vehículos.

- Las categorías de pedido (temperatura controlada, ADR, requisitos de equipamiento) se mapean a *order categories*, que luego se cruzan con las categorías de vehículos, depósitos y recursos para asegurar compatibilidad.

- Los Vehículos del maestro de flota se convierten en *vehicles/resources* de OptiFlow, con sus capacidades, costes, restricciones, equipamientos y, si se quiere, perfiles de coste horario y por kilómetro.

- Los Depósitos / Hubs definidos en Guraify se mapean a *depots*, con sus localizaciones, horarios y, en su caso, perfiles de servicio específicos.

- Opcionalmente, se pueden utilizar parámetros económicos de cada pedido para alimentar los campos de *outsourcing cost* e *insourcing revenue*, de forma que el optimizador pueda decidir dejar fuera pedidos poco rentables o priorizar aquellos que aportan mayor margen, de acuerdo a la definición de la propia API.

.. _resultados-que-vuelven-y-se-exponen-en-el-tms-2:

**Resultados que vuelven y se exponen en el TMS**
'''''''''''''''''''''''''''''''''''''''''''''''''

OptiFlow devuelve un plan de rutas completo: listado de rutas con sus vehículos asignados, secuencias de órdenes/paradas, horarios, ocupación de capacidades y métricas globales de coste y rendimiento.

En Guraify, ese plan se traduce en:

- Creación o actualización de Viajes propuestos, con sus Paradas ya asignadas y secuenciadas.

- Asignación automática de recursos (vehículo y, cuando corresponda, conductor).

- Cálculo de distancias, tiempos y niveles de ocupación por viaje y por tramo.

- Identificación de órdenes no planificadas, junto con la razón (incompatibilidades, sobrecoste, falta de recursos), alineado con la lógica de órdenes “outsourced” que describe OptiFlow.

El usuario del TMS no ve el detalle técnico de la API, sino una propuesta de planificación coherente con el modelo Orden–Tramo–Parada–Viaje. Puede aceptarla tal cual, ajustarla manualmente o combinarla con reglas de negocio propias de la compañía.

[TIP]

Routing enriquece Viajes existentes,

Secuenciación optimiza el orden de Paradas,

OptiFlow propone directamente qué Viajes crear y cómo llenarlos.

Toda la parametrización nace de los maestros del TMS.

**1.4.3 Capa de integración (API / EDI)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El sistema incorpora una capa de integración que permite intercambiar información estructurada con sistemas externos mediante:

- Ficheros CSV o Excel.

- API REST.

- Webhooks.

- Automatizaciones programadas.

Las integraciones no crean estructuras paralelas, sino que alimentan directamente las entidades nativas del modelo (Orden, Tramo, Parada, Viaje). Esto garantiza coherencia entre datos importados y ejecución real.

.. _section-1:

**1.4.4 Arquitectura móvil y tecnologías embarcadas**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La aplicación móvil de Guraify TMS es una extensión operativa del backend. No es únicamente una interfaz de confirmación de entregas, sino un punto activo de generación de datos estructurales que alimentan la trazabilidad en tiempo real,

Es la responsable de actualizar estados, registrar incidencias, capturar POD digitales y sincronizar eventos operativos con el backend en tiempo real

La aplicación móvil de Guraify TMS integra el Scandit Barcode Scanner SDK como motor de captura inteligente de códigos de barras. La tecnología no se utiliza de una única forma, sino que se estructura en tres modos operativos distintos: escaneo simple, escaneo masivo y escaneo en vídeo continuo. Cada uno responde a una necesidad diferente dentro del flujo logístico.

Cada escaneo actualiza automáticamente la trazabilidad y puede activar eventos posteriores como desbloqueo de facturación o liquidación, recalculos de ETA o envío de alertas.

.. _section-2:

.. _section-3:

**Tipologías de escaneo**
^^^^^^^^^^^^^^^^^^^^^^^^^

**1. Escaneo simple (unitario)**
''''''''''''''''''''''''''''''''

Es el modo clásico de lectura individual. El usuario enfoca un único código y el sistema lo identifica inmediatamente.

Este tipo de escaneo se caracteriza por:

- Lectura rápida y precisa de un único código.

- Confirmación inmediata.

- Validación directa contra el modelo de datos (bulto, parada, viaje).

- Registro automático del evento en la trazabilidad.

Es el modo más controlado y se utiliza cuando se requiere precisión individual en la validación de mercancía.

**2. Escaneo masivo**
'''''''''''''''''''''

El escaneo masivo permite capturar múltiples códigos de forma consecutiva en una misma sesión, validándolos contra el conjunto esperado de bultos asociados a un Viaje o Parada.

A diferencia del modo simple, aquí el objetivo no es validar una unidad concreta, sino verificar el conjunto completo.

El sistema:

- Compara los bultos escaneados con los asignados.

- Detecta faltantes.

- Detecta duplicados.

- Impide validar el proceso si existen inconsistencias.

Este modo actúa como mecanismo de control y verificación global antes de cerrar una fase operativa.

**3. Escaneo en vídeo (modo continuo con validación visual)**
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Es el modo más avanzado y diferencial. Utiliza la cámara en modo continuo para detectar múltiples códigos simultáneamente en tiempo real.

El sistema analiza constantemente la imagen capturada y superpone información visual en pantalla:

- Indicador verde si el bulto pertenece al Viaje o Parada.

- Indicador rojo si no corresponde.

- Confirmación inmediata sin necesidad de lectura individualizada.

Este modo permite interacción dinámica y reduce drásticamente el tiempo operativo en escenarios de alto volumen.

[NOTE]

El escaneo en vídeo no es una lectura rápida.

Es validación contextual en tiempo real contra la estructura del Viaje.

**Uso dentro del flujo operativo**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una vez definidos los modos de escaneo, su aplicación dentro del flujo logístico es la siguiente:

**Entrada de mercancía en almacén**
'''''''''''''''''''''''''''''''''''

Se utiliza el escaneo simple. Cada bulto que entra en el sistema —ya sea por primera vez o en procesos de devolución— se identifica individualmente, activando su trazabilidad. Aquí prima la precisión individual.

**Proceso de removido en hub**
''''''''''''''''''''''''''''''

Se utiliza el escaneo en vídeo. El conductor o el operario enfoca las etiquetas y el sistema indica visualmente si cada bulto pertenece o no a su ruta. Esto permite separar rápidamente mercancía correcta de mercancía incorrecta sin validaciones manuales adicionales. Aquí prima la velocidad con validación contextual.

**Verificación completa antes de carga**
''''''''''''''''''''''''''''''''''''''''

Se utiliza el escaneo masivo. Una vez que el conductor considera que tiene toda la mercancía preparada, el sistema verifica que el conjunto de bultos escaneados coincide exactamente con los asignados al Viaje. Si falta alguno, no se permite validar la salida. Aquí prima el control de coherencia total.

[IMPORTANT]

El escaneo masivo es un punto de control previo a la ejecución del Viaje.

**Localización de bultos durante el reparto**
'''''''''''''''''''''''''''''''''''''''''''''

Durante la ejecución, el conductor puede utilizar el escaneo en vídeo para localizar mercancía dentro del vehículo.

Simplemente enfocando las etiquetas, el sistema le indica si ese bulto corresponde a la parada actual o a una parada posterior. Esto reduce errores de entrega y evita búsquedas manuales innecesarias dentro del vehículo. Aquí prima la asistencia operativa en tiempo real.

.. _section-4:

**Confirmación en entrega o recogida**
''''''''''''''''''''''''''''''''''''''

Se utiliza principalmente el escaneo masivo, asegurando que:

- Se entregan exactamente los bultos asignados.

- No quedan bultos pendientes.

- Las recogidas se vinculan correctamente a la parada correspondiente.

.. _section-5:

**Impacto estructural**
^^^^^^^^^^^^^^^^^^^^^^^

En todos los casos, el escaneo no es una acción aislada. Cada lectura genera:

- Actualización de estado del Bulto.

- Registro en el histórico de la Parada.

- Impacto en el estado del Viaje.

- Evidencia operativa trazable.

La tecnología de Scandit actúa como acelerador operativo, pero el resultado siempre es estructural: el modelo de datos se actualiza en tiempo real y mantiene coherencia entre ejecución física y representación digital.

**1.4.5 Modelo de geolocalización y normalización de coordenadas**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Guraify TMS se basa en la geolocalización como fundamento estructural para múltiples procesos: asignación automática a áreas operativas, cálculo de rutas, segmentación tarifaria y planificación por zonas.

Para comprender correctamente este modelo, es necesario distinguir tres conceptos geométricos fundamentales que se utilizan de forma recurrente dentro del sistema:

- Coordenada (punto)

- Polígono (superficie)

- Polilínea (trayectoria)

Estos tres elementos constituyen la base geométrica sobre la que se construyen muchas de las funciones del TMS.

.. _section-6:

**Coordenada: la representación puntual**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toda entidad que represente una localización física dentro del sistema —punto de entrega, recogida, hub, almacén o cualquier dirección operativa— dispone de una coordenada geográfica compuesta por: Latitud (lat), Longitud (lon)

Esta pareja de valores numéricos define un punto exacto sobre la superficie terrestre. Desde el punto de vista matemático, una coordenada es una posición puntual sin superficie.

En el TMS, cada registro de localización almacena estas coordenadas como parte estructural de su modelo de datos. No se trata de un atributo accesorio; es el elemento que permite:

- Calcular distancias reales.

- Planificar rutas.

- Determinar pertenencia a áreas.

- Aplicar tarifas zonales.

- Evaluar restricciones geográficas.

[WARNING]

Sin coordenada válida no existe planificación fiable

**Polígono: la representación de superficie**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mientras que una coordenada representa un punto, un polígono representa una superficie delimitada por un conjunto de vértices conectados.

En Guraify TMS, cualquier entidad que represente un área geográfica —zona operativa, área tarifaria, zona de bajas emisiones, región de planificación o segmento logístico— se modeliza mediante un polígono.

La información del polígono se almacena utilizando el estándar GeoJSON, un formato estructurado ampliamente utilizado para representar geometrías geográficas. Un polígono en GeoJSON está compuesto por una lista ordenada de coordenadas que definen su perímetro.

Este enfoque permite que el sistema pueda responder a preguntas como:

- ¿Esta entrega pertenece a la Zona Norte?

- ¿Este cliente está dentro de un área tarifaria específica?

- ¿Este destino se encuentra dentro de una ZBE (Zona de Bajas Emisiones)?

La lógica que se aplica es puramente geométrica: se comprueba si la coordenada (punto) cae dentro del polígono (superficie).

[IMPORTANT]

Una localización es un punto (lat, lon).

Un área es una superficie (polígono GeoJSON).

La pertenencia se calcula geométricamente.

.. _section-7:

**Polilínea: la representación de una ruta**
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

**Proceso de geolocalización de coordenadas**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para que este modelo funcione, cada dirección debe transformarse en una coordenada fiable. Este proceso se denomina geocodificación.

Guraify TMS utiliza un modelo jerárquico de geolocalización basado en dos proveedores: PTV y Google Maps, ambos configurables mediante token en la configuración del sistema Odoo.

El flujo de geocodificación es el siguiente:

1. Se intenta geolocalizar utilizando PTV como primera capa.

2. Se evalúa la calidad del resultado devuelto.

3. Si la calidad es inferior al 80 %, se realiza un segundo intento mediante Google Maps.

4. Si la calidad sigue siendo inferior al 80 %, se asigna automáticamente la coordenada del centroide del código postal o localidad.

En este último escenario, la localización queda marcada como “Normalizable”, lo que implica que la coordenada no es suficientemente precisa y requiere validación manual por parte del usuario antes de utilizarla en una expedición definitiva.

[IMPORTANT]

Una coordenada con calidad inferior al 80 % no se considera válida para planificación definitiva.

Cuando un usuario intenta validar una expedición que utiliza una localización con baja calidad, el sistema obliga a realizar una normalización manual. Este mecanismo no es una excepción operativa, sino un control de calidad estructural que evita errores de planificación, desvíos innecesarios y problemas en la ETA.

Más adelante en el manual se detallará el procedimiento paso a paso de normalización manual.

.. _section-9:

**Gestión y creación de áreas geográficas**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para la creación y mantenimiento de áreas (polígonos), el sistema integra servicios basados en OpenStreetMap, plataforma cartográfica de uso libre.

OpenStreetMap se utiliza para:

- Visualizar mapas base.

- Dibujar polígonos manualmente.

- Editar áreas existentes.

- Exportar e importar geometrías en formato GeoJSON.

El uso de OSM permite que la gestión de áreas sea independiente de proveedores propietarios y garantiza flexibilidad en la definición de superficies operativas.

.. _section-10:

**Modelo conceptual de asignación geográfica**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El funcionamiento interno puede representarse de forma simplificada mediante el siguiente esquema lógico:

[NOTE]

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

[NOTE]

+---------------------------+

\| Área Operativa \|

\| (Polígono GeoJSON \|

\| \|

\| • \|

\| (lat, lon) \|

\| Punto Localización \|

+---------------------------+

Si el punto se encuentra dentro de los límites del polígono, la localización queda automáticamente asociada a esa área. Si no pertenece a ningún polígono definido, el sistema puede:

- Dejarla sin asignación.

- Asociarla al área más cercana..

- Requerir intervención manual según configuración.

[IMPORTANT]

La asignación a áreas no se basa en texto ni en códigos postales.

Se basa en geometría real sobre coordenadas verificadas.

**Implicaciones prácticas**
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este modelo permite que:

- Una misma dirección cambie automáticamente de área si se corrige su coordenada.

- Las tarifas zonales se apliquen de forma automática y coherente.

- Las restricciones geográficas (ZBE, áreas restringidas) se validen antes de planificar.

- La planificación avanzada tenga información espacial fiable.

En definitiva, el sistema no interpreta “direcciones”, interpreta geometría. La dirección textual es solo el punto de partida; la coordenada validada es la base real de toda la lógica espacial del TMS.

.. _section-11:

**Impacto arquitectónico**
^^^^^^^^^^^^^^^^^^^^^^^^^^

La combinación de:

- Coordenadas precisas (lat, lon),

- Polígonos en formato GeoJSON,

- Geocodificación jerárquica con control de calidad,

- Normalización manual obligatoria cuando procede,

permite que la asignación automática a áreas, la tarificación zonal y la planificación avanzada funcionen sobre bases geométricas fiables.

Este modelo convierte la geolocalización en un componente estructural del TMS, no en una funcionalidad accesoria. Sin precisión geográfica no hay planificación fiable, y sin áreas correctamente definidas no existe automatización tarifaria ni segmentación operativa coherente.

**1.5 Filosofía operativa del sistema**
---------------------------------------

La filosofía operativa de Guraify TMS no parte de la herramienta, sino del modelo. El sistema está diseñado sobre una premisa clara: el transporte debe representarse de forma estructural, desacoplada y trazable en todas sus dimensiones.

Tres principios articulan esta filosofía.

El primero es la separación estructural entre ingreso y coste. La Orden representa el compromiso comercial y genera el ingreso; el Viaje representa la ejecución real y genera el coste. Esta separación no es únicamente contable, sino arquitectónica. Permite reorganizar la ejecución sin alterar el contrato, agrupar múltiples órdenes en un mismo viaje, dividir una orden en varios recursos y analizar márgenes en cualquier dimensión sin reconciliaciones manuales posteriores.

El segundo principio es la planificación basada en eventos físicos. El sistema no planifica órdenes abstractas, sino Paradas geolocalizadas. Cada parada es un evento real con coordenada, ventana horaria y tiempo de servicio. Esta decisión permite que la optimización (Routing, Secuenciación u OptiFlow) trabaje sobre entidades físicas concretas y que la ejecución, a través de la aplicación móvil, actualice el modelo en tiempo real con base en hechos y no en estimaciones teóricas.

El tercer principio es la integración nativa entre operativa y economía. La tarificación no es un cálculo externo; nace de la estructura operativa. La liquidación no es un proceso posterior; se genera en la ejecución. La imputación prorrateada no es un informe adicional; es una consecuencia del modelo relacional. Esto convierte al sistema en una herramienta de control de rentabilidad basada en datos estructurales coherentes con la realidad operativa.

Desde esta perspectiva, la tecnología —Odoo como base ERP, PTV como motor matemático, Scandit como acelerador de captura operativa, la geolocalización jerárquica con control de calidad y el modelo geométrico punto–polígono— no son piezas aisladas. Todas responden a una misma lógica: garantizar que cada decisión operativa tenga una representación estructural precisa y trazable.

El sistema no está concebido como un simple planificador de rutas ni como un generador de albaranes. Está diseñado como una arquitectura desacoplada capaz de:

- Adaptarse a distintos modelos de negocio sin alterar su núcleo.

- Escalar en volumen sin perder coherencia estructural.

- Integrarse con terceros sin duplicar modelos.

- Analizar rentabilidad en micro-dimensiones operativas.

- Mantener trazabilidad completa desde el bulto hasta el margen final.

En definitiva, la filosofía operativa de Guraify TMS consiste en transformar la complejidad logística en una estructura formal coherente, donde cada evento físico, cada coordenada, cada escaneo y cada optimización matemática se traduce en información analizable y económicamente relevante.

Sobre esta filosofía se construyen los capítulos siguientes del manual, donde se detallará la organización funcional del sistema y su implementación práctica en entornos reales.

**2. MODELO CONCEPTUAL DEL TMS**
================================

**2.1 Lógica estructural del sistema**
--------------------------------------

La lógica estructural de Guraify TMS se fundamenta en una decisión arquitectónica deliberada: separar de forma explícita el encargo comercial del cliente de su ejecución operativa y de su impacto económico. Esta separación no es únicamente conceptual, sino que determina la estructura del modelo de datos, la organización funcional del sistema y la propia metodología de implantación.

Desde el punto de vista del negocio, todo comienza con la necesidad de representar digitalmente un servicio solicitado por un cliente. Esa representación es la Orden. La Orden formaliza el compromiso contractual: define qué servicio debe prestarse y bajo qué condiciones se facturará. En ella nace el ingreso y desde ella se articula el resto de la estructura operativa.

Sin embargo, una Orden no describe la ejecución física del transporte. Para ello se introduce el Tramo, que permite descomponer el compromiso comercial en movimientos logísticos concretos entre un origen y un destino. Esta descomposición es lo que permite modelar tanto un servicio simple puerta a puerta como operativas complejas con múltiples fases, arrastres entre hubs o escenarios de reagenda, sin romper la coherencia administrativa.

Cuando una Orden se valida, el sistema traduce su estructura lógica en eventos físicos reales mediante la generación automática de Paradas. La Parada representa el punto operativo trazable: recogida, entrega, entrada en hub o cualquier evento intermedio necesario. Desde el punto de vista de planificación, la Parada es la unidad mínima operativa, ya que es sobre ella donde trabajan los algoritmos de optimización y las herramientas de planificación.

Finalmente, las Paradas se agrupan en Viajes, que representan la ejecución real asignada a un recurso. El Viaje consolida paradas en una ruta ejecutable, genera la orden de compra correspondiente al transportista y materializa el coste de la operación.

[IMPORTANT]

La Orden representa el ingreso.

El Viaje representa el coste.

Esta separación estructural es el principio clave que permite analizar la rentabilidad en múltiples dimensiones sin mezclar ejecución y facturación.

Gracias a este diseño, una misma Orden puede ejecutarse en varios Viajes y un mismo Viaje puede contener paradas procedentes de distintas Órdenes. Este desacoplamiento es el que permite soportar operativas de grupaje, distribución multicliente y modelos de última milla sin alterar la lógica base del sistema.

El flujo estructural puede entenderse como una progresión lógica: se crea la Orden, se descompone en Tramos, se generan Paradas al validar y posteriormente estas se agrupan en Viajes. No obstante, lo verdaderamente relevante no es la secuencia, sino la independencia entre las capas comercial, operativa y económica, que permite reorganizar la ejecución sin modificar el compromiso contractual original.

Esta lógica conceptual no es abstracta ni teórica. Se refleja directamente en la estructura funcional del sistema, organizada en los bloques de Operaciones, Administración, Maestros y Configuración , donde cada sección materializa una dimensión distinta del modelo. Del mismo modo, el propio programa de implantación parte de la comprensión de esta estructura base —Orden, Tramo, Parada y Viaje— como primer paso antes de entrar en parametrización avanzada , lo que confirma que el modelo conceptual es la base real sobre la que se construye cualquier proyecto.

En consecuencia, la lógica estructural de Guraify TMS no consiste únicamente en definir entidades relacionadas, sino en establecer una arquitectura desacoplada que permita escalabilidad, optimización avanzada, integración masiva y análisis económico granular. Sobre este principio se construye toda la arquitectura funcional y técnica del sistema.

.. _section-12:

**2.1.1 La Orden**
------------------

La Orden es la entidad que representa digitalmente el encargo del cliente dentro de Guraify TMS. Constituye el punto de partida estructural del sistema y el eje sobre el que se articula toda la operativa posterior. Desde una perspectiva conceptual, la Orden responde a una pregunta sencilla pero fundamental: qué servicio debemos ejecutar y posteriormente facturar.

En términos funcionales, la Orden formaliza el compromiso contractual con el cliente. Contiene la información administrativa y comercial necesaria para definir el servicio, determina la lógica de facturación y establece el marco económico bajo el cual se desarrollará la operación. No describe la ejecución física del transporte, sino el acuerdo que da origen a dicha ejecución.

Cada Orden está obligatoriamente vinculada a un cliente y a un proyecto. El proyecto actúa como contenedor de configuración y permite que la Orden herede automáticamente parámetros críticos como la tarifa aplicable, el modo de división de ventas, el planning asociado, los tipos de servicio permitidos y otras restricciones operativas. Esta herencia garantiza coherencia entre configuración estratégica y ejecución diaria, evitando configuraciones manuales repetitivas y reduciendo riesgos de error.

Desde el punto de vista del modelo de datos, la Orden puede contener uno o varios Tramos. Esta capacidad de descomposición permite representar desde un servicio simple de origen a destino hasta estructuras más complejas en las que una misma relación contractual se materializa en múltiples fases logísticas. A pesar de esta posible complejidad operativa, la Orden mantiene siempre su unidad económica y administrativa.

La Orden es también el origen del ingreso. En ella se generan las líneas de venta y se activan las reglas de tasación configuradas en el sistema. El cálculo económico no se realiza de forma externa ni posterior, sino que forma parte del propio diseño estructural del modelo.

[IMPORTANT]

Una Orden no es una ruta ni una planificación física.

Es un compromiso de servicio con impacto económico.

Esta diferenciación es clave para entender la arquitectura completa del sistema. Gracias a ella, la ejecución puede reorganizarse —mediante distintos Viajes o recursos— sin alterar la naturaleza contractual del servicio ni su lógica de facturación.

En definitiva, la Orden debe entenderse como la unidad contractual y económica del TMS. Es el objeto que conecta cliente, proyecto, tarificación y estructura operativa, y sobre ella se construye todo el desarrollo logístico posterior.

**2.1.2 El Tramo**
------------------

El Tramo es la unidad operativa contenida dentro de una Orden. Si la Orden define el compromiso comercial —qué servicio se debe prestar—, el Tramo concreta cómo se materializa ese compromiso desde el punto de vista logístico. En términos simples, el Tramo responde a la pregunta: desde dónde hasta dónde se presta el servicio.

Cada tramo define un movimiento específico entre un punto de carga y un punto de descarga. En él se registran los datos esenciales que permiten ejecutar y valorar ese desplazamiento: localizaciones, información de mercancía, parámetros temporales y las reglas de tasación que puedan aplicarse a esa fase concreta del servicio. Esto significa que la dimensión económica no se calcula únicamente a nivel global de la Orden, sino que puede vincularse a cada tramo cuando la operativa lo requiere.

La función principal del Tramo es permitir la descomposición controlada de una Orden en operaciones logísticas independientes sin perder la unidad contractual. Gracias a esta estructura, el sistema puede modelar con coherencia escenarios muy distintos: un servicio puerta a puerta se representará mediante un único tramo, mientras que un arrastre entre hubs podrá estructurarse en dos o más tramos dentro de la misma Orden. Del mismo modo, en operativas de última milla masiva o en casos de reagenda, basta con añadir tramos adicionales sin necesidad de crear nuevas órdenes ni alterar la lógica administrativa original.

Esta capacidad de segmentación aporta flexibilidad sin introducir fragmentación económica. La Orden sigue siendo el marco contractual, pero el Tramo permite adaptar la ejecución a la realidad operativa.

[IMPORTANT]

El Tramo es la entidad que da origen a las Paradas.

Sin tramo no existe evento físico planificable.

Desde el punto de vista estructural, el Tramo actúa como puente entre la dimensión comercial (Orden) y la dimensión física (Paradas). Es la pieza que traduce el compromiso contractual en movimientos logísticos concretos sobre los que posteriormente se construirá la planificación y la ejecución real.

**2.1.3 La Parada**
-------------------

La Parada representa el evento físico real dentro de la operativa del transporte. Si el Tramo define un movimiento lógico entre un origen y un destino, la Parada es el punto concreto donde ocurre una acción trazable: una recogida, una entrega, una entrada o salida de hub, una parada técnica o cualquier otro evento que deba registrarse en el flujo operativo.

Desde el punto de vista del sistema, la Parada no se introduce manualmente en condiciones normales. Su generación forma parte del comportamiento estructural del modelo. Cuando una Orden se valida, el sistema analiza los tramos que la componen y genera automáticamente todas las paradas necesarias, vinculándolas al tramo correspondiente y conservando la coherencia jerárquica entre entidades. Este mecanismo garantiza que la representación física de la operación sea siempre consistente con la estructura contractual definida previamente.

En escenarios de importación masiva, el comportamiento es aún más sofisticado. El sistema es capaz de consolidar en una única parada aquellos tramos que comparten cliente, localización y una ventana horaria compatible. Esta lógica reduce la fragmentación innecesaria y prepara la información de forma óptima para la fase de planificación, especialmente en operativas de alta densidad como la última milla o el grupaje urbano.

La relevancia de la Parada no es únicamente operativa, sino también estratégica dentro del modelo de planificación.

[IMPORTANT]

La Parada es la unidad mínima de planificación.

El optimizador no trabaja sobre Órdenes ni sobre Tramos, sino sobre Paradas.

Esta decisión arquitectónica permite que la planificación sea completamente flexible. Las órdenes pueden reorganizarse, agruparse o dividirse sin alterar su dimensión contractual, porque la lógica de optimización se basa exclusivamente en eventos físicos con coordenadas, ventanas horarias y tiempos de servicio asociados.

En consecuencia, la Parada actúa como el punto de convergencia entre estructura lógica y ejecución real. Es donde la operación deja de ser un compromiso abstracto y se convierte en un evento planificable, trazable y medible dentro del sistema.

**2.1.4 El Viaje**
------------------

El Viaje es la entidad que representa la ejecución real del transporte. Si la Orden formaliza el compromiso con el cliente y el Tramo estructura el movimiento logístico, el Viaje responde a una pregunta operativa concreta: qué conjunto de paradas ejecuta un recurso en una ruta real.

Desde el punto de vista funcional, el Viaje agrupa paradas para construir una ruta ejecutable. En él se asigna el recurso —propio o externo— que realizará el servicio, se consolidan los tiempos y distancias previstos y se genera la correspondiente orden de compra cuando interviene un transportista colaborador. Por tanto, el Viaje no es solo una estructura de planificación, sino también la unidad que activa la liquidación económica del servicio hacia el proveedor.

Su creación puede realizarse de forma manual, utilizando herramientas de filtrado y agrupación que permiten seleccionar paradas según múltiples criterios operativos, o de forma automática mediante el optimizador integrado con PTV, que construye rutas considerando restricciones horarias, tiempos de servicio, capacidades del vehículo, normativas de conducción y otros parámetros configurados en el sistema. En ambos casos, el resultado es una estructura coherente que traduce eventos físicos individuales en una secuencia operativa ejecutable.

Desde el punto de vista arquitectónico, el Viaje introduce la dimensión del coste dentro del modelo. Mientras que la Orden mantiene la unidad contractual y el ingreso asociado al cliente, el Viaje materializa el gasto derivado de la ejecución.

[IMPORTANT]

La Orden representa el ingreso, El Viaje representa el coste.

Esta separación estructural permite que una misma Orden pueda ejecutarse en varios Viajes distintos o que un Viaje agrupe paradas procedentes de múltiples Órdenes, algo habitual en operativas de grupaje y distribución multicliente. Gracias a este desacoplamiento, el sistema puede reorganizar la ejecución sin alterar la lógica comercial, manteniendo trazabilidad completa y control económico en todas las dimensiones.

El Viaje, por tanto, es la unidad de ejecución y coste del sistema, y cierra el ciclo iniciado por la Orden dentro del modelo estructural del TMS.

**2.2 Relación entre entidades**
--------------------------------

Una vez definidas las entidades principales —Orden, Tramo, Parada y Viaje—, es necesario entender cómo se relacionan entre sí dentro del flujo estructural del sistema. La potencia del modelo no reside únicamente en cada entidad por separado, sino en la forma en que se encadenan y, al mismo tiempo, permanecen desacopladas.

.. _section-13:

**2.2.1 Flujo lógico estructural**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El flujo comienza cuando un cliente solicita un servicio. Ese compromiso se formaliza mediante la creación de una Orden, que actúa como unidad contractual y económica. A partir de ella se generan uno o varios Tramos que describen los movimientos logísticos necesarios para cumplir el servicio.

Cuando la Orden se valida, el sistema transforma la estructura lógica en eventos físicos reales generando automáticamente las Paradas asociadas a cada tramo. Estas paradas, que constituyen la unidad mínima planificable, se agrupan posteriormente en Viajes, ya sea manualmente o mediante optimización automática. Una vez creado el Viaje, se asigna a un recurso, se ejecuta la operación y finalmente se activan los procesos de liquidación y facturación correspondientes.

Este flujo no debe entenderse únicamente como una secuencia técnica, sino como una transición progresiva desde la dimensión comercial hasta la dimensión operativa y económica de la ejecución real.

.. _section-14:

**2.2.2 Separación conceptual clave**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada entidad representa una capa distinta dentro del modelo y cumple un papel específico tanto operativo como económico. La Orden representa el ingreso y concentra el impacto en facturación; el Tramo estructura la operación logística y aporta trazabilidad dentro del servicio; la Parada materializa el evento físico y constituye la base de la planificación; el Viaje agrupa esas paradas en una ruta ejecutable y genera el coste asociado a su ejecución.

[IMPORTANT]

El modelo no fusiona ingreso y ejecución en una única entidad.

Separa explícitamente compromiso comercial, operación logística y coste real.

Esta separación conceptual es lo que permite que el sistema escale sin perder coherencia. Gracias a ella, es posible reorganizar la ejecución sin alterar la facturación, agrupar múltiples órdenes en un mismo viaje, dividir una orden en distintos recursos o analizar márgenes en distintas dimensiones operativas.

En consecuencia, la arquitectura no solo facilita la planificación y la ejecución, sino que habilita flexibilidad operativa, optimización avanzada y un control económico real basado en la estructura misma del modelo, no en procesos externos de conciliación.

**2.3 Modelo de Trazabilidad**
------------------------------

La trazabilidad en Guraify TMS es una consecuencia directa de su arquitectura desacoplada. Al estructurar el sistema en Orden, Tramo, Parada y Viaje, cada transición operativa queda registrada como parte natural del modelo, permitiendo reconstruir el recorrido completo de un servicio sin depender de procesos externos.

El sistema articula la trazabilidad en tres capas complementarias. La primera es la trazabilidad de mercancía, que opera a nivel de bultos o unidades transportadas. Cada bulto se vincula estructuralmente a un tramo y, a través de este, a sus paradas y viajes asociados. Esto permite seguir el recorrido físico de la mercancía dentro de la red logística, incluso cuando intervienen múltiples hubs o recursos.

La segunda capa es la trazabilidad de eventos, basada en las Paradas. Cada parada constituye un evento operativo concreto y registra estados, fechas previstas y reales, tiempos de servicio y cualquier modificación relevante. Dado que la Parada es la unidad mínima de planificación, también es la unidad mínima de trazabilidad temporal.

La tercera capa es la trazabilidad documental, donde se integran pruebas de entrega (POD), incidencias, fotografías, firmas digitales y cualquier documentación generada durante la ejecución.

Lo verdaderamente relevante es que esta información no se actualiza de forma manual posterior, sino que se alimenta automáticamente desde los puntos de ejecución del sistema.

La app móvil utilizada por conductores y personal de almacén actualiza en tiempo real los estados de las paradas, registra firmas, captura fotografías, declara incidencias y confirma tiempos efectivos de servicio. Cada acción genera un cambio de estado que queda persistido en el histórico de la entidad correspondiente. Del mismo modo, el equipo de operaciones puede actualizar eventos desde el backend cuando la operativa lo requiere, manteniendo coherencia entre planificación y realidad ejecutada. En escenarios integrados, los sistemas externos también pueden alimentar estados mediante API o procesos EDI.

\ **[NOTE]**

La trazabilidad no es declarativa.

Se construye automáticamente a partir de la ejecución real registrada en la app, el backoffice y las integraciones.

Gracias a este diseño, cada entidad conserva un histórico completo y auditable. En cualquier momento es posible conocer dónde se encuentra la mercancía, en qué estado operativo está, qué recurso la transporta o la ha transportado y qué incidencias han afectado al servicio. La trazabilidad no es una capa añadida, sino una propiedad emergente del propio modelo estructural del TMS.

Este enfoque garantiza visibilidad operativa en tiempo real y, al mismo tiempo, una base sólida para análisis de calidad, control de servicio y gestión de responsabilidades dentro de la cadena logística.

**2.4 Modelo Económico Vinculado**
----------------------------------

Uno de los elementos diferenciales de Guraify TMS es que la dimensión económica no se gestiona como una capa externa al TMS, sino como una consecuencia directa de la estructura operativa. El sistema no obliga a reconciliar después lo que se ejecuta con lo que se factura; ambas dimensiones están integradas desde el diseño conceptual.

La arquitectura separa claramente ingreso y coste, pero los mantiene vinculados estructuralmente a las entidades que los generan. Esto elimina duplicidades, reduce conciliaciones manuales y permite que el análisis económico se construya sobre datos operativos reales.

[NOTE]

En Guraify TMS la economía no es un proceso posterior.

Es una propiedad estructural del modelo operativo.

**2.4.1 Ingreso (Activo)**
~~~~~~~~~~~~~~~~~~~~~~~~~~

El ingreso nace en la Orden, ya que es la entidad que representa el compromiso contractual con el cliente. El cálculo puede realizarse automáticamente mediante reglas de tarifa configuradas en el sistema o aplicando condiciones económicas pactadas previamente. En ambos casos, el importe no es un valor aislado, sino el resultado de la estructura logística definida.

Cuando la operativa lo requiere, el ingreso puede segmentarse por Tramo, permitiendo que distintas fases del servicio tengan impacto económico diferenciado. Cada línea económica generada queda vinculada al contexto operativo que la origina —orden, tramo, servicio, producto— lo que garantiza trazabilidad financiera completa.

De esta forma, el ingreso no es un dato agregado al final del proceso, sino una consecuencia directa de la configuración operativa.

**2.4.2 Coste (Pasivo)**
~~~~~~~~~~~~~~~~~~~~~~~~

El coste, por su parte, se genera en el Viaje, ya que este representa la ejecución real asignada a un recurso. El Viaje actúa como unidad de coste porque es la entidad que materializa la prestación efectiva del servicio, ya sea mediante flota propia o transportistas externos.

En caso de colaboradores externos, el Viaje genera automáticamente la orden de compra correspondiente y activa el proceso de liquidación. Cuando el modelo operativo lo requiere, el coste puede dividirse entre las distintas paradas que componen el viaje, según el criterio de reparto configurado.

Esta separación estructural permite analizar de forma clara qué se factura al cliente y qué se paga por ejecutar el servicio, sin mezclar ambas dimensiones.

.. _section-15:

**2.4.3 Imputación prorrateada multidimensional**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aquí reside uno de los mayores diferenciales del sistema. Guraify TMS no limita el análisis económico al nivel agregado de Orden o Viaje, sino que permite imputar tanto el ingreso como el coste en cualquier nivel estructural del modelo: Orden, Tramo, Parada o Viaje.

Esto significa que el ingreso generado por una Orden puede distribuirse proporcionalmente entre sus tramos, y que el coste generado por un Viaje puede dividirse entre sus paradas. Como resultado, el margen puede calcularse no solo a nivel global, sino en micro-unidades operativas.

La imputación puede realizarse según criterios configurables adaptados a la realidad del negocio: peso, volumen, número de bultos, pallets, metros lineales, kilómetros recorridos o combinaciones de estas variables. También es posible aplicar una distribución lineal cuando la operativa lo requiera.

[IMPORTANT]

El margen no se calcula únicamente por cliente o por viaje.

Puede analizarse en cualquier dimensión estructural del sistema.

**2.4.4 Resultado: análisis avanzado de margen**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gracias a esta arquitectura económica desacoplada y prorrateada, el sistema permite calcular margen no solo por Orden o por Viaje, sino también por Tramo, Parada, Proyecto, Cliente, Planning, Zona geográfica, Tipo de servicio o cualquier dimensión analítica configurada.

Esto abre un campo de análisis estratégico que va más allá de la simple facturación. Permite identificar qué zonas son realmente rentables, qué servicios generan mayor margen real, qué clientes aportan volumen pero reducen rentabilidad, qué paradas penalizan la operación o qué transportistas optimizan mejor el coste por kilómetro o por unidad transportada.

La combinación de operativa estructurada, tarificación automática e imputación prorrateada convierte al sistema no solo en un TMS de ejecución, sino en una herramienta avanzada de análisis de rentabilidad operativa basada en datos reales y coherentes con la ejecución física del transporte.

Sobre esta base económica se apoyan posteriormente los mecanismos de control analítico, reporting y toma de decisiones estratégicas del sistema.

.. _section-16:

.. _section-17:

.. _section-18:

.. _section-19:

.. _section-20:

.. _section-21:

.. _section-22:

**2.5 Diagrama Oficial del Modelo**
===================================

[IMAGE]

|image1|

.. _section-23:

**2.6 Modelo Relacional Conceptual Simplificado**
-------------------------------------------------

El Modelo Relacional Conceptual formaliza las relaciones estructurales entre las entidades principales del sistema: Orden, Tramo, Parada y Viaje. Si en los apartados anteriores se ha explicado su función operativa y económica, aquí se define cómo se vinculan entre sí desde el punto de vista lógico y de cardinalidad.

Este modelo constituye la base sobre la que se construye la arquitectura técnica del sistema. No es una representación teórica, sino la traducción estructural del comportamiento real del TMS.

**2.6.1 Entidades principales**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La Orden representa el encargo comercial del cliente. Es la entidad contractual, genera el ingreso y puede contener múltiples tramos.

El Tramo es la unidad operativa dependiente de una Orden. Define un origen y un destino concretos y es el elemento que da lugar a la generación de paradas.

La Parada es el evento físico asociado a un tramo. Puede corresponder a una carga, descarga, entrada en hub u otro evento intermedio. Es la unidad mínima de planificación.

El Viaje es la unidad de ejecución operativa. Agrupa múltiples paradas en una ruta ejecutable y genera el coste asociado a dicha ejecución.

[IMAGE]

|image2|

**2.6.2 Cardinalidades estructurales**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Desde el punto de vista relacional, el modelo puede representarse de forma simplificada mediante las siguientes cardinalidades:

ORDEN (1) ──────── (N) TRAMO

TRAMO (1) ──────── (N) PARADA

PARADA (N) ──────── (1) VIAJE

La relación entre Orden y Tramo es de uno a muchos. Una Orden puede contener múltiples Tramos, pero cada Tramo pertenece exclusivamente a una única Orden. Se trata de una dependencia estructural fuerte: sin Orden, el Tramo carece de sentido lógico.

La relación entre Tramo y Parada también es de uno a muchos. Un Tramo genera al menos dos Paradas —carga y descarga— aunque en escenarios complejos puede generar más. De nuevo, es una dependencia fuerte: la Parada no puede existir sin un Tramo que la origine.

La relación entre Parada y Viaje es distinta. Una Parada pertenece a un único Viaje operativo en un momento dado, pero un Viaje puede agrupar múltiples Paradas. Aquí no hablamos de dependencia estructural, sino de asignación operativa.

[NOTE]

Las relaciones Orden→Tramo y Tramo→Parada son dependencias estructurales fuertes.

La relación Parada→Viaje es una asignación operativa.

**2.6.3 Relación indirecta Orden ↔ Viaje**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No existe una relación estructural directa entre Orden y Viaje. La conexión se produce de forma indirecta a través de las Paradas.

Esto implica que un Viaje puede contener Paradas procedentes de múltiples Órdenes, y que una Orden puede distribuir sus Paradas en distintos Viajes. Conceptualmente, esto genera una relación N:M indirecta entre Orden y Viaje.

Este comportamiento es especialmente relevante en operativas de grupaje, última milla, entornos multicliente o estructuras multihub, donde la ejecución real no coincide necesariamente con la unidad contractual.

Esta ausencia de dependencia directa es lo que permite reorganizar la ejecución sin alterar el compromiso comercial.

.. _section-24:

**2.6.4 Dependencias funcionales**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El modelo distingue claramente entre dependencias estructurales y dependencias operativas.

Las dependencias estructurales son fuertes: el Tramo depende de la Orden y la Parada depende del Tramo. Si se elimina la entidad padre, las hijas pierden sentido lógico dentro del modelo.

Las dependencias operativas son débiles: la Parada se asigna a un Viaje, pero el Viaje no depende estructuralmente de una Orden concreta. Esto permite replanificar, reasignar viajes, optimizar dinámicamente y mantener separadas las dimensiones de ingreso y coste.

Esta diferenciación es esencial para la escalabilidad del sistema.

**2.6.5 Impacto en la arquitectura del sistema**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La arquitectura relacional descrita no solo define relaciones técnicas; habilita comportamientos funcionales avanzados. Gracias a este modelo es posible agrupar múltiples órdenes en un mismo viaje, redistribuir paradas entre recursos, realizar imputación económica multidimensional y mantener independencia entre facturación y ejecución.

La separación estructural entre encargo comercial (Orden) y ejecución operativa (Viaje) solo es posible porque el modelo relacional evita una dependencia directa entre ambas entidades.

[NOTE]

La independencia entre ingreso y ejecución no es una decisión funcional aislada.

Es una consecuencia directa del modelo relacional.

En definitiva, el Modelo Relacional Conceptual es el fundamento lógico que permite que Guraify TMS sea escalable, flexible y económicamente analizable en múltiples dimensiones. Sobre esta base se construye la arquitectura técnica y funcional descrita en los capítulos siguientes.

**3. ARQUITECTURA FUNCIONAL DEL SISTEMA**
=========================================

Este capítulo describe cómo el modelo conceptual presentado en el capítulo anterior se materializa dentro de la aplicación. Mientras que el capítulo 2 definía las entidades fundamentales del sistema (Orden, Tramo, Parada y Viaje) desde un punto de vista conceptual, el presente capítulo explica cómo dichas entidades se organizan dentro de la estructura funcional del TMS y cómo interactúan con los diferentes componentes del sistema.

El objetivo es proporcionar una visión clara de la organización del sistema dentro de la plataforma Odoo, identificando los menús principales, los modelos de datos operativos y los módulos funcionales que permiten ejecutar la operativa diaria del transporte.

**3.1 Organización funcional del sistema**
------------------------------------------

Guraify TMS organiza sus funcionalidades en varios bloques que reflejan la lógica operativa de una empresa de transporte. Esta organización permite separar claramente las actividades de ejecución diaria, planificación, gestión económica y configuración estructural del sistema.

La estructura principal del sistema se divide en cuatro áreas funcionales:

- Operaciones

- Administración

- Maestros

- Configuración

Cada una de estas áreas agrupa distintos menús y herramientas que permiten gestionar los diferentes aspectos de la operativa del transporte.

**3.1.1 Operaciones**
~~~~~~~~~~~~~~~~~~~~~

El bloque de Operaciones constituye el núcleo operativo del sistema. En esta sección se gestionan las entidades vivas del modelo conceptual y se ejecuta la operativa diaria del departamento de tráfico.

Este bloque se organiza en tres subconjuntos funcionales:

**Tráfico**
^^^^^^^^^^^

Contiene las herramientas utilizadas para gestionar la demanda de transporte y la ejecución de los servicios, incluye los siguientes menús principales:

- Órdenes

- Viajes

- Manifiestos

- API Inbox

Estas herramientas permiten registrar los encargos de los clientes, estructurar las expediciones, organizar los servicios y controlar su ejecución.

**Planificación**
^^^^^^^^^^^^^^^^^

La sección de planificación agrupa las herramientas destinadas a organizar los recursos y optimizar la ejecución de los servicios.

Incluye:

- Plan de disponibilidad de conductores

- Optimizador de Paradas

Estas herramientas permiten gestionar la disponibilidad de recursos humanos y ejecutar procesos de optimización de rutas mediante el motor de planificación integrado.

**Maestros operativos**
^^^^^^^^^^^^^^^^^^^^^^^

Esta sección agrupa entidades operativas que forman parte del modelo logístico y que son utilizadas por los distintos procesos del sistema.

Incluye:

- Tramos

- Paradas

- Bultos

- Trazabilidad

Aunque estas entidades se generan habitualmente de forma automática durante el flujo operativo, el sistema permite consultarlas y gestionarlas directamente desde estos menús para tareas de control, auditoría o gestión de incidencias.

**3.1.2 Administración**
~~~~~~~~~~~~~~~~~~~~~~~~

El bloque de Administración agrupa los procesos relacionados con la gestión económica del transporte.

En esta sección se gestionan los procesos administrativos derivados de la operativa logística, incluyendo:

- facturación a clientes

- liquidación de servicios a transportistas

- control de costes operativos

- seguimiento de estados económicos de las operaciones

La estrecha vinculación entre operativa y economía permite que los eventos logísticos generen automáticamente información económica coherente dentro del ERP.

**3.1.3 Maestros**
~~~~~~~~~~~~~~~~~~

La sección de Maestros contiene las entidades estructurales que configuran el comportamiento del sistema.

Incluye información relativamente estable que se utiliza como base para los procesos operativos, tales como:

- clientes

- transportistas

- vehículos

- recursos humanos

- localizaciones

- proyectos logísticos

Estos datos constituyen la base de configuración sobre la que operan los diferentes módulos del TMS.

**3.1.4 Configuración**
~~~~~~~~~~~~~~~~~~~~~~~

La sección de Configuración permite definir los parámetros estructurales del sistema y adaptar su comportamiento a las necesidades específicas de cada implantación.

En esta área se gestionan, entre otros aspectos:

- parámetros del sistema

- configuración de integraciones

- reglas de negocio

- automatizaciones

- estructuras de planificación

- configuraciones de tarificación

Estas configuraciones permiten adaptar el TMS a distintos modelos operativos sin necesidad de modificar su arquitectura base.

**3.2 Modelo de datos operativo**
---------------------------------

Una vez descrita la organización funcional del sistema, el siguiente paso consiste en analizar las principales entidades de datos que soportan la operativa del transporte dentro de la aplicación.

Las entidades principales del modelo de datos operativo son:

- Órdenes

- Tramos

- Paradas

- Viajes

- Bultos

- Líneas de Venta

- Líneas de Compra

Cada una de ellas cumple un papel específico dentro del ciclo operativo del transporte.

**3.3 Modelo de planificación**
-------------------------------

El modelo de planificación agrupa las herramientas que permiten organizar la ejecución de los servicios de transporte teniendo en cuenta restricciones operativas, disponibilidad de recursos y objetivos de optimización.

Estas herramientas permiten transformar la demanda logística en rutas ejecutables asignadas a recursos concretos.

Incluye los siguientes elementos:

- Planning

- Planes de transporte

- Zonas geográficas

- Franjas horarias

- Tiempos de servicio

- Horas de conducción

Estos componentes permiten definir las reglas bajo las cuales el sistema puede organizar la ejecución de las operaciones.

**3.4 Modelo de tarificación**
------------------------------

El modelo de tarificación define las reglas mediante las cuales el sistema calcula automáticamente el precio de los servicios de transporte.

La arquitectura tarifaria del sistema permite representar distintos modelos comerciales y aplicar reglas complejas de cálculo basadas en múltiples variables logísticas.

Los elementos principales de este modelo son:

- Productos

- Reglas de tasación

- Zonas tarifarias

- Tarifas base

- Tarifas

- División de costes

Gracias a esta estructura, el sistema puede calcular automáticamente el ingreso asociado a cada operación a partir de su estructura logística.

**3.5 Modelo de integración**
-----------------------------

El modelo de integración define los mecanismos mediante los cuales el TMS puede intercambiar información con sistemas externos.

Estas integraciones permiten automatizar la entrada de demanda, sincronizar información con otros sistemas empresariales y facilitar la interoperabilidad con plataformas logísticas externas.

El sistema soporta distintos mecanismos de integración:

- Definición de ficheros estructurados

- Integraciones API

- Endpoints de servicio

- Webhooks

- Automatizaciones programadas

La arquitectura de integración permite que los datos externos se transformen directamente en entidades nativas del sistema, manteniendo la coherencia del modelo operativo interno.

4. PARAMETRIZACIÓN DEL SISTEMA
==============================

Este capítulo describe cómo se configura Guraify TMS para adaptarse a la operativa de una empresa de transporte. A diferencia de los capítulos anteriores —donde se ha explicado el modelo conceptual y la arquitectura funcional— aquí se documentan los elementos de parametrización que permiten que el sistema reproduzca el comportamiento real del negocio.

La parametrización no consiste únicamente en introducir datos en tablas de configuración. Cada elemento definido en este capítulo influye directamente en el funcionamiento de los algoritmos de planificación, en el cálculo económico de los servicios y en la lógica de ejecución operativa.

Por este motivo, la configuración se organiza en distintos bloques que reflejan las dimensiones fundamentales del sistema:

- configuración operativa

- configuración logística

- configuración de planificación

- configuración económica

- configuración de proyectos

Cada bloque agrupa registros maestros que definen reglas estructurales del sistema y que posteriormente serán utilizados por los procesos automáticos de generación de paradas, planificación de viajes, cálculo de tarifas y ejecución operativa.

Es importante entender que estas configuraciones no actúan de forma aislada. La mayoría de ellas se vinculan posteriormente dentro del Proyecto, que actúa como contenedor de configuración para cada operativa o cliente.

4.1 Configuración Operativa Inicial
-----------------------------------

La configuración operativa inicial define las tipologías básicas que estructuran la actividad del sistema. Estas tipologías permiten clasificar los distintos tipos de servicios, órdenes, paradas y participantes que intervienen en la operativa logística.

Aunque conceptualmente son simples catálogos, su impacto es significativo porque muchos procesos automáticos del sistema utilizan estas clasificaciones como criterios de filtrado, segmentación o aplicación de reglas.

Las tipologías definidas en esta sección se utilizan posteriormente en:

• reglas de tarifa

• filtros de planificación

• segmentación operativa

• validaciones de compatibilidad

• lógica de creación de órdenes

Dentro de este bloque se configuran los siguientes elementos.

4.1.1 Tipos de Servicio
~~~~~~~~~~~~~~~~~~~~~~~

Los Tipos de Servicio constituyen uno de los primeros elementos de configuración operativa del sistema. Su objetivo es clasificar la naturaleza de los servicios de transporte gestionados dentro del TMS y establecer la relación entre la operativa logística y los conceptos económicos que se utilizarán posteriormente en la facturación.

En la práctica, el tipo de servicio permite identificar el modelo de transporte que se está aplicando a una expedición. Esta clasificación facilita la gestión de diferentes operativas dentro de una misma organización, como por ejemplo:

- carga completa

- grupaje

- distribución urbana

- same da

- entregas con compromiso horario

La selección del tipo de servicio durante la creación de una orden no solo cumple una función descriptiva. También determina qué productos del catálogo de Odoo se utilizarán posteriormente para registrar los ingresos asociados a la operación.

De este modo, el tipo de servicio actúa como un elemento de conexión entre:

- la estructura operativa de la orden

- las variables logísticas que intervienen en el transporte

- la generación automática de conceptos económicos

Gracias a esta relación, el sistema puede traducir la información operativa del transporte en registros económicos sin necesidad de introducir datos adicionales durante el proceso de facturación.

Campos principales
^^^^^^^^^^^^^^^^^^

El modelo de tipos de servicio incluye los siguientes campos funcionales.

+-----------------------+------------------------------------------------------------------------------------------------------------------+
| **Campo**             | **Descripción**                                                                                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Nombre                | Identificador del tipo de servicio dentro del sistema. Permite reconocer la naturaleza operativa del transporte. |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Secuencia             | Orden de visualización utilizado para organizar los servicios en las interfaces del sistema.                     |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Descripción económica | Texto utilizado como concepto económico cuando el servicio genera líneas de facturación.                         |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Productos asociados   | Productos del catálogo de Odoo que se utilizarán para registrar los ingresos generados por el servicio.          |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Tipos de expedición   | Define qué tipos de expedición pueden utilizar este servicio.                                                    |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Bultos                | Indica si el número de bultos puede intervenir en el cálculo económico del servicio.                             |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Cantidad              | Permite utilizar la cantidad de unidades como variable logística relevante.                                      |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Metros                | Indica si los metros lineales deben considerarse en la valoración del servicio.                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Pallets               | Permite utilizar el número de pallets como dimensión logística.                                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Información adicional | Campo descriptivo utilizado para documentar características del servicio.                                        |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Compañía              | Permite definir configuraciones específicas en entornos multiempresa.                                            |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Color                 | Identificador visual utilizado en algunas interfaces de planificación.                                           |
+=======================+==================================================================================================================+

.. _section-25:

**Uso dentro del sistema**
--------------------------

Los tipos de servicio intervienen en diferentes procesos del TMS.

Durante la creación de órdenes, el tipo de servicio define la naturaleza operativa de la expedición y determina qué variables logísticas pueden utilizarse posteriormente en las reglas de cálculo económico.

Durante el proceso de tarificación, el servicio actúa como uno de los criterios utilizados para seleccionar las reglas de tarifa aplicables.

Finalmente, en el proceso de facturación, los productos asociados al servicio permiten generar automáticamente las líneas económicas correspondientes dentro del sistema ERP.

Este diseño permite mantener alineadas las tres dimensiones principales del sistema:

- operativa logística

- planificación de transporte

- gestión económica

[NOTE]

La correcta definición de los tipos de servicio es fundamental para garantizar que el cálculo de tarifas y la generación de ingresos reflejen correctamente la operativa real del transporte.

**4.1.2 Tipos de Orden**
~~~~~~~~~~~~~~~~~~~~~~~~

Los Tipos de Orden definen la naturaleza operativa de una expedición dentro del sistema. Mientras que los tipos de servicio clasifican la dimensión comercial del transporte, los tipos de orden describen el comportamiento logístico que tendrá la orden dentro del flujo operativo del TMS.

En otras palabras, el tipo de orden determina cómo se comporta una expedición dentro de la red logística.

Esta clasificación permite diferenciar distintos escenarios operativos, como por ejemplo:

• recogidas en origen

• entregas a destinatario

• operaciones entre hubs

• servicios directos

• movimientos internos dentro de la red

La definición del tipo de orden influye directamente en la forma en que el sistema genera la estructura logística de la expedición, especialmente en lo relativo a la creación de tramos y paradas.

Por este motivo, los tipos de orden forman parte de los elementos estructurales del modelo operativo del TMS.

.. _campos-principales-1:

**Campos principales**
^^^^^^^^^^^^^^^^^^^^^^

El modelo de tipos de orden incluye los siguientes campos funcionales.

+-------------+------------------------------------------------------------------------------------------------------------------------+
| **Campo**   | **Descripción**                                                                                                        |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Nombre      | Identificador del tipo de orden dentro del sistema. Permite reconocer el tipo de operación logística que representa.   |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Secuencia   | Orden de visualización utilizado para organizar los tipos de orden dentro de las interfaces del sistema.               |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Descripción | Texto descriptivo utilizado para documentar el comportamiento del tipo de orden.                                       |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Compañía    | Permite definir configuraciones específicas en entornos multiempresa.                                                  |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Color       | Identificador visual utilizado en algunas interfaces para facilitar la identificación de los distintos tipos de orden. |
+=============+========================================================================================================================+

**Papel dentro del modelo operativo**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los tipos de orden intervienen principalmente durante el proceso de creación y estructuración de una orden de transporte.

Cuando se registra una nueva expedición en el sistema, el tipo de orden seleccionado indica al sistema qué lógica operativa debe aplicarse para generar la estructura logística de la operación.

Esta lógica puede afectar, entre otros aspectos, a:

• la creación automática de tramos

• la generación de paradas de recogida y entrega

• la clasificación de la operación dentro de la red logística

Gracias a esta configuración, el sistema puede adaptar su comportamiento a distintos modelos operativos sin necesidad de modificar la lógica interna del módulo.

Por ejemplo, una empresa puede gestionar simultáneamente:

• servicios directos entre origen y destino

• operativas hub-and-spoke

• redes de distribución urbana

Cada uno de estos modelos puede utilizar tipos de orden distintos que permitan al sistema interpretar correctamente el flujo logístico de la expedición.

⸻

Relación con otros elementos del sistema

Los tipos de orden interactúan con varios componentes clave del modelo operativo del TMS.

En primer lugar, se utilizan durante la creación de órdenes de transporte, donde determinan el comportamiento logístico de la expedición.

Posteriormente, esta información se utiliza durante la generación de tramos y paradas, que constituyen la estructura operativa que será utilizada por el proceso de planificación.

Además, el tipo de orden puede utilizarse como criterio en distintos procesos de configuración, como por ejemplo:

• reglas de planificación

• reglas de tarifa

• validaciones operativas

De esta forma, los tipos de orden permiten adaptar el comportamiento del sistema a distintos modelos logísticos sin alterar la arquitectura general del TMS.

⸻

Note

En el modelo conceptual del sistema, el tipo de orden actúa como uno de los elementos que determinan cómo se estructura una expedición en términos de tramos y paradas. Su correcta configuración resulta esencial para que el sistema represente fielmente la operativa logística de la empresa.

⸻

Si quieres, en el siguiente paso podemos hacer 4.1.3 Tipos de Parada.

Ese apartado es todavía más interesante a nivel de arquitectura, porque conecta directamente con:

• la trazabilidad

• la ejecución del viaje

• la app del conductor

• los eventos logísticos.

4.1.3 Tipos de Parada
~~~~~~~~~~~~~~~~~~~~~

4.1.4 Tipos de Destinatario
~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.1.5 Tipos de Transportista
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.1.6 Tipos de Reembolso
~~~~~~~~~~~~~~~~~~~~~~~~

4.2 Configuración Logística
---------------------------

4.2.1 Equipamientos
~~~~~~~~~~~~~~~~~~~

4.2.2 Categorías de Carga
~~~~~~~~~~~~~~~~~~~~~~~~~

4.2.3 Tipo de Bulto
~~~~~~~~~~~~~~~~~~~

4.2.4 Modelos de Vehículo
~~~~~~~~~~~~~~~~~~~~~~~~~

4.3 Configuración de Planificación
----------------------------------

4.3.1 Planning
~~~~~~~~~~~~~~

4.3.2 Planes de Transporte
~~~~~~~~~~~~~~~~~~~~~~~~~~

4.3.3 Áreas Geográficas
~~~~~~~~~~~~~~~~~~~~~~~

4.3.4 Franjas Horarias
~~~~~~~~~~~~~~~~~~~~~~

4.3.5 Tiempos de Servicio
~~~~~~~~~~~~~~~~~~~~~~~~~

4.3.6 Horas de Conducción
~~~~~~~~~~~~~~~~~~~~~~~~~

4.4 Configuración Económica
---------------------------

4.4.1 Zonas Tarifarias
~~~~~~~~~~~~~~~~~~~~~~

4.4.2 Tarifas Base
~~~~~~~~~~~~~~~~~~

4.4.3 Reglas de Tarifa
~~~~~~~~~~~~~~~~~~~~~~

4.4.4 Tarifas
~~~~~~~~~~~~~

4.4.5 Productos asociados
~~~~~~~~~~~~~~~~~~~~~~~~~

4.5 Configuración de Proyectos
------------------------------

.. _administración-1:

4.5.1 Administración
~~~~~~~~~~~~~~~~~~~~

4.5.2 Entrada Hub / Recogida
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.5.3 Activación
~~~~~~~~~~~~~~~~

4.5.4 Asignación
~~~~~~~~~~~~~~~~

4.5.5 Configuración App
~~~~~~~~~~~~~~~~~~~~~~~

4.5.6 Otros Parámetros
~~~~~~~~~~~~~~~~~~~~~~

5. FLUJO OPERATIVO END TO END
=============================

5.1 Creación de Orden
---------------------

5.2 Generación de Tramos
------------------------

5.3 Generación automática de Paradas
------------------------------------

5.4 Validación de Orden
-----------------------

5.5 Generación de Viajes
------------------------

5.5.1 Manual
~~~~~~~~~~~~

5.5.2 Automática con PTV
~~~~~~~~~~~~~~~~~~~~~~~~

5.6 Asignación de Recursos
--------------------------

5.7 Ejecución desde App
-----------------------

5.8 Cierre de Viaje
-------------------

5.9 Liquidación Económica
-------------------------

5.10 Facturación
----------------

6. APLICACIÓN MÓVIL
===================

6.1 Arquitectura funcional
--------------------------

6.2 Perfil de Aplicación
------------------------

6.3 Flujo del Conductor
-----------------------

6.4 POD Digital
---------------

6.5 POD Físico
--------------

6.6 Incidencias
---------------

6.7 Reembolsos
--------------

6.8 Escaneo Masivo y Spark Scan
-------------------------------

7. EDI E INTEGRACIONES
======================

7.1 Estrategia de Integración
-----------------------------

7.2 Importación de Ficheros
---------------------------

7.3 Mapeo de Campos
-------------------

7.4 Transformaciones Python
---------------------------

7.5 Integraciones API
---------------------

7.6 Configuración de Endpoints
------------------------------

7.7 Webhooks
------------

7.8 Acciones Automáticas
------------------------

7.9 Buenas Prácticas de Integración
-----------------------------------

8. ADMINISTRACIÓN Y CONTROL ECONÓMICO
=====================================

8.1 Modelo de Costes
--------------------

8.2 División de Ventas
----------------------

8.3 División de Costes
----------------------

8.4 Órdenes de Compra Automáticas
---------------------------------

8.5 Liquidación Transportistas
------------------------------

8.6 Cuenta Analítica
--------------------

8.7 Reporting
-------------

9. BUENAS PRÁCTICAS Y ARQUITECTURA RECOMENDADA
==============================================

9.1 Diseño Escalable de Proyectos
---------------------------------

9.2 Estructuración de Planning
------------------------------

9.3 Optimización de Reglas de Tarifa
------------------------------------

9.4 Diseño de Zonas Geográficas
-------------------------------

9.5 Control de Complejidad
--------------------------

9.6 Estrategia de Implantación Recomendada
------------------------------------------

.. _modelo-de-datos-operativo-1:

3.2 Modelo de Datos Operativo
-----------------------------

El modelo de datos operativo no debe entenderse únicamente como un conjunto de entidades técnicas, sino como la organización funcional del trabajo diario dentro del bloque Operaciones.

En el menú del TMS, el área de Operaciones se estructura en tres secciones claramente diferenciadas: Tráfico, Planificación y Maestros. Esta división no es casual. Responde a la separación entre ejecución diaria, optimización de recursos y consulta estructural del modelo.

En Tráfico se gestionan las entidades vivas que evolucionan constantemente: Órdenes, Viajes, Manifiestos y el API Inbox. Es el espacio natural del departamento de tráfico, donde se crea, ajusta y supervisa la actividad operativa.

En Planificación se concentran las herramientas que permiten organizar recursos y optimizar la ejecución. Aquí se trabaja con la disponibilidad de conductores y con el optimizador de paradas, conectando directamente con la integración PTV descrita en el capítulo anterior.

En Maestros, dentro del propio bloque de Operaciones, se exponen las entidades estructurales que sustentan la ejecución: Tramos, Paradas, Bultos y la Trazabilidad. Aunque conceptualmente dependen de Órdenes y Viajes, aquí se consultan y gestionan como registros independientes cuando la operativa lo requiere.

Esta organización permite que el usuario operativo entienda dónde debe trabajar según la naturaleza de la tarea: crear y gestionar servicios, planificar recursos o consultar el detalle estructural de la ejecución.

3.2.1 Órdenes
~~~~~~~~~~~~~

Las Órdenes se gestionan dentro de la sección Tráfico y constituyen la entidad contractual a partir de la cual se articula toda la operativa. Sin embargo, su creación no responde a un único patrón, sino a distintos flujos operativos que reflejan la realidad de una empresa de transporte.

Una Orden puede crearse de forma individual por parte del operador, cuando se trata de un servicio puntual o de baja volumetría. No obstante, en entornos profesionales lo habitual es la generación en bloque mediante Manifiestos.

El Manifiesto actúa como contenedor de importación y estructuración de múltiples órdenes. Desde él pueden crearse órdenes manualmente o generarse a partir de ficheros estructurados enviados por el cliente. Este mecanismo permite absorber grandes volúmenes de expediciones sin introducir registros uno a uno. A su vez, los Manifiestos pueden alimentarse automáticamente desde el API Inbox, cuando la información proviene de integraciones externas.

De esta forma, la Orden no es necesariamente el primer paso visible para el operador; puede ser el resultado de un proceso previo de consolidación e importación.

Nota:

Las Órdenes pueden crearse individualmente,

pero en entornos de alto volumen nacen habitualmente desde Manifiestos o integraciones.

Una vez generada, la Orden pasa a formar parte del circuito operativo y queda disponible para su descomposición en Tramos y su posterior planificación.

Estados de la Orden
^^^^^^^^^^^^^^^^^^^

La Orden combina tres dimensiones de estado que conviven en paralelo:

1. Estados comerciales nativos de Odoo (venta)
''''''''''''''''''''''''''''''''''''''''''''''

Al estar basada técnicamente en el modelo de pedido de venta, la Orden hereda los estados estándar:

- Presupuesto (draft)

- Presupuesto enviado (sent)

- Pedido de venta confirmado (sale)

- Bloqueado / Hecho (done)

- Cancelado (cancel)

Estos estados reflejan la dimensión contractual y administrativa del servicio.

.. _section-26:

2. Estados de facturación
'''''''''''''''''''''''''

De forma complementaria, la Orden dispone de la lógica de facturación propia de Odoo:

- A facturar (to invoice)

- Facturado (invoiced)

- Nada que facturar (no)

Esta capa indica el estado económico de la relación con el cliente, independientemente de la ejecución física.

3. Estado operativo
'''''''''''''''''''

Adicionalmente, la Orden dispone de un estado operativo dinámico, que no es estático ni manual, sino heredado del Tramo activo y, en última instancia, de la Parada activa.

Las opciones de estado operativo (tal como se observa en la configuración mostrada) incluyen, entre otras:

- Borrador (draft)

- En proceso (in_process)

- Procesado (processed)

- Hecho (completed)

- Reserva (reserves)

- Fallo (failed)

- Reprogramado (rescheduled)

- Devuelto (returned)

- Loaded (loaded)

- Running (running)

- Cancelado (canceled)

Este estado operativo se actualiza automáticamente a medida que se producen eventos reales: generación de tramos, planificación, carga, inicio de viaje, entrega, incidencias o devoluciones.

Importante:

El estado operativo de la Orden no se gestiona manualmente.

Es el reflejo dinámico de la ejecución real heredada de Tramos y Paradas.

Esta triple dimensión —comercial, económica y operativa— es coherente con la filosofía estructural del sistema. Una Orden puede estar confirmada comercialmente, pendiente de facturar y al mismo tiempo en ejecución operativa. Las tres capas conviven sin interferirse, permitiendo un control granular de cada dimensión.

Papel estructural dentro del modelo operativo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aunque en el menú de Maestros puedan consultarse Tramos, Paradas o Bultos de forma independiente, la Orden sigue siendo la referencia administrativa y contractual principal. Es el objeto que conecta:

- Cliente y proyecto.

- Estructura logística.

- Planificación.

- Facturación.

- Análisis de rentabilidad.

Su diseño híbrido —venta + ejecución + trazabilidad— es uno de los elementos que permiten integrar operativa y economía sin duplicar modelos.

3.2.2 Viajes
~~~~~~~~~~~~

Los Viajes se gestionan dentro de la sección Tráfico y representan la ejecución operativa real del transporte. Si la Orden define el compromiso comercial, el Viaje define cómo y con qué recursos se ejecuta físicamente ese compromiso.

Desde el punto de vista del departamento de tráfico, el Viaje es la entidad donde se materializa la planificación: aquí se agrupan Paradas, se asignan vehículos y conductores, se supervisa la ejecución y se controla el impacto económico del servicio.

Creación del Viaje
^^^^^^^^^^^^^^^^^^

Un Viaje puede generarse de tres maneras distintas, dependiendo del modelo operativo:

1. Creación manual mediante agrupación de Paradas
'''''''''''''''''''''''''''''''''''''''''''''''''

El operador selecciona Paradas y las agrupa en un Viaje. Este escenario es habitual en operativas de distribución donde el vehículo carga en uno o varios hubs y reparte múltiples entregas.

En este caso, tras la agrupación, la secuencia de entrega puede definirse manualmente o optimizarse posteriormente mediante el servicio de secuenciación.

2. Creación a través del Optimízador de Paradas
'''''''''''''''''''''''''''''''''''''''''''''''

En este escenario, el sistema utiliza el motor de optimización para asignar y secuenciar automáticamente las Paradas. El resultado final es un Viaje ya ordenado y estructurado conforme a las restricciones configuradas (capacidades, ventanas horarias, horas de conducción, etc.).

Este modelo es propio de distribuciones complejas, grupaje o entornos multihub.

3. Creación automática al validar la Orden
''''''''''''''''''''''''''''''''''''''''''

En operativas directas o puerta a puerta, donde una Orden equivale prácticamente a un servicio individual, el Viaje puede generarse automáticamente en el momento de validar la Orden.

Este modelo es habitual en transportes directos con asignación inmediata de recurso.

Importante:

El Viaje puede generarse manualmente, mediante optimización o automáticamente desde la Orden.

Pero siempre nace a partir de Paradas previamente estructuradas.



Secuenciación y Enriquecimiento mediante Routing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando el Viaje se crea manualmente, es necesario definir el orden de ejecución. Esto puede hacerse manualmente o mediante el servicio de secuenciación.

Independientemente del método de creación, todos los Viajes se enriquecen mediante el servicio de Routing. Este proceso añade:

- Polilínea de la ruta óptima.

- Rutas alternativas disponibles.

- Kilómetros totales y entre paradas.

- Tiempos estimados de conducción y servicio.

- Peajes.

- Emisiones estimadas de CO₂.

Este enriquecimiento convierte el Viaje en un objeto dinámico y medible, no en una simple agrupación de paradas.

Ver Tambien:

Para más detalle técnico sobre Routing, Secuenciación y Optimización avanzada, consultar la sección 1.4.2 Integración con PTV.



Relación entre Viaje y Orden de Compra
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Desde el punto de vista económico, el Viaje es la unidad de coste del sistema.

Cada vez que se trafica por primera vez el pasivo asociado a un Viaje —es decir, cuando se confirma la ejecución económica hacia un transportista— el sistema genera automáticamente una Orden de Compra vinculada a ese Viaje.

Esta relación es estructural:

- La Orden de Compra representa el compromiso económico con el proveedor.

- El Viaje representa la ejecución operativa que origina ese coste.

No se generan órdenes de compra independientes del modelo operativo; el coste siempre nace de la ejecución real.

Nota:

La Orden genera ingreso.

El Viaje genera coste mediante su Orden de Compra asociada.



Estados del Viaje: tres dimensiones simultáneas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Viaje dispone de tres dimensiones de estado que conviven de forma independiente pero relacionada.

1. Estado Operativo (trip.state)
''''''''''''''''''''''''''''''''

Es el estado propio del Viaje y refleja la situación real de ejecución:

- Borrador

- En proceso

- Procesado

- Hecho

- Fallo

Este estado evoluciona dinámicamente en función de los eventos reportados desde la app móvil y de las acciones realizadas en tráfico.

.. _section-27:

2. Estado Administrativo (po_state)
'''''''''''''''''''''''''''''''''''

Corresponde al estado de la Orden de Compra asociada:

- Solicitud de presupuesto

- Enviado

- Para aprobar

- Pedido de compra

- Bloqueado

- Cancelado

Este estado refleja la dimensión contractual con el transportista.

.. _section-28:

3. Estado de Facturación (invoice_status)
'''''''''''''''''''''''''''''''''''''''''

También heredado de la Orden de Compra, indica la situación económica:

- Nada para facturar

- Para facturar

- Totalmente facturado

Estas tres capas permiten que un Viaje pueda estar:

- Operativamente completado,

- Administrativamente confirmado,

- Y económicamente pendiente de facturar.

O cualquier combinación intermedia.

Importante:

El Viaje no tiene un único estado.

Tiene estado operativo, administrativo y económico.



.. _papel-dentro-del-modelo-operativo-1:

Papel dentro del modelo operativo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Viaje es el punto de convergencia entre planificación, ejecución y coste. Es donde se cruzan:

- Paradas estructuradas.

- Recursos asignados.

- Optimización matemática.

- Control económico.

- Seguimiento en tiempo real.

Si la Orden representa el contrato con el cliente, el Viaje representa la realidad operativa sobre el terreno.

.. _section-29:

3.2.3 Manifiestos
~~~~~~~~~~~~~~~~~

El Manifiesto es el mecanismo de entrada masiva de expediciones en el sistema. No representa una ejecución operativa ni una entidad económica en sí misma; su función es estructurar la demanda antes de que esta entre en el circuito operativo definitivo.

En entornos profesionales de transporte, especialmente en distribución, grupaje o última milla, las expediciones no se crean una a una. El cliente envía información estructurada con múltiples servicios. El Manifiesto es el contenedor que permite absorber esa información, validarla y transformarla en Órdenes operativas coherentes con el modelo del TMS.

Origen del Manifiesto
^^^^^^^^^^^^^^^^^^^^^

Un Manifiesto puede generarse de distintas maneras:

- Importación de fichero estructurado (CSV, Excel u otro formato acordado con el cliente).

- Generación automática desde el API Inbox, cuando la información proviene de integraciones externas.

- Creación manual por parte del operador.

- Generación desde el Portal de Clientes.

Independientemente del origen, el comportamiento interno es el mismo: el sistema crea inicialmente las Órdenes y sus Tramos asociados, pero todavía no genera Paradas ni Viajes. En esta fase la información está estructurada a nivel contractual y logístico, pero no está preparada para planificación.

El cierre del Manifiesto: transformación a estructura operativa
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El momento clave del Manifiesto es su cierre. Cerrar un Manifiesto no es una acción administrativa simple; es el proceso que transforma expediciones estructuradas en eventos físicos planificables.

Durante el cierre, el sistema ejecuta un algoritmo que:

1. Recorre todas las expediciones (Shipments) y sus tramos operativos (Legs).

2. Completa y consolida la información de carga y descarga.

3. Agrupa tramos que, en la práctica, deben convertirse en una misma Parada (por tipo de operación, localización y ventana horaria).

4. Crea las Paradas correspondientes.

5. Genera, cuando la configuración del proyecto lo contempla o cuando la información lo permite, los Viajes asociados.

6. Ordena internamente las Paradas dentro de cada Viaje según la secuencia lógica de carga y descarga.

7. Marca las entidades generadas para su posterior cálculo de tarifa.

Nota:

Mientras el Manifiesto no esté cerrado, no existen Paradas planificables.

El cierre convierte estructura administrativa en estructura operativa real.

A partir de ese momento, las expediciones abandonan la fase de entrada de datos y pasan al circuito normal de planificación y ejecución.

.. _section-30:

Reglas de validación y bloqueos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El cierre del Manifiesto incorpora controles estructurales que garantizan la coherencia del modelo antes de permitir la generación de Paradas.

Entre los principales motivos de bloqueo se encuentran:

- Localizaciones marcadas como “Normalizable”: si un punto de recogida o entrega no dispone de coordenadas válidas o su calidad es inferior al umbral configurado, el sistema impide el cierre. El operario debe normalizar manualmente la dirección antes de continuar.

- Información horaria obligatoria no informada: en proyectos donde se gestionan ventanas horarias en puntos de recogida o entrega, la ausencia de esta información también bloquea el proceso.

Estos controles evitan que se generen Paradas sobre información espacial o temporal imprecisa, protegiendo la planificación posterior.

Peligro:

No se permite avanzar hacia planificación si la información geográfica o temporal no es fiable.



.. _section-31:

Relación con el modelo operativo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una vez cerrado el Manifiesto:

- Las Órdenes quedan activas.

- Los Tramos generan sus Paradas.

- Las Paradas pasan a estar disponibles en Planificación.

- Los Viajes pueden generarse automáticamente o construirse posteriormente.

- Las estructuras creadas quedan marcadas para cálculo de tarifa.

El Manifiesto deja de intervenir en el flujo operativo. Su función ha sido cumplida: transformar datos de entrada en estructura operativa coherente con el modelo Orden–Tramo–Parada–Viaje.

.. _section-32:

Papel arquitectónico dentro del TMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Desde una perspectiva arquitectónica, el Manifiesto actúa como frontera entre el exterior y el núcleo operativo del sistema, permite desacoplar:

- Integraciones y cargas masivas.

- Modelo estructural interno.

- Planificación avanzada.

- Impacto económico posterior.

En empresas de alto volumen, el Manifiesto no es simplemente una herramienta de importación. Es el mecanismo que garantiza que la demanda entre al sistema bajo reglas de calidad, coherencia geográfica y consistencia temporal antes de convertirse en ejecución real.

3.2.4 API Inbox
~~~~~~~~~~~~~~~

El API Inbox es la herramienta utilizada para gestionar la entrada de Órdenes provenientes de clientes integrados mediante Web Service. Su función no es crear directamente estructuras operativas definitivas, sino registrar, organizar y transformar las llamadas recibidas antes de convertirlas en Manifiestos.

Cuando un cliente está integrado con el TMS, las Órdenes no se introducen manualmente ni mediante fichero. Se transmiten mediante API en tiempo real. Cada llamada queda registrada en el sistema y visible dentro del API Inbox.

Desde el punto de vista del usuario, lo que se visualiza en el API Inbox es un conjunto de registros agrupados por orden recibida. Cada registro representa una llamada entrante, con su información estructurada, lista para ser procesada.

.. _section-33:

.. _section-34:

.. _section-35:

Funcionamiento operativo
^^^^^^^^^^^^^^^^^^^^^^^^

El API Inbox puede gestionarse de dos formas:

.. _section-36:

1. Cierre automático programado
'''''''''''''''''''''''''''''''

Puede configurarse un cierre automático diario.

Este modelo es habitual cuando existe un acuerdo operativo con el cliente del tipo:

   “Todo lo que entre hoy hasta las XX:XX se entregará mañana”.

En este escenario, el sistema agrupa automáticamente todas las llamadas recibidas dentro del intervalo definido y genera un Manifiesto automático, que a su vez crea las Órdenes y Tramos correspondientes.

Este enfoque permite automatizar completamente la entrada de demanda cuando el modelo operativo es estable y predecible.

2. Cierre manual por parte del operador
'''''''''''''''''''''''''''''''''''''''

En escenarios más dinámicos —por ejemplo, cuando las órdenes entran para distintas fechas de entrega— el operador de tráfico debe intervenir.

El flujo habitual es:

1. Acceder al API Inbox.

2. Agrupar los registros por fecha operativa o criterio necesario.

3. Seleccionar las órdenes que deben consolidarse.

4. Ejecutar la acción de Crear Manifiesto.

Este proceso genera un Manifiesto que crea las Órdenes y sus Tramos asociados, pasando posteriormente al flujo de cierre y validación descrito en el apartado anterior.

Importante:

El API Inbox no genera directamente Paradas ni Viajes.

Genera Manifiestos que estructuran la demanda antes de entrar en ejecución.



.. _section-37:

.. _section-38:

Relación con el Manifiesto
^^^^^^^^^^^^^^^^^^^^^^^^^^

El API Inbox es, en la práctica, una capa previa al Manifiesto cuando la entrada es vía integración.

- API → API Inbox → Manifiesto → Órdenes/Tramos → Cierre → Paradas/Viajes

Este desacoplamiento permite:

- Revisar llamadas antes de impactar en operativa.

- Agrupar órdenes según criterio operativo.

- Mantener trazabilidad técnica de lo recibido.

- Evitar generación automática de estructuras sin control humano cuando el proyecto lo requiere.

Papel dentro de la arquitectura
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arquitectónicamente, el API Inbox actúa como buffer entre sistemas externos y el modelo interno del TMS.

Permite absorber entradas en tiempo real sin romper la coherencia estructural del sistema y mantiene el principio fundamental ya descrito en capítulos anteriores: ninguna entidad operativa crítica se genera sin pasar por un proceso de validación y estructuración previo.

En proyectos altamente integrados, el API Inbox se convierte en el punto de control diario del departamento de tráfico para gestionar demanda entrante digital.

.. |image1| image:: images/media/image1.png
   :width: 5.7224in
   :height: 8.95518in
.. |image2| image:: images/media/image2.png
   :width: 6.23651in
   :height: 3.60855in
