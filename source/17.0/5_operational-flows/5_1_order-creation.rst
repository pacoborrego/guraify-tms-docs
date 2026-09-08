5.1 Creación de Orden
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Órdenes

La creación de la Orden (``sale.order``) es **donde empieza todo el flujo operativo**:
todo lo demás —tramos, paradas, viajes, ejecución, liquidación y facturación— se
construye a partir de ella. La Orden es una extensión del pedido de venta estándar de
Odoo, por lo que reutiliza la maquinaria comercial del ERP (líneas de venta, facturación,
estado del pedido) y le añade la capa logística del TMS.

Una Orden puede darse de alta de **dos formas**:

- **Manual**, una a una, desde el formulario (ver :ref:`alta-manual`).
- **Masiva**, importando varias órdenes a la vez mediante un **Manifiesto**, ya sea desde
  un fichero o desde una integración (ver :ref:`alta-masiva`).

.. mermaid::

   flowchart LR
       MAN["Alta manual<br/>(formulario)"] --> ORD["Orden"]
       FILE["Fichero"] --> MF["Manifiesto"]
       API["Integración API"] --> MF
       MF --> ORD
       ORD --> VAL{{"Validar"}}
       VAL --> ST["Paradas"]
       ST --> PLAN["Lista para<br/>planificación"]

.. CAPTURA: 5_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_1_order-creation_01_orden-nueva.png
      :alt: Creación de una Orden

      Formulario de creación de una Orden.

.. _alta-manual:

5.1.1 Alta manual
~~~~~~~~~~~~~~~~~

El alta manual es el camino habitual para registrar una orden puntual. Los pasos son:

#. **Nuevo.** Desde la lista de Órdenes, pulsar **Nuevo** para abrir una orden en blanco.
#. **Cliente.** Seleccionar el cliente. Si el cliente tiene **un único proyecto**
   asociado, el sistema lo **precarga automáticamente**; si tiene varios, el usuario
   **elige** entre los proyectos disponibles. Al fijar el :term:`Proyecto`, se **recargan los parámetros y las validaciones** que regirán la orden (tarifa, tipos
   de servicio/orden permitidos, agencia, hub, planning, etc.), definidos en el Proyecto
   (ver :doc:`/17.0/4_parametrization/4_5_project-configuration`). Por eso una orden sin un
   proyecto bien parametrizado no puede avanzar con fiabilidad.
#. **Guardar** la orden.
#. **Generar los Tramos.** Con **Nuevo Tramo**, añadir el Tramo, o los que haga falta según
   el **tipo de orden**, que describen los movimientos logísticos (origen y
   destino).
#. **Completar cada Tramo** con:

   - las **líneas** de mercancía/facturación (qué se transporta y cómo se valora),
   - los **reembolsos** asociados, si los hay,
   - y la **información operativa**: dónde y cuándo se carga y se descarga, ventanas
     horarias, contactos, etc.

#. **Validar.** Pulsar el botón **Validar**, **paso obligatorio**. La validación hace
   **dos cosas**: comprueba que la orden está completa y **genera automáticamente las
   Paradas** a partir de los tramos. El detalle se describe en
   :ref:`validacion-orden`.

.. CAPTURA: 5_1_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_1_order-creation_02_validar.png
      :alt: Botón Validar de la orden

      Botón **Validar** de la orden: valida y genera las Paradas.

Tras validar, la orden queda **lista para planificación**.

.. _alta-masiva:

5.1.2 Alta masiva por manifiesto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando la demanda llega en volumen, las órdenes no se teclean una a una: se importan
mediante un :term:`Manifiesto`, que agrupa los datos recibidos, los revisa y los convierte en
Órdenes con sus Tramos y Paradas. El camino, cuando los datos vienen en un fichero, es:

#. **Crear el Manifiesto** desde TMS › Operaciones › Tráfico › Manifiestos, indicando el
   **cliente** y la :term:`Definición de fichero` que dice cómo leer sus columnas. Un
   Manifiesto puede no tener cliente, sólo Definición de fichero.
#. **Importar el fichero** con el botón **Fichero de Importación**: se elige el XLSX o CSV y
   se pulsa **Validar e importar**. El contenido entra en una cola que el sistema procesa cada
   cinco minutos, o antes con **Importar Fichero Ahora**. Al terminar, el Manifiesto contiene
   una Orden por cada envío del fichero, todavía sin Paradas.
#. **Revisar y normalizar.** El botón inteligente **Normalizar** indica cuántas direcciones de
   carga o descarga no tienen una coordenada fiable o les falta el horario. Hay que
   corregirlas desde ahí: el Manifiesto no se cierra mientras quede alguna.
#. **Cerrar el Manifiesto** con **Cerrar Manifiesto** (o **Cerrar Manifiesto Ahora** para no
   esperar a la cola). El cierre valida cada Orden, genera sus Paradas y, si el fichero traía la
   asignación a viajes, crea también los Viajes (ver
   :doc:`5_2_trip-generation`).

Cuando los datos llegan por API, el sistema del cliente los deposita en la
:term:`Bandeja de entrada API`, que los valida y los agrupa en un Manifiesto; a partir de ahí
el camino es el mismo desde el paso 3. Los estados del Manifiesto, sus botones y los criterios
exactos de normalización están en :doc:`/17.0/3_functional-architecture/3_2_3_manifests`; la
Bandeja, en :doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`; y la configuración de los
canales de entrada, en la :doc:`Guía del integrador </17.0/7_edi-integrations/index>`.

.. _validacion-orden:

5.1.3 Validación de Orden y generación de Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La validación es el paso que **transforma una orden introducida en una estructura
operativa lista para planificar**. Se lanza con el botón **Validar** y, antes de generar
nada, comprueba que la orden está completa:

- que tenga tramos y, cuando el flujo lo requiera, líneas de mercancía;
- que los tramos tengan **origen y destino** informados;
- que existan **fechas y ventanas horarias** operativas;
- que no queden **contactos pendientes de normalizar** (una dirección incompleta o de
  baja calidad afecta a la geocodificación, la planificación y la ejecución).

Superadas las comprobaciones, la validación **genera automáticamente las Paradas**: agrupa los tramos por criterios compatibles (ubicación, fecha, ventana
horaria, planning y, si viene informado, nombre de viaje) para **evitar paradas
duplicadas**, y asigna a cada una su **Tipo de Parada** (recogida, entrega, hub, directo,
recogida a domicilio…), que determina si la parada es planificable, si aparece en la app
y si participa en la optimización. Además, completa información derivada del proyecto
(p. ej. la carga desde hub en entregas) y recalcula la parte económica cuando procede.

.. list-table:: Qué hace la validación
   :header-rows: 1
   :widths: 32 68

   * - Acción
     - Resultado
   * - Generación de Paradas
     - Crea la estructura operativa ejecutable a partir de los tramos.
   * - Actualización de estados
     - Recalcula la situación logística de la orden y sus tramos.
   * - Recálculo económico
     - Actualiza la tarifa de venta (y de viaje) cuando aplica.
   * - Sincronización de hub
     - Ajusta las operaciones de hub en los viajes afectados.
   * - Inventario
     - Genera movimientos de stock si el proyecto lo requiere.
   * - Log de validación
     - Devuelve avisos, incidencias o errores detectados.

.. note::

   Validar **no** es cerrar administrativamente la orden: la validación prepara la
   operación para su ejecución logística; la confirmación administrativa y el cierre
   económico dependen del estado operativo posterior y del flujo de facturación.

.. note::

   Aunque el usuario vea una "Orden TMS", el registro principal es un pedido de venta
   estándar de Odoo. Por eso la confirmación, la facturación y el estado del pedido usan los
   mecanismos estándar del ERP.
