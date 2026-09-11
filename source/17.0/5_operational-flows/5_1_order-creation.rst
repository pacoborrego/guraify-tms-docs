5.1 Creación de Orden
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Órdenes · TMS › Operaciones › Tráfico › Manifiestos

La creación de la Orden (``sale.order``) es donde empieza todo el flujo operativo: Tramos,
Paradas, Viajes, ejecución, tarificación y facturación se construyen a partir de ella. La Orden
es una extensión del pedido de venta estándar de Odoo, así que reutiliza la maquinaria
comercial del ERP (líneas de venta, confirmación, facturación) y le añade la capa logística del
TMS. Puede darse de alta de dos formas: **a mano**, una a una, desde el formulario, o **en
masa**, importando varias a la vez mediante un :term:`Manifiesto`, ya sea desde un fichero o
desde una integración API.

.. mermaid::

   flowchart LR
       MAN["Alta manual<br/>(formulario)"] --> ORD["Orden"]
       FILE["Fichero"] --> MF["Manifiesto"]
       API["Integración API"] --> MF
       MF -->|cerrar| ORD

.. CAPTURA: 5_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_1_order-creation_01_orden-nueva.png
      :alt: Creación de una Orden

      Formulario de creación de una Orden.

5.1.1 Alta manual
~~~~~~~~~~~~~~~~~

El alta manual es el camino habitual para registrar una Orden puntual. Los pasos son:

#. **Nuevo.** Desde la lista de Órdenes, pulsar **Nuevo** para abrir una Orden en blanco.
#. **Cliente y Proyecto.** Seleccionar el cliente. Si tiene un único :term:`Proyecto`, el
   sistema lo precarga; si tiene varios, el usuario elige. Al fijar el Proyecto se cargan los
   parámetros y las validaciones que regirán la Orden: tarifa, Tipos de Servicio y de Orden
   admitidos, agencia, hub, Planning (ver
   :doc:`/17.0/4_parametrization/4_5_project-configuration`). Una Orden sin un Proyecto bien
   parametrizado no puede avanzar con fiabilidad.
#. **Guardar** la Orden.
#. **Añadir los Tramos.** Con **Nuevo Tramo** se añade cada movimiento logístico, con su punto
   de carga y su punto de descarga. El Tipo de Orden no crea los Tramos: propone qué lado es
   el del cliente y cuál el del hub o la agencia del Proyecto, y decide cómo se interpretarán
   al validar (ver :doc:`/17.0/4_parametrization/4_1_operational-configuration`). Una Orden
   puerta a puerta tiene un Tramo; una con paso por hub, dos o más.
#. **Completar cada Tramo** con las líneas de mercancía (qué se transporta y cómo se mide), los
   Reembolsos, si los hay, y la información operativa: dónde y cuándo se carga y se descarga,
   franjas horarias y contactos.
#. **Validar.** Pulsar **Validar**, paso obligatorio. La validación comprueba que la Orden está
   completa y genera las Paradas a partir de los Tramos (ver 5.1.3).

.. CAPTURA: 5_1_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_1_order-creation_02_validar.png
      :alt: Botón Validar de la Orden

      Botón **Validar** de la Orden: valida y genera las Paradas.

Tras validar, la Orden queda lista para planificar.

5.1.2 Alta masiva por Manifiesto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando la demanda llega en volumen, las Órdenes no se teclean una a una: se importan mediante
un :term:`Manifiesto`, que agrupa los datos recibidos, los revisa y los convierte en Órdenes
con sus Tramos y Paradas. El camino, cuando los datos vienen en un fichero, es:

#. **Crear el Manifiesto** desde TMS › Operaciones › Tráfico › Manifiestos, indicando el
   cliente y la :term:`Definición de fichero` que dice cómo leer sus columnas. Un Manifiesto
   puede no tener cliente, solo Definición de fichero.
#. **Importar el fichero** con el botón **Importar fichero**: se elige el XLSX o CSV y
   se pulsa **Validar e importar**. El contenido entra en la cola de importación, que el
   sistema procesa periódicamente, o antes con **Importar Fichero Ahora**. Al terminar, el
   Manifiesto contiene una Orden por cada fila del fichero, todavía sin Paradas.
#. **Revisar y normalizar.** El botón inteligente **Normalizar** indica cuántas direcciones de
   carga o descarga no tienen una coordenada fiable o les falta el horario. Hay que corregirlas
   desde ahí: el Manifiesto no se cierra mientras quede alguna.
#. **Cerrar el Manifiesto** con **Cerrar Manifiesto** (o **Cerrar Manifiesto Ahora** para no
   esperar a la cola). El cierre valida cada Orden, genera sus Paradas y, si el fichero traía
   la asignación a Viajes, crea también los Viajes (ver :doc:`5_2_trip-generation`).

Cuando los datos llegan por API, el sistema del cliente los deposita en la
:term:`Bandeja de entrada API`, que los valida y los agrupa en un Manifiesto; a partir de ahí
el camino es el mismo desde la revisión y la normalización. Los estados del Manifiesto, sus
botones, la cola y los criterios exactos de normalización están en
:doc:`/17.0/3_functional-architecture/3_2_3_manifests`; la Bandeja, en
:doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`; y la configuración de los canales de
entrada, en la :doc:`Guía del integrador </17.0/7_edi-integrations/index>`.

5.1.3 Validación de la Orden y generación de Paradas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La validación transforma una Orden introducida en una estructura operativa lista para
planificar. Se lanza con el botón **Validar** y, antes de generar nada, comprueba que la Orden
está completa: que tenga Tramos y, cuando el flujo lo requiera, líneas de mercancía; que los
Tramos tengan origen y destino; que existan fechas y franjas horarias; y que no queden
contactos pendientes de normalizar.

Superadas las comprobaciones, la validación genera las Paradas. Recorre los Tramos, agrupa en
una misma Parada los que coinciden en tipo de evento, contacto, franja horaria, Planning y
Proyecto (y en nombre de viaje, si el fichero lo trae), y asigna a cada Parada su Tipo de Parada
según el Tipo de Orden y el lado del Tramo. El criterio exacto de agrupación y los tipos que
resultan están en :doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`. Además de crear
las Paradas, la validación recalcula el estado de la Orden y de sus Tramos, lanza la
tarificación de venta (y la de compra, si la Orden ya está en un Viaje), ajusta las operaciones
de hub de los Viajes afectados, genera el albarán si el Proyecto lo pide y deja un registro de
validación con los avisos e incidencias detectados.

Validar no es confirmar la Orden. La validación prepara la operación para ejecutarla; la
confirmación (el paso a *Pedido de venta*, el estado nativo de Odoo) llega con el cierre del
Viaje y la tarificación, como se cuenta en :doc:`5_5_trip-closing`.
