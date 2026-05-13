Ejecución desde App
-----------------------

La aplicación móvil del conductor consume los viajes asignados a su partner y que se encuentran en estado operativo procesado.

El endpoint de la app recupera el último viaje disponible para el conductor y devuelve una estructura operativa completa.

Entre los datos incluidos se encuentran:

- paradas
- tramos
- líneas
- bultos
- reembolsos
- perfiles de aplicación
- motivos de incidencia
- geolocalización
- métricas de ruta

Durante la ejecución, el conductor avanza por las distintas paradas y genera trazabilidad sobre entidades concretas del sistema.

Los eventos enviados desde la aplicación se registran sobre:

- viaje
- parada
- tramo
- bulto
- reembolso

Cada evento queda registrado con información completa de auditoría:

- fecha y hora
- usuario
- geolocalización
- dispositivo
- motivo
- comentario
- adjuntos (cuando existan)



Eventos operativos principales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+--------------------------------------------------------------+
| Evento            | Descripción                                                  |
+===================+==============================================================+
| standby           | Estado inicial previo al desplazamiento.                     |
+-------------------+--------------------------------------------------------------+
| on_way            | El conductor está en camino hacia la operación.              |
+-------------------+--------------------------------------------------------------+
| running           | Operación en curso.                                          |
+-------------------+--------------------------------------------------------------+
| lo_ok             | Carga realizada correctamente.                               |
+-------------------+--------------------------------------------------------------+
| lo_ok_reserve     | Carga realizada con reservas.                                |
+-------------------+--------------------------------------------------------------+
| lo_failed         | Carga no realizada.                                          |
+-------------------+--------------------------------------------------------------+
| ok                | Entrega o recogida completada correctamente.                 |
+-------------------+--------------------------------------------------------------+
| ok_reserve        | Operación completada con reservas.                           |
+-------------------+--------------------------------------------------------------+
| failed            | Operación fallida.                                           |
+-------------------+--------------------------------------------------------------+

La lógica funcional de la app distingue el comportamiento según el tipo de parada.

Dependiendo del contexto operativo, una parada puede representar:

- recogida
- entrega
- operación hub
- home collection

Según el tipo de parada, el comportamiento cambia.

Ejemplos:

- En recogidas, puede reportarse carga de bultos
- En entregas, pueden capturarse POD, incidencias o reservas
- En operaciones hub, se actualiza entrada o salida de mercancía

Cuando una parada contiene múltiples tramos, el sistema propaga automáticamente la trazabilidad a todos los elementos vinculados.

Si el flujo operativo lo permite, también puede autoreportar bultos pendientes para mantener consistencia física y documental.

El detalle funcional completo de la aplicación móvil se desarrolla en el capítulo 6.

En este capítulo es importante remarcar que la app no funciona como un sistema aislado.

Sus eventos actualizan directamente:

- tramos
- paradas
- bultos
- reembolsos
- estado operativo de la orden
- estado agregado del viaje

Esto convierte la aplicación móvil en una extensión operativa directa del núcleo TMS.