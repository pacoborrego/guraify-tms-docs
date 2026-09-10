A.13 Zonas de tarifa
====================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Opciones de Tarifa › Zonas de Tarifa

Modelo Odoo: ``tms.pricelist.zone``. La agrupación de áreas geográficas a efectos de precio. Una Tarifa se apoya en una zona.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre / Descripción
     - Texto
     - Cómo se identifica la zona. Ambos obligatorios.
   * - Áreas
     - Lista de Áreas geográficas
     - Las áreas de tipo Zona Tarifa que componen la zona. Los detalles de las líneas de tarifa fijan precios entre estas áreas.
   * - Agencia
     - Relación con Contacto (agencia)
     - Agencia de referencia de la zona.
   * - Activo
     - Sí/No
     - Permite ocultar zonas obsoletas sin borrarlas.
   * - Vista Seguimiento
     - Mapa (calculado)
     - Previsualización de las áreas.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_4_economic-configuration`.
