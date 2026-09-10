A.3 Reglas de tarifa (unidad de medida)
=======================================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › Regla de tarifa

Modelo Odoo: ``tms.pricelist.rule``. Cómo se mide operativamente una línea de mercancía: bultos, palés, cantidad o metros lineales. No lleva precios.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la regla.
   * - Descripción
     - Texto
     - Explicación breve. Obligatoria.
   * - Descripción singular / plural
     - Texto
     - Cómo se nombra la unidad en líneas, etiquetas e informes: «bulto» y «bultos», «palé» y «palés».
   * - Físico
     - Sí/No
     - Si la unidad es un objeto trazable. Con Físico, cada unidad genera un Bulto con su código de barras y se puede escanear; sin él, la cantidad es un dato y no hay bultos.
   * - Bultos / Cantidad / Metros / Pallets
     - Sí/No (cuatro casillas)
     - Qué magnitudes pide la línea al usuario. Se pueden activar varias: una regla de palés puede pedir también los bultos que van encima.
   * - Anchura, Altura y Profundidad del bulto (cm)
     - Número
     - Dimensiones por defecto de la unidad. El sistema las usa para calcular el volumen cuando la línea no las trae.
   * - Peso del bulto (kg)
     - Número
     - Peso por defecto de la unidad, con el mismo uso.
   * - Cliente
     - Relación con Contacto
     - Si la regla es propia de un cliente, se restringe a él. Vacío es para todos.
   * - Foto
     - Imagen
     - Imagen de la unidad, para la app y los informes.
   * - Validar / Errores de validación
     - Calculado
     - Comprobación de que la regla es coherente (por ejemplo, que una regla física tenga dimensiones). El texto de errores dice qué falta.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_2_logistic-configuration`.
