Generación automática de Paradas
--------------------------------

Las Paradas se generan a partir de los tramos.

Mientras el tramo describe el movimiento entre origen y destino, la parada representa el punto operativo que debe aparecer en:

- planificación
- mapa
- viaje
- aplicación móvil del conductor

Al validar una orden, el sistema agrupa los tramos según criterios operativos compatibles.

Entre ellos:

- ubicación
- fecha
- ventana horaria
- planning
- nombre de viaje importado (cuando exista)

El objetivo es evitar paradas duplicadas y permitir que varios tramos compatibles compartan una misma parada operativa.

La generación automática distingue el papel funcional de cada punto mediante los Tipos de Parada configurados en el sistema.

De forma simplificada, el sistema puede generar:

- paradas de recogida a domicilio
- paradas de ruta
- recogidas directas
- entregas directas
- operaciones de hub

El tipo asignado condiciona posteriormente:

- si la parada es planificable
- si aparece en la app móvil
- si participa en optimización
- si actúa como punto intermedio de transferencia



**Reglas principales de generación**

+----------------------------------+--------------------------------------------------------------+
| Escenario                        | Comportamiento                                               |
+==================================+==============================================================+
| Entregas                         | Completa origen desde proyecto y genera entrega destino.     |
+----------------------------------+--------------------------------------------------------------+
| Recogidas                        | Genera carga y completa descarga hacia hub.                  |
+----------------------------------+--------------------------------------------------------------+
| Directos                         | Crea recogida directa y entrega directa diferenciadas.       |
+----------------------------------+--------------------------------------------------------------+
| Operaciones hub                  | Clasifica la parada como operación interna.                  |
+----------------------------------+--------------------------------------------------------------+
| Parada existente compatible      | Reutiliza la parada existente y vincula nuevos tramos.       |
+----------------------------------+--------------------------------------------------------------+
| Viaje importado informado        | Reutiliza o crea viaje automáticamente.                      |
+----------------------------------+--------------------------------------------------------------+

Si el tramo trae un nombre de viaje, el sistema puede:

- crear automáticamente el viaje
- reutilizar un viaje existente
- vincular paradas
- vincular tramos
- vincular reembolsos asociados

El resultado de esta fase es que cada tramo queda enlazado con su parada de carga y/o descarga.

A partir de este punto, la operación ya puede:

- planificarse
- optimizarse
- enviarse a agencia
- ejecutarse desde la app móvil

según el flujo operativo configurado.