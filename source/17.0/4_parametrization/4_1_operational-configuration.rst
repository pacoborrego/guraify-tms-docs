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

Tipos de Servicio
~~~~~~~~~~~~~~~~~

Los Tipos de Servicio constituyen uno de los primeros elementos de configuración operativa del sistema. Su objetivo es clasificar la naturaleza de los servicios de transporte gestionados dentro del TMS y establecer la relación entre la operativa logística y los conceptos económicos que se utilizarán posteriormente en la facturación.

En la práctica, el tipo de servicio permite identificar el modelo de transporte que se está aplicando a una expedición. Esta clasificación facilita la gestión de diferentes operativas dentro de una misma organización, como por ejemplo:

- carga completa

- grupaje

- distribución urbana

- same da

- entregas con compromiso horario

La selección del tipo de servicio durante la creación de una orden no solo cumple una función descriptiva. También determina qué productos del catálogo de Odoo se utilizarán posteriormente para registrar los ingresos asociados a la operación.

De este modo, el tipo de servicio actúa como un elemento de conexión entre:

- la estructura operativa de la orden

- las variables logísticas que intervienen en el transporte

- la generación automática de conceptos económicos

Gracias a esta relación, el sistema puede traducir la información operativa del transporte en registros económicos sin necesidad de introducir datos adicionales durante el proceso de facturación.

**Campos principales**

El modelo de tipos de servicio incluye los siguientes campos funcionales.

+-----------------------+------------------------------------------------------------------------------------------------------------------+
| **Campo**             | **Descripción**                                                                                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Nombre                | Identificador del tipo de servicio dentro del sistema. Permite reconocer la naturaleza operativa del transporte. |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Secuencia             | Orden de visualización utilizado para organizar los servicios en las interfaces del sistema.                     |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Descripción económica | Texto utilizado como concepto económico cuando el servicio genera líneas de facturación.                         |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Productos asociados   | Productos del catálogo de Odoo que se utilizarán para registrar los ingresos generados por el servicio.          |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Tipos de expedición   | Define qué tipos de expedición pueden utilizar este servicio.                                                    |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Bultos                | Indica si el número de bultos puede intervenir en el cálculo económico del servicio.                             |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Cantidad              | Permite utilizar la cantidad de unidades como variable logística relevante.                                      |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Metros                | Indica si los metros lineales deben considerarse en la valoración del servicio.                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Pallets               | Permite utilizar el número de pallets como dimensión logística.                                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Información adicional | Campo descriptivo utilizado para documentar características del servicio.                                        |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Compañía              | Permite definir configuraciones específicas en entornos multiempresa.                                            |
+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Color                 | Identificador visual utilizado en algunas interfaces de planificación.                                           |
+=======================+==================================================================================================================+

.. _section-25:

**Uso dentro del sistema**

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
~~~~~~~~~~~~~~~

Los Tipos de Orden definen la naturaleza operativa de una expedición dentro del sistema. Mientras que los tipos de servicio clasifican la dimensión comercial del transporte, los tipos de orden describen el comportamiento logístico que tendrá la orden dentro del flujo operativo del TMS.

En otras palabras, el tipo de orden determina cómo se comporta una expedición dentro de la red logística.

Esta clasificación permite diferenciar distintos escenarios operativos, como por ejemplo:

• recogidas en origen

• entregas a destinatario

• operaciones entre hubs

• servicios directos

• movimientos internos dentro de la red

La definición del tipo de orden influye directamente en la forma en que el sistema genera la estructura logística de la expedición, especialmente en lo relativo a la creación de tramos y paradas.

Por este motivo, los tipos de orden forman parte de los elementos estructurales del modelo operativo del TMS.

**Campos principales**

El modelo de tipos de orden incluye los siguientes campos funcionales.

+-------------+------------------------------------------------------------------------------------------------------------------------+
| **Campo**   | **Descripción**                                                                                                        |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Nombre      | Identificador del tipo de orden dentro del sistema. Permite reconocer el tipo de operación logística que representa.   |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Secuencia   | Orden de visualización utilizado para organizar los tipos de orden dentro de las interfaces del sistema.               |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Descripción | Texto descriptivo utilizado para documentar el comportamiento del tipo de orden.                                       |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Compañía    | Permite definir configuraciones específicas en entornos multiempresa.                                                  |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| Color       | Identificador visual utilizado en algunas interfaces para facilitar la identificación de los distintos tipos de orden. |
+=============+========================================================================================================================+

**Papel dentro del modelo operativo**

Los tipos de orden intervienen principalmente durante el proceso de creación y estructuración de una orden de transporte.

Cuando se registra una nueva expedición en el sistema, el tipo de orden seleccionado indica al sistema qué lógica operativa debe aplicarse para generar la estructura logística de la operación.

Esta lógica puede afectar, entre otros aspectos, a:

• la creación automática de tramos

• la generación de paradas de recogida y entrega

• la clasificación de la operación dentro de la red logística

Gracias a esta configuración, el sistema puede adaptar su comportamiento a distintos modelos operativos sin necesidad de modificar la lógica interna del módulo.

Por ejemplo, una empresa puede gestionar simultáneamente:

• servicios directos entre origen y destino

• operativas hub-and-spoke

• redes de distribución urbana

Cada uno de estos modelos puede utilizar tipos de orden distintos que permitan al sistema interpretar correctamente el flujo logístico de la expedición.

⸻

**Relación con otros elementos del sistema**

Los tipos de orden interactúan con varios componentes clave del modelo operativo del TMS.

En primer lugar, se utilizan durante la creación de órdenes de transporte, donde determinan el comportamiento logístico de la expedición.

Posteriormente, esta información se utiliza durante la generación de tramos y paradas, que constituyen la estructura operativa que será utilizada por el proceso de planificación.

Además, el tipo de orden puede utilizarse como criterio en distintos procesos de configuración, como por ejemplo:

• reglas de planificación

• reglas de tarifa

• validaciones operativas

De esta forma, los tipos de orden permiten adaptar el comportamiento del sistema a distintos modelos logísticos sin alterar la arquitectura general del TMS.

.. note::

   En el modelo conceptual del sistema, el tipo de orden actúa como uno de los elementos que determinan cómo se estructura una expedición en términos de tramos y paradas. Su correcta configuración resulta esencial para que el sistema represente fielmente la operativa logística de la empresa.
Si quieres, en el siguiente paso podemos hacer 4.1.3 Tipos de Parada.

Ese apartado es todavía más interesante a nivel de arquitectura, porque conecta directamente con:

• la trazabilidad

• la ejecución del viaje

• la app del conductor

• los eventos logísticos.
