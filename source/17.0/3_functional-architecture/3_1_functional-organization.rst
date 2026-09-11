3.1 Organización funcional del sistema
--------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Menú raíz: TMS, con las áreas TMS › **Operaciones**, TMS › **Administración**,
   TMS › **Maestros** y TMS › **Configuración**.

Guraify TMS organiza sus funcionalidades en cuatro áreas que reflejan la lógica de una empresa
de transporte: la ejecución diaria, la gestión económica, los datos maestros y la configuración
estructural. Cada área agrupa los menús con los que se gestiona ese aspecto de la operativa. El
motor de indicadores añade una quinta área, **Métricas**, que se describe con el control
económico en :doc:`/17.0/8_economic-administration/8_8_control-reporting`.

.. mermaid::

   flowchart TB
       TMS["TMS"] --> OP["Operaciones"]
       TMS --> ADM["Administración"]
       TMS --> MAE["Maestros"]
       TMS --> CFG["Configuración"]
       OP --> TRA["Tráfico<br/>Órdenes · Viajes · Manifiestos<br/>Trazabilidad · Bandeja de entrada API"]
       OP --> PLA["Planning<br/>Plan Disponibilidad Conductores<br/>Optimizador de Paradas"]
       OP --> MOP["Maestros<br/>Tramos · Líneas · Paradas · Bultos"]
       OP --> TAB["Tableros"]
       ADM --> ADM1["Opciones de Tarifa · Maestros<br/>Reembolsos · Transacciones"]
       MAE --> MAE1["Equipos · Recursos Humanos<br/>Operaciones (contactos, hubs, agencias)"]
       CFG --> CFG1["Ajustes · Proyectos · Planes de Transporte<br/>Áreas Geográficas · Tiempos de Servicio<br/>Reglas · App · EDI"]

.. figure:: /_static/img/3_functional-architecture/3_1_functional-organization_01_menu-raiz.png
   :alt: Menú raíz de Guraify TMS en Odoo

   Áreas funcionales del menú raíz de Guraify TMS.

3.1.1 Operaciones
~~~~~~~~~~~~~~~~~

Operaciones es el núcleo del sistema: aquí viven las entidades del modelo conceptual y aquí
trabaja a diario el departamento de tráfico. Se organiza en tres submenús y un acceso a los
Tableros.

3.1.1.1 Tráfico
^^^^^^^^^^^^^^^

Reúne las herramientas para gestionar la demanda y la ejecución de los servicios: las
**Órdenes**, los **Viajes**, los **Manifiestos**, la **Trazabilidad** y la **Bandeja de entrada
API**. Desde aquí se registran los encargos de los clientes, se estructuran en Viajes y se
controla su ejecución; la Trazabilidad es el histórico de eventos de cada Parada, Tramo y
Orden. Cada una de estas entidades tiene su propia sección en :doc:`3_2_operational-data-model`.

3.1.1.2 Planificación (menú «Planning»)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Agrupa las dos herramientas con las que se organizan los recursos y se optimiza la ejecución:
el :term:`Plan de disponibilidad de conductores` (menú **Plan Disponibilidad Conductores**),
donde se declara qué conductor está disponible, cuándo y con qué vehículo, y el
:term:`Optimizador de Paradas`, que agrupa las Paradas pendientes en Viajes sobre el mapa con el
motor de PTV. Ambas se describen en :doc:`3_3_planning-model`. El submenú se llama «Planning» en
la interfaz, la misma palabra que la entidad :term:`Planning`; en esta documentación se le llama
Planificación cuando se habla del menú.

3.1.1.3 Maestros
^^^^^^^^^^^^^^^^

Da acceso directo a las entidades que el flujo operativo genera por sí solo: los **Tramos**, las
**Líneas** (las líneas de venta de la Orden, una por mercancía o concepto), las **Paradas** y
los **Bultos**. Aunque normalmente no se crean a mano, el sistema permite consultarlas y
gestionarlas desde estos menús para tareas de control, auditoría o resolución de incidencias.
Los Tramos y las Paradas se explican en :doc:`3_2_6_legs-and-stops`.

3.1.1.4 Tableros
^^^^^^^^^^^^^^^^

El menú **Tableros** abre las hojas de cálculo con tablas dinámicas sobre los datos vivos del
TMS: de serie vienen tres :term:`Tableros <Tablero>`, dos de operaciones con filtros por fecha,
Planning, Cliente y Transportista, y uno de facturación pendiente con filtro por periodo. Se
describen en :doc:`/17.0/8_economic-administration/8_8_control-reporting`.

3.1.2 Administración
~~~~~~~~~~~~~~~~~~~~

Administración agrupa la gestión económica del transporte. Contiene las **Opciones de Tarifa**
(**Tarifa**, **Zonas de Tarifa**, **Tarifa Base**, **Detalle de línea de tarifa** y el
**Diagnóstico de tarifa** de órdenes y de viajes), un segundo submenú **Maestros** con los
maestros económicos (**Productos**, **Clientes** y **Proveedores**), los **Reembolsos**
cobrados en la entrega y las **Transacciones**: las **Líneas de Orden de Venta**, las **Líneas
de Orden de Compra** y la **Lista de facturas**. La vinculación entre operativa y economía hace
que los eventos logísticos generen aquí información económica coherente sin intervención
manual; el detalle está en :doc:`3_4_pricing-model` y en
:doc:`/17.0/8_economic-administration/index`.

3.1.3 Maestros
~~~~~~~~~~~~~~

Maestros contiene los datos estructurales, relativamente estables, sobre los que operan los
procesos: los **Equipos** (**Vehículos**, sus **Modelos** y sus **Categorías**), los **Recursos
Humanos** (**Conductores**) y las **Operaciones** (**Contactos**, **Hubs** y **Agencias**). Los
clientes y los transportistas son contactos de Odoo con un papel marcado en su ficha.

3.1.4 Configuración
~~~~~~~~~~~~~~~~~~~

Configuración define los parámetros estructurales del sistema y adapta su comportamiento a cada
implantación. Empieza por **Ajustes**, la página del TMS dentro de los Ajustes de Odoo, que
reúne en una sola pantalla los accesos a los catálogos operativos del capítulo 4 (tipos de
servicio, de Orden, de Parada, de bulto, de destinatario, de transportista y de reembolso,
Plannings, franjas horarias, reglas de tarifa, opciones de trazabilidad, equipamientos,
categorías de carga, perfiles de jornada) y las opciones de compañía, como qué transportistas
son flota propia. Siguen los
**Proyectos**, que concentran la configuración de cada cliente u operativa; los **Planes de
Transporte** y las **Áreas Geográficas**, con su **Asistente de áreas OSM** para importarlas
desde OpenStreetMap; los **Tiempos de Servicio**; las **Reglas** de asignación, restricción y
prioridad entre contactos, conductores, vehículos y áreas; el submenú **App**, con los perfiles
y roles de la aplicación del conductor, sus dispositivos y los motivos que ofrece; y el submenú
**EDI**, con las **Integraciones API**, sus **Endpoints API**, las **Definiciones de fichero** y
las **Funciones preestablecidas** de transformación. Estas configuraciones adaptan el TMS a
distintos modelos operativos sin modificar su arquitectura base; el
:doc:`capítulo 4 </17.0/4_parametrization/index>` las recorre una a una y la
:doc:`Guía del integrador </17.0/7_edi-integrations/index>` desarrolla el submenú EDI.
