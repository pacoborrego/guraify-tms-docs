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
permitidos, los automatismos, la app, el albarán y la integración. Casi todo lo que llega a
una Orden, un Tramo, una Parada o un Viaje se hereda de su Proyecto, así que una configuración
incompleta aparece después como incidencia de importación, de planificación, de la app o de
tarifa.

Un Proyecto es de **Órdenes** (de un cliente) o de **Viajes** (de un transportista o agencia),
según el campo **Aplicar en**. Un cliente puede tener varios Proyectos si tiene operativas con
configuraciones distintas, y un transportista, uno por cada operativa en la que participa. La
lista completa de campos, agrupada como en el formulario, está en
:doc:`/17.0/annexes/A_18_proyecto`; aquí se recorren las decisiones grupo a grupo de la pestaña
TMS y después las otras pestañas.

4.5.1 Administración
~~~~~~~~~~~~~~~~~~~~

El grupo **Administración** fija el alcance económico del Proyecto.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Tarifa
     - La tarifa de venta o de compra del Proyecto. Al elegirla, el Proyecto lee sus líneas y
       precarga en Activación los catálogos que usan (Tipos de Orden, de Servicio, de
       Transportista, de Destinatario y categorías de vehículo), para no activar nada sin
       cobertura económica.
   * - Modo de división
     - Cómo se divide el precio de una Orden entre sus Tramos: por peso, volumen, bultos, palés,
       cantidad, metros o combinados con kilómetros. Por defecto, kilómetros y peso. Es la
       :term:`División de ventas` (ver :doc:`/17.0/8_economic-administration/8_2_sales-split`).
   * - Cuenta analítica
     - Dónde se agrupan en contabilidad los ingresos y costes del Proyecto.
   * - Política de fecha administrativa
     - Qué fecha decide la versión de tarifa cuando una operación cruza un cambio de precios: la
       de cierre operativo (la de la parada activa, por defecto), la de creación, la de carga
       (la más temprana de los Tramos) o la de descarga (la más tardía). Es la fecha con la que
       se elige la versión de la Tarifa (ver :doc:`4_4_economic-configuration`).

4.5.2 Entrada en hub y recogida
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El grupo **Entrada Hub / Recogida en Cliente** dice cómo entra la mercancía en la red.

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
       franja horaria. Si no hay punto de recogida, se propone el hub.
   * - Servicio de recogida a domicilio
     - El tipo de servicio con que se tarifica la recogida inicial en casa del cliente, para
       distinguirla económicamente del resto de la operativa.

4.5.3 Activación y asignación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los grupos **Activación** y **Tarea** (así se llama en la interfaz el grupo de asignación por
defecto) definen qué catálogos admite el Proyecto y cuál se propone por defecto. Activación no
crea nada: filtra. Sus listas (Tipos de Orden, de Servicio, de Transportista, de Destinatario
y de Bulto, y categorías de vehículo) son los valores que se pueden elegir en las Órdenes del
Proyecto y los que una importación acepta. Si un catálogo queda con un único valor, ese valor
pasa al campo por defecto correspondiente del grupo Tarea; si hay varios, el defecto se deja
vacío para elegir en cada Orden.

Los valores del grupo Tarea son los que heredan las Órdenes y los Viajes cuando nadie indica
otro:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Planning
     - La segmentación operativa de todo el Proyecto (ver :doc:`4_3_planning-configuration`).
       Se copia a Órdenes, Tramos y Viajes.
   * - Plan de transporte
     - La red con la que se resuelven zonas operativas, hubs y agencias.
   * - Tiempo de servicio
     - El esquema con que se calcula la duración de cada Parada.
   * - Producto
     - El producto por defecto de las líneas económicas.
   * - Equipamiento de vehículos y categorías de carga
     - Lo que la operativa exige a los vehículos y la mercancía que mueve. Restringen los
       recursos compatibles en la asignación y el optimizador.

4.5.4 Otros parámetros y automatismos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_5_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_5_project-configuration_03_otros-parametros.png
      :alt: Grupo Otros parámetros del Proyecto

      Otros parámetros: los interruptores que automatizan el Proyecto.

El grupo **Otros parámetros** reúne los interruptores que adaptan el mismo motor a una
operativa manual, importada o integrada. Cada uno cambia un paso del flujo del
:doc:`capítulo 5 </17.0/5_operational-flows/index>`.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Horarios informados
     - Si las Órdenes traen sus franjas horarias. Si no, se usan las del contacto o las horas
       predeterminadas del Proyecto, y un contacto sin horario queda pendiente de normalizar en
       el Manifiesto.
   * - Horas predeterminadas
     - La franja que se aplica cuando no hay horario informado.
   * - Aplicar fecha común
     - Al cerrar un Manifiesto, pide una fecha de servicio común para todas sus Órdenes.
   * - Hora de cita única y tolerancia
     - Para carga completa y directos: el cliente da una hora, no una franja. Solo se pide la
       hora de inicio y el fin se construye sumando la tolerancia en minutos.
   * - Secuenciar Viaje
     - Al cerrar un Manifiesto cuyo fichero no trae la secuencia, pide a PTV la
       :term:`secuenciación <Secuenciación>` de las Paradas de cada Viaje antes del cálculo de
       ruta (ver :doc:`/17.0/5_operational-flows/5_2_trip-generation`).
   * - Generar viaje al validar
     - Crea el Viaje al validar la Orden, sin pasar por el asistente.
   * - Crear traslado a hub al asignar
     - Al asignar paradas a una agencia, divide los Tramos y crea la parada intermedia en el
       hub.
   * - Procesar viaje de agencia automáticamente
     - El Viaje que nace al enviar Paradas a una agencia se crea ya en **Procesado**, listo
       para la app, en vez de en borrador.
   * - Autoasignar zona operativa y zona de tarifa más cercanas
     - Si una dirección no cae en ningún área, se le asigna la más cercana, por separado para la
       zona operativa y para la de tarifa. Evita operaciones sin zona, pero anota kilómetros
       extra que afectan al precio.

4.5.5 Aplicación móvil
~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_5_04 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_5_project-configuration_04_app.png
      :alt: Grupo Aplicación móvil del Proyecto

      Aplicación móvil: qué pide la app al conductor en las Paradas del Proyecto.

El grupo **Aplicación móvil** define qué exige la app del conductor en las Paradas de este
Proyecto. Es la palanca para ir de una operativa sencilla a una con validación física intensa
sin cambiar nada más.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Perfil de la aplicación
     - El Perfil de la app (``tms_app.profile``) que reciben las Paradas del Proyecto. Un perfil
       es un nombre, una descripción y la lista de **motivos** que la app ofrece al conductor
       cuando algo no sale bien: motivos de reserva, de fallo, de bulto con problema y de
       reembolso no cobrado. No hay perfiles de serie: se crean en la implantación, en TMS ›
       Configuración › App › Perfiles de la app, y sus motivos en App › Motivos de la app. Un
       Viaje con Paradas de varios Proyectos lleva a la app los perfiles de todos ellos.
   * - POD digital
     - Al entregar, la app pide nombre, documento y firma en pantalla: la :term:`prueba de
       entrega (POD) <POD>` digital.
   * - POD físico
     - Al entregar, la app exige fotografiar el albarán firmado para completar la Parada.
   * - Escaneo Masivo
     - Activa el modo **Encontrar bultos**: con la cámara sobre muchas etiquetas, la app resalta
       las de la Parada.
   * - Escaneo Spark
     - Activa el modo **Comprobación de carga**: la lectura continua de los Bultos esperados en
       la Parada o el Tramo.

La **Lectura individual** de una etiqueta está siempre disponible. Los tres modos de escaneo se
describen en :doc:`/17.0/1_introduction/1_4_technological-architecture`, y su uso paso a paso
en el :doc:`Manual del conductor </17.0/10_manual_app/index>`.

4.5.6 Líneas por defecto
~~~~~~~~~~~~~~~~~~~~~~~~

La pestaña **Líneas por defecto** guarda plantillas de mercancía del Proyecto: Regla de tarifa,
Tipo de bulto, cantidades, peso, dimensiones y descripciones. No son líneas económicas ni
sustituyen a la tarifa. Cuando un fichero o una Orden manual no detallan la mercancía, el
sistema crea las líneas del Tramo a partir de estas plantillas; si no hay ni mercancía
informada ni líneas por defecto, la importación se bloquea. Son la solución natural para
Proyectos con mercancía homogénea y recurrente.

4.5.7 Albarán
~~~~~~~~~~~~~

La pestaña **Albarán** conecta el TMS con el Inventario de Odoo. Con **Crear albarán** activo,
validar una Orden del Proyecto genera un albarán con las líneas de mercancía de la Orden (no
las de venta), resolviendo el producto físico por el código de la Regla de tarifa. Hacen falta
el tipo de albarán y las ubicaciones de origen y destino; si falta alguno, la creación se
bloquea. Solo tiene sentido cuando la operativa mueve inventario real.

4.5.8 Bandeja de entrada API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La pestaña **Bandeja de entrada API**
convierte el Proyecto en la unidad de integración y de seguridad con el sistema del cliente.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Token API
     - Con qué se autentica el sistema externo de este Proyecto. Un token por Proyecto aísla
       las integraciones por cliente, operativa o contrato.
   * - Permisos
     - Qué puede hacer el token: enviar órdenes, consultar el seguimiento, descargar adjuntos.
   * - Límites por minuto y por día
     - La cuota de llamadas.
   * - Enviar por API al asignar y sus puntos de conexión
     - Si al enviar Paradas a una agencia se ejecutan los puntos de conexión de salida
       configurados, y en qué orden.

Lo que llega por el token cae en la :term:`Bandeja de entrada API` del Proyecto, donde se
valida y agrupa en un Manifiesto antes de crear nada (ver
:doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`). La configuración de los canales y de
los contratos está en la :doc:`Guía del integrador </17.0/7_edi-integrations/index>`.

4.5.9 La vista kanban de Proyectos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 4_5_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_5_project-configuration_02_kanban-proyectos.png
      :alt: Vista kanban de Proyectos

      La kanban de Proyectos: cada tarjeta resume un contrato.

El menú de Proyectos abre una vista kanban que resume cada Proyecto en una tarjeta, para leer
el estado de un contrato sin abrir el formulario. Las tarjetas se agrupan en dos columnas según
**Aplicar en**: Proyectos de **Órdenes** y de **Viajes**. Cada tarjeta lleva el nombre, el
cliente o el transportista, la agencia si la hay, la tarifa y el Planning, los indicadores del
periodo y las banderas de configuración.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Indicador
     - Qué muestra
   * - Órdenes abiertas / total
     - En Proyectos de Órdenes: las Órdenes no cerradas ni canceladas sobre el histórico
       completo del Proyecto.
   * - Ingresos de 30 días
     - El importe sin impuestos de las Órdenes creadas en los últimos 30 días.
   * - Viajes abiertos / total
     - En Proyectos de Viajes: los Viajes no completados ni fallidos sobre el total.
   * - Ingresos y coste de 30 días
     - En Proyectos de Viajes: el importe de las Órdenes de compra de los Viajes creados en 30
       días y el coste calculado por el TMS. Pueden diferir mientras la Orden de compra no esté
       cerrada.
   * - Banderas HUB, AUTO y API
     - Los automatismos de 4.5.4 y 4.5.8 que están activos: traslado a hub al asignar, procesar
       Viaje de agencia automáticamente y enviar por API al asignar. Un Proyecto sin banderas
       tiene la configuración mínima.
   * - Última actividad
     - La fecha de la Orden o el Viaje más reciente del Proyecto. Sin ella, el contrato está
       dormido.

Los indicadores se calculan al abrir la vista sobre los datos vivos. Desde la tarjeta se abre
el formulario, cuya cabecera muestra el botón inteligente **Órdenes** o **Viajes** con el
recuento de abiertos sobre el total.
