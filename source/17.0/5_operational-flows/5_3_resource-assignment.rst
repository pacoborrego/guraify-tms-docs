5.3 Asignación de Recursos
--------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Viajes (``tms.trip``).

.. CAPTURA: 5_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_3_resource-assignment_01_recursos.png
      :alt: Asignación de recursos a un viaje

      Viaje (``tms.trip``) con conductor, vehículo y transportista asignados.

La asignación de recursos completa el viaje con los elementos necesarios para su ejecución física y su liquidación económica.

Los recursos pueden llegar desde distintos orígenes:

- importación externa
- slot de planificación
- optimización automática con PTV
- asignación manual por operador

El objetivo de esta fase es garantizar que el viaje disponga de toda la información operativa necesaria para ejecución, seguimiento y liquidación.



5.3.1 Recursos principales
~~~~~~~~~~~~~~~~~~~~~~~~~~



.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Recurso
     - Descripción
   * - Transportista
     - Proveedor, agencia o flota que ejecuta el viaje.
   * - Tarifa de compra
     - Tarifa económica para cálculo del coste.
   * - Conductor
     - Recurso humano asignado a la ejecución.
   * - Vehículo y remolques
     - Recursos físicos utilizados en la ruta.
   * - Categoría de vehículo
     - Capacidades y restricciones aplicables.
   * - Planning y slot
     - Marco temporal y operativo del viaje.
   * - Hub y agencia
     - Referencias logísticas territoriales.

Cuando se informa:

- transportista
- tarifa de compra

el viaje queda preparado para generar o actualizar la orden de compra asociada.

Si el viaje no dispone de tarifa de compra, pero existe un precio cerrado:

- el coste puede liquidarse utilizando dicho importe como base económica

La asignación de recursos no afecta únicamente al viaje.

La información se propaga también hacia las paradas operativas para mantener coherencia entre todos los componentes del flujo.

Esto permite que trabajen con los mismos datos:

- aplicación móvil del conductor
- informes de ruta
- trazabilidad operativa
- seguimiento
- liquidación económica

De este modo, conductor, transportista y condiciones económicas permanecen alineados durante toda la ejecución del viaje.