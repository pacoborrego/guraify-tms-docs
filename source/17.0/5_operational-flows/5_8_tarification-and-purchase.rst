Cierre de Viaje
---------------

El cierre del viaje se calcula a partir del estado operativo de sus paradas.

Cuando todas las paradas válidas alcanzan un estado final de ejecución, el viaje pasa a estado completado y se ejecutan las acciones económicas necesarias para preparar la liquidación del transportista.



Estados considerados de cierre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


+------------------------------+--------------------------------------------------------------+
| Estado                       | Descripción                                                  |
+==============================+==============================================================+
| Completado                   | Operación ejecutada correctamente.                           |
+------------------------------+--------------------------------------------------------------+
| Reservas                     | Operación completada con incidencias o reservas.             |
+------------------------------+--------------------------------------------------------------+
| Fallido                      | Operación no ejecutada.                                      |
+------------------------------+--------------------------------------------------------------+
| Reprogramado                 | Operación cerrada con nueva ejecución prevista.              |
+------------------------------+--------------------------------------------------------------+
| Devuelto                     | Operación finalizada con devolución asociada.                |
+------------------------------+--------------------------------------------------------------+
| Cancelado                    | Operación cerrada sin ejecución.                             |
+------------------------------+--------------------------------------------------------------+

Cuando el viaje se cierra, el sistema ejecuta automáticamente varios procesos de consistencia económica y administrativa.

Entre ellos:

- recalcular la tarifa de compra, cuando aplica
- bloquear administrativamente el viaje
- actualizar liquidación pendiente del transportista

Si existe una orden de compra vinculada al viaje, el sistema además:

- valida sus líneas económicas
- actualiza cantidades recibidas
- actualiza cantidades pendientes de facturación
- confirma la orden de compra si aún no estaba confirmada

Este comportamiento garantiza coherencia entre:

- ejecución operativa
- liquidación económica
- documentación administrativa

Una vez facturada la compra, el viaje no debería desbloquearse.

Esta restricción evita modificaciones posteriores sobre:

- costes
- estados operativos
- recursos asignados
- datos de liquidación

.. note::

   Una ruta puede considerarse operativamente cerrada aunque una o varias
   paradas hayan terminado en fallo o con reservas.

   El cierre operativo indica que ya no quedan acciones pendientes
   de ejecución.

   No implica necesariamente que todas las operaciones hayan sido exitosas.