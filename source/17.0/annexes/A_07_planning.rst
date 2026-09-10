A.7 Planning
============

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › Planificaciones

Modelo Odoo: ``tms.planning``. La segmentación operativa: última milla, recogidas, distribución urbana, larga distancia. Se escribe siempre «Planning», sin traducir.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre del Planning. Obligatorio.
   * - Descripción
     - Texto
     - Explicación breve. Obligatoria.
   * - Información
     - Texto
     - Notas internas.
   * - Plan de Transporte
     - Relación con Plan de transporte
     - La red territorial sobre la que opera este Planning. Obligatorio: sin él no se resuelven las zonas operativas.
   * - Tiempo Recogida (seg) / Tiempo de Servicio (seg)
     - Número
     - Segundos que se añaden a cada recogida y a cada entrega cuando se envía el Planning al optimizador, además del tiempo de servicio propio de la parada.
   * - Modo División Viaje
     - Selección
     - Cómo se reparten los importes de un Viaje entre sus paradas: Volumen, Lineal, Metros, Bulto, Pallets, Cantidad, Peso, o cualquiera de ellos combinado con los kilómetros (Km y Peso, Km y Bulto...).
   * - Remitente
     - Relación con Contacto
     - Remitente asociado al Planning, cuando toda la operativa es de un mismo origen.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
