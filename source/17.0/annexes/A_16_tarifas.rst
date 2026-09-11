A.16 Tarifas y versiones
========================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Opciones de Tarifa › Tarifa

Modelo Odoo: ``tms.pricelist``. El contenedor de precios de un cliente o un transportista, con su
histórico de versiones.

Además de los campos de la tabla, la Tarifa lleva tres de los campos comunes de los catálogos del
TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual) y **Compañía** (a qué compañía
pertenece; vacío es compartido).

A.16.1 Tarifa
-------------

La Tarifa (``tms.pricelist``) es el contenedor.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre / Descripción
     - Texto
     - Cómo se identifica la Tarifa. La descripción es obligatoria.
   * - Estado
     - Selección
     - Borrador, Activo, Caducado o Archivado. Se sincroniza con las fechas de las versiones.
   * - Activo
     - Sí/No
     - Permite ocultar la Tarifa sin borrarla.
   * - Moneda
     - Relación con Moneda
     - Moneda de todos los importes. Obligatoria.
   * - Cliente
     - Lista de Contactos
     - Los clientes o transportistas a los que aplica la Tarifa.
   * - Zonas Disponibles
     - Relación con Zona de tarifa
     - La Zona de tarifa sobre la que se definen las áreas de los detalles. Obligatoria.
   * - Modo de referencia de zona
     - Selección
     - Cómo se decide la zona de un Viaje: Primera/última parada por secuencia, o Carga/descarga del
       tramo más largo (km). Obligatorio.
   * - Versiones / Versión actual
     - Lista / Relación
     - Las versiones de la Tarifa y la vigente hoy.
   * - Fecha Inicio / Fecha Fin
     - Fecha (calculadas)
     - El intervalo que cubren las versiones.
   * - Líneas de tarifa / Detalles de tarifa
     - Listas (calculadas)
     - Las líneas y los detalles de la versión actual, para consulta.

A.16.2 Versión
--------------

La Versión de tarifa (``tms.pricelist.version``) es un periodo de vigencia con sus propias líneas.

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
     - Vigencia. Las versiones de una Tarifa son consecutivas: el sistema rechaza solapes y huecos,
       solo una puede estar activa y esa debe ser la última por fecha; solo la última puede quedar
       sin fecha de fin.
   * - Versión base
     - Relación con Versión
     - La versión de la que se copiaron las líneas al crear esta.
   * - Líneas de tarifa
     - Lista de Líneas de tarifa
     - Las líneas de la versión.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_4_economic-configuration`.
