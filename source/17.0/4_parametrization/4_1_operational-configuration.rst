Configuración Operativa Inicial
-------------------------------

La configuración operativa inicial define las tipologías básicas que estructuran la actividad del sistema. Estas tipologías permiten clasificar los distintos tipos de servicios, órdenes, paradas y participantes que intervienen en la operativa logística.

Aunque conceptualmente son simples catálogos, su impacto es significativo porque muchos procesos automáticos del sistema utilizan estas clasificaciones como criterios de filtrado, segmentación o aplicación de reglas.

Las tipologías definidas en esta sección se utilizan posteriormente en:

• reglas de tarifa

• filtros de planificación

• segmentación operativa

• validaciones de compatibilidad

• lógica de creación de órdenes

Dentro de este bloque se configuran los siguientes elementos.

Todos estos catálogos son accesibles desde el panel **Configuración → Ajustes**, sección "Datos auxiliares", que actúa como punto de entrada único a las tablas de configuración operativa.

.. image:: /_static/images/Config_Datos_Auxiliares_Index.png
   :align: center

.. note::

   Cada enlace de la sección "Datos auxiliares" abre la lista del catálogo correspondiente. Desde la lista pueden crearse, modificarse y eliminarse registros, así como inspeccionar el detalle de cada tipo.

Tipos de Servicio
~~~~~~~~~~~~~~~~~

Los Tipos de Servicio constituyen uno de los primeros elementos de configuración operativa del sistema.

Su objetivo es clasificar la naturaleza de los servicios de transporte gestionados dentro del TMS y establecer la relación entre la operativa logística y los conceptos económicos que se utilizarán posteriormente en la facturación.

En la práctica, el tipo de servicio permite identificar el modelo de transporte aplicado a una expedición.

Esta clasificación facilita la gestión de diferentes operativas dentro de una misma organización, como por ejemplo:

- Carga completa
- Grupaje
- Distribución urbana
- Same day
- Entregas con compromiso horario

La vista de lista permite revisar de un vistazo todos los tipos de servicio configurados, junto con los productos asociados, los tipos de expedición compatibles y las variables logísticas activas para cada uno.

.. image:: /_static/images/Config_Tipo_Servicio_Lista.png
   :align: center

La selección del tipo de servicio durante la creación de una orden no solo cumple una función descriptiva.

También determina qué productos del catálogo de Odoo se utilizarán posteriormente para registrar los ingresos asociados a la operación.

De este modo, el tipo de servicio actúa como un elemento de conexión entre:

- La estructura operativa de la orden
- Las variables logísticas que intervienen en el transporte
- La generación automática de conceptos económicos

Gracias a esta relación, el sistema puede traducir la información operativa del transporte en registros económicos sin necesidad de introducir datos adicionales durante el proceso de facturación.

Campos principales de Tipos de Servicio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La vista de formulario de un Tipo de Servicio agrupa todos sus campos en una única pantalla, incluyendo los switches que controlan qué variables logísticas (bultos, cantidad, metros, pallets) intervienen en el cálculo económico.

.. image:: /_static/images/Config_Tipo_Servicio_Form.png
   :align: center

El modelo de Tipos de Servicio incluye los siguientes campos funcionales.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Identificador del tipo de servicio dentro del sistema. Permite reconocer la naturaleza operativa del transporte.
   * - Secuencia
     - Orden de visualización utilizado para organizar los servicios en las interfaces del sistema.
   * - Descripción económica
     - Texto utilizado como concepto económico cuando el servicio genera líneas de facturación.
   * - Productos asociados
     - Productos del catálogo de Odoo que se utilizarán para registrar los ingresos generados por el servicio.
   * - Tipos de expedición
     - Define qué tipos de expedición pueden utilizar este servicio.
   * - Bultos
     - Indica si el número de bultos puede intervenir en el cálculo económico del servicio.
   * - Cantidad
     - Permite utilizar la cantidad de unidades como variable logística relevante.
   * - Metros
     - Indica si los metros lineales deben considerarse en la valoración del servicio.
   * - Pallets
     - Permite utilizar el número de pallets como dimensión logística.
   * - Información adicional
     - Campo descriptivo utilizado para documentar características del servicio.
   * - Compañía
     - Permite definir configuraciones específicas en entornos multiempresa.
   * - Color
     - Identificador visual utilizado en algunas interfaces de planificación.

.. _section-25:

Contexto operativo del servicio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los tipos de servicio intervienen en diferentes procesos del TMS.

Durante la creación de órdenes, el tipo de servicio define la naturaleza operativa de la expedición y determina qué variables logísticas pueden utilizarse posteriormente en las reglas de cálculo económico.

Durante el proceso de tarificación, el servicio actúa como uno de los criterios utilizados para seleccionar las reglas de tarifa aplicables.

Finalmente, en el proceso de facturación, los productos asociados al servicio permiten generar automáticamente las líneas económicas correspondientes dentro del sistema ERP.

Este diseño permite mantener alineadas las tres dimensiones principales del sistema:

- operativa logística

- planificación de transporte

- gestión económica

.. note::

   La correcta definición de los tipos de servicio es fundamental para garantizar que el cálculo de tarifas y la generación de ingresos reflejen correctamente la operativa real del transporte.


Tipos de Orden
~~~~~~~~~~~~~~

Los Tipos de Orden definen la naturaleza operativa de una expedición dentro del sistema.

Mientras que los Tipos de Servicio clasifican la dimensión comercial del transporte, los Tipos de Orden describen el comportamiento logístico que tendrá la orden dentro del flujo operativo del TMS.

En otras palabras, el tipo de orden determina cómo se comporta una expedición dentro de la red logística.

Esta clasificación permite diferenciar distintos escenarios operativos, como por ejemplo:

- Recogidas en origen
- Entregas a destinatario
- Operaciones entre hubs
- Servicios directos
- Movimientos internos dentro de la red

La vista de lista resume el conjunto de tipos disponibles. Las columnas booleanas (Entrega, Recogida, Directo, Hub, Punto de Recogida Habitual) y los porcentajes de carga/descarga muestran de forma compacta el comportamiento logístico de cada tipo.

.. image:: /_static/images/Config_Tipo_Orden_Lista.png
   :align: center

La definición del tipo de orden influye directamente en la forma en que el sistema genera la estructura logística de la expedición, especialmente en lo relativo a la creación de tramos y paradas.

Por este motivo, los Tipos de Orden forman parte de los elementos estructurales del modelo operativo del TMS.

Campos principales de Tipos de Orden
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El modelo de Tipos de Orden incluye los siguientes campos funcionales.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Identificador del tipo de orden dentro del sistema.
   * - Secuencia
     - Orden de visualización utilizado para organizar los tipos de orden.
   * - Descripción
     - Texto descriptivo del comportamiento funcional.
   * - Compañía
     - Configuración específica en entornos multiempresa.
   * - Color
     - Identificador visual para facilitar su reconocimiento.

Papel dentro del modelo operativo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los Tipos de Orden intervienen principalmente durante el proceso de creación y estructuración de una orden de transporte.

Cuando se registra una nueva expedición, el tipo de orden seleccionado indica al sistema qué lógica operativa debe aplicarse para generar la estructura logística correspondiente.

Esta lógica puede afectar a:

- La creación automática de tramos
- La generación de paradas de recogida y entrega
- La clasificación de la operación dentro de la red logística

Gracias a esta configuración, el sistema puede adaptar su comportamiento a distintos modelos operativos sin modificar la lógica interna del módulo.

Por ejemplo, una empresa puede gestionar simultáneamente:

- Servicios directos entre origen y destino
- Operativas hub-and-spoke
- Redes de distribución urbana

Relación con otros elementos del sistema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los Tipos de Orden interactúan con varios componentes clave del modelo operativo del TMS.

Se utilizan durante la creación de órdenes de transporte, donde determinan el comportamiento logístico de la expedición.

Posteriormente, esta información se utiliza durante la generación de tramos y paradas, que constituyen la estructura operativa utilizada por planificación.

Además, el tipo de orden puede utilizarse como criterio en:

- Reglas de planificación
- Reglas de tarifa
- Validaciones operativas

.. note::

   El tipo de orden determina cómo se estructura una expedición
   en términos de tramos y paradas.
   Una configuración incorrecta impactará directamente
   en la representación logística del flujo operativo.



Tipos de Parada
~~~~~~~~~~~~~~~

Contexto funcional de Tipos de Parada
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los Tipos de Parada constituyen uno de los pilares de la modelización operativa dentro de Guraify TMS.

Mientras que el tipo de orden define la naturaleza del encargo, el tipo de parada determina cómo se materializa dicho encargo en el plano físico y planificable.

En el modelo del sistema, la parada es la unidad mínima sobre la que operan planificación, ejecución y trazabilidad.

Una parada puede representar:

- Una recogida
- Una entrega
- Una operación de hub
- Una parada de ruta
- Una recogida directa
- Una entrega directa
- Un evento generado por el optimizador

La configuración estándar del sistema incluye seis tipos de parada, cada uno con una única marca booleana activa que define su papel dentro del flujo operativo.

.. image:: /_static/images/Config_Tipo_Parada_Lista.png
   :align: center

Esta clasificación condiciona:

- La generación automática de paradas
- La planificación de rutas
- Las validaciones operativas
- El comportamiento de la app del conductor
- La trazabilidad del servicio

Campos principales de Tipos de Parada
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Campo
     - Descripción
   * - Nombre
     - Identificador funcional del tipo de parada.
   * - Secuencia
     - Orden de visualización.
   * - Descripción
     - Definición funcional.
   * - Compañía
     - Configuración multiempresa.
   * - Color
     - Identificador visual.
   * - Imagen
     - Icono asociado.
   * - Es operación de hub
     - Marca operaciones de centro logístico.
   * - Es recogida a domicilio
     - Define home collection.
   * - Es parada de ruta
     - Marca paradas planificables.
   * - Es recogida directa
     - Flujo directo de recogida.
   * - Es entrega directa
     - Flujo directo de entrega.
   * - Es parada de optimizador
     - Eventos generados automáticamente.

Comportamiento operativo de Tipos de Parada
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los tipos de parada intervienen directamente en la construcción de la estructura operativa de una orden.

El sistema decide:

- Qué paradas son planificables
- Qué pertenecen a operaciones de hub
- Qué movimientos deben tratarse como directos

También se utilizan en:

- Acciones masivas
- Filtros de planificación
- Validaciones previas
- Comunicación con la app

.. note::

   La marca "Es parada de ruta" es crítica.
   Una clasificación incorrecta puede dejar una parada
   fuera de planificación, secuenciación u optimización.



Tipos de Destinatario
~~~~~~~~~~~~~~~~~~~~~

Contexto funcional de Tipos de Destinatario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los Tipos de Destinatario permiten segmentar el perfil del receptor final de la mercancía.

Ejemplos habituales:

- B2B
- B2C
- Retail
- Horeca
- Gran superficie
- Punto de conveniencia

La lista de tipos configurados muestra los segmentos disponibles en el sistema, junto con la marca de valor por defecto y el color asociado a cada uno.

.. image:: /_static/images/Config_Tipo_Destinatario_Lista.png
   :align: center

Campos principales de Tipos de Destinatario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Código identificador.
   * - Secuencia
     - Orden de visualización.
   * - Descripción
     - Definición funcional.
   * - Compañía
     - Configuración multiempresa.
   * - Valor por defecto
     - Clasificación estándar.
   * - Información adicional
     - Notas internas.

Aplicación operativa de Tipos de Destinatario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Se vinculan con:

- Proyectos
- Órdenes
- Reglas tarifarias
- Filtros de planificación

Permiten:

- Limitar destinatarios válidos
- Aplicar reglas específicas
- Diferenciar operativas de última milla



Tipos de Transportista
~~~~~~~~~~~~~~~~~~~~~~

Contexto funcional de Tipos de Transportista
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los Tipos de Transportista permiten clasificar los recursos que ejecutan el transporte.

Esta clasificación permite distinguir, por ejemplo, entre transporte con medios propios, colaboradores regulares con contrato estable o proveedores puntuales para picos de demanda.

.. image:: /_static/images/Config_Tipo_Transportista_Lista.png
   :align: center

Campos principales de Tipos de Transportista
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Identificador funcional.
   * - Secuencia
     - Orden de visualización.
   * - Descripción
     - Definición funcional.
   * - Compañía
     - Configuración multiempresa.
   * - Valor por defecto
     - Clasificación estándar.
   * - Información adicional
     - Notas internas.
   * - Color
     - Identificador visual.

Aplicación operativa de Tipos de Transportista
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Se utilizan en:

- Configuración de proyectos
- Asignación de viajes
- Reglas económicas

Permiten:

- Definir transportistas admisibles
- Condicionar tarifas de compra
- Analizar rentabilidad por proveedor



Tipos de Reembolso
~~~~~~~~~~~~~~~~~~

Contexto funcional de Tipos de Reembolso
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los Tipos de Reembolso definen modalidades de cobro o devolución asociadas a una expedición.

Ejemplos:

- Contra reembolso
- Cobro en entrega
- Gestión de efectivo

La configuración del sistema contempla las modalidades habituales: cobro en metálico, mediante TPV propio o del cliente, y cheque bancario.

.. image:: /_static/images/Config_Tipo_Reembolso_Lista.png
   :align: center

Campos principales de Tipos de Reembolso
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Campo
     - Descripción
   * - Nombre
     - Identificador funcional.
   * - Secuencia
     - Orden de visualización.
   * - Descripción
     - Definición funcional.
   * - Compañía
     - Configuración multiempresa.
   * - Valor por defecto
     - Clasificación estándar.
   * - Información adicional
     - Notas internas.
   * - Color
     - Identificador visual.

Aplicación operativa de Tipos de Reembolso
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Permiten:

- Clasificar importes asociados
- Relacionar cobros con trazabilidad
- Integrar información con liquidación económica

Especialmente relevantes cuando:

- El conductor reporta importes desde la app
- Se requiere control financiero detallado
