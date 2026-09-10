A.18 Proyecto
=============

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Proyectos

Modelo Odoo: ``project.project``. Los campos que el TMS añade al Proyecto de Odoo, agrupados como en su formulario. Es el maestro con más decisiones del sistema.

Cabecera
--------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Aplicar en
     - Selección
     - Órdenes (proyecto de cliente) o Viajes (proyecto de transportista). Cambia qué pestañas y campos aplican.
   * - Cliente / Transportista
     - Relación con Contacto
     - El cliente del proyecto de Órdenes, o el transportista del proyecto de Viajes.
   * - Órdenes / Viajes (abiertas / total)
     - Botones inteligentes (calculados)
     - Acceso a las Órdenes o los Viajes del proyecto, con el recuento de abiertos sobre el total.

Pestaña TMS › Administración
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tarifa
     - Relación con Tarifa
     - La tarifa de venta (proyecto de Órdenes) o de compra (proyecto de Viajes). Al elegirla, el proyecto precarga los catálogos que usan sus líneas.
   * - Modo de División
     - Selección
     - Cómo se divide el precio de una Orden entre sus Tramos: Volumen, Lineal, Metros, Bulto, Pallets, Cantidad, Peso, o combinados con Km. Por defecto, Km y Peso.
   * - Cuenta analítica
     - Relación con Cuenta analítica
     - La cuenta de Odoo a la que van los ingresos y costes del proyecto.
   * - Política fecha administrativa
     - Selección
     - Qué fecha decide la versión de tarifa: Fecha de cierre (la de la parada activa, por defecto), Fecha de creación, Fecha de carga (la más temprana) o Fecha de descarga (la más tardía).

Pestaña TMS › Entrada Hub / Recogida en Cliente
-----------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Agencia / Hub
     - Relación con Contacto
     - La agencia responsable y el hub por el que entra la mercancía.
   * - Punto de Recogida
     - Relación con Contacto
     - El origen que se propone por defecto a las Órdenes; si falta, se usa el hub.
   * - Hora Inicio / Tiempo Fin
     - Hora
     - La ventana de recogida por defecto.
   * - Servicio de recogida a domicilio
     - Relación con Tipo de servicio
     - El tipo de servicio con que se tarifica la recogida a domicilio, distinto del resto de la operativa.

Pestaña TMS › Otros parámetros
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Horarios Informados
     - Sí/No
     - Si las Órdenes traen sus ventanas horarias. Si no, se usan las del contacto o las horas predeterminadas del proyecto, y el contacto sin horario se marca para normalizar.
   * - Hora Inicio Predeterminada / Hora Fin Predeterminada
     - Hora
     - La ventana que se aplica cuando no hay horario informado.
   * - Aplicar fecha común
     - Sí/No
     - Al cerrar un Manifiesto, pide una fecha de servicio común para todas sus Órdenes.
   * - Hora de cita única / Tolerancia de cita (min)
     - Sí/No / Número
     - Carga completa y directos: el cliente da una hora, no una ventana. Sólo se pide la hora de inicio y el fin se construye sumando la tolerancia (0 = la misma hora).
   * - Secuenciar Viaje
     - Sí/No
     - Al cerrar un Manifiesto sin secuencia, ordena las paradas con PTV antes de calcular la ruta.
   * - Generar viaje al validar
     - Sí/No
     - Crea el Viaje al validar la Orden, sin pasar por el asistente.
   * - Crear traslado hub al asignar
     - Sí/No
     - Al asignar paradas a una agencia, divide los Tramos y crea la parada intermedia en el hub.
   * - Procesar viaje de agencia automáticamente
     - Sí/No
     - El Viaje que nace al asignar a una agencia se crea ya en Procesado, no en borrador.
   * - Autoasignar zona operativa más cercana / zona de tarifa más cercana
     - Sí/No
     - Si la dirección no cae en ningún área, se asigna la más cercana (operativa y de tarifa por separado).

Pestaña TMS › Tarea (asignación por defecto)
--------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Planificación
     - Relación con Planning
     - El Planning que heredan Órdenes, Tramos y Viajes. En la interfaz el campo se llama «Planificación».
   * - Plan de Transporte
     - Relación con Plan de transporte
     - La red territorial para resolver zonas, hubs y agencias.
   * - Tiempo Servicio
     - Relación con Tiempos de servicio
     - El esquema con que se calcula la duración de las paradas.
   * - Producto
     - Relación con Producto (TMS)
     - El producto por defecto de las líneas económicas.
   * - Orden, Servicio, Tipo de Bulto, Tipo de vehículo, Tipo Transportista, Tipo Destinatario
     - Relaciones (calculadas)
     - El valor por defecto de cada catálogo: se rellena solo cuando la Activación deja un único valor.
   * - Equipamiento de vehículos / Categorías de Carga
     - Listas
     - Lo que exige la operativa del proyecto a los vehículos y la mercancía que mueve.

Pestaña TMS › Activación
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Órdenes, Servicios, Tipos de Transportistas, Tipos de destinatarios, Tipos de Bulto, Tipos de Vehículos
     - Listas
     - Los catálogos habilitados en el proyecto. Actúan como filtro en las Órdenes y como validación en las importaciones. La tarifa los precarga desde sus líneas.

Pestaña Líneas por defecto
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Líneas por defecto
     - Lista de plantillas de línea
     - Plantillas de mercancía (regla de tarifa, tipo de bulto, cantidades, peso, dimensiones y descripciones) que se copian a los Tramos cuando el fichero o el usuario no detallan la mercancía.

Pestaña Albarán
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Crear albarán
     - Sí/No
     - Si validar una Orden del proyecto genera un albarán de inventario.
   * - Tipo de albarán / Ubicación origen de stock / Ubicación destino de stock
     - Relaciones
     - Los tres datos que el albarán necesita. Si falta alguno, la creación se bloquea.

Pestaña Etiquetas
-----------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Formato de etiqueta / Diseño de etiqueta
     - Selección / Relación
     - El formato (10 x 6 horizontal, 10 x 15 vertical) y el diseño que el asistente de impresión propone para los bultos del proyecto.
   * - Orden de etiquetas por defecto
     - Lista
     - El orden (campo y sentido) con que se imprimen las etiquetas.

Pestaña API Inbox (módulo de integraciones)
-------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Token API
     - Texto
     - El token con que se autentica el sistema externo de este proyecto.
   * - Bandeja de entrada API
     - Relación con Bandeja de entrada API
     - La bandeja donde caen las Órdenes que llegan por API.
   * - Publicar datos importados / Obtener seguimiento / Obtener adjunto
     - Sí/No
     - Los tres permisos del token: enviar órdenes, consultar el seguimiento y descargar adjuntos.
   * - Límite por minuto / por día
     - Número
     - Cuota de llamadas del token.
   * - Enviar por API al asignar / Endpoints de envío
     - Sí/No / Lista de endpoints
     - Si al asignar paradas a una agencia se ejecutan los endpoints de envío configurados, y cuáles, en orden.

Grupo Aplicación móvil (módulo de la app)
-----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Perfil de la aplicación
     - Relación con Perfil de la app
     - El perfil funcional que carga la app del conductor para las paradas del proyecto.
   * - POD digital
     - Sí/No
     - La app pide nombre, documento y firma en pantalla al entregar.
   * - POD físico
     - Sí/No
     - La app exige fotografiar el albarán firmado para completar la entrega.
   * - Escaneo Masivo
     - Sí/No
     - Activa «Encontrar bultos», la búsqueda con la cámara de los bultos de la parada.
   * - Escaneo Spark
     - Sí/No
     - Activa la comprobación de bultos por lectura continua en el flujo de la parada.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_5_project-configuration`.
