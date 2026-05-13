Generación de Tramos
------------------------

Los Tramos representan los movimientos logísticos que componen una orden.

Una misma orden puede contener uno o varios tramos.

Cada tramo define:

- origen
- destino
- fechas
- ventanas horarias
- tipo de movimiento
- mercancía asociada
- posibles importes de reembolso

El tramo es la unidad que conecta la información comercial con la ejecución física.

A partir de sus datos, el sistema determina:

- dónde debe cargarse
- dónde debe descargarse
- qué bultos están implicados
- qué parada es la activa
- qué viaje ejecuta el movimiento

La creación de tramos puede ser:

- manual
- automática mediante importación

En creación manual, el botón de nuevo tramo hereda el contexto de la orden y aplica valores por defecto según el tipo de operativa.

Por ejemplo:

- una entrega completa datos de carga desde hub/agencia
- una recogida completa datos de descarga
- un directo requiere origen y destino explícitos
- una operación hub utiliza la configuración territorial del proyecto

**Campos funcionales del tramo**

+------------------------------+--------------------------------------------------------------+
| Campo                        | Descripción                                                  |
+==============================+==============================================================+
| Orden vinculada              | Expedición TMS propietaria del tramo.                        |
+------------------------------+--------------------------------------------------------------+
| Tipo de movimiento           | Entrega, recogida, directo, hub o home collection.           |
+------------------------------+--------------------------------------------------------------+
| Datos de carga               | Contacto, hub, agencia, fecha y ventana de origen.           |
+------------------------------+--------------------------------------------------------------+
| Datos de descarga            | Contacto, hub, agencia, fecha y ventana de destino.          |
+------------------------------+--------------------------------------------------------------+
| Líneas y bultos             | Mercancía transportada y unidades asociadas.                 |
+------------------------------+--------------------------------------------------------------+
| Paradas carga/descarga       | Paradas operativas vinculadas.                               |
+------------------------------+--------------------------------------------------------------+
| Viaje asociado               | Ruta operativa asignada.                                     |
+------------------------------+--------------------------------------------------------------+
| Estado operativo             | Situación logística actual del tramo.                        |
+------------------------------+--------------------------------------------------------------+

El estado operativo se calcula a partir de la trazabilidad del flujo y permite identificar situaciones como:

- pendiente
- cargado
- completado
- con reservas
- fallido
- reprogramado

Aunque técnicamente puede modificarse manualmente, no se recomienda hacerlo, ya que rompe la coherencia de trazabilidad.

En importaciones masivas, el sistema compara los movimientos recibidos con los ya existentes.

La comparación se realiza utilizando criterios como:

- orden
- tipo de movimiento
- direcciones
- contexto operativo

Si el tramo ya existe y permanece en estado editable:

- se actualiza

Si no existe:

- se crea

Una vez procesado, el sistema recalcula automáticamente:

- zonas operativas
- zonas tarifarias
- referencias territoriales

para dejar el tramo preparado para validación, planificación y tarificación.