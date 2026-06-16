5.1 Creación de Orden
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Órdenes (la Orden, ``sale.order``).

La creación de la Orden (``sale.order``) es **donde empieza todo el flujo operativo**:
todo lo demás —tramos, paradas, viajes, ejecución, liquidación y facturación— se
construye a partir de ella. Técnicamente, la Orden es una expedición TMS sobre el pedido
de venta estándar de Odoo (indicador ``is_tms_order``), por lo que reutiliza la
maquinaria comercial del ERP (líneas de venta, facturación, estados administrativos) y le
añade la capa logística del TMS.

Una Orden puede darse de alta de **dos formas**:

- **Manual**, una a una, desde el formulario (ver :ref:`alta-manual`).
- **Masiva**, importando varias órdenes a la vez mediante un **Manifiesto**, ya sea desde
  un fichero o desde una integración (ver :ref:`alta-masiva`).

.. mermaid::

   flowchart LR
       MAN["Alta manual<br/>(formulario)"] --> ORD["Orden<br/>(sale.order)"]
       FILE["Fichero"] --> MF["Manifiesto<br/>(tms.edi.manifest)"]
       API["Integración API"] --> MF
       MF --> ORD
       ORD --> VAL{{"Validar"}}
       VAL --> ST["Paradas<br/>(tms.stop)"]
       ST --> PLAN["Lista para<br/>planificación"]

.. CAPTURA: 5_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_1_order-creation_01_orden-nueva.png
      :alt: Creación de una Orden

      Formulario de creación de una Orden (``sale.order``).

.. _alta-manual:

5.1.1 Alta manual
~~~~~~~~~~~~~~~~~~

El alta manual es el camino habitual para registrar una expedición puntual. Los pasos son:

#. **Nuevo.** Desde la lista de Órdenes, pulsar **Nuevo** para abrir una orden en blanco.
#. **Cliente.** Seleccionar el cliente. Si el cliente tiene **un único proyecto**
   asociado, el sistema lo **precarga automáticamente**; si tiene varios, el usuario
   **elige** entre los proyectos disponibles. Al fijar el Proyecto (``project.project``),
   se **recargan los parámetros y las validaciones** que regirán la orden (tarifa, tipos
   de servicio/orden permitidos, agencia, hub, planning, etc.), definidos en el Proyecto
   (ver :doc:`/17.0/4_parametrization/4_5_project-configuration`). Por eso una orden sin un
   proyecto bien parametrizado no puede avanzar con fiabilidad.
#. **Guardar** la orden.
#. **Generar los Tramos.** Añadir el Tramo (``tms.shipment.leg``) —o los que haga falta
   según el **tipo de orden**— que describen los movimientos logísticos (origen y
   destino).
#. **Completar cada Tramo** con:

   - las **líneas** de mercancía/facturación (qué se transporta y cómo se valora),
   - los **reembolsos** asociados, si los hay,
   - y la **información operativa**: dónde y cuándo se carga y se descarga, ventanas
     horarias, contactos, etc.

#. **Validar.** Pulsar el botón **Validar** —**paso obligatorio**—. La validación hace
   **dos cosas**: comprueba que la orden está completa y **genera automáticamente las
   Paradas** (``tms.stop``) a partir de los tramos. El detalle se describe en
   :ref:`validacion-orden`.

.. CAPTURA: 5_1_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_1_order-creation_02_validar.png
      :alt: Botón Validar de la orden

      Botón **Validar** de la orden: valida y genera las Paradas.

Tras validar, la orden queda **lista para planificación**.

.. _alta-masiva:

5.1.2 Alta masiva por manifiesto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando la demanda llega en volumen, las órdenes no se teclean una a una: se importan
mediante un **Manifiesto** (``tms.edi.manifest``), que agrupa los datos recibidos, los
valida y los materializa en Órdenes. Hay dos orígenes:

- **Por fichero.** El operador crea un Manifiesto, selecciona el **cliente** y el campo
  **Fichero EDI** (``tms.edi.file``, que define cómo se interpretan las columnas del
  fichero), pulsa importar y elige el **fichero** (XLSX/CSV). También es posible crear
  Manifiestos **no vinculados a un cliente**: en ese caso se deja el cliente vacío y se
  selecciona únicamente el **Fichero EDI**.
- **Por integración.** Los datos entran por API REST y se depositan en la **Bandeja de
  Entrada API** (``tms_int.api.inbox``), desde la que se agrupan en un Manifiesto (ver
  :doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`).

El procesamiento del Manifiesto no es instantáneo: al importar, el fichero entra en una
**cola** que el sistema procesa periódicamente, y al final el Manifiesto debe **cerrarse**
para materializar las Órdenes. El cierre se bloquea si quedan direcciones (contactos de
carga/descarga) **sin normalizar**. Todo este funcionamiento —colas, botones de la
pantalla del Manifiesto y criterios de normalización— se detalla en
:doc:`/17.0/3_functional-architecture/3_2_3_manifests`; los contratos de integración, en
el :doc:`capítulo 7 </17.0/7_edi-integrations/index>`.

.. _validacion-orden:

5.1.3 Validación de Orden y generación de Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La validación es el paso que **transforma una orden introducida en una estructura
operativa lista para planificar**. Se lanza con el botón **Validar** y, antes de generar
nada, comprueba que la orden está completa:

- que tenga tramos y, cuando el flujo lo requiera, líneas de mercancía;
- que los tramos tengan **origen y destino** informados;
- que existan **fechas y ventanas horarias** operativas;
- que no queden **contactos pendientes de normalizar** (una dirección incompleta o de
  baja calidad afecta a la geocodificación, la planificación y la ejecución).

Superadas las comprobaciones, la validación **genera automáticamente las Paradas**
(``tms.stop``): agrupa los tramos por criterios compatibles (ubicación, fecha, ventana
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

   Aunque el usuario vea una "Orden TMS", el registro principal es una orden de venta
   estándar de Odoo (``sale.order``). Por eso la confirmación, la facturación y el estado
   administrativo usan los mecanismos estándar del ERP.
