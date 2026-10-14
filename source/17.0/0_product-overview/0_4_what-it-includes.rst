Qué incluye
-----------

Guraify TMS se entrega como un conjunto de módulos de Odoo que se instalan juntos o por
partes. Para quien lo usa son áreas de una misma aplicación; para quien lo implanta, módulos
con nombre propio. Aquí van las áreas; al final se indica dónde está la relación de módulos.

Gestión de órdenes y ejecución
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El núcleo: Órdenes, Tramos, Paradas y Viajes, con sus estados, su bloqueo al cerrar y sus
indicadores. Incluye los Manifiestos para las cargas masivas y los automatismos descritos en
:doc:`Cómo funciona <0_3_how-it-works>`: normalización de direcciones, trazabilidad y
documentos de transporte.

.. figure:: /_static/img/3_functional-architecture/3_2_1_orders_01_orden.png
   :alt: Formulario de una Orden en Guraify TMS

   Una Orden con su Tramo, sus datos económicos y sus indicadores de estado.

Planificación y optimización
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un plan de disponibilidad de conductores en formato calendario, un optimizador de Paradas con
mapa que agrupa y secuencia Paradas en Viajes, y el cálculo de ruta, distancias y horas de
llegada con el motor cartográfico de PTV. Se puede planificar a mano, con ayuda del mapa, o
dejar que el optimizador proponga y ajustar después. Sin contrato PTV el mapa funciona sobre
OpenStreetMap y la planificación es manual.

.. figure:: /_static/img/3_functional-architecture/3_3_planning-model_01_optimizador.png
   :alt: Optimizador de Paradas con mapa

   El Optimizador de Paradas: los Viajes a la izquierda, el mapa en el centro y las Paradas
   pendientes a la derecha.

Tarificación, liquidación y facturación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tarifas por cliente y por transportista con zonas, rangos, tipos de servicio y de vehículo;
diagnóstico de tarifa para ver por qué una Orden vale lo que vale; orden de compra automática
al transportista al cerrar el Viaje; reparto del coste del Viaje entre las Órdenes que lleva;
y facturación al cliente con la contabilidad de Odoo.

App del conductor
~~~~~~~~~~~~~~~~~

Aplicación para Android e iPhone con la que el conductor ejecuta el Viaje: Paradas ordenadas,
navegación, escaneo de Bultos con la cámara, prueba de entrega (POD) con firma o foto,
reembolsos e incidencias. Funciona con cobertura intermitente y lleva la marca de la empresa.
Tiene :doc:`su propia página <0_5_driver-app>` y su propio manual.

Integraciones
~~~~~~~~~~~~~

Entrada de Órdenes por fichero (Excel o CSV, con plantillas por cliente), por API y por avisos
automáticos entre sistemas (webhooks); salida de estados, POD y documentos hacia los sistemas
de los clientes; y registro de toda la actividad de integración. Tiene :doc:`su propia página
<0_6_integrations>` y una guía técnica.

Tableros e indicadores
~~~~~~~~~~~~~~~~~~~~~~

Tres tableros sobre los datos reales del sistema: operación (volumen, rentabilidad y
puntualidad por cliente, Planning y conductor), Paradas (reparto, recogidas y movimientos de
Hub) y facturación pendiente, con filtros de periodo y, en los dos primeros, de Planning,
cliente y transportista. Además, indicadores configurables desde el propio Odoo, sin
desarrollar pantallas nuevas.

.. figure:: /_static/img/0_product-overview/0_4_what-it-includes_01_tablero.png
   :alt: Tablero de operaciones de Guraify TMS

   Tablero de operaciones: volumen, puntualidad y estado de las Paradas del día.

Gestión de recursos
~~~~~~~~~~~~~~~~~~~

Kilometraje único por vehículo, venga de la app, del taller o de una importación, con
detección de lecturas anómalas; y mantenimiento preventivo de flota por kilómetros y por
tiempo, con sus órdenes de trabajo, sus etapas y su calendario, sobre el módulo de
mantenimiento de Odoo.

Documento de control (DeCA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

El documento electrónico de control administrativo que exige el transporte de mercancías por
carretera en España desde octubre de 2026, emitido por el propio TMS a partir de lo que el Tramo
y el Viaje ya saben: se decide qué envíos están obligados y cuáles exentos, se emite al despachar
el Viaje como PDF con un código QR que el inspector descarga sin credenciales, se envía al
transportista o al cliente, y se conserva cada versión el tiempo que la norma manda.

Avisos al Destinatario
~~~~~~~~~~~~~~~~~~~~~~

Mensajes automáticos por correo, SMS o WhatsApp a quien recibe una entrega, en los momentos que
el cliente elija: cuando se planifica, el día anterior, cuando es la siguiente Parada, cuando se
entrega o falla. Se configuran sin programar, respetan el consentimiento y el horario de silencio
de cada Destinatario, y cada aviso queda registrado en su Orden. Los SMS pueden salir por
Esendex; WhatsApp necesita Odoo Enterprise y una cuenta de Meta.

Marca blanca y multiempresa
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La app del conductor lleva el logotipo y los colores de cada compañía, configurados en Odoo; el
DeCA lleva su logotipo y los avisos al Destinatario, su nombre de remitente. Varias empresas
pueden convivir en la misma instalación con sus datos separados, lo que permite a un
distribuidor operar varios clientes o a un grupo tener varias marcas.

Entorno de demostración
~~~~~~~~~~~~~~~~~~~~~~~

Configuración operativa completa y datos maestros inventados (clientes, transportistas,
conductores, flota, direcciones) instalables en minutos, para enseñar el producto o arrancar
un piloto sin partir de cero.

Áreas y módulos
~~~~~~~~~~~~~~~

Cada área de esta página corresponde a uno o varios módulos de Odoo que se instalan según lo que
el cliente contrate. La relación de módulos, para quien instala, está en el Manual de implantación:
:ref:`17.0/1_introduction/1_4_technological-architecture:1.4.1 Plataforma base Odoo`.
