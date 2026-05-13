Configuración de proyectos
--------------------------


El Proyecto es la unidad central de parametrización TMS.

Une cliente, tarifa, Planning, red territorial, tipos operativos, reglas de entrada, automatismos, stock e integración.

La mayoría de valores que llegan a una orden, tramo, parada o viaje se heredan directa o indirectamente del proyecto.

Por ello, una configuración incompleta del proyecto suele manifestarse posteriormente como incidencias de importación, planificación, aplicación móvil o tarificación.

El proyecto puede definirse tanto para clientes como para transportistas.

Un mismo cliente puede tener varios proyectos cuando existen operativas distintas con configuraciones diferentes.

De igual forma, un mismo transportista puede participar en varias operativas con parámetros específicos.

El proyecto es especialmente útil porque permite precargar configuración durante la creación de:

- Órdenes
- Viajes
- Importaciones
- Integraciones API



Administración
~~~~~~~~~~~~~~~~

El bloque Administración define el alcance económico y estructural del proyecto.

**Campos principales**

+-----------------------------------+-------------------------------------------------------------+
| Campo                             | Descripción                                                 |
+===================================+=============================================================+
| Aplicar en                        | Define si el proyecto opera sobre órdenes o viajes.         |
+-----------------------------------+-------------------------------------------------------------+
| Tarifa                            | Tarifa principal del proyecto.                              |
+-----------------------------------+-------------------------------------------------------------+
| Modo de división                  | Criterio de reparto económico u operativo.                  |
+-----------------------------------+-------------------------------------------------------------+
| Cuenta analítica                  | Cuenta Odoo para seguimiento financiero.                    |
+-----------------------------------+-------------------------------------------------------------+
| Política fecha administrativa     | Regla de selección temporal para tarificación.              |
+-----------------------------------+-------------------------------------------------------------+

Uso dentro del sistema en Administración del Proyecto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La tarifa seleccionada alimenta la configuración económica disponible del proyecto.

El onchange recopila automáticamente:

- Tipos de expedición
- Servicios
- Transportistas
- Destinatarios
- Vehículos

detectados en las reglas tarifarias.

La política de fecha administrativa determina qué versión tarifaria debe utilizarse cuando una operación cruza cambios de vigencia.

Puede basarse en:

- Fecha de creación
- Fecha de carga
- Fecha de descarga
- Fecha de cierre operativo

El modo de división condiciona cómo se reparten importes o magnitudes cuando la operación se distribuye entre tramos o viajes.



Entrada Hub / Recogida
~~~~~~~~~~~~~~~~~~~~~~~~~

Define cómo entra la mercancía en la red logística.

**Campos principales**

+-----------------------------------+-------------------------------------------------------------+
| Campo                             | Descripción                                                 |
+===================================+=============================================================+
| Agencia                           | Centro operativo responsable.                               |
+-----------------------------------+-------------------------------------------------------------+
| Hub                               | Ubicación principal de consolidación.                       |
+-----------------------------------+-------------------------------------------------------------+
| Lugar de recogida                 | Punto permitido de recogida.                                |
+-----------------------------------+-------------------------------------------------------------+
| Horario de recogida               | Ventana operativa por defecto.                              |
+-----------------------------------+-------------------------------------------------------------+
| Servicio home collection          | Servicio específico para recogidas domiciliarias.           |
+-----------------------------------+-------------------------------------------------------------+

Uso dentro del sistema en Entrada Hub / Recogida
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Estos campos se utilizan durante:

- Importaciones
- Creación manual
- Manifiestos
- Home collection

Si el proyecto tiene un lugar de recogida definido, se propone automáticamente como origen.

Si no existe, el sistema puede apoyarse en el hub.

Los horarios se copian como defaults cuando no existe un dato más específico.

El servicio de home collection permite distinguir económicamente la recogida inicial respecto del resto de la operativa.


Activación
~~~~~~~~~~~

Activación define qué catálogos están disponibles dentro del proyecto.

No crea operaciones por sí misma.

**Campos principales**

+-----------------------------------+-------------------------------------------------------------+
| Campo                             | Descripción                                                 |
+===================================+=============================================================+
| Tipos de expedición               | Modalidades permitidas.                                     |
+-----------------------------------+-------------------------------------------------------------+
| Tipos de servicio                 | Servicios operativos habilitados.                           |
+-----------------------------------+-------------------------------------------------------------+
| Tipos de transportista            | Categorías de carrier disponibles.                          |
+-----------------------------------+-------------------------------------------------------------+
| Tipos de destinatario             | Segmentos operativos permitidos.                            |
+-----------------------------------+-------------------------------------------------------------+
| Categorías de vehículo            | Recursos compatibles.                                       |
+-----------------------------------+-------------------------------------------------------------+

Uso dentro del sistema en Activación del Proyecto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando una tarifa contiene reglas parametrizadas, el proyecto puede precargar automáticamente estos catálogos.

Esto reduce errores y evita activar opciones sin cobertura económica.

Si un catálogo tiene un único valor activo:

- se asigna automáticamente

Si existen varios:

- el valor queda vacío para selección posterior

Estos catálogos actúan como:

- dominios
- defaults
- validaciones
- criterios de compatibilidad



Asignación
~~~~~~~~~~~~

Asignación contiene los valores por defecto necesarios para transformar una orden en estructura logística ejecutable.

**Campos principales**

+-----------------------------------+-------------------------------------------------------------+
| Campo                             | Descripción                                                 |
+===================================+=============================================================+
| Planning                          | Segmentación operativa principal.                           |
+-----------------------------------+-------------------------------------------------------------+
| Plan de Transporte                | Red territorial asociada.                                   |
+-----------------------------------+-------------------------------------------------------------+
| Tiempo de Servicio                | Esquema de cálculo de duración.                             |
+-----------------------------------+-------------------------------------------------------------+
| Producto                          | Producto TMS por defecto.                                   |
+-----------------------------------+-------------------------------------------------------------+
| Equipamientos vehículo            | Requisitos físicos o técnicos.                              |
+-----------------------------------+-------------------------------------------------------------+
| Categorías de carga               | Naturaleza logística permitida.                             |
+-----------------------------------+-------------------------------------------------------------+

Uso dentro del sistema en Asignación del Proyecto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Planning se copia automáticamente a:

- expediciones
- tramos
- viajes

cuando no existe otro valor informado.

El Plan de Transporte permite resolver:

- áreas operativas
- zonas
- hubs
- agencias

El Tiempo de Servicio calcula duración esperada de paradas.

Equipamientos y categorías de carga restringen recursos compatibles.

Todo ello constituye la base operativa del motor de asignación y optimización.



Configuración App
~~~~~~~~~~~~~~~~~~

La Configuración App define el comportamiento de la aplicación móvil del conductor para las operaciones del proyecto.

Permite activar o desactivar funcionalidades relacionadas con:

- Evidencias
- Firma
- Escaneo documental
- Escaneo avanzado de bultos

**Campos principales**

+-----------------------------+-------------------------------------------------------------+
| Campo                       | Descripción                                                 |
+=============================+=============================================================+
| Perfil de la Aplicación     | Perfil funcional general de la app.                         |
+-----------------------------+-------------------------------------------------------------+
| POD Digital                 | Firma digital en pantalla.                                  |
+-----------------------------+-------------------------------------------------------------+
| POD Físico                  | Escaneo obligatorio de documentación física.                |
+-----------------------------+-------------------------------------------------------------+
| Escaneo Masivo              | Escaneo IA mediante vídeo (Scandit).                        |
+-----------------------------+-------------------------------------------------------------+
| Escaneo Spark               | Identificación visual avanzada de bultos.                   |
+-----------------------------+-------------------------------------------------------------+

Uso dentro del sistema en Configuración App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Estos parámetros condicionan directamente la experiencia del conductor.

Cuando está activo POD Digital:

- la app solicita firma

Cuando está activo POD Físico:

- la app exige escaneo documental

El Escaneo Masivo permite lectura acelerada mediante IA.

El Escaneo Spark ayuda a identificar visualmente:

- bultos correctos
- bultos incorrectos

mostrando feedback en tiempo real.

.. note::

   Esta configuración permite adaptar el nivel de control móvil
   desde operativas simples hasta flujos avanzados con validación
   física intensiva.


Otros Parámetros
~~~~~~~~~~~~~~~~~


Otros Parámetros agrupa automatismos que ajustan el comportamiento del proyecto en creación, validación, planificación, stock e integración.

**Campos principales**

+------------------------------------------+--------------------------------------------------------------+
| Campo                                    | Descripción                                                  |
+==========================================+==============================================================+
| Horarios informados                      | Indica si las órdenes traen sus propias ventanas horarias.   |
+------------------------------------------+--------------------------------------------------------------+
| Programación predeterminada              | Horario por defecto cuando no hay horarios informados.       |
+------------------------------------------+--------------------------------------------------------------+
| Aplicar fecha común                      | Solicita fecha de servicio común al cerrar manifiestos.      |
+------------------------------------------+--------------------------------------------------------------+
| Auto secuenciar viaje                    | Reordena paradas automáticamente.                            |
+------------------------------------------+--------------------------------------------------------------+
| Generar viaje en validación              | Crea viajes automáticamente al validar órdenes.              |
+------------------------------------------+--------------------------------------------------------------+
| Crear transferencia a hub                | Genera movimientos automáticos entre hubs.                   |
+------------------------------------------+--------------------------------------------------------------+
| Autoasignar zona operativa/tarifaria     | Permite resolución por proximidad.                           |
+------------------------------------------+--------------------------------------------------------------+

Uso dentro del sistema en Otros Parámetros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Estos parámetros permiten adaptar el mismo motor TMS a operativas:

- Manuales
- Importadas
- Integradas vía API

Un proyecto puede limitarse a defaults básicos o automatizar:

- Creación de viajes
- Asignación territorial
- Flujos logísticos
- Integraciones externas

La resolución por zona más cercana evita operaciones sin zona, pero debe utilizarse con criterio porque puede generar kilómetros extra y afectar el cálculo económico.

Los parámetros de stock conectan la validación logística con inventario.

Los parámetros API convierten el proyecto en unidad de integración y seguridad.



Líneas por Defecto
~~~~~~~~~~~~~~~~~~~

La pestaña Líneas por Defecto permite definir plantillas reutilizables de mercancía para un proyecto.

No son líneas económicas.

No sustituyen la tarifa.

Representan plantillas logísticas reutilizables.

**Campos principales**

+------------------------------+--------------------------------------------------------------+
| Campo                        | Descripción                                                  |
+==============================+==============================================================+
| Líneas por defecto           | Conjunto de plantillas logísticas del proyecto.              |
+------------------------------+--------------------------------------------------------------+
| Nueva línea                  | Acción de creación rápida de plantilla.                      |
+------------------------------+--------------------------------------------------------------+
| Regla de Tarifa              | Define comportamiento operativo de la línea.                 |
+------------------------------+--------------------------------------------------------------+
| Tipo de Bulto                | Clasificación logística de mercancía.                        |
+------------------------------+--------------------------------------------------------------+
| Cantidades                   | Packs, pallets, quantity y meters por defecto.               |
+------------------------------+--------------------------------------------------------------+
| Peso, dimensiones y volumen  | Datos físicos de la línea.                                   |
+------------------------------+--------------------------------------------------------------+
| Descripciones                | Textos operativos para manifiesto o etiquetas.               |
+------------------------------+--------------------------------------------------------------+

Uso dentro del sistema en Líneas por Defecto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En creación manual de tramos, el sistema puede copiar estas líneas cuando el flujo lo permita.

En importaciones, si no existe detalle de mercancía, el sistema puede construir automáticamente las líneas del tramo a partir de estas plantillas.

Si no hay:

- mercancía informada
- líneas por defecto

la importación puede bloquearse.

La Regla de Tarifa sigue condicionando:

- magnitudes declaradas
- acumulados
- trazabilidad física

Estas plantillas son especialmente útiles en proyectos homogéneos con mercancía recurrente.



Inventario
~~~~~~~~~~~

La pestaña Inventario conecta TMS con Odoo Inventory.

Su objetivo es decidir si las expediciones del proyecto deben generar movimientos de stock.

**Campos principales**

+------------------------------+--------------------------------------------------------------+
| Campo                        | Descripción                                                  |
+==============================+==============================================================+
| Crear Stock Picking          | Activa creación de pickings.                                 |
+------------------------------+--------------------------------------------------------------+
| Tipo de Operación            | Tipo de picking Odoo utilizado.                              |
+------------------------------+--------------------------------------------------------------+
| Ubicación Origen             | Punto de salida del inventario.                              |
+------------------------------+--------------------------------------------------------------+
| Ubicación Destino            | Punto destino del inventario.                                |
+------------------------------+--------------------------------------------------------------+
| Grupo aprovisionamiento      | Relación técnica con pickings generados.                     |
+------------------------------+--------------------------------------------------------------+
| Mapeo de producto            | Conversión entre líneas TMS y productos físicos Odoo.        |
+------------------------------+--------------------------------------------------------------+

Uso dentro del sistema en Inventario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Cuando Crear Stock Picking está activo, validar una orden o manifiesto puede generar automáticamente un picking.

Antes de ejecutar el flujo, el sistema valida:

- Tipo de operación
- Ubicación origen
- Ubicación destino

Si falta alguno:

- se bloquea la creación

La integración no usa líneas de venta.

Usa líneas logísticas de expedición.

El producto físico se resuelve mediante el código configurado en la Regla de Tarifa.

Este bloque debe utilizarse únicamente cuando la operativa impacta inventario real.



Bandeja de Entrada API
~~~~~~~~~~~~~~~~~~~~~~~~

La Bandeja de Entrada API configura el proyecto como punto de integración externa.

Agrupa:

- autenticación
- permisos
- recepción
- límites de uso

No es una simple configuración técnica.

Es el perímetro de integración del proyecto.

**Campos principales**

+------------------------------+--------------------------------------------------------------+
| Campo                        | Descripción                                                  |
+==============================+==============================================================+
| API Token                    | Token único de autenticación.                                |
+------------------------------+--------------------------------------------------------------+
| API Inbox                    | Bandeja de recepción del proyecto.                           |
+------------------------------+--------------------------------------------------------------+
| Permiso Post Import Data     | Autoriza importaciones externas.                             |
+------------------------------+--------------------------------------------------------------+
| Permiso Get Tracking         | Autoriza consultas de tracking.                              |
+------------------------------+--------------------------------------------------------------+
| Permiso Get Attachment       | Autoriza acceso a adjuntos.                                  |
+------------------------------+--------------------------------------------------------------+
| Límite por minuto            | Protección frente a exceso de llamadas.                      |
+------------------------------+--------------------------------------------------------------+
| Límite por día               | Límite operativo diario.                                     |
+------------------------------+--------------------------------------------------------------+
| Endpoints permitidos         | Restricciones técnicas de integración.                       |
+------------------------------+--------------------------------------------------------------+

Uso dentro del sistema en Bandeja de Entrada API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los sistemas externos se autentican utilizando el token del proyecto.

Esto permite aislar integraciones por:

- cliente
- operativa
- contrato

Cuando entra una importación API:

- se localiza o crea la bandeja
- se registra el payload recibido
- se conservan referencias externas
- se trazan datos operativos

Si el payload contiene maestros:

- clientes
- transportistas
- conductores
- vehículos
- viajes

también se almacenan.

La bandeja desacopla recepción y creación.

Recibir datos no implica necesariamente crear órdenes inmediatamente.

Esto permite:

- validación
- revisión
- agrupación
- control de incidencias

.. important::

   Los permisos y límites actúan como mecanismo de gobierno
   de integración y deben configurarse con criterio.