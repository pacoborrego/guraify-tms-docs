Configuración de planificación
------------------------------

La configuración de planificación define cómo se agrupan, ordenan y ejecutan las operaciones.

Incluye los maestros que permiten transformar órdenes y paradas en viajes planificables: Planning, Planes de Transporte, Áreas Geográficas, Franjas Horarias, Tiempos de Servicio y Horas de Conducción.



Planning
~~~~~~~~

Planning es una de las entidades maestras más importantes del sistema, porque actúa como eje de segmentación operativa entre la expedición, las paradas, los viajes, la planificación de recursos, la optimización y la tarificación.

No representa un viaje concreto, sino una forma de organizar cómo deben planificarse y procesarse determinados servicios logísticos.

Un Planning permite clasificar operativamente expediciones que comparten una misma lógica de transporte: última milla, recogidas, distribución urbana, rutas con hub, rutas directas, servicios dedicados, reparto por zonas o cualquier otro flujo definido por la operación.

Esta clasificación se hereda normalmente desde el proyecto y se propaga a expediciones, tramos, paradas y viajes. Por este motivo, una selección incorrecta de Planning puede afectar a varios procesos posteriores.

**Campos principales**

+---------------------------------------------+--------------------------------------------------------------------------------+
| Campo                                       | Descripción                                                                    |
+=============================================+================================================================================+
| Nombre y Descripción                        | Identifican la planificación.                                                  |
+---------------------------------------------+--------------------------------------------------------------------------------+
| Plan de transporte                          | Red geográfica asociada al Planning.                                           |
+---------------------------------------------+--------------------------------------------------------------------------------+
| Tiempos de servicio de recogida y entrega   | Tiempos operativos aplicables a recogidas y entregas.                          |
+---------------------------------------------+--------------------------------------------------------------------------------+
| Modo de división de viaje                   | Criterio usado para repartir carga o importes.                                 |
+---------------------------------------------+--------------------------------------------------------------------------------+
| Shipper                                     | Cargador o entidad operativa asociada.                                         |
+---------------------------------------------+--------------------------------------------------------------------------------+
| Valor por defecto, compañía y color         | Campos estándar de clasificación, compañía y visualización.                    |
+---------------------------------------------+--------------------------------------------------------------------------------+

Uso dentro del sistema en Planning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Planning está vinculado a un Plan de Transporte. Esta relación es relevante porque el Plan de Transporte define el marco territorial sobre el que se opera: zonas, áreas de transporte y agencia asociada.

A partir de esta relación, el sistema puede filtrar áreas disponibles, asociar paradas a una lógica territorial concreta y mantener coherencia entre la planificación operativa y la estructura geográfica configurada.

Dentro del flujo de creación de expediciones, el Planning se asigna desde el proyecto y queda registrado en la expedición. Cuando se crean los tramos, el Planning se transfiere también a cada tramo.

Posteriormente, al generar paradas desde manifiestos o desde procesos operativos, el sistema utiliza el Planning como parte de la clave de agrupación. Esto significa que dos operaciones con la misma ubicación y franja horaria no se agrupan necesariamente si pertenecen a Planning diferentes.

Esta separación evita mezclar flujos operativos distintos en una misma parada o viaje.

En la creación de viajes, Planning también es obligatorio. El sistema lo utiliza para construir viajes coherentes, filtrar recursos disponibles y agrupar paradas que pertenecen al mismo flujo operativo.

En las pantallas de planificación de conductores, los slots se asocian a un Planning, de modo que al asignar paradas a recursos el sistema puede buscar únicamente slots compatibles para una fecha determinada.

Esto permite separar, por ejemplo, rutas de reparto, rutas de recogida, rutas de temperatura controlada o servicios especiales.

Planning también interviene en la optimización. Cuando se envía información al motor de optimización, se utilizan los tiempos de servicio definidos en el Planning: tiempo de servicio de recogida y tiempo de servicio de entrega.

Estos valores se añaden a los tiempos propios de las paradas y permiten calcular rutas más realistas. Si estos tiempos están mal configurados, el optimizador puede generar rutas aparentemente válidas pero inviables en operación.

Otro punto crítico es el campo Modo de división de viaje. Este parámetro define cómo se calcula el factor de reparto dentro de un viaje.

El sistema puede repartir importes o cargas según peso, volumen, bultos, pallets, metros, cantidad, distancia o combinaciones de distancia con esas magnitudes.

Por ejemplo, un Planning configurado con ``km_weight`` reparte considerando distancia por peso; uno configurado con ``packs`` reparte según número de bultos; uno configurado con ``km_pallets`` pondera pallets y distancia.

Este factor se utiliza en paradas y viajes para calcular bases de reparto, porcentajes y asignaciones económicas cuando hay importes de viaje que deben distribuirse entre operaciones.

La elección del Modo de división de viaje debe responder a la naturaleza real del servicio. En distribución ligera puede tener sentido repartir por bultos o por distancia y bultos. En paletería puede ser más adecuado usar pallets o kilómetros por pallet. En transporte voluminoso puede ser mejor usar metros, volumen o kilómetros por volumen.

Esta configuración tiene impacto económico, no solo operativo, porque condiciona cómo se imputan costes e ingresos sobre paradas y tramos.

Planning también se utiliza como condición de tarifa. Las reglas de tarifa pueden limitarse a uno o varios Planning, de forma que una misma tarifa puede aplicar importes diferentes según el flujo operativo.

Esto permite distinguir precios de reparto, recogida, directo, hub, urgente o cualquier otra planificación definida. Si una tarifa tiene configurado Planning y la expedición o el viaje no coincide, el motor de tarificación descartará esa regla.

En integraciones e importaciones, Planning puede recibirse como dato externo del viaje. Cuando el fichero o API informa el Planning del viaje, el sistema lo utiliza para crear o actualizar el viaje y mantener la trazabilidad entre la planificación externa y la interna.

Si el Planning no existe, algunos flujos de importación pueden crearlo automáticamente con una configuración básica, por lo que es recomendable mantener previamente los Planning maestros bien definidos.

.. important::

   Planning no debe entenderse como una simple etiqueta.
   Es una dimensión operativa que determina cómo se agrupan las operaciones,
   qué zonas se aplican, qué recursos pueden utilizarse, cómo se optimizan rutas,
   cómo se calculan tiempos de servicio, cómo se reparten costes e ingresos
   y qué reglas de tarifa son aplicables.



Planes de Transporte
~~~~~~~~~~~~~~~~~~~~~

Los Planes de Transporte definen la red geográfica operativa sobre la que trabaja un Planning.

Agrupan áreas de transporte, agencia responsable y representación cartográfica, y sirven como marco territorial para resolver zonas operativas durante la creación de tramos, paradas y viajes.

No son una ruta ni una tarifa. Su función es delimitar qué polígonos pertenecen a una red operativa concreta y qué agencia o hub debe quedar asociado cuando una dirección cae dentro de una de esas áreas.

**Campos principales**

+----------------------+--------------------------------------------------------------------------------+
| Campo                | Descripción                                                                    |
+======================+================================================================================+
| Nombre               | Identificador funcional del plan de transporte.                                |
+----------------------+--------------------------------------------------------------------------------+
| Agencia              | Partner marcado como agencia responsable del plan.                             |
+----------------------+--------------------------------------------------------------------------------+
| Áreas                | Conjunto de Áreas Geográficas que componen la red operativa.                   |
+----------------------+--------------------------------------------------------------------------------+
| Por defecto          | Marca el plan principal de la compañía.                                        |
+----------------------+--------------------------------------------------------------------------------+
| Compañía             | Empresa propietaria del plan.                                                  |
+----------------------+--------------------------------------------------------------------------------+
| Vista de mapa        | Previsualización embebida de agencia y polígonos asociados.                    |
+----------------------+--------------------------------------------------------------------------------+

Uso dentro del sistema en Planes de Transporte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Plan de Transporte se vincula al Planning. Esta relación permite que una planificación tenga un ámbito territorial concreto y que, al resolver una dirección, el sistema busque únicamente dentro de las áreas de esa red.

En tramos y paradas, la recalculación de zonas operativas toma el Planning, accede a su Plan de Transporte y compara las coordenadas del partner con los polígonos configurados.

Si encuentra coincidencia, informa la zona operativa y propaga hub y agencia desde el área.

Si el proyecto permite asignación por proximidad, puede seleccionar el área más cercana cuando la ubicación queda fuera de todos los polígonos.

También se utiliza en planificación de recursos: al cambiar el Planning de un slot, las áreas seleccionables quedan filtradas por el Plan de Transporte del Planning. De esta forma se evita asignar recursos de una red territorial a otra.

La vista de mapa y los endpoints internos devuelven nombre, coordenadas de agencia y geometría de las áreas, lo que facilita revisar visualmente si una red está correctamente parametrizada antes de usarla en operación.


Áreas Geográficas
~~~~~~~~~~~~~~~~~~

Las Áreas Geográficas son polígonos o multipolígonos GeoJSON que representan territorios del sistema.

Una misma entidad técnica se usa con distintos propósitos:

- Áreas operativas de transporte
- Zonas tarifarias
- Áreas extra de precio
- Elementos de operación
- Zonas de bajas emisiones

Su importancia es doble: permiten ubicar direcciones dentro de una red operativa y, al mismo tiempo, sirven como condición territorial para tarifas, reglas y diagnósticos económicos.

**Campos principales**

+-----------------------------+--------------------------------------------------------------------------------+
| Campo                       | Descripción                                                                    |
+=============================+================================================================================+
| Nombre y descripción        | Identifican el área en listas, reglas y resultados geográficos.                |
+-----------------------------+--------------------------------------------------------------------------------+
| Tipo                        | Clasifica el uso del área.                                                     |
+-----------------------------+--------------------------------------------------------------------------------+
| Polígono GeoJSON            | Geometría almacenada en el campo de polígono.                                  |
+-----------------------------+--------------------------------------------------------------------------------+
| Centro latitud/longitud     | Centro calculado a partir de la geometría.                                     |
+-----------------------------+--------------------------------------------------------------------------------+
| Agencia y hub               | Valores operativos que pueden propagarse a tramos o paradas.                   |
+-----------------------------+--------------------------------------------------------------------------------+
| Planes de Transporte        | Relación con los planes donde actúa como territorio operativo.                 |
+-----------------------------+--------------------------------------------------------------------------------+
| Zonas Tarifarias            | Relación con zonas donde actúa como territorio económico.                      |
+-----------------------------+--------------------------------------------------------------------------------+
| Días disponibles            | Calendario semanal admitido para áreas de transporte.                          |
+-----------------------------+--------------------------------------------------------------------------------+
| Franjas horarias            | Ventanas asociadas al área como referencia de disponibilidad territorial.       |
+-----------------------------+--------------------------------------------------------------------------------+
| Filtros include/exclude     | Dominios previstos para reglas avanzadas de inclusión o exclusión.             |
+-----------------------------+--------------------------------------------------------------------------------+

Uso dentro del sistema en Áreas Geográficas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En el flujo operativo, las áreas de tipo Plan de Transporte se usan para resolver zonas operativas de carga, descarga o parada.

Cuando una dirección cae dentro de un polígono, la operación queda etiquetada con esa zona y puede heredar hub y agencia.

El sistema evita recalcular zonas en estados cerrados, facturados o cancelados para reducir escrituras en cascada.

En procesos masivos puede usar cachés de geometría y resolución, lo que reduce coste cuando muchas paradas comparten áreas o coordenadas.

En el flujo económico, las áreas de tipo Zona Tarifaria delimitan qué tarifa aplica a una operación. Las áreas extra permiten suplementos geográficos mediante reglas de precio de tipo geo.

Los días disponibles del área se usan como control operativo. Si una carga o descarga se programa en un día no permitido por la zona operativa, el sistema puede avisar o bloquear para evitar planificaciones fuera de calendario.



Franjas Horarias
~~~~~~~~~~~~~~~~~

Las Franjas Horarias normalizan ventanas de servicio reutilizables.

Cada franja define una hora de inicio y fin en formato decimal de Odoo y genera un nombre legible de forma automática.

Se utilizan para informar ventanas de carga y descarga sin introducir manualmente las horas en cada operación.

**Campos principales**

+----------------------+--------------------------------------------------------------------------------+
| Campo                | Descripción                                                                    |
+======================+================================================================================+
| Nombre               | Campo calculado con formato ``HH:MM - HH:MM``.                                 |
+----------------------+--------------------------------------------------------------------------------+
| Inicio               | Hora inicial de la ventana.                                                    |
+----------------------+--------------------------------------------------------------------------------+
| Fin                  | Hora final de la ventana.                                                      |
+----------------------+--------------------------------------------------------------------------------+
| Tipos de servicio    | Servicios a los que puede asociarse la franja.                                 |
+----------------------+--------------------------------------------------------------------------------+
| Compañía             | Empresa propietaria de la franja.                                              |
+----------------------+--------------------------------------------------------------------------------+

Uso dentro del sistema
^^^^^^^^^^^^^^^^^^^^^^

En tramos y asistentes de creación, las franjas pueden asignarse a la carga o descarga.

Al seleccionarlas, el sistema copia inicio y fin a los campos horarios de la operación.

Si se activa una franja personalizada en una operación nueva, el sistema advierte que puede implicar coste adicional. Esto separa la ventana estándar de la excepción operativa.

Cuando el proyecto no recibe horarios informados, el sistema puede completar horarios desde el partner o desde los valores por defecto del proyecto.

La franja horaria permite ajustar esos horarios de forma controlada en carga o descarga.

La relación con áreas permite documentar qué ventanas son válidas para una zona territorial, aunque el dato que se aplica finalmente sobre el tramo es la franja seleccionada en carga o descarga.



Tiempos de Servicio
~~~~~~~~~~~~~~~~~~~

Los Tiempos de Servicio calculan la duración operativa que una parada requiere, más allá del tiempo de conducción.

El modelo permite parametrizar tiempos fijos o variables según dificultad, pisos, ascensor, peso y tipo de operación.

Esta configuración es crítica para que las rutas optimizadas tengan una duración realista y para que la ETA no dependa únicamente de kilómetros.

**Campos principales**

+-----------------------------+--------------------------------------------------------------------------------+
| Campo                       | Descripción                                                                    |
+=============================+================================================================================+
| Nombre                      | Identificador del esquema de tiempos de servicio.                              |
+-----------------------------+--------------------------------------------------------------------------------+
| Kg nivel 0                  | Valor por defecto utilizado para detalles de nivel cero.                       |
+-----------------------------+--------------------------------------------------------------------------------+
| Kg nivel superior           | Valor por defecto utilizado para niveles superiores.                           |
+-----------------------------+--------------------------------------------------------------------------------+
| Por defecto                 | Esquema usado como fallback.                                                   |
+-----------------------------+--------------------------------------------------------------------------------+
| Líneas                      | Conjunto de operaciones que forman el cálculo del tiempo.                      |
+-----------------------------+--------------------------------------------------------------------------------+
| Operación                   | Plantilla que determina tipo de cálculo, aplicación y factor.                  |
+-----------------------------+--------------------------------------------------------------------------------+
| Tipo de operación           | Dificultad, niveles o fijo.                                                     |
+-----------------------------+--------------------------------------------------------------------------------+
| Aplicar en                  | Indica si la operación pertenece al tramo o a la parada.                       |
+-----------------------------+--------------------------------------------------------------------------------+
| Tipo de factor              | Define si el tiempo se calcula por operación o por kilos.                      |
+-----------------------------+--------------------------------------------------------------------------------+
| Detalles                    | Matriz de dificultad, niveles, factor y segundos.                              |
+-----------------------------+--------------------------------------------------------------------------------+

Uso dentro del sistema en Tiempos de Servicio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El proyecto referencia un Tiempo de Servicio. Al calcular una parada, el sistema toma ese esquema y evalúa las líneas contra las características de la ubicación: dificultad de aparcamiento, existencia de ascensor, pisos y peso de la parada.

Para operaciones de dificultad, se selecciona el detalle correspondiente a la dificultad del partner. Para niveles, se diferencia si hay ascensor y cuántos pisos deben subirse. Para operaciones fijas, se suma el tiempo configurado sin depender de la carga.

El resultado se guarda en segundos y horas sobre la parada. Este dato alimenta la optimización PTV y los cálculos posteriores de tiempos de ruta, ETA y duración total.

El onchange de operación reconstruye los detalles con comandos One2many en memoria, evitando crear registros intermedios mientras la línea no está guardada. Esto reduce errores en el cliente web y mantiene estable la edición de matrices.



Horas de Conducción
~~~~~~~~~~~~~~~~~~~~

Horas de Conducción almacena los presets de jornada y regulación que se envían a los motores PTV.

No calcula por sí mismo la ruta, sino que define qué restricción de tiempo de conducción debe aplicar el optimizador, el secuenciador o el routing.

El dato puede venir de la categoría de vehículo o de la plantilla del slot de planificación, según el flujo utilizado.

**Campos principales**

+-----------------------------+--------------------------------------------------------------------------------+
| Campo                       | Descripción                                                                    |
+=============================+================================================================================+
| Nombre y descripción        | Identifican el preset de horas de conducción.                                  |
+-----------------------------+--------------------------------------------------------------------------------+
| Preset de secuenciación     | Valor enviado a PTV en procesos de secuenciación.                              |
+-----------------------------+--------------------------------------------------------------------------------+
| Preset de optimización      | Valor enviado a PTV Route Optimization.                                        |
+-----------------------------+--------------------------------------------------------------------------------+
| Por defecto                 | Marca de referencia funcional.                                                 |
+-----------------------------+--------------------------------------------------------------------------------+
| Información                 | Texto descriptivo para explicar cuándo debe utilizarse.                        |
+-----------------------------+--------------------------------------------------------------------------------+
| Secuencia, compañía y color | Campos de ordenación, multi-compañía y clasificación visual.                   |
+-----------------------------+--------------------------------------------------------------------------------+

Uso dentro del sistema en Horas de Conducción
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La categoría de vehículo puede tener asignado un preset de Horas de Conducción. Cuando se optimiza una ruta sin slot concreto, el sistema puede tomar el preset desde el vehículo o su categoría.

Cuando la optimización se ejecuta sobre slots de Planning, la plantilla del slot también puede aportar el preset. En ese caso, el optimizador recibe disponibilidad del slot y regulación asociada al conductor o recurso planificado.

En la llamada a PTV se envía el valor técnico del preset como ``workingHoursPreset``.

Esto permite aplicar restricciones estándar como regulaciones europeas o americanas sin reimplementar esa lógica dentro de Odoo.

.. important::

   Las Horas de Conducción deben mantenerse alineadas con la política operativa real del transportista.
   Una configuración incorrecta puede producir rutas aparentemente válidas,
   pero imposibles de ejecutar dentro de la jornada permitida.