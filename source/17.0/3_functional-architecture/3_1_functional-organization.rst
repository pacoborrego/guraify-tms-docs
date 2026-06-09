3.1 Organización funcional del sistema
--------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Menú raíz: TMS, con las áreas TMS › **Operaciones**, TMS › **Administración**,
   TMS › **Maestros** y TMS › **Configuración**.

Guraify TMS organiza sus funcionalidades en varios bloques que reflejan la lógica operativa de una empresa de transporte. Esta organización permite separar claramente las actividades de ejecución diaria, planificación, gestión económica y configuración estructural del sistema.

La estructura principal del sistema se divide en cuatro áreas funcionales:

- Operaciones

- Administración

- Maestros

- Configuración

Cada una de estas áreas agrupa distintos menús y herramientas que permiten gestionar los diferentes aspectos de la operativa del transporte.

.. mermaid::

   flowchart TB
       TMS["TMS"] --> OP["Operaciones"]
       TMS --> ADM["Administración"]
       TMS --> MAE["Maestros"]
       TMS --> CFG["Configuración"]
       OP --> TRA["Tráfico<br/>Órdenes · Viajes · Manifiestos · API Inbox"]
       OP --> PLA["Planificación<br/>Plan de conductores · Optimizador"]
       OP --> MOP["Maestros operativos<br/>Tramos · Paradas · Bultos · Trazabilidad"]
       ADM --> ADM1["Facturación a clientes · Liquidación a transportistas<br/>Control de costes · Estados económicos"]
       MAE --> MAE1["Clientes · Transportistas · Vehículos<br/>Recursos humanos · Localizaciones · Proyectos"]
       CFG --> CFG1["Parámetros · Integraciones (EDI) · Reglas de negocio<br/>Automatizaciones · Planificación · Tarificación"]

.. CAPTURA: 3_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_1_functional-organization_01_menu-raiz.png
      :alt: Menú raíz de Guraify TMS en Odoo

      Áreas funcionales del menú raíz de Guraify TMS.

3.1.1 Operaciones
~~~~~~~~~~~~~~~~~~

El bloque de Operaciones constituye el núcleo operativo del sistema. En esta sección se gestionan las entidades vivas del modelo conceptual y se ejecuta la operativa diaria del departamento de tráfico.

Este bloque se organiza en tres subconjuntos funcionales:

3.1.1.1 Tráfico
^^^^^^^^^^^^^^^

Contiene las herramientas utilizadas para gestionar la demanda de transporte y la ejecución de los servicios, incluye los siguientes menús principales:

- Órdenes (``sale.order``)

- Viajes (``tms.trip``)

- Manifiestos (``tms.edi.manifest``)

- API Inbox (``tms_int.api.inbox``)

Estas herramientas permiten registrar los encargos de los clientes, estructurar las expediciones, organizar los servicios y controlar su ejecución.

3.1.1.2 Planificación
^^^^^^^^^^^^^^^^^^^^^^

La sección de planificación agrupa las herramientas destinadas a organizar los recursos y optimizar la ejecución de los servicios.

Incluye:

- Plan de disponibilidad de conductores

- Optimizador de Paradas

Estas herramientas permiten gestionar la disponibilidad de recursos humanos y ejecutar procesos de optimización de rutas mediante el motor de planificación integrado.

3.1.1.3 Maestros operativos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta sección agrupa entidades operativas que forman parte del modelo logístico y que son utilizadas por los distintos procesos del sistema.

Incluye:

- Tramos (``tms.shipment.leg``)

- Paradas (``tms.stop``)

- Bultos (``tms.shipment.pack``)

- Trazabilidad (``tms.traceability``)

Aunque estas entidades se generan habitualmente de forma automática durante el flujo operativo, el sistema permite consultarlas y gestionarlas directamente desde estos menús para tareas de control, auditoría o gestión de incidencias.

3.1.2 Administración
~~~~~~~~~~~~~~~~~~~~~

El bloque de Administración agrupa los procesos relacionados con la gestión económica del transporte.

En esta sección se gestionan los procesos administrativos derivados de la operativa logística, incluyendo:

- facturación a clientes

- liquidación de servicios a transportistas

- control de costes operativos

- seguimiento de estados económicos de las operaciones

La estrecha vinculación entre operativa y economía permite que los eventos logísticos generen automáticamente información económica coherente dentro del ERP.

3.1.3 Maestros
~~~~~~~~~~~~~~

La sección de Maestros contiene las entidades estructurales que configuran el comportamiento del sistema.

Incluye información relativamente estable que se utiliza como base para los procesos operativos, tales como:

- clientes

- transportistas

- vehículos

- recursos humanos

- localizaciones

- proyectos logísticos

Estos datos constituyen la base de configuración sobre la que operan los diferentes módulos del TMS.

3.1.4 Configuración
~~~~~~~~~~~~~~~~~~~~

La sección de Configuración permite definir los parámetros estructurales del sistema y adaptar su comportamiento a las necesidades específicas de cada implantación.

En esta área se gestionan, entre otros aspectos:

- parámetros del sistema

- configuración de integraciones

- reglas de negocio

- automatizaciones

- estructuras de planificación

- configuraciones de tarificación

Estas configuraciones permiten adaptar el TMS a distintos modelos operativos sin necesidad de modificar su arquitectura base.
