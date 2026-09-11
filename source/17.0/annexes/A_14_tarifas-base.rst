A.14 Tarifas base
=================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Opciones de Tarifa › Tarifa Base

Modelo Odoo: ``tms.pricelist.base``. La magnitud sobre la que se calcula un precio y las plantillas
de rangos para escalar.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos
del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué
compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando
hay que elegir uno y nadie ha elegido).

A.14.1 Tarifa base
------------------

La Tarifa base (``tms.pricelist.base``) dice qué se mide.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre / Código
     - Texto
     - Nombre y código técnico. El código no se traduce y es el que usan las Líneas de tarifa y el
       motor de tarificación.
   * - Tipo Cálculo
     - Selección
     - La magnitud: Peso, Volumen, Bulto, Pallets, Metros, Cantidad, Distancia, Hora u Otros.
       Obligatorio.
   * - Descripción
     - Texto
     - Explicación funcional.
   * - Rangos de Tarifa Base
     - Lista de rangos
     - Plantillas de escalado reutilizables al crear los detalles de una línea.

A.14.2 Rango y sus escalones
----------------------------

El rango (``tms.pricelist.base.range``) es una plantilla de escalones de la magnitud.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la plantilla de rangos: «Peso 0-5000 en escalones de 100».
   * - Desde / Hasta
     - Número
     - Cada escalón del rango, en la unidad de la Tarifa base.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_4_economic-configuration`.
