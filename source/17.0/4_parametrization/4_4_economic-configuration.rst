Configuración económica
-----------------------


La Configuración Económica agrupa los maestros que transforman actividad logística en líneas de venta y compra.

Incluye zonas tarifarias, bases de cálculo, reglas, versiones de tarifa y productos contables.

El motor de tarificación combina estos datos con el contexto operativo: cliente, transportista, proyecto, Planning, servicio, vehículo, zonas, fechas y magnitudes de carga.



Zonas Tarifarias
~~~~~~~~~~~~~~~~

Las Zonas Tarifarias agrupan áreas geográficas utilizadas para calcular precios.

Son independientes de los Planes de Transporte: un plan organiza la operación, mientras una zona tarifaria organiza el criterio económico.

**Campos principales**

+------------------------+------------------------------------------------------------------+
| Campo                  | Descripción                                                      |
+========================+==================================================================+
| Nombre y descripción   | Identifican la finalidad económica de la zona.                   |
+------------------------+------------------------------------------------------------------+
| Áreas                  | Áreas Geográficas de tipo Zona Tarifaria.                        |
+------------------------+------------------------------------------------------------------+
| Agencia                | Agencia de referencia para visualización y contexto territorial. |
+------------------------+------------------------------------------------------------------+
| Por defecto            | Zona principal de la compañía.                                   |
+------------------------+------------------------------------------------------------------+
| Activo                 | Permite ocultar zonas obsoletas sin eliminarlas.                 |
+------------------------+------------------------------------------------------------------+
| Secuencia y color      | Ordenación y clasificación visual.                               |
+------------------------+------------------------------------------------------------------+
| Compañía               | Empresa propietaria de la zona.                                  |
+------------------------+------------------------------------------------------------------+
| Vista de mapa          | Previsualización cartográfica.                                   |
+------------------------+------------------------------------------------------------------+

Uso dentro del sistema en Zonas Tarifarias
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cada Tarifa referencia una Zona Tarifaria.

Al actualizar zonas en tramos o paradas, el sistema toma la tarifa de cliente o transportista, obtiene su zona tarifaria y resuelve la dirección contra sus áreas.

La resolución se usa tanto para venta como para compra.

En venta se informan zonas tarifarias del cliente.

En compra se informan zonas tarifarias del transportista.

En ambos casos, el resultado puede condicionar qué detalle de tarifa aplica.

Si el proyecto permite asignar la zona más cercana, cuando una dirección queda fuera del polígono se puede seleccionar el área más próxima y registrar kilómetros extra.

Este dato permite tratar operaciones fuera de cobertura sin dejar la operación sin zona.

A nivel viaje, el sistema calcula zonas iniciales y finales.

Según el modo de la tarifa, puede usar:

- Primera y última parada por secuencia
- Zonas del tramo más largo



Tarifas Base
~~~~~~~~~~~~

Las Tarifas Base definen la magnitud sobre la que se calcula una regla económica:

- Peso
- Volumen
- Bultos
- Pallets
- Metros
- Cantidad
- Distancia
- Tiempo
- Otros conceptos

Funcionan como puente entre los datos logísticos medidos y los rangos de precio configurados.

**Campos principales**

+------------------------+------------------------------------------------------------------+
| Campo                  | Descripción                                                      |
+========================+==================================================================+
| Nombre                 | Identificador de la base de cálculo.                             |
+------------------------+------------------------------------------------------------------+
| Código                 | Código técnico usado por UI y lógica interna.                    |
+------------------------+------------------------------------------------------------------+
| Tipo de cálculo        | Magnitud usada como factor económico.                            |
+------------------------+------------------------------------------------------------------+
| Descripción            | Explicación funcional de la base.                                |
+------------------------+------------------------------------------------------------------+
| Rangos                 | Plantillas de escalado reutilizables.                            |
+------------------------+------------------------------------------------------------------+
| Secuencia, compañía    | Ordenación y segmentación multiempresa.                          |
| y color                |                                                                  |
+------------------------+------------------------------------------------------------------+

Uso dentro del sistema en Tarifas Base
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Durante la tarificación, la base determina qué factor se utiliza para calcular el precio.

Según el ámbito:

- Expedición
- Tramo
- Parada
- Viaje

el sistema leerá magnitudes distintas.

Si la regla activa conversión volumétrica, el sistema compara:

- Peso real
- Peso volumétrico convertido

y utiliza el valor mayor.

Esto permite aplicar peso tasable.

Los rangos permiten generar automáticamente escalados de tarifa mediante asistentes de parametrización.

.. note::

   La Tarifa Base no contiene precios.
   Únicamente define cómo se mide la operación.



Reglas de Tarifa
~~~~~~~~~~~~~~~~~

En este apartado, Reglas de Tarifa hace referencia al conjunto formado por el ítem de tarifa y sus detalles.

El ítem define cuándo aplica una regla.

El detalle define:

- Zona
- Rango
- Vehículo
- Importe

Esta separación permite que una misma tarifa tenga reglas por:

- Expedición
- Tramo
- Parada
- Viaje

con condiciones distintas según el contexto operativo.

**Campos principales**

+---------------------------+------------------------------------------------------------------+
| Campo                     | Descripción                                                      |
+===========================+==================================================================+
| Tarifa y versión          | Vinculan la regla con una tarifa y su periodo de vigencia.       |
+---------------------------+------------------------------------------------------------------+
| Base de tarifa            | Magnitud utilizada como factor económico.                        |
+---------------------------+------------------------------------------------------------------+
| Aplicar en                | Ámbito operativo de aplicación.                                  |
+---------------------------+------------------------------------------------------------------+
| Producto                  | Producto TMS utilizado para generar líneas económicas.           |
+---------------------------+------------------------------------------------------------------+
| Filtros operativos        | Condiciones funcionales de aplicación.                           |
+---------------------------+------------------------------------------------------------------+
| Conversión volumétrica    | Permite aplicar peso volumétrico.                                |
+---------------------------+------------------------------------------------------------------+
| Zonas del detalle         | Áreas tarifarias o zonas origen/destino.                         |
+---------------------------+------------------------------------------------------------------+
| Rango desde/hasta         | Intervalo del factor aplicable.                                  |
+---------------------------+------------------------------------------------------------------+
| Precio                    | Precio unitario, mínimo, máximo, forfait o porcentaje.           |
+---------------------------+------------------------------------------------------------------+
| Aplicación del precio     | Base económica concreta utilizada.                               |
+---------------------------+------------------------------------------------------------------+
| Partners y flota          | Restricciones opcionales por partner o vehículo.                 |
+---------------------------+------------------------------------------------------------------+

Uso dentro del sistema en Reglas de Tarifa
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El motor de tarificación selecciona primero los ítems compatibles con el ámbito que se está calculando.

Posteriormente filtra por contexto:

- Planning
- Tipo de servicio
- Tipo de expedición
- Tipo de parada
- Cliente
- Transportista
- Vehículo
- Zona

Una vez seleccionada la regla, calcula el factor utilizando la Tarifa Base.

Solo se aplican detalles cuyo rango incluya dicho factor.

Si existen límites:

- mínimo facturable
- máximo facturable

el importe final se ajusta automáticamente.

Las reglas pueden generar:

- Líneas de venta
- Líneas de compra

sobre:

- Pedido
- Parada
- Tramo
- Viaje

Cada resultado conserva referencias a:

- Tarifa
- Regla
- Detalle
- Zona
- Producto

Esto facilita auditoría y diagnóstico posterior.

Cuando no existe coincidencia, el sistema registra diagnósticos de tarificación.

Esto permite identificar si el fallo proviene de:

- Ausencia de tarifa
- Versión no vigente
- Zona no resuelta
- Planning incompatible
- Rango fuera de escala
- Restricción por partner
- Restricción por vehículo



 Tarifas
~~~~~~~~~

La Tarifa es el contenedor económico principal del sistema.

Agrupa:

- Clientes o transportistas
- Moneda
- Zona tarifaria
- Versiones
- Reglas económicas

Su diseño permite mantener histórico de precios sin perder trazabilidad sobre operaciones ya calculadas.

**Campos principales**

+---------------------------+------------------------------------------------------------------+
| Campo                     | Descripción                                                      |
+===========================+==================================================================+
| Nombre y descripción      | Identifican la tarifa y su alcance funcional.                    |
+---------------------------+------------------------------------------------------------------+
| Estado                    | Borrador, activa, expirada o archivada.                          |
+---------------------------+------------------------------------------------------------------+
| Moneda y compañía         | Contexto económico y multiempresa.                               |
+---------------------------+------------------------------------------------------------------+
| Partners asociados        | Clientes o transportistas vinculados.                            |
+---------------------------+------------------------------------------------------------------+
| Zona tarifaria            | Territorio económico de referencia.                              |
+---------------------------+------------------------------------------------------------------+
| Modo de referencia zona   | Criterio territorial de cálculo.                                 |
+---------------------------+------------------------------------------------------------------+
| Versiones                 | Periodos de vigencia con reglas propias.                         |
+---------------------------+------------------------------------------------------------------+
| Versión actual            | Versión activa de referencia.                                    |
+---------------------------+------------------------------------------------------------------+
| Fechas inicio/fin         | Intervalo calculado a partir de versiones.                       |
+---------------------------+------------------------------------------------------------------+

Uso dentro del sistema en Tarifas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Las tarifas pueden asignarse a:

- Proyectos
- Expediciones
- Tramos
- Paradas
- Viajes
- Slots de planificación

Pueden representar:

- Precio de cliente
- Coste de transportista

Para calcular una tarifa, el sistema obtiene la versión aplicable según fecha de referencia.

Dependiendo del flujo, puede utilizar:

- Fecha de orden
- Fecha administrativa
- Fecha del viaje

.. note::
   La **fecha administrativa** (``order_date`` en ``sale.order``) es un campo
   calculado y estable, independiente de la fecha de orden de Odoo
   (``date_order``). Determina la versión tarifaria aplicable según la política
   de fecha administrativa configurada en el proyecto (ver
   :doc:`4_5_project-configuration`).

Las versiones validan una línea temporal coherente:

- Una única versión activa
- Sin solapes
- Sin huecos entre periodos

Esto evita conflictos entre versiones concurrentes.

El estado y el campo activo se sincronizan con las fechas.

Las tarifas expiradas pueden ocultarse sin perder histórico operativo.


Productos asociados
~~~~~~~~~~~~~~~~~~~~

Los Productos asociados conectan la lógica TMS con la contabilidad estándar de Odoo.

Solo los productos marcados como producto TMS pueden utilizarse dentro de:

- Reglas de tarifa
- Proyectos
- Conceptos económicos del módulo

**Campos principales**

+------------------------------+--------------------------------------------------------------+
| Campo                        | Descripción                                                  |
+==============================+==============================================================+
| Producto TMS                 | Marca de habilitación para uso en TMS.                       |
+------------------------------+--------------------------------------------------------------+
| Nombre y referencia interna  | Identificación comercial y contable.                         |
+------------------------------+--------------------------------------------------------------+
| Unidad de medida             | Unidad usada en líneas económicas.                           |
+------------------------------+--------------------------------------------------------------+
| Impuestos y cuentas          | Configuración fiscal y contable estándar Odoo.               |
+------------------------------+--------------------------------------------------------------+
| Relación con tipos servicio  | Restricciones funcionales opcionales.                        |
+------------------------------+--------------------------------------------------------------+
| Uso en reglas                | Producto utilizado en líneas generadas por tarifa.           |
+------------------------------+--------------------------------------------------------------+
| Producto del proyecto        | Producto por defecto del proyecto.                           |
+------------------------------+--------------------------------------------------------------+

Uso dentro del sistema en Productos asociados
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando el motor de tarifa crea líneas económicas, convierte el producto plantilla TMS en su variante de producto Odoo y lo asigna a la línea resultante.

Esto garantiza coherencia en:

- Cuentas contables
- Impuestos
- Unidades
- Reporting económico
- Facturación

Mantener productos separados por concepto facilita el análisis económico.

Ejemplos habituales:

- Portes
- Suplementos
- Reembolsos
- Servicios especiales

.. important::

   La separación correcta de productos TMS es clave para
   mantener trazabilidad económica y control real de márgenes.