Configuración logística
-----------------------

La configuración logística describe los recursos físicos y las restricciones materiales que condicionan la ejecución del transporte.

En este bloque se definen equipamientos, categorías de carga, reglas de medición logística, tipos de mercancía y capacidades de vehículo.

Estos elementos permiten que el sistema determine compatibilidades entre mercancía, vehículo, transportista y planificación.

También alimentan procesos de optimización, cálculo de capacidad, validaciones operativas y generación de líneas logísticas.



Equipamientos
~~~~~~~~~~~~~

Los Equipamientos representan capacidades, accesorios o requisitos técnicos necesarios para ejecutar determinados servicios de transporte.

Pueden describir elementos como:

- Plataforma elevadora
- Frío
- ADR
- Jaula
- Transpaleta
- Doble tripulación
- Otros requisitos operativos específicos

Campos principales
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Código o identificador funcional del equipamiento.
   * - Secuencia
     - Orden de visualización dentro del sistema.
   * - Descripción
     - Texto descriptivo del equipamiento.
   * - Compañía
     - Configuración específica por compañía.
   * - Valor por defecto
     - Clasificación estándar.
   * - Información adicional
     - Notas internas de parametrización.
   * - Color
     - Identificador visual utilizado en interfaces.

Aplicación operativa de Equipamientos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los equipamientos se relacionan con:

- Categorías de vehículo
- Proyectos
- Reglas operativas
- Restricciones logísticas

Su función es garantizar que el recurso asignado disponga de las capacidades necesarias para ejecutar correctamente el servicio.

Cuando una operación exige determinados equipamientos, estos actúan como criterio de filtrado para:

- Asignación de vehículos
- Validaciones operativas
- Reglas económicas
- Restricciones de planificación



Categorías de Carga
~~~~~~~~~~~~~~~~~~~

Las Categorías de Carga permiten clasificar la naturaleza logística de la mercancía transportada.

A diferencia del Tipo de Bulto, que describe la unidad física manipulada, la categoría de carga define el comportamiento operativo de la mercancía.

Ejemplos habituales:

- Refrigerada
- Seca
- Paletizada
- Frágil
- ADR
- Voluminosa

Campos principales
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Código identificador de la categoría.
   * - Secuencia
     - Orden de visualización.
   * - Descripción
     - Definición funcional.
   * - Compañía
     - Configuración multiempresa.
   * - Valor por defecto
     - Clasificación estándar.
   * - Información adicional
     - Notas internas.
   * - Color
     - Identificador visual.

Aplicación operativa de Categorías de Carga
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Las categorías de carga intervienen en:

- Proyectos
- Categorías de vehículo
- Reglas TMS
- Restricciones operativas
- Optimización

Permiten determinar:

- Qué vehículos son compatibles
- Qué restricciones deben respetarse
- Qué reglas económicas o de planificación deben aplicarse

También pueden intervenir en reglas tarifarias cuando la naturaleza de la mercancía afecta al cálculo económico.



Reglas de Tarifa
~~~~~~~~~~~~~~~~

Las Reglas de Tarifa definen cómo se mide operativamente la mercancía dentro de una expedición.

Este maestro no define precios.

Define la forma en que la carga se representa operativamente.

Ejemplos:

- Bultos
- Pallets
- Cantidad
- Metros lineales

Campos principales
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Campo
     - Descripción
   * - Nombre
     - Identificador funcional de la regla.
   * - Descripción
     - Definición operativa.
   * - Físico
     - Indica si representa una unidad física trazable.
   * - Ancho, alto, largo y peso por defecto
     - Datos utilizados para volumen y validaciones.
   * - Descripción singular/plural
     - Textos mostrados en líneas e informes.
   * - Magnitudes disponibles
     - Bultos, cantidad, metros o pallets.

Comportamiento operativo de Reglas de Tarifa
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Bultos**

Se utiliza cuando la unidad operativa es el bulto individual.

El sistema:

- Solicita número de unidades
- Calcula volumen
- Genera registros físicos individuales
- Permite trazabilidad y escaneo

**Pallets**

Funciona de forma equivalente, utilizando el pallet como unidad operativa principal.

**Cantidad**

Representa unidades no trazadas individualmente.

No genera bultos físicos ni códigos de barras.

**Metros**

Representa metros lineales de ocupación de carga.

.. note::

   La Regla de Tarifa define cómo se mide la línea operativa.

   La tarifa económica determinará posteriormente qué magnitud
   se utilizará para calcular el precio.

.. note::

   Actualmente la validación dimensional en ``tms.pricelist.rule``
   se ejecuta antes de distinguir entre reglas físicas y no físicas.

   Conviene revisar este comportamiento para reglas basadas
   en cantidad o metros.



Tipos de Bulto
~~~~~~~~~~~~~~

El Tipo de Bulto representa la clasificación logística de la mercancía transportada.

Debe diferenciarse claramente de la Regla de Tarifa.

Mientras la Regla de Tarifa responde a cómo se mide la carga, el Tipo de Bulto responde a qué tipo de mercancía se está transportando.

Ejemplos:

- Seco
- Refrigerado
- Congelado
- Frágil
- Textil
- Alimentación

Campos principales
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Identificador corto del tipo.
   * - Descripción
     - Definición funcional.
   * - Información
     - Campo informativo adicional.
   * - Imagen
     - Icono asociado.
   * - Equipamientos
     - Requisitos vinculados.
   * - Por defecto
     - Registro fallback.
   * - Secuencia
     - Orden de aparición.
   * - Color
     - Clasificación visual.
   * - Compañía
     - Empresa propietaria.

Aplicación operativa de Tipos de Bulto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Tipo de Bulto se utiliza principalmente en líneas de expedición.

Cada línea puede contener:

- Una Regla de Tarifa
- Un Tipo de Bulto

Ambos datos son complementarios.

También interviene en:

- Integraciones EDI/API
- Manifiestos
- Clasificación operativa
- Preparación de carga

.. note::

   El Tipo de Bulto responde a:

   "Qué mercancía transporto"

   La Regla de Tarifa responde a:

   "Cómo se mide operativamente"



Modelos y Categorías de Vehículo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los Modelos y Categorías de Vehículo amplían la gestión estándar de flota de Odoo con información logística específica de transporte.

Esta parametrización es utilizada por:

- Planificación interna
- Routing
- Optimización
- Tarificación
- Validaciones operativas

Campos principales de Categoría
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Campo
     - Descripción
   * - Perfil de vehículo
     - Perfil compatible con PTV.
   * - Equipamientos y categorías de carga
     - Capacidades asociadas.
   * - Capacidades máximas
     - Peso, volumen, pallets, metros y otras magnitudes.
   * - Ubicación inicial y final
     - Referencias utilizadas para routing.
   * - Límites operativos
     - Restricciones de distancia, intervalos y paradas.
   * - Horas de conducción
     - Preset normativo aplicable.
   * - Zona tarifaria y valor por defecto
     - Datos de cálculo y asignación.

Campos principales de Modelo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Tipo de vehículo
     - Rígido, tractor, semirremolque u otros.
   * - Pesos técnicos
     - Peso permitido, peso vacío y capacidad.
   * - Dimensiones
     - Altura, anchura y longitud.
   * - Motor y combustible
     - Tipología energética.
   * - Emisiones
     - CO2, Euro class y restricciones ambientales.

Aplicación operativa de Categorías de Vehículo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La categoría de vehículo es uno de los principales criterios de asignación operativa.

Sus capacidades determinan:

- Qué carga puede consolidarse
- Qué rutas son viables
- Qué restricciones deben respetarse
- Qué reglas económicas son aplicables

En integraciones con PTV se consideran:

- Dimensiones reales
- Restricciones viarias
- Emisiones
- Tiempos de conducción
- Tipología del vehículo