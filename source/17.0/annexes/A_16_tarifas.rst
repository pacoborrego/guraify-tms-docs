A.16 Tarifas y versiones
========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Opciones de Tarifa › Tarifa

Modelo Odoo: ``tms.pricelist``. El contenedor de precios de un cliente o un transportista, con su histórico de versiones.

Tarifa (tms.pricelist)
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre / Descripción
     - Texto
     - Cómo se identifica la tarifa. La descripción es obligatoria.
   * - Estado
     - Selección
     - Borrador, Activo, Caducado o Archivado. Se sincroniza con las fechas de las versiones.
   * - Activo
     - Sí/No
     - Permite ocultar la tarifa sin borrarla.
   * - Moneda
     - Relación con Moneda
     - Moneda de todos los importes. Obligatoria.
   * - Cliente
     - Lista de Contactos
     - Los clientes o transportistas a los que aplica la tarifa.
   * - Zonas Disponibles
     - Relación con Zona de tarifa
     - La zona de tarifa sobre la que se definen las áreas de los detalles. Obligatoria.
   * - Modo de referencia de zona
     - Selección
     - Cómo se decide la zona de un Viaje: Primera/última parada por secuencia, o Carga/descarga del tramo más largo (km). Obligatorio.
   * - Versiones / Versión actual
     - Lista / Relación
     - Las versiones de la tarifa y la vigente hoy.
   * - Fecha Inicio / Fecha Fin
     - Fecha (calculadas)
     - El intervalo que cubren las versiones.
   * - Reglas Tarifa / Detalles de tarifa
     - Listas (calculadas)
     - Las líneas y los detalles de la versión actual, para consulta.

Versión (tms.pricelist.version)
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la versión: «2026», «Julio 2026».
   * - Estado
     - Selección
     - Borrador, Activo o Archivado.
   * - Fecha inicio / Fecha fin
     - Fecha
     - Vigencia. Las versiones de una tarifa no pueden solaparse ni dejar huecos, y sólo una está activa.
   * - Versión base
     - Relación con Versión
     - La versión de la que se copiaron las líneas al crear ésta.
   * - Reglas de zona
     - Lista de Líneas de tarifa
     - Las líneas de la versión.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_4_economic-configuration`.
