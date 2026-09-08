Qué incluye
-----------

Guraify TMS se entrega como un conjunto de módulos de Odoo que se instalan juntos o por
partes. Para quien lo usa son áreas de una misma aplicación; para quien lo implanta, módulos
con nombre propio. Aquí van las áreas; la tabla del final las cruza con los módulos.

Gestión de órdenes y ejecución
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El núcleo: órdenes, tramos, paradas y viajes, con sus estados, su bloqueo al cerrar y sus
indicadores. Incluye los manifiestos para las cargas masivas, la normalización de direcciones,
la trazabilidad completa y los documentos de transporte: etiquetas de bulto, manifiesto de
transporte y detalle de la orden y del viaje.

.. figure:: /_static/img/3_functional-architecture/3_2_1_orders_01_orden.png
   :alt: Formulario de una Orden en Guraify TMS

   Una Orden con su tramo, sus datos económicos y sus indicadores de estado.

Planificación y optimización
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un plan de disponibilidad de conductores en formato calendario, un optimizador de paradas con
mapa que agrupa y secuencia paradas en viajes, y el cálculo de rutas, distancias y horas de
llegada con el motor cartográfico de PTV. Se puede planificar a mano, con ayuda del mapa, o
dejar que el optimizador proponga y ajustar después. Sin contrato PTV el mapa funciona sobre
OpenStreetMap y la planificación es manual.

.. figure:: /_static/img/3_functional-architecture/3_3_planning-model_01_optimizador.png
   :alt: Optimizador de Paradas con mapa

   El Optimizador de Paradas: paradas pendientes a la izquierda, viajes propuestos en el mapa.

Tarificación, liquidación y facturación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tarifas por cliente y por transportista con zonas, rangos, tipos de servicio y de vehículo;
diagnóstico de tarifa para ver por qué una orden vale lo que vale; orden de compra automática
al transportista al cerrar el viaje; reparto del coste del viaje entre las órdenes que lleva;
y facturación al cliente con la contabilidad de Odoo. El margen queda calculado sin trabajo
adicional.

App del conductor
~~~~~~~~~~~~~~~~~

Aplicación para Android e iPhone con la que el conductor ejecuta el viaje: paradas ordenadas,
navegación, escaneo de bultos con la cámara, prueba de entrega con firma o foto, reembolsos,
incidencias y notificaciones. Funciona con cobertura intermitente y lleva la marca de la
empresa. Tiene :doc:`su propia página <0_5_driver-app>` y su propio manual.

Integraciones
~~~~~~~~~~~~~

Entrada de órdenes por fichero (Excel o CSV, con plantillas por cliente), por API y por
webhooks; salida de estados, prueba de entrega y documentos hacia los sistemas de los
clientes; registro de toda la actividad de integración; y un portal donde el cliente ve lo
que ha enviado y lo que ha fallado. Tiene :doc:`su propia página <0_6_integrations>` y una
guía técnica.

Tableros e indicadores
~~~~~~~~~~~~~~~~~~~~~~

Tableros de operación, de paradas y de facturación pendiente sobre los datos reales del
sistema, con filtros de periodo que incluyen hoy y los próximos días; e indicadores
configurables desde el propio Odoo, sin programar, para el backoffice y para el portal.

.. CAPTURA: 0_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/0_product-overview/0_4_what-it-includes_01_tablero.png
      :alt: Tablero de operaciones de Guraify TMS

      Tablero de operaciones: volumen, puntualidad y estado de las paradas del día.

Gestión de recursos
~~~~~~~~~~~~~~~~~~~

Kilometraje único por vehículo, venga de la app, del taller o de una importación, con
detección de lecturas anómalas; y mantenimiento preventivo de flota por kilómetros y por
tiempo, con órdenes de trabajo, etapas y calendario sobre el módulo de mantenimiento de Odoo.

Marca blanca y multiempresa
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La app del conductor y las comunicaciones llevan el logotipo, los colores y la tipografía de
cada compañía, configurados en Odoo. Varias empresas pueden convivir en la misma instalación
con sus datos separados, lo que permite a un distribuidor operar varios clientes o a un grupo
tener varias marcas.

Entorno de demostración
~~~~~~~~~~~~~~~~~~~~~~~

Configuración operativa completa y datos maestros inventados (clientes, transportistas,
conductores, flota, direcciones) instalables en minutos, para enseñar el producto o arrancar
un piloto sin partir de cero.

Áreas y módulos
~~~~~~~~~~~~~~~

Para el distribuidor o el técnico que instala:

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - Área
     - Módulos
     - Notas
   * - Gestión de órdenes y ejecución
     - ``tms``
     - Núcleo. Requiere Ventas, Compras, Contabilidad, Flota, Proyectos, Planificación e
       Inventario de Odoo
   * - Planificación y optimización
     - ``tms``, ``tms_map``
     - Motor PTV opcional
   * - Tarificación y facturación
     - ``tms``
     - Sobre la facturación de Odoo
   * - App del conductor
     - ``tms_app``, ``tms_branding``
     - Más la app móvil, distribuida aparte
   * - Integraciones
     - ``tms_int``, ``tms_portal``
     - Más el gateway de API para sistemas externos
   * - Tableros e indicadores
     - ``tms_dashboard``, ``tms_dashboard_filters``, ``tms_kpi``
     - Sobre los tableros de hoja de cálculo de Odoo
   * - Gestión de recursos
     - ``tms_resources``, ``tms_maintenance``
     - Sobre Flota y Mantenimiento de Odoo
   * - Entorno de demostración
     - ``tms_demo_config``, ``tms_demo_master``
     - Sólo para demos y pilotos
