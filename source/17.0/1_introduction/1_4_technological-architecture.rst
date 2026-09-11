1.4 Arquitectura tecnológica
----------------------------

Guraify TMS está construido sobre una arquitectura modular que separa la capa de datos, la
lógica de negocio y la presentación, siguiendo las prácticas del framework Odoo. No es una
aplicación monolítica, sino un conjunto de bloques que se hablan de forma controlada: la
plataforma ERP, los módulos del TMS, los servicios cartográficos de PTV, la capa de integración
con sistemas externos y la aplicación móvil del conductor. Cada bloque puede evolucionar sin
comprometer el núcleo funcional.

Esta sección describe cada bloque **tal y como está implementado**. Lo que está en desarrollo se
recoge aparte, al final, en
:ref:`17.0/1_introduction/1_4_technological-architecture:1.4.6 Evolución prevista`.

.. mermaid::

   flowchart TB
       ODOO[Plataforma ERP Odoo 17] --> TMS[Guraify TMS]
       TMS --> PTV[Servicios PTV<br/>geocodificación · mapa · cálculo de ruta<br/>secuenciación · optimización]
       PTV -.respaldo.-> OSM[Google · OpenStreetMap]
       TMS --> INT[Capa de integración<br/>ficheros · API REST · webhooks]
       TMS --> APP[App móvil del conductor<br/>POD · escaneo Scandit · trazabilidad]
       INT <--> EXT[Sistemas externos]

1.4.1 Plataforma base Odoo
~~~~~~~~~~~~~~~~~~~~~~~~~~

El núcleo es Odoo 17, que aporta el ORM, la seguridad por roles, las vistas, las
automatizaciones y la integración nativa con la contabilidad y la analítica. El TMS se
implementa como una extensión sobre esa base y reutiliza lo que ya existe: contabilidad y
facturación, contactos, empleados, la app Planificación de Odoo, flota, proyectos, documentos
adjuntos y acciones automáticas y programadas. Así el TMS no es un sistema aislado, sino una
especialización logística dentro de un ERP horizontal: la factura del transporte es una
factura de Odoo y el Transportista es un proveedor de Odoo.

Guraify TMS se distribuye como un conjunto de módulos, uno o varios por área funcional:

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - Área
     - Módulos
     - Notas
   * - Gestión de Órdenes y ejecución
     - ``tms``
     - Núcleo. Requiere Ventas, Compras, Contabilidad, Flota, Proyectos, Planificación e
       Inventario de Odoo
   * - Planificación y optimización
     - ``tms``, ``tms_map``
     - Motor PTV opcional
   * - Tarificación y facturación
     - ``tms``
     - Sobre la facturación de Odoo
   * - App del conductor
     - ``tms_app``, ``tms_branding``
     - Más la app móvil, distribuida aparte
   * - Integraciones
     - ``tms_int``, ``tms_portal``
     - Más la pasarela de API para sistemas externos
   * - Tableros e indicadores
     - ``tms_dashboard``, ``tms_dashboard_filters``, ``tms_kpi``
     - Sobre los tableros de hoja de cálculo de Odoo
   * - Gestión de recursos
     - ``tms_resources``, ``tms_maintenance``
     - Sobre Flota y Mantenimiento de Odoo
   * - Entorno de demostración
     - ``tms_demo_config``, ``tms_demo_master``
     - Solo para demos y pilotos

1.4.2 Servicios de PTV
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   Ajustes › Integraciones › Rutas del mapa (PTV) › Token

PTV Developer es el proveedor cartográfico y matemático del sistema: geocodifica direcciones,
sirve el mapa base, calcula rutas, ordena Paradas y propone Viajes completos. El contrato con
PTV se paga **por vehículo**, no por llamada; el TMS se autentica con **un token por compañía**,
de modo que cada compañía consume su propia cuota aunque el usuario que lance el cálculo trabaje
en varias. Sin token, o si PTV no responde, el sistema sigue funcionando sobre OpenStreetMap y
planifica a mano.

La regla de diseño no cambia por usar PTV: la entidad planificable sigue siendo la Parada y la
unidad de ejecución el Viaje. PTV aporta el cálculo sobre esa estructura, no la sustituye. En la
planificación intervienen tres servicios, con tres niveles de uso progresivos:

.. list-table::
   :header-rows: 1
   :widths: 14 26 30 30

   * - Servicio
     - Cuándo se lanza
     - Qué envía el TMS
     - Qué vuelve y dónde queda
   * - **Cálculo de ruta**
     - Al crear Viajes desde un Manifiesto que trae la secuencia; al reordenar, añadir o quitar
       Paradas en el mapa del Optimizador; con el botón **Enrutar Viaje** del Viaje.
     - Cada Parada con su coordenada, tiempo de servicio y franja horaria; el perfil de vehículo
       de la categoría; el perfil de jornada; la hora de salida; tráfico realista.
     - En el Viaje: trazado, distancia, duración y hora prevista de fin. En cada Parada: ETA,
       llegada, salida, kilómetros y tiempo de conducción acumulados.
   * - **Secuenciación**
     - Con el botón **Secuenciar Viaje** del Viaje o desde el Optimizador de Paradas sobre un
       Viaje ya formado; al cerrar un Manifiesto sin secuencia si el Proyecto tiene activado
       **Secuenciar Viaje**.
     - Las Paradas como transportes con cantidades, tiempo de servicio y prioridad; horarios
       de apertura de Hubs y Clientes; perfil, inicio, fin y distancia máxima del vehículo;
       disponibilidad del conductor.
     - El nuevo orden de las Paradas y sus horas de llegada y salida. Después se relanza el
       cálculo de ruta para refrescar el trazado.
   * - **Optimización completa**
     - Desde el Optimizador de Paradas sobre las Paradas pendientes de una fecha.
     - Vehículos con capacidades, equipamiento, inicio, fin y distancia máxima; conductores con
       disponibilidad y jornada; transportes con cantidades, tiempos de servicio y prioridad;
       Hubs con horarios.
     - Viajes nuevos con sus Paradas asignadas y secuenciadas, vehículo y conductor, horas por
       Parada, y la lista de lo que no se ha podido planificar.

El **cálculo de ruta** es el nivel básico: el Viaje ya existe, con sus Paradas y su recurso, y
PTV lo enriquece con la red viaria profesional. Las horas de conducción y las pausas las fija el
:term:`perfil de jornada <Perfil de jornada>` (por defecto, el reglamento europeo 561/2006): si
el Viaje nace de una franja del :term:`Plan de disponibilidad de conductores`, se usa el perfil
de esa franja; si no, el de la categoría del vehículo. El ETA que devuelve es el que ven el
planificador, el conductor en la app y, por las integraciones, el Cliente. El cálculo cubre
siempre el Viaje completo desde su hora de salida.

La **secuenciación** actúa cuando las Paradas ya están en un Viaje pero su orden no es el mejor.
Las cantidades de cada Parada se envían en seis dimensiones (peso, volumen, bultos, palés,
unidades y metros lineales) y los horarios de Hubs y Clientes salen de las franjas por día de
cada contacto. El TMS aplica el orden devuelto conservando la vinculación de cada Parada con su
Tramo y su Orden. Si alguna Parada no cabe en las restricciones, avisa al planificador con la
lista.

La **optimización completa** no ordena Paradas dentro de un Viaje: propone qué Viajes crear y
cómo llenarlos. Se lanza desde el :term:`Optimizador de Paradas` en uno de dos modos. En el
**modo por franja**, cada franja del Plan de disponibilidad aporta un vehículo y un conductor
concretos, con su disponibilidad y su perfil de jornada, y el resultado los deja asignados a
cada Viaje. En el **modo por categoría de vehículo**, el planificador indica cuántos vehículos de
cada categoría tiene, sin decir cuáles, y el recurso se asigna después. Las Paradas se envían como
entregas desde el Hub, recogidas hacia el Hub o servicios directos, con capacidades reales en las
mismas seis dimensiones y respetando las prioridades. Si ningún vehículo puede cubrir las
Paradas, el sistema lo dice con las causas posibles (capacidad, jornada, distancia máxima o
número de Paradas) en lugar de crear Viajes vacíos. El planificador revisa la propuesta, la
ajusta a mano si hace falta y la confirma. Toda la parametrización sale de los maestros del TMS:
categorías de vehículo, planes de disponibilidad, horarios de los contactos y tiempos de
servicio.

1.4.2.1 El ETA durante la ejecución
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › bloque «Operation» › «Operations Policy» para la política;
   pestaña «ETA and Routing» del Viaje, con el botón «Recompute ETA Now», para el resultado.
   Las etiquetas están en inglés en la interfaz.

Cuando el Viaje está en marcha, el ETA de las Paradas que quedan por hacer se vuelve a calcular.
Hay dos niveles. El **recálculo ligero** reutiliza el cálculo de ruta que PTV ya hizo y le pide
solo la llegada a lo pendiente, a partir de la posición real del vehículo si el sistema la conoce
o, si no, de la última Parada cerrada y el tiempo de servicio consumido en ella. El **recálculo
completo** repite el cálculo de ruta sobre las Paradas pendientes, y solo se hace cuando el
anterior no sirve: el Viaje nunca se enrutó, el cálculo guardado ha caducado, la secuencia cambió
o PTV lo rechaza. El completo deja un cálculo fresco que abarata el siguiente.

Cuándo se recalcula lo decide una **política operativa** por compañía, que un Proyecto puede
sobrescribir para sus Viajes: al cerrarse cada Parada (el comportamiento por defecto), cada
cierto número de minutos, ambas cosas, al desviarse el vehículo del plan, o nunca. La política
fija también un espaciado mínimo entre recálculos y un tope diario por Viaje, porque cada
recálculo es una llamada a PTV. El planificador puede forzar uno desde el Viaje; la política se
aplica igual.

El ETA que se prometió al planificar se conserva junto al vigente, y cada Parada guarda el
historial de sus ETA con la posición desde la que se calcularon, de modo que la deriva respecto a
la promesa se puede leer y medir. Si PTV falla, el sistema deja los valores anteriores y marca el
ETA de las Paradas pendientes como obsoleto, en lugar de borrarlo.

Sobre el mismo cálculo de ruta, el Viaje se **enriquece** sin repetirlo: los **peajes**,
que PTV desglosa por país y moneda, se suman en la moneda del Viaje; las **emisiones de CO₂**
(del depósito a la rueda y del pozo a la rueda) y el **consumo** se toman según el esquema que
elija la política, EN 16258:2012 o ISO 14083:2023, y las emisiones del Viaje se reparten a las
Órdenes que lleva, por distancia recorrida o por número de Paradas. Lo que PTV devuelve y no
tiene campo propio se guarda tal cual en el Viaje para su análisis posterior.

1.4.2.2 Referencia técnica
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Elemento
     - Modelo / campo
     - Qué es
   * - Política operativa
     - ``tms.operations.policy``
     - Una por compañía y, opcionalmente, una por Proyecto (gana la del Proyecto):
       ``eta_recompute_mode``, ``eta_recompute_interval_min``, ``eta_recompute_min_gap_min``,
       ``eta_daily_call_cap``, ``routing_results_toll``, ``routing_results_emissions``,
       ``co2_allocation_method``
   * - ETA de la Parada
     - ``tms.stop``: ``eta``, ``eta_planned``, ``eta_stale``, ``eta_drift_min``
     - ETA vigente, ETA prometido al planificar, marca de obsoleto y deriva en minutos
   * - Historial de ETA
     - ``tms.stop.eta.history``
     - Una fila por recálculo y Parada, con origen, posición y retraso por tráfico
   * - Enriquecimiento del Viaje
     - ``tms.trip``: ``toll_cost``, ``co2e_ttw_kg``, ``co2e_wtw_kg``, ``fuel_consumption_l``,
       ``emissions_scheme``, ``routing_enrichment_json``
     - Peajes, emisiones, consumo, esquema aplicado y el resto de la respuesta en bruto
   * - Emisiones de la Orden
     - ``sale.order``: ``co2e_wtw_kg``
     - La parte del CO₂ del Viaje que corresponde a la Orden
   * - Perfil de jornada
     - ``tms.driver.working.hours``
     - Se elige en la plantilla de la franja del Plan de disponibilidad y en la categoría del
       vehículo
   * - Tarea programada
     - «TMS: recompute ETA of running trips»
     - Cada minuto atiende la cola de recálculos pendientes según la política

1.4.3 Geolocalización, mapa y áreas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La geolocalización es un fundamento estructural, no un accesorio: de ella dependen la
asignación a planes de transporte, la tarificación por zonas, el cálculo de ruta y la
planificación. Tres geometrías bastan para todo. La **coordenada** (latitud y longitud)
representa una localización; el **polígono**, guardado en GeoJSON, representa un área; la
**polilínea** representa el trazado que devuelve el cálculo de ruta.

1.4.3.1 Geocodificación de direcciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cada dirección se convierte en coordenada mediante una cascada de cuatro proveedores, por
orden de preferencia: PTV con la dirección completa; Google Maps, si la compañía tiene
configurada su clave; PTV de nuevo, solo con país, provincia y código postal; y OpenStreetMap
(Nominatim) como respaldo gratuito. Cada resultado trae una **puntuación de calidad** y un tipo
de precisión, que se guardan en la localización. Una coordenada con puntuación inferior a 80,
o que solo llega a precisión de código postal, queda **pendiente de normalizar**: sitúa el punto
en el mapa, pero no vale para planificar. La Orden señala sus direcciones pendientes, el
Manifiesto no se cierra mientras las haya y la normalización se hace a mano sobre la ficha de la
localización, con un buscador sobre el mapa. Los criterios exactos están en
:doc:`/17.0/3_functional-architecture/3_2_3_manifests`.

La cascada funciona también al revés: cuando una localización llega con coordenada pero sin
código postal, localidad o país, el sistema completa la dirección a partir del punto.

1.4.3.2 Mapa base
^^^^^^^^^^^^^^^^^

El mapa del backend de Odoo (la vista mapa, el Optimizador de Paradas y el editor de áreas) y el
mapa de la app del conductor se dibujan con MapLibre GL sobre las **teselas vectoriales de PTV**,
autenticadas con el token de la compañía. Sin token, o si PTV no responde, el mapa arranca
sobre OpenStreetMap y lo avisa: la operación no se detiene por una caída del proveedor.

1.4.3.3 Áreas geográficas
^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Áreas Geográficas

Cualquier superficie con significado operativo es un :term:`Área geográfica` (``tms.area``): un
polígono GeoJSON con un tipo que dice para qué sirve. Hay cinco: área de un
:term:`Plan de transporte`, :term:`Zona de tarifa`, extra de tarifa (un área que el detalle de
una Línea de tarifa puede usar como criterio de precio), elemento de operación y zona de bajas
emisiones. Un área puede llevar los días y franjas horarias en que está activa.

Las áreas se **dibujan** sobre el mapa desde la ficha del área, de la Zona de tarifa o del Plan
de transporte, o se **importan de OpenStreetMap** con un asistente que busca límites
administrativos (municipios, comarcas, provincias) y los trae como polígonos, de uno en uno o
en bloque. Varias áreas se pueden fusionar en una.

La pregunta que responde el sistema es siempre la misma: ¿esta coordenada cae dentro de este
polígono? Con ella asigna cada Tramo a su zona operativa y a sus Zonas de tarifa de Cliente y
de Transportista, en origen y en destino. Si la coordenada no cae en ningún área, el Tramo
queda sin zona; el Proyecto puede pedir que en ese caso se asigne **el área más cercana**, con
una opción para la zona operativa y otra para la de tarifa. La asignación no se basa en texto ni
en códigos postales, sino en geometría sobre coordenadas verificadas: si se corrige la coordenada
de una dirección, su zona cambia sola.

1.4.4 Capa de integración
~~~~~~~~~~~~~~~~~~~~~~~~~

El sistema intercambia información con el exterior por cuatro canales: ficheros CSV o Excel con
una Definición de fichero por Cliente, una API REST con su Bandeja de entrada API, webhooks
entrantes protegidos con clave, y envíos salientes de estados y pruebas de entrega (POD) hacia el
sistema de cada Cliente. Delante de la API hay una pasarela con documentación interactiva,
autenticación y registro de cada llamada. El encuadre de esos mecanismos está en
:doc:`/17.0/3_functional-architecture/3_5_integration-model` y su detalle, canal por canal, en la
:doc:`Guía del integrador </17.0/7_edi-integrations/index>`.

1.4.5 La app del conductor y el escaneo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La aplicación móvil es una extensión operativa del backend de Odoo, no una interfaz de
confirmación. Es una app híbrida (Ionic y Capacitor) para iOS y Android que habla con Odoo por
una API propia: recibe el Viaje, guía al conductor Parada a Parada, registra estados,
incidencias, firmas, fotos y Reembolsos, y devuelve cada evento al TMS con quién lo hizo, cuándo
y desde dónde. Su mapa usa el token PTV de la compañía, que recibe al iniciar sesión.

Para leer los códigos de barras de los Bultos integra el **Scandit Barcode Scanner SDK** en
tres modos:

.. list-table::
   :header-rows: 1
   :widths: 18 22 60

   * - Modo
     - Tecnología
     - Para qué sirve
   * - **Lectura individual**
     - Barcode Capture
     - Leer una etiqueta, localizar ese Bulto en el sistema, ver su estado y actuar sobre él.
       Interpreta las etiquetas GS1 con identificadores de aplicación.
   * - **Comprobación de carga**
     - SparkScan (lectura continua)
     - Recorrer la lista de Bultos esperados de una Parada o de un Tramo escaneando en ráfaga.
       La app marca cada Bulto encontrado, lleva el contador sobre el total y responde con
       acierto o error. Se usa al comprobar la carga antes de salir y en la entrega con
       reservas.
   * - **Encontrar bultos**
     - Barcode Find (realidad aumentada)
     - Con la cámara sobre muchas etiquetas a la vez, la app resalta las que pertenecen a la
       Parada actual, para localizar mercancía en el vehículo sin leerlas una a una.

Cada lectura llega a Odoo con la fecha, el conductor y el contexto de la Parada: el Bulto cambia
de estado y el evento queda en la trazabilidad de la Parada. El servidor puede rechazar la
lectura por una regla de negocio (un Bulto que no corresponde a esa Parada, un estado que no
admite la acción) y la app se lo dice al conductor al instante. Si la misma lectura llega dos
veces, se procesa una sola.

1.4.6 Evolución prevista
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   Lo que sigue **no forma parte de la versión que describen las secciones anteriores**
   (septiembre de 2026). Cada punto lleva su estado; a medida que se despliegue, pasará a ellas.

Son los prerrequisitos de la **torre de control** que se está construyendo sobre el TMS:

- **Telemática** (hecho en el código, pendiente de despliegue). Un conector de proveedores de
  telemática que trae al Viaje y al vehículo la posición, el odómetro y otras señales, con la
  app del conductor como primer proveedor. La posición que aporta es la que usará el recálculo
  ligero del ETA descrito en
  :ref:`17.0/1_introduction/1_4_technological-architecture:1.4.2.1 El ETA durante la ejecución`.
- **Avisos al Destinatario** (hecho en el código, pendiente de despliegue). Un motor de avisos por
  WhatsApp, SMS y correo que informa al Destinatario del estado de su entrega y de su hora
  prevista, con enlace de seguimiento, consentimiento y lista de permitidos.
- **Optimizador** (en desarrollo). Migración a PTV OptiFlow en convivencia con el servicio
  actual, comparando resultados sobre planificaciones reales antes de cambiar. Aporta
  capacidades reales también en la secuenciación, pausas y jornada del conductor explícitas,
  categorías de carga y compatibilidades vehículo ↔ Orden, costes por vehículo (fijo, por hora,
  por kilómetro, por Parada), coste de subcontratación e ingreso de internalización por Orden,
  preferencias de compacidad y equilibrio entre Viajes, y un informe de Órdenes no planificadas
  con su motivo y de restricciones incumplidas. Cada optimización quedará guardada como registro
  consultable.
