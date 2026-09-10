4.5 Configuración de proyectos
------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Proyectos

.. CAPTURA: 4_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_5_project-configuration_01_proyecto.png
      :alt: Formulario de configuración de un Proyecto

      El formulario del Proyecto: la pestaña TMS con sus cinco grupos.

El :term:`Proyecto` (``project.project``) es la unidad de parametrización del TMS. Reúne, para
un cliente o para un transportista, la tarifa, el Planning, la red territorial, los catálogos
permitidos, los automatismos, la app, el inventario y la integración. Casi todo lo que llega a
una Orden, un Tramo, una Parada o un Viaje se hereda de su Proyecto, así que una configuración
incompleta aparece después como incidencia de importación, de planificación, de la app o de
tarifa.

Un Proyecto es de **Órdenes** (de un cliente) o de **Viajes** (de un transportista o agencia),
según el campo Aplicar en. Un cliente puede tener varios proyectos si tiene operativas con
configuraciones distintas, y un transportista, uno por cada operativa en la que participa. La
lista completa de campos, agrupada como en el formulario, está en
:doc:`/17.0/annexes/A_18_proyecto`; aquí se recorren las decisiones pestaña a pestaña.

4.5.1 Administración
~~~~~~~~~~~~~~~~~~~~

El grupo Administración fija el alcance económico del proyecto.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Tarifa
     - La tarifa de venta o de compra del proyecto. Al elegirla, el proyecto lee sus líneas y
       precarga los catálogos que usan (tipos de orden, servicios, transportistas,
       destinatarios, categorías de vehículo), para no activar nada sin cobertura económica.
   * - Modo de división
     - Cómo se divide el precio de una Orden entre sus Tramos: por peso, volumen, bultos, palés,
       cantidad, metros o combinados con kilómetros. Por defecto, kilómetros y peso.
   * - Cuenta analítica
     - Dónde se agrupan en contabilidad los ingresos y costes del proyecto.
   * - Política de fecha administrativa
     - Qué fecha decide la versión de tarifa cuando una operación cruza un cambio de precios: la
       de cierre operativo (la de la parada activa, por defecto), la de creación, la de carga
       (la más temprana de los tramos) o la de descarga (la más tardía).

La fecha administrativa se guarda en un campo propio y estable de la Orden, distinto de la
fecha de pedido de Odoo. Si la política elegida no tiene fecha disponible, se usa la fecha de
pedido y, en último término, la de creación.

4.5.2 Entrada en hub y recogida
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El grupo Entrada Hub / Recogida en Cliente dice cómo entra la mercancía en la red.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Agencia y hub
     - La agencia responsable de la operativa y el hub por el que entra la mercancía. Se
       heredan a los tramos cuando la geografía no dice otra cosa.
   * - Punto de recogida y su horario
     - El origen que se propone por defecto al crear Órdenes, a mano o por fichero, con su
       ventana horaria. Si no hay punto de recogida, se propone el hub.
   * - Servicio de recogida a domicilio
     - El tipo de servicio con que se tarifica la recogida inicial en casa del cliente, para
       distinguirla económicamente del resto de la operativa.

4.5.3 Activación y asignación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los grupos Activación y Tarea (asignación por defecto) definen qué catálogos admite el proyecto
y cuál se propone por defecto. Activación no crea nada: filtra. Sus listas (tipos de orden,
servicios, tipos de transportista, tipos de destinatario, tipos de bulto, categorías de
vehículo) son los valores que se pueden elegir en las Órdenes del proyecto y los que una
importación acepta. La tarifa los precarga desde sus líneas; si un catálogo queda con un único
valor, ese valor pasa solo al campo por defecto correspondiente de Tarea; si hay varios, el
defecto se deja vacío para elegir en cada Orden.

Los valores de Tarea son los que heredan las Órdenes y los Viajes cuando nadie indica otro:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Planning
     - La segmentación operativa de todo el proyecto (ver :doc:`4_3_planning-configuration`).
       Se copia a Órdenes, Tramos y Viajes.
   * - Plan de transporte
     - La red con la que se resuelven zonas operativas, hubs y agencias.
   * - Tiempo de servicio
     - El esquema con que se calcula la duración de cada parada.
   * - Producto
     - El producto por defecto de las líneas económicas.
   * - Equipamiento de vehículos y categorías de carga
     - Lo que la operativa exige a los vehículos y la mercancía que mueve. Restringen los
       recursos compatibles en la asignación y el optimizador.

4.5.4 Otros parámetros: los automatismos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_5_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_5_project-configuration_03_otros-parametros.png
      :alt: Grupo Otros parámetros del Proyecto

      Otros parámetros: los interruptores que automatizan el proyecto.

El grupo Otros parámetros reúne los interruptores que adaptan el mismo motor a una operativa
manual, importada o integrada. Cada uno cambia un paso del flujo del capítulo 5.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Horarios informados
     - Si las Órdenes traen sus ventanas horarias. Si no, se usan las del contacto o las horas
       predeterminadas del proyecto, y un contacto sin horario queda pendiente de normalizar en
       el Manifiesto.
   * - Horas predeterminadas
     - La ventana que se aplica cuando no hay horario informado.
   * - Aplicar fecha común
     - Al cerrar un Manifiesto, pide una fecha de servicio común para todas sus Órdenes.
   * - Hora de cita única y tolerancia
     - Para carga completa y directos: el cliente da una hora, no una ventana. Sólo se pide la
       hora de inicio y el fin se construye sumando la tolerancia en minutos.
   * - Secuenciar viaje
     - Al cerrar un Manifiesto sin secuencia, ordena las paradas con PTV antes de calcular la
       ruta (ver :doc:`/17.0/5_operational-flows/5_2_trip-generation`).
   * - Generar viaje al validar
     - Crea el Viaje al validar la Orden, sin pasar por el asistente.
   * - Crear traslado a hub al asignar
     - Al asignar paradas a una agencia, divide los Tramos y crea la parada intermedia en el
       hub.
   * - Procesar viaje de agencia automáticamente
     - El Viaje que nace al asignar a una agencia se crea ya en Procesado, listo para la app.
   * - Autoasignar zona operativa y zona de tarifa más cercanas
     - Si una dirección no cae en ningún área, se le asigna la más cercana, por separado para la
       zona operativa y para la de tarifa. Evita operaciones sin zona, pero añade kilómetros
       extra que afectan al precio: úsese con criterio.

4.5.5 Aplicación móvil
~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_5_04 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_5_project-configuration_04_app.png
      :alt: Grupo Aplicación móvil del Proyecto

      Aplicación móvil: qué pide la app al conductor en las paradas del proyecto.

El grupo Aplicación móvil define qué exige la app del conductor en las paradas de este
proyecto. Es la palanca para ir de una operativa sencilla a una con validación física intensa
sin cambiar nada más.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Perfil de la aplicación
     - El perfil funcional que carga la app: qué pantallas y acciones ve el conductor.
   * - POD digital
     - Al entregar, la app pide nombre, documento y firma en pantalla.
   * - POD físico
     - Al entregar, la app exige fotografiar el albarán firmado para completar la parada.
   * - Escaneo Masivo
     - Activa «Encontrar bultos»: la cámara resalta entre muchas etiquetas los bultos de la
       parada.
   * - Escaneo Spark
     - Activa la comprobación de bultos por lectura continua en el flujo de la parada.

Los tres modos de escaneo se describen en
:ref:`17.0/1_introduction/1_4_technological-architecture:1.4.5 La app del conductor y el escaneo`,
y su uso paso a paso en el :doc:`Manual del conductor </17.0/10_manual_app/index>`.

4.5.6 Líneas por defecto
~~~~~~~~~~~~~~~~~~~~~~~~

La pestaña Líneas por defecto guarda plantillas de mercancía del proyecto: regla de tarifa, tipo
de bulto, cantidades, peso, dimensiones y descripciones. No son líneas económicas ni sustituyen
a la tarifa. Cuando un fichero o una Orden manual no detallan la mercancía, el sistema crea las
líneas del Tramo a partir de estas plantillas; si no hay ni mercancía informada ni líneas por
defecto, la importación se bloquea. Son la solución natural para proyectos con mercancía
homogénea y recurrente.

4.5.7 Albarán
~~~~~~~~~~~~~

La pestaña Albarán conecta el TMS con el Inventario de Odoo. Con **Crear albarán** activo,
validar una Orden del proyecto genera un albarán con las líneas de mercancía de la Orden (no
las de venta), resolviendo el producto físico por el código de la regla de tarifa. Hacen falta
el tipo de albarán y las ubicaciones de origen y destino; si falta alguno, la creación se
bloquea. Sólo tiene sentido cuando la operativa mueve inventario real.

4.5.8 Bandeja de entrada API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La pestaña API Inbox convierte el proyecto en la unidad de integración y de seguridad con el
sistema del cliente.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Token API
     - Con qué se autentica el sistema externo de este proyecto. Un token por proyecto aísla
       las integraciones por cliente, operativa o contrato.
   * - Permisos
     - Qué puede hacer el token: enviar órdenes, consultar el seguimiento, descargar adjuntos.
   * - Límites por minuto y por día
     - La cuota de llamadas.
   * - Enviar por API al asignar y sus endpoints
     - Si al asignar paradas a una agencia se ejecutan los endpoints de envío configurados, y
       en qué orden.

Lo que llega por el token cae en la :term:`Bandeja de entrada API` del proyecto, donde se
valida y agrupa en un Manifiesto antes de crear nada (ver
:doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`). La configuración de los canales y
los contratos están en la :doc:`Guía del integrador </17.0/7_edi-integrations/index>`.

4.5.9 La vista kanban de proyectos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_5_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_5_project-configuration_02_kanban-proyectos.png
      :alt: Vista kanban de Proyectos

      La kanban de Proyectos: cada tarjeta resume un contrato.

El menú de Proyectos abre una vista kanban que resume cada proyecto en una tarjeta, para leer
el estado de un contrato sin abrir el formulario. Las tarjetas se agrupan en dos columnas según
Aplicar en: proyectos de **Órdenes** (etiqueta azul) y de **Viajes** (etiqueta naranja), con
el color del proyecto.

Cada tarjeta lleva, de arriba abajo, el nombre y la etiqueta de tipo; el cliente o el
transportista, la agencia si la hay, y en gris la tarifa y el Planning; los indicadores del
periodo; y, abajo a la derecha, las banderas de configuración y la fecha de la última
actividad.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Indicador
     - Qué muestra
   * - Órdenes abiertas / total (proyectos de Órdenes)
     - Las Órdenes no cerradas ni canceladas sobre el histórico completo del proyecto.
   * - Ingresos de 30 días (verde)
     - El importe sin impuestos de las Órdenes creadas en los últimos 30 días. Sólo aparece si
       es mayor que cero.
   * - Viajes abiertos / total (proyectos de Viajes)
     - Los Viajes no completados ni fallidos sobre el total.
   * - Ingresos de 30 días (rosa) y coste de 30 días (rojo)
     - En proyectos de Viajes: el importe de las órdenes de compra de los viajes creados en 30
       días, y el coste pasivo calculado por el TMS. Pueden diferir mientras la orden de compra
       no esté cerrada.
   * - Banderas HUB, AUTO y API
     - Traslado a hub al asignar, procesar viaje de agencia automáticamente y enviar por API al
       asignar, cuando están activos. Un proyecto sin banderas tiene la configuración mínima.
   * - Última actividad
     - La fecha de la Orden o el Viaje más reciente del proyecto. Sin ella, el contrato está
       dormido.

Los indicadores se calculan al abrir la vista sobre los datos vivos. La búsqueda ofrece filtros
por tipo de proyecto y por cada bandera, agrupaciones por tipo, cliente, transportista, tarifa
y Planning, y un panel lateral para combinar tipo, tarifa y Planning con contadores. Al abrir
un proyecto desde la kanban, la cabecera del formulario muestra el botón inteligente
**Órdenes** o **Viajes** con el recuento de abiertos sobre el total, que lleva a la lista
filtrada por el proyecto. El botón de ayuda de la cabecera de la kanban abre esta página de la
documentación; la dirección se puede cambiar en los parámetros del sistema de Odoo.

.. note::

   Las etiquetas de la kanban (Orders, Trips, Revenue, Cost, Help) están hoy en inglés en la
   interfaz porque el módulo no las traduce todavía. La corrección está anotada en la lista de
   correcciones de Odoo del plan de documentación.
