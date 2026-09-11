A.24 Tipos de Orden
===================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › Tipos de Orden

Modelo Odoo: ``tms.shipment.type``. El comportamiento logístico de la Orden: entrega desde el hub, recogida hacia el hub, servicio directo u operación de hub.

Además de los campos de la tabla, el maestro lleva tres de los campos comunes a los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual) y **Compañía** (a qué compañía pertenece). El nombre debe ser único dentro de cada compañía, y en las listas el registro se muestra como «Nombre - Descripción».

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre corto del tipo, tal y como aparece en Órdenes, Tramos y tarifas. Es traducible.
   * - Descripción
     - Texto
     - Descripción del comportamiento. Obligatoria y traducible; acompaña al nombre en las listas.
   * - Imagen
     - Imagen
     - Icono del tipo, que se muestra en las listas de Órdenes y Tramos.
   * - Entrega
     - Sí/No
     - La Orden es una entrega: se carga en el hub o la agencia del Proyecto y se descarga en el cliente.
   * - Recogida
     - Sí/No
     - La Orden es una recogida: se carga en el cliente y se descarga en el hub o la agencia del Proyecto.
   * - Directo
     - Sí/No
     - La Orden va de un punto del cliente a otro sin pasar por hub.
   * - Hub
     - Sí/No
     - La Orden es una operación de hub: los dos lados del Tramo son el hub del Proyecto, con el horario de recogida del Proyecto.
   * - Punto de Recogida Habitual
     - Sí/No
     - Marca el tipo con el que el sistema crea la Orden de recogida a domicilio del Manifiesto. Debe haber uno marcado para que el cierre del Manifiesto pueda crearla.
   * - Activo Carga %
     - Porcentaje
     - Parte del ingreso del Tramo que se imputa a su Parada de carga.
   * - Activo Descarga %
     - Porcentaje
     - Parte del ingreso del Tramo que se imputa a su Parada de descarga. Con el anterior debe sumar el 100 %; si no, el registro no se guarda.
   * - Información
     - Texto
     - Notas internas de parametrización.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`.
