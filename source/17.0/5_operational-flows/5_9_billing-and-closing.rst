Liquidación Económica
----------------------

La liquidación económica del TMS se divide en dos dimensiones diferenciadas:

- venta al cliente
- compra al transportista

Esta separación permite calcular margen económico a distintos niveles operativos:

- orden
- tramo
- parada
- viaje

También permite diferenciar claramente:

- la tarifa comercial cobrada al cliente
- el coste operativo pagado al proveedor



Liquidación de venta
~~~~~~~~~~~~~~~~~~~~~~~~~

En el lado de venta, la orden TMS calcula líneas económicas a partir de:

- tarifa de cliente
- reglas tarifarias
- zonas económicas
- tipo de servicio
- tipo de orden
- magnitudes logísticas
- nivel de aplicación configurado

Según la parametrización económica, la tarifa puede aplicarse sobre:

- expedición
- tramo
- parada
- viaje



Liquidación de compra
~~~~~~~~~~~~~~~~~~~~~~~~~

En el lado de compra, el viaje genera o actualiza una orden de compra vinculada al transportista.

Para ello, el sistema requiere:

- transportista
- tarifa de compra

o alternativamente:

- precio cerrado informado en el viaje

La orden de compra queda enlazada directamente con el viaje y recoge información como:

- descripción de ruta
- fecha
- distancia
- tiempos operativos
- conceptos económicos calculados



Elementos que intervienen en la liquidación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+--------------------------------------------------------------+
| Elemento                             | Descripción                                                  |
+======================================+==============================================================+
| Tarifa cliente                       | Precio comercial aplicado al cliente.                        |
+--------------------------------------+--------------------------------------------------------------+
| Tarifa transportista                 | Coste económico aplicado al proveedor.                       |
+--------------------------------------+--------------------------------------------------------------+
| Magnitudes logísticas                | Peso, volumen, bultos, pallets, metros, cantidad, tiempo.   |
+--------------------------------------+--------------------------------------------------------------+
| Zonas tarifarias                     | Territorios económicos origen/destino.                       |
+--------------------------------------+--------------------------------------------------------------+
| Reembolsos                           | Importes adicionales asociados a la operación.               |
+--------------------------------------+--------------------------------------------------------------+
| Diagnóstico de tarifa                | Registro de incidencias de cálculo económico.                |
+--------------------------------------+--------------------------------------------------------------+

Las magnitudes utilizadas en liquidación pueden incluir:

- peso
- volumen
- bultos
- pallets
- metros lineales
- cantidad
- distancia
- tiempo de ejecución

Las zonas tarifarias pueden resolverse mediante:

- origen y destino del tramo
- zonas de parada
- resolución geográfica sobre contactos
- rutas tarifarias específicas

Los reembolsos pueden incorporarse como conceptos adicionales dentro del flujo económico.

Cuando el cálculo detecta inconsistencias, el sistema registra diagnóstico de tarifa.

Ejemplos habituales:

- ausencia de regla tarifaria
- zona no resuelta
- ruta económica inexistente
- incompatibilidad de planning
- falta de magnitudes necesarias
- parametrización incompleta

Este diagnóstico permite al operador corregir la incidencia antes de avanzar hacia facturación.

.. warning::

   El sistema evita avanzar silenciosamente con cálculos económicos
   incompletos o incoherentes.

   Toda incidencia económica relevante debe quedar trazada para
   garantizar consistencia financiera y auditabilidad.