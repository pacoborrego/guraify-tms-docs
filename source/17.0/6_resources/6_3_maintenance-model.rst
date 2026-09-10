6.3 Mantenimiento: el vehículo como elemento mantenible
-------------------------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Mantenimiento › Órdenes de trabajo, Calendario y Tablero del taller.

El mantenimiento se apoya en el módulo nativo de Mantenimiento de Odoo, con una diferencia de
diseño: **el elemento que se mantiene es el vehículo**, directamente, sin crear un «equipo» de
mantenimiento por cada vehículo. El vehículo de la Flota incorpora el comportamiento
mantenible del módulo nativo, y con él llegan gratis el equipo de taller y el técnico
responsables, los contadores de órdenes abiertas, las fechas del último fallo y los indicadores
de fiabilidad (tiempo medio entre fallos y tiempo medio de reparación).

6.3.1 La orden de trabajo
~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_3_maintenance-model_01_orden-trabajo.png
      :alt: Formulario de una orden de trabajo

      Una orden de trabajo: vehículo, trabajo, tarea, odómetro y etapa.

La :term:`Orden de trabajo` (``maintenance.request``) es la solicitud de mantenimiento nativa
de Odoo con los datos del taller: el **vehículo**, el **trabajo** a realizar (del catálogo de
la Flota), la **tarea** que lo clasifica, el **odómetro** en el momento del trabajo y, si nació
de una regla de preventivo, la regla. Es **correctiva** cuando la abre alguien porque algo se
ha roto o hay que revisar, y **preventiva** cuando la genera una regla o una recurrencia. El
asunto se compone solo con el trabajo y la matrícula («Aceite de Motor — AA102SQ») y se puede
sobrescribir; lo que teclee el usuario no se toca.

La orden recorre cuatro etapas: **Pendiente** (abierta, sin empezar), **En taller**, **Realizada**
(cerrada) y **Descartada** (cerrada sin hacerse). Las dos últimas cuentan como cerradas: la orden
entra en el historial y alimenta el motor. Una orden anulada no es una etapa, es el archivo de
Odoo. El calendario, el kanban por etapas y el tablero del taller son los nativos, con el
kilometraje actual del vehículo añadido a las tarjetas y a la lista, y un filtro **Pendientes**
que reúne lo que no está cerrado.

.. important::

   Una orden de trabajo sobre un vehículo **no se puede cerrar sin su kilometraje**. Es la regla
   que hace posible todo el preventivo por kilómetros: cada trabajo realizado deja el
   kilometraje real en el que se hizo, y ese dato es el que las reglas usan para calcular cuándo
   toca el siguiente. El flujo de cierre está en :doc:`6_5_workshop-flows`.

6.3.2 Trabajos y tareas
~~~~~~~~~~~~~~~~~~~~~~~

El **trabajo** es lo que se hace: cambio de aceite de motor, filtro de aire, frenos,
inyectores. El catálogo es el de tipos de servicio de la Flota de Odoo (``fleet.service.type``),
extendido con la tarea, el material y el intervalo por defecto de cada trabajo, y con la marca
de si participa en el preventivo. El sistema viene con veintiún trabajos preventivos y los
cuatro objetivos periódicos (lavado, engrase, calibración y relevamiento de cubiertas), y el
cliente añade los suyos. Los nombres son únicos sin distinguir mayúsculas.

La **tarea** (``tms.maintenance.task``) es la clasificación con la que el taller filtra su
lista: Preventivo, Taller, Reparación, Repuesto, Gomería, Lavado, Engrase, Mejora, Auxilio,
Multimedia, Mano de obra. Cada trabajo tiene una tarea por defecto y cada orden hereda la del
trabajo o lleva la suya. Ambos catálogos se mantienen en :doc:`6_8_configuration`.

6.3.3 La ficha del vehículo
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_3_maintenance-model_02_pestana-mantenimiento.png
      :alt: Pestaña Maintenance (TMS) del vehículo

      La pestaña de mantenimiento del vehículo: control de service, fiabilidad, reglas y órdenes.

La ficha del vehículo reúne todo lo del taller en la pestaña **Maintenance (TMS)**: el control de
service a dos niveles, los indicadores de fiabilidad que da el módulo nativo (tiempo medio
entre fallos, tiempo medio de reparación, próximo fallo estimado, último fallo, equipo y
técnico), la configuración de la unidad, las reglas de preventivo con su semáforo (de solo
lectura: se editan en su pantalla) y el historial de órdenes. Un botón inteligente muestra las
órdenes abiertas, y los botones de la pestaña lanzan la carga masiva de service, el texto para
el taller y la orden de trabajo impresa (ver :doc:`6_5_workshop-flows` y :doc:`6_6_outputs`).

Dar de baja una unidad es **archivarla**, como cualquier registro de Odoo: desaparece de las
listas, los rankings y las alertas y conserva todo su historial. Campos en
:doc:`/17.0/annexes/A_20_mantenimiento`.
