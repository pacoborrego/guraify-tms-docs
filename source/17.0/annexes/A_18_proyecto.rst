A.18 Proyecto
=============

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Proyectos

Modelo Odoo: ``project.project``. Los campos que el TMS añade al Proyecto de Odoo, agrupados como en
su formulario. Es el maestro con más decisiones del sistema.

A.18.1 Cabecera
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Aplicar en
     - Selección
     - Órdenes (Proyecto de cliente) o Viajes (Proyecto de transportista). Cambia qué pestañas y
       campos aplican.
   * - Cliente / Transportista
     - Relación con Contacto
     - El cliente del Proyecto de Órdenes, o el transportista del Proyecto de Viajes.
   * - Órdenes / Viajes (abiertas / total)
     - Botones inteligentes (calculados)
     - Acceso a las Órdenes o los Viajes del Proyecto, con el recuento de abiertos sobre el total.

A.18.2 Pestaña TMS › Administración
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tarifa
     - Relación con Tarifa
     - La Tarifa de venta (Proyecto de Órdenes) o de compra (Proyecto de Viajes). Al elegirla, el
       Proyecto precarga los catálogos que usan sus líneas.
   * - Modo de División
     - Selección
     - Cómo se divide el precio de una Orden entre sus Tramos: Volumen, Lineal, Metros, Bulto,
       Pallets, Cantidad, Peso, o combinados con Km. Por defecto, Km y Peso. Ver
       :doc:`/17.0/8_economic-administration/8_2_sales-split`.
   * - Cuenta analítica
     - Relación con Cuenta analítica
     - La cuenta de Odoo a la que van los ingresos y costes del Proyecto.
   * - Política fecha administrativa
     - Selección
     - Qué fecha decide la Versión de tarifa: Fecha de cierre (la de la Parada activa, por defecto),
       Fecha de creación, Fecha de carga (la más temprana) o Fecha de descarga (la más tardía).

A.18.3 Pestaña TMS › Entrada Hub / Recogida en Cliente
------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Agencia / Hub
     - Relación con Contacto
     - La Agencia responsable y el Hub por el que entra la mercancía.
   * - Punto de Recogida
     - Relación con Contacto
     - El origen que se propone por defecto a las Órdenes; si falta, se usa el Hub.
   * - Hora Inicio / Tiempo Fin
     - Hora
     - La franja de recogida por defecto.
   * - Servicio de recogida a domicilio
     - Relación con Tipo de Servicio
     - El Tipo de Servicio con que se tarifica la recogida a domicilio, distinto del resto de la
       operativa.

A.18.4 Pestaña TMS › Otros parámetros
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Horarios Informados
     - Sí/No
     - Si las Órdenes traen sus franjas horarias. Si no, se usan las del contacto o las horas
       predeterminadas del Proyecto, y el contacto sin horario se marca para normalizar.
   * - Hora Inicio Predeterminada / Hora Fin Predeterminada
     - Hora
     - La franja que se aplica cuando no hay horario informado.
   * - Aplicar fecha común
     - Sí/No
     - Al cerrar un Manifiesto, pide una fecha de servicio común para todas sus Órdenes.
   * - Hora de cita única / Tolerancia de cita (min)
     - Sí/No / Número
     - Para carga completa y directos, donde el cliente da una hora y no una franja: solo se pide la
       hora de inicio y el fin se construye sumando la tolerancia (0 = la misma hora).
   * - Secuenciar Viaje
     - Sí/No
     - Al cerrar un Manifiesto sin secuencia, ordena las Paradas con PTV (secuenciación) antes del
       cálculo de ruta.
   * - Generar viaje al validar
     - Sí/No
     - Crea el Viaje al validar la Orden, sin pasar por el asistente.
   * - Crear traslado hub al asignar
     - Sí/No
     - Al asignar Paradas a una Agencia, divide los Tramos y crea la Parada intermedia en el Hub.
   * - Procesar viaje de agencia automáticamente
     - Sí/No
     - El Viaje que nace al asignar a una Agencia se crea ya en Procesado, no en borrador.
   * - Autoasignar zona operativa más cercana / zona de tarifa más cercana
     - Sí/No
     - Si la dirección no cae en ningún área, se asigna la más cercana (operativa y de tarifa por
       separado).

A.18.5 Pestaña TMS › Tarea (asignación por defecto)
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Planificación
     - Relación con Planning
     - El Planning que heredan Órdenes, Tramos y Viajes. En la interfaz el campo se llama
       «Planificación».
   * - Plan de Transporte
     - Relación con Plan de transporte
     - La red territorial para resolver zonas, hubs y agencias.
   * - Tiempo Servicio
     - Relación con Tiempos de servicio
     - El esquema con que se calcula la duración de las Paradas.
   * - Producto
     - Relación con Producto (TMS)
     - El producto por defecto de las líneas económicas.
   * - Orden, Servicio, Tipo de Bulto, Tipo de vehículo, Tipo Transportista, Tipo Destinatario
     - Relaciones (calculadas)
     - El valor por defecto de cada catálogo: se rellena solo cuando la Activación deja un único
       valor.
   * - Equipamiento de vehículos / Categorías de Carga
     - Listas
     - Lo que exige la operativa del Proyecto a los vehículos y la mercancía que mueve.

A.18.6 Pestaña TMS › Activación
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Órdenes, Servicios, Tipos de Transportistas, Tipos de destinatarios, Tipos de Bulto, Tipos de
       Vehículos
     - Listas
     - Los catálogos habilitados en el Proyecto. Actúan como filtro en las Órdenes y como validación
       en las importaciones. La Tarifa los precarga desde sus líneas.

A.18.7 Pestaña Líneas por defecto
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Líneas por defecto
     - Lista de plantillas de línea
     - Plantillas de mercancía (Regla de tarifa, Tipo de bulto, cantidades, peso, dimensiones y
       descripciones) que se copian a los Tramos cuando el fichero o el usuario no detallan la
       mercancía.

A.18.8 Pestaña Albarán
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Crear albarán
     - Sí/No
     - Si validar una Orden del Proyecto genera un albarán de inventario.
   * - Tipo de albarán / Ubicación origen de stock / Ubicación destino de stock
     - Relaciones
     - Los tres datos que el albarán necesita. Si falta alguno, la creación se bloquea.

A.18.9 Pestaña Etiquetas
------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Formato de etiqueta / Diseño de etiqueta
     - Selección / Relación
     - El formato (10 x 6 horizontal, 10 x 15 vertical) y el diseño que el asistente de impresión
       propone para los Bultos del Proyecto.
   * - Orden de etiquetas por defecto
     - Lista
     - El orden (campo y sentido) con que se imprimen las etiquetas.

A.18.10 Pestaña Bandeja de entrada API
--------------------------------------



.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Token API
     - Texto
     - El token con que se autentica el sistema externo de este Proyecto.
   * - Bandeja de entrada API
     - Relación con Bandeja de entrada API
     - La bandeja donde caen las Órdenes que llegan por API.
   * - Publicar datos importados / Obtener seguimiento / Obtener adjunto
     - Sí/No
     - Los tres permisos del token: enviar Órdenes, consultar el seguimiento y descargar adjuntos.
   * - Límite por minuto / por día
     - Número
     - Cuota de llamadas del token.
   * - Enviar por API al asignar / Endpoints de envío
     - Sí/No / Lista de puntos de conexión
     - Si al asignar Paradas a una Agencia se ejecutan los puntos de conexión de envío configurados,
       y cuáles, en orden. La lista se llama «Endpoints de envío» en la interfaz.

A.18.11 Grupo Aplicación móvil
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Perfil de la aplicación
     - Relación con Perfil de la app
     - El perfil funcional que carga la app del conductor para las Paradas del Proyecto.
   * - POD digital
     - Sí/No
     - La app pide nombre, documento y firma en pantalla al entregar (prueba de entrega digital).
   * - POD físico
     - Sí/No
     - La app exige fotografiar el albarán firmado para completar la entrega.
   * - Escaneo Masivo
     - Sí/No
     - Activa «Encontrar bultos», la búsqueda con la cámara de los Bultos de la Parada.
   * - Escaneo Spark
     - Sí/No
     - Activa la comprobación de Bultos por lectura continua en el flujo de la Parada. Así se llama
       la casilla en la interfaz.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_5_project-configuration`.
