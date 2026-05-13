Validación de Orden
-------------------

La validación de la orden es el proceso que transforma una expedición introducida en una estructura operativa lista para planificación.

Se ejecuta desde el botón de validación de la orden y concentra las comprobaciones mínimas antes de generar paradas y tarifas.

Antes de crear la estructura operativa, el sistema verifica que:

- la orden esté marcada como TMS
- existan tramos asociados
- existan líneas de mercancía cuando el flujo lo requiera
- los tramos tengan origen y destino informados
- existan fechas operativas válidas
- existan ventanas horarias obligatorias

También bloquea la validación cuando existen contactos pendientes de normalización.

Esto es crítico porque una dirección incompleta, inconsistente o duplicada afecta directamente a:

- geocodificación
- resolución territorial
- planificación
- optimización
- ejecución móvil

Una vez superadas las validaciones, el sistema completa automáticamente información derivada del proyecto.

Ejemplos habituales:

- En entregas, completa la carga desde hub o punto de recogida
- En recogidas, completa la descarga hacia hub
- En flujos mixtos, ajusta datos operativos según tipo de movimiento

Posteriormente:

- agrupa tramos
- crea o reutiliza paradas
- actualiza relaciones entre orden, tramo, parada y viaje
- recalcula información económica cuando el contexto lo permite



**Efectos de la validación**

+--------------------------------------+--------------------------------------------------------------+
| Acción                               | Resultado                                                    |
+======================================+==============================================================+
| Generación de paradas                | Crea estructura operativa ejecutable.                        |
+--------------------------------------+--------------------------------------------------------------+
| Actualización de estados             | Recalcula situación logística de orden y tramos.             |
+--------------------------------------+--------------------------------------------------------------+
| Recalculo económico                  | Actualiza tarifa de venta y viaje cuando aplica.             |
+--------------------------------------+--------------------------------------------------------------+
| Sincronización de hub                | Ajusta operaciones hub en viajes afectados.                  |
+--------------------------------------+--------------------------------------------------------------+
| Integración con inventario           | Genera movimientos stock si el proyecto lo requiere.         |
+--------------------------------------+--------------------------------------------------------------+
| Log de validación                    | Devuelve avisos, incidencias o errores detectados.           |
+--------------------------------------+--------------------------------------------------------------+

.. note::

   Validar una orden no equivale necesariamente a cerrarla administrativamente.

   La validación prepara la operación para ejecución logística.

   La confirmación administrativa o cierre económico dependen del estado
   operativo posterior y del flujo de facturación definido.