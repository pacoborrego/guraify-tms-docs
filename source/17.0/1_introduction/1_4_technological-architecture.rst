1.4 Arquitectura tecnológica
----------------------------

Guraify TMS está construido sobre una arquitectura modular que separa la capa de datos, la
lógica de negocio y la presentación, siguiendo las prácticas del framework Odoo. No es una
aplicación monolítica, sino un conjunto de bloques que se hablan de forma controlada: la
plataforma ERP, el módulo TMS, los servicios cartográficos de PTV, la capa de integración con
sistemas externos y la aplicación móvil del conductor. Cada bloque puede evolucionar sin
comprometer el núcleo funcional.

Esta sección describe cada bloque **tal y como está implementado**. Lo que está en desarrollo se
recoge aparte, al final, en :ref:`17.0/1_introduction/1_4_technological-architecture:1.4.6 Evolución prevista`.

.. mermaid::

   flowchart TB
       ODOO[Plataforma ERP Odoo 17] --> TMS[Módulo Guraify TMS<br/>tms_suite]
       TMS --> PTV[Servicios PTV<br/>geocodificación · mapa · routing<br/>secuenciación · optimización]
       PTV -.respaldo.-> OSM[Google · OpenStreetMap]
       TMS --> INT[Capa de integración<br/>ficheros · API REST · webhooks]
       TMS --> APP[App móvil del conductor<br/>POD · escaneo Scandit · trazabilidad]
       INT <--> EXT[Sistemas externos]

1.4.1 Plataforma base Odoo
~~~~~~~~~~~~~~~~~~~~~~~~~~

El núcleo es Odoo 17, que aporta el ORM, la seguridad por roles, las vistas, las
automatizaciones y la integración nativa con la contabilidad y la analítica. El TMS se
implementa como una extensión sobre esa base y reutiliza lo que ya existe: contabilidad y
facturación, contactos, empleados y Planificación (Planning), flota, proyectos, documentos
adjuntos y acciones automáticas y programadas. Así el TMS no es un sistema aislado, sino una
especialización logística dentro de un ERP horizontal: la factura del transporte es una
factura de Odoo y el transportista es un proveedor de Odoo.

1.4.2 Servicios de PTV
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   Ajustes › Integraciones › Rutas del mapa (PTV) › Token

PTV Developer es el proveedor cartográfico y matemático del sistema: geocodifica direcciones,
sirve el mapa base, calcula rutas, ordena paradas y propone viajes completos. Todos los
servicios se autentican con **un token por compañía**, de modo que cada compañía paga sus
propias llamadas aunque el usuario que las lance trabaje en varias.

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
   * - **Routing**
     - Al crear Viajes desde un Manifiesto que trae la secuencia; al reordenar, añadir o quitar
       paradas en el mapa del Optimizador; con los botones del Viaje.
     - Cada parada con su coordenada, tiempo de servicio y ventana horaria; el perfil de
       vehículo de la categoría; el preset de horas de conducción; la hora de salida; tráfico
       realista.
     - En el Viaje: trazado, distancia, duración y hora prevista de fin. En cada Parada: ETA,
       llegada, salida, kilómetros y tiempo de conducción acumulados.
   * - **Secuenciación**
     - Desde el Optimizador de Paradas sobre un Viaje ya formado; al cerrar un Manifiesto sin
       secuencia si el Proyecto tiene autosecuenciación.
     - Las paradas como transportes con cantidades, tiempo de servicio y prioridad; horarios
       de apertura de hubs y clientes; perfil, inicio, fin y distancia máxima del vehículo;
       disponibilidad del conductor.
     - El nuevo orden de las Paradas y sus horas de llegada y salida. Después se relanza el
       routing para refrescar el trazado.
   * - **Optimización completa**
     - Desde el Optimizador de Paradas sobre las Paradas pendientes de una fecha.
     - Vehículos con capacidades, equipamiento, inicio, fin y distancia máxima; conductores con
       disponibilidad y jornada; transportes con cantidades, tiempos de servicio y prioridad;
       hubs con horarios.
     - Viajes nuevos con sus Paradas asignadas y secuenciadas, vehículo y conductor, horas por
       parada, y la lista de lo que no se ha podido planificar.

El **routing** es el nivel básico: el Viaje ya existe, con sus paradas y su recurso, y PTV lo
enriquece con la red viaria profesional. El preset de horas de conducción sale del
:term:`Plan de disponibilidad de conductores` (por defecto, el reglamento europeo 561/2006). El
ETA que devuelve es el que ven el planificador, el conductor en la app y, por las
integraciones, el cliente. El cálculo cubre siempre el Viaje completo desde su hora de salida;
si la llamada falla, el Viaje queda sin datos de ruta y se puede relanzar.

La **secuenciación** actúa cuando las paradas ya están en un Viaje pero su orden no es el
mejor. Las cantidades de cada parada se envían en seis dimensiones (peso, volumen, bultos,
palés, unidades y metros lineales) y los horarios de hubs y clientes salen de las franjas por
día de cada contacto. El TMS aplica el orden devuelto conservando la vinculación de cada Parada
con su Tramo y su Orden. Si alguna parada no cabe en las restricciones, reintenta hasta dos
veces relajando las ventanas horarias y, si sigue fuera, avisa al planificador con la lista.

La **optimización completa** no ordena paradas dentro de un Viaje: propone qué Viajes crear y
cómo llenarlos. Se lanza desde el :term:`Optimizador de Paradas` en uno de dos modos. **Por
turnos del Planning**, cada turno aporta un vehículo y un conductor concretos, con su
disponibilidad y su preset de jornada, y el resultado los deja asignados a cada Viaje. **Por
categorías de vehículo**, el planificador indica cuántos vehículos de cada categoría tiene, sin
decir cuáles, y el recurso se asigna después. Las paradas se envían como entregas desde el
hub, recogidas hacia el hub o servicios directos, con capacidades reales en las mismas seis
dimensiones, y la optimización se pide con calidad alta y respetando las prioridades. Si
ningún vehículo puede cubrir las paradas, el sistema lo dice con las causas posibles
(capacidad, jornada, distancia máxima o número de paradas) en lugar de crear viajes vacíos.
El planificador revisa la propuesta, la ajusta a mano si hace falta y la confirma.

.. tip::

   Routing enriquece Viajes existentes. Secuenciación ordena las Paradas de un Viaje.
   Optimización completa propone qué Viajes crear y cómo llenarlos. Toda la parametrización
   sale de los maestros del TMS: categorías de vehículo, planes de disponibilidad, horarios de
   los contactos y tiempos de servicio.

1.4.3 Geolocalización, mapa y áreas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La geolocalización es un fundamento estructural, no un accesorio: de ella dependen la
asignación a planes de transporte, la tarificación por zonas, el cálculo de rutas y la
planificación. Tres geometrías bastan para todo. La **coordenada** (latitud y longitud)
representa una localización; el **polígono**, guardado en GeoJSON, representa un área; la
**polilínea** representa el trazado de una ruta calculada por el routing.

Geocodificación de direcciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cada dirección se convierte en coordenada mediante una cascada de cuatro proveedores, por
orden de preferencia: PTV con la dirección completa; Google Maps, si la compañía tiene
configurada su clave; PTV de nuevo, sólo con país, provincia y código postal; y OpenStreetMap
(Nominatim) como respaldo gratuito. Cada resultado trae una **puntuación de calidad** y un tipo
de precisión, que se guardan en la localización. Una coordenada con puntuación inferior a 80,
o que sólo llega a precisión de código postal, queda **pendiente de normalizar**: sitúa el punto
en el mapa, pero no vale para planificar.

.. important::

   Una coordenada con puntuación inferior a 80 no se considera válida para la planificación.
   La Orden calcula la lista de sus direcciones pendientes de normalizar y el Manifiesto no se
   cierra mientras las haya. La normalización se hace a mano sobre la ficha de la localización,
   con un buscador de direcciones sobre el mapa. No es una excepción operativa sino un control
   de calidad estructural: evita paradas mal situadas, desvíos y ETAs falsos.

La cascada funciona también al revés: cuando una localización llega con coordenada pero sin
código postal, localidad o país, el sistema completa la dirección a partir del punto.

Mapa base
^^^^^^^^^

El mapa del backend (la vista mapa, el Optimizador de Paradas y el editor de áreas) y el mapa
de la app del conductor se dibujan con MapLibre GL sobre las **teselas vectoriales de PTV**,
autenticadas con el token de la compañía. Sin token, o si PTV no responde, el mapa arranca
sobre OpenStreetMap y lo avisa: la operación no se detiene por una caída del proveedor.

Áreas geográficas
^^^^^^^^^^^^^^^^^

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Zonas Geográficas

Cualquier superficie con significado operativo es un :term:`Área geográfica` (``tms.area``): un
polígono GeoJSON con un tipo que dice para qué sirve. Hay cinco: área de un
:term:`Plan de transporte`, :term:`Zona de tarifa`, extra de tarifa, elemento de operación y
zona de bajas emisiones. Un área puede llevar los días y franjas horarias en que está activa.

Las áreas se **dibujan** sobre el mapa desde la ficha del área, de la zona de tarifa o del plan
de transporte, o se **importan de OpenStreetMap** con un asistente que busca límites
administrativos (municipios, comarcas, provincias) y los trae como polígonos, de uno en uno o
en bloque. Varias áreas se pueden fusionar en una.

La pregunta que responde el sistema es siempre la misma: ¿esta coordenada cae dentro de este
polígono? Con ella asigna cada Tramo a su zona operativa y a sus zonas de tarifa de cliente y
de transportista, en origen y en destino. Si la coordenada no cae en ningún área, el Tramo
queda sin zona; el Proyecto puede pedir que en ese caso se asigne **el área más cercana**, con
una opción para la zona operativa y otra para la de tarifa.

.. important::

   La asignación a áreas no se basa en texto ni en códigos postales, sino en geometría sobre
   coordenadas verificadas. Si se corrige la coordenada de una dirección, su zona cambia sola.

1.4.4 Capa de integración
~~~~~~~~~~~~~~~~~~~~~~~~~

El sistema intercambia información con el exterior por cuatro canales: ficheros CSV o Excel
con una definición de fichero por cliente, una API REST con su Bandeja de entrada API,
webhooks entrantes protegidos con clave, y envíos salientes de estados y pruebas de entrega
hacia el sistema de cada cliente. Delante de la API hay una pasarela con documentación
interactiva, autenticación y registro de cada llamada.

Las integraciones no crean estructuras paralelas: alimentan directamente la Orden, el Tramo, la
Parada y el Viaje, de modo que lo importado y lo ejecutado son la misma cosa. La
:doc:`Guía del integrador </17.0/7_edi-integrations/index>` explica cada canal.

1.4.5 La app del conductor y el escaneo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La aplicación móvil es una extensión operativa del backend, no una interfaz de confirmación.
Es una app híbrida (Ionic y Capacitor) para iOS y Android que habla con Odoo por una API
propia: recibe el Viaje, guía al conductor parada a parada, registra estados, incidencias,
firmas, fotos y cobros, y devuelve cada evento al TMS con quién lo hizo, cuándo y desde dónde.
Su mapa usa el token PTV de la compañía, que recibe al iniciar sesión.

Para leer los códigos de barras de los bultos integra el **Scandit Barcode Scanner SDK** en
tres modos:

.. list-table::
   :header-rows: 1
   :widths: 18 22 60

   * - Modo
     - Tecnología
     - Para qué sirve
   * - **Lectura individual**
     - Barcode Capture
     - Leer una etiqueta, localizar ese bulto en el sistema, ver su estado y actuar sobre él.
       Interpreta las etiquetas GS1 con identificadores de aplicación.
   * - **Comprobación de carga**
     - SparkScan (lectura continua)
     - Recorrer la lista de bultos esperados de una parada o de un tramo escaneando en ráfaga.
       La app marca cada bulto encontrado, lleva el contador sobre el total y responde con
       acierto o error. Se usa al comprobar la carga antes de salir y en la entrega con
       reservas.
   * - **Encontrar bultos**
     - Barcode Find (realidad aumentada)
     - Con la cámara sobre muchas etiquetas a la vez, la app resalta las que pertenecen a la
       parada actual, para localizar mercancía en el vehículo sin leerlas una a una.

Cada lectura llega a Odoo con la fecha, el conductor y el contexto de la parada: el Bulto cambia
de estado y el evento queda en la trazabilidad de la Parada. El servidor puede rechazar la
lectura por una regla de negocio (un bulto que no corresponde a esa parada, un estado que no
admite la acción) y la app se lo dice al conductor al instante. Si la misma lectura llega dos
veces, se procesa una sola.

1.4.6 Evolución prevista
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   Lo que sigue **está en desarrollo** en el momento de escribir este manual (septiembre de
   2026) y no forma parte de la versión que describen las secciones anteriores. A medida que se
   entregue, pasará a ellas.

Son los prerrequisitos de la **torre de control** que se está construyendo sobre el TMS, y
afectan sobre todo a los servicios de PTV:

- **Routing enriquecido.** Peajes por país y moneda, emisiones de CO₂ y consumo según los
  esquemas EN 16258 e ISO 14083, calculados con los parámetros del modelo de vehículo, y
  reparto de las emisiones del Viaje a cada Orden.
- **ETA incremental.** Recalcular sólo las paradas pendientes a partir de la posición real del
  conductor o de la última parada completada, según una política por compañía y por Proyecto.
  El ETA prometido en la planificación se conserva junto al vigente, con historial, y un fallo
  de PTV deja el valor anterior en lugar de borrarlo.
- **Telemática.** Un conector de proveedores de telemática que traiga al Viaje y al vehículo la
  posición, el odómetro y otras señales, con la app del conductor como un proveedor más.
- **Optimizador.** Migración a PTV OptiFlow en convivencia con el servicio actual, comparando
  resultados sobre planificaciones reales antes de cambiar. Aporta capacidades reales también
  en la secuenciación, pausas y jornada del conductor explícitas, categorías de carga y
  compatibilidades vehículo ↔ pedido, costes por vehículo (fijo, por hora, por kilómetro, por
  parada), coste de subcontratación e ingreso de internalización por pedido, preferencias de
  compacidad y equilibrio entre rutas, y un informe de pedidos no planificados con su motivo y
  de restricciones incumplidas. Cada optimización quedará guardada como registro consultable.
