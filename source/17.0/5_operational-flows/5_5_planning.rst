Generación de Viajes
-------------------

El Viaje agrupa las paradas que serán ejecutadas por un conductor, vehículo o transportista en una fecha determinada.

Es la entidad que concentra:

- planificación de ruta
- asignación de recursos
- tiempos y distancias
- trazabilidad agregada
- liquidación económica de compra

Un viaje puede originarse por distintos mecanismos:

- nombre de viaje recibido en importación
- creación manual desde órdenes o paradas
- optimización automática con PTV
- generación automática por configuración de proyecto

En todos los casos, el viaje termina vinculando:

- paradas
- tramos
- bultos
- reembolsos asociados



Información principal del viaje
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------------------+--------------------------------------------------------------+
| Campo                                | Descripción                                                  |
+======================================+==============================================================+
| Fecha y horarios                     | Inicio y fin previstos de ejecución.                         |
+--------------------------------------+--------------------------------------------------------------+
| Planning y slot                      | Contexto operativo de planificación.                         |
+--------------------------------------+--------------------------------------------------------------+
| Agencia y hubs                       | Referencias territoriales del viaje.                         |
+--------------------------------------+--------------------------------------------------------------+
| Recursos asignados                   | Transportista, conductor, vehículo y remolques.             |
+--------------------------------------+--------------------------------------------------------------+
| Tarifa de compra                     | Base económica de liquidación.                               |
+--------------------------------------+--------------------------------------------------------------+
| Paradas y tramos                     | Operaciones incluidas en la ruta.                            |
+--------------------------------------+--------------------------------------------------------------+
| Métricas agregadas                   | Peso, volumen, pallets, distancia, tiempos, etc.            |
+--------------------------------------+--------------------------------------------------------------+
| Datos de optimización                | Polilínea, respuesta cartográfica y secuencias calculadas.   |
+--------------------------------------+--------------------------------------------------------------+



Generación Manual
~~~~~~~~~~~~~~~~~

La generación manual se utiliza cuando el operador decide explícitamente qué paradas deben formar parte de un viaje.

Es habitual en escenarios como:

- bajo volumen
- rutas fijas
- ajustes manuales
- correcciones operativas
- planificación dirigida por operador

Normalmente parte de una selección de:

- órdenes
- paradas pendientes

y abre un asistente de asignación.

El asistente permite dos modos:

- viaje nuevo
- viaje existente

En modo viaje nuevo pueden configurarse:

- proyecto
- fecha
- ventana horaria
- conductor
- vehículo
- categoría
- transportista
- tarifa de compra
- servicios
- planning
- tipo de transportista
- tipo de destinatario
- precio cerrado (cuando aplique)

En modo viaje existente:

- se selecciona una ruta abierta
- se incorporan nuevas paradas

Al completar la asignación:

- la parada se vincula mediante ``trip_id``
- los tramos quedan asociados al viaje
- los reembolsos quedan disponibles para liquidación

Si el proyecto tiene secuenciación automática activa:

- el sistema puede reordenar la ruta automáticamente



Generación Automática con PTV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La generación automática con PTV se ejecuta desde la acción de optimización.

El sistema envía al motor PTV:

- ubicaciones de clientes
- hubs
- transportes pendientes
- vehículos disponibles
- conductores (cuando aplique)
- ventanas horarias
- restricciones operativas
- capacidades
- reglas logísticas

La optimización puede trabajar en dos modos:

- por slots de planificación
- por categorías de vehículo

Modo por slot
^^^^^^^^^^^^^

En este escenario, el sistema utiliza recursos ya definidos:

- conductor
- vehículo
- transportista
- tarifa de compra
- disponibilidad temporal

Esto permite optimización sobre recursos reales ya planificados.

Modo por categoría
^^^^^^^^^^^^^^^^^

En este escenario, el sistema optimiza en base a capacidad disponible por categoría de vehículo.

Posteriormente, el operador puede asignar recursos concretos manualmente.



Requisitos previos
^^^^^^^^^^^^^^^^^^

+--------------------------------------+--------------------------------------------------------------+
| Requisito                            | Descripción                                                  |
+======================================+==============================================================+
| Token PTV                            | Configuración activa del servicio.                           |
+--------------------------------------+--------------------------------------------------------------+
| Geocodificación                      | Coordenadas válidas en ubicaciones.                          |
+--------------------------------------+--------------------------------------------------------------+
| Paradas pendientes                   | Operaciones disponibles para planificación.                  |
+--------------------------------------+--------------------------------------------------------------+
| Ventanas horarias coherentes         | Restricciones temporales consistentes.                       |
+--------------------------------------+--------------------------------------------------------------+
| Planning / slots / categorías        | Contexto operativo correctamente configurado.                |
+--------------------------------------+--------------------------------------------------------------+
| Capacidades y restricciones          | Equipamientos, carga y límites parametrizados.               |
+--------------------------------------+--------------------------------------------------------------+

Tras recibir la respuesta del optimizador:

- se crean viajes en borrador
- se asignan paradas
- se actualiza secuencia
- se calculan ETAs
- se calculan distancias
- se calculan tiempos de conducción
- se registran esperas
- se registran descansos
- se guarda la respuesta completa del motor

Posteriormente, el sistema solicita cálculo cartográfico adicional para obtener:

- polilínea
- visualización de mapa
- información de navegación
- soporte para aplicación móvil