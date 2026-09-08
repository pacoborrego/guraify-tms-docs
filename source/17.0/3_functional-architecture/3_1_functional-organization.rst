3.1 Organización funcional del sistema
--------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Menú raíz: TMS, con las áreas TMS › **Operaciones**, TMS › **Administración**,
   TMS › **Maestros** y TMS › **Configuración**.

Guraify TMS organiza sus funcionalidades en cuatro áreas que reflejan la lógica de una empresa
de transporte: la ejecución diaria, la gestión económica, los datos maestros y la configuración
estructural. Cada área agrupa los menús con los que se gestiona ese aspecto de la operativa.

.. mermaid::

   flowchart TB
       TMS["TMS"] --> OP["Operaciones"]
       TMS --> ADM["Administración"]
       TMS --> MAE["Maestros"]
       TMS --> CFG["Configuración"]
       OP --> TRA["Tráfico<br/>Órdenes · Viajes · Manifiestos<br/>Bandeja de entrada API · Trazabilidad"]
       OP --> PLA["Planificación<br/>Plan de disponibilidad de conductores<br/>Optimizador de Paradas"]
       OP --> MOP["Maestros operativos<br/>Tramos · Líneas · Paradas · Bultos"]
       ADM --> ADM1["Opciones de tarifa · Productos, clientes y proveedores<br/>Reembolsos · Transacciones"]
       MAE --> MAE1["Equipos (vehículos) · Recursos humanos<br/>Operaciones (contactos, hubs, agencias)"]
       CFG --> CFG1["Proyectos · Planes de transporte · Zonas geográficas<br/>Tiempos de servicio · Reglas · EDI"]

.. figure:: /_static/img/3_functional-architecture/3_1_functional-organization_01_menu-raiz.png
   :alt: Menú raíz de Guraify TMS en Odoo

   Áreas funcionales del menú raíz de Guraify TMS.

3.1.1 Operaciones
~~~~~~~~~~~~~~~~~

Operaciones es el núcleo del sistema: aquí viven las entidades del modelo conceptual y aquí
trabaja a diario el departamento de tráfico. Se organiza en tres submenús.

3.1.1.1 Tráfico
^^^^^^^^^^^^^^^

Reúne las herramientas para gestionar la demanda y la ejecución de los servicios: las
**Órdenes**, los **Viajes**, los **Manifiestos**, la **Bandeja de entrada API** y la
**Trazabilidad**. Desde aquí se registran los encargos de los clientes, se estructuran en
viajes y se controla su ejecución; la Trazabilidad es el histórico de eventos de cada
Parada, Tramo y Orden. Cada una de estas entidades tiene su propia sección en
:doc:`3_2_operational-data-model`.

3.1.1.2 Planificación
^^^^^^^^^^^^^^^^^^^^^

Agrupa las dos herramientas con las que se organizan los recursos y se optimiza la ejecución:
el :term:`Plan de disponibilidad de conductores`, donde se declara qué conductor está
disponible, cuándo y con qué vehículo, y el :term:`Optimizador de Paradas`, que agrupa las
Paradas pendientes en Viajes sobre el mapa con el motor de PTV. Ambas se describen en
:doc:`3_3_planning-model`.

3.1.1.3 Maestros operativos
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Da acceso directo a las entidades que el flujo operativo genera por sí solo: los **Tramos**,
las **Líneas** (las líneas de servicio de cada Orden), las **Paradas** y los **Bultos**. Aunque
normalmente no se crean a mano, el sistema permite consultarlas y gestionarlas desde estos
menús para tareas de control, auditoría o resolución de incidencias.

3.1.2 Administración
~~~~~~~~~~~~~~~~~~~~

Administración agrupa la gestión económica del transporte. Contiene las **Opciones de tarifa**
(tarifas, zonas de tarifa, tarifas base, detalles de línea de tarifa y el diagnóstico de tarifa
de órdenes y de viajes), los maestros económicos (**Productos**, **Clientes** y
**Proveedores**), los **Reembolsos** cobrados en la entrega y las **Transacciones**: las líneas
de venta, las líneas de compra y la lista de facturas. La vinculación entre operativa y
economía hace que los eventos logísticos generen aquí información económica coherente sin
intervención manual.

3.1.3 Maestros
~~~~~~~~~~~~~~

Maestros contiene los datos estructurales, relativamente estables, sobre los que operan los
procesos: los **Equipos** (vehículos, sus modelos y sus categorías), los **Recursos humanos**
(conductores) y las **Operaciones** (contactos, hubs y agencias). Los clientes y los
transportistas son contactos de Odoo con un papel marcado en su ficha.

3.1.4 Configuración
~~~~~~~~~~~~~~~~~~~

Configuración define los parámetros estructurales del sistema y adapta su comportamiento a cada
implantación: los **Proyectos**, que concentran la configuración de cada cliente u operativa;
los **Planes de transporte** y las **Zonas geográficas**, con su asistente de importación desde
OpenStreetMap; los **Tiempos de servicio**; las **Reglas** de negocio; y el submenú **EDI**, con
las integraciones API, sus endpoints, las definiciones de fichero, las funciones
preestablecidas de transformación y los registros de las llamadas. Estas configuraciones
adaptan el TMS a distintos modelos operativos sin modificar su arquitectura base; el capítulo 4
las recorre una a una.
