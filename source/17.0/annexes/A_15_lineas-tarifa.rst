A.15 Líneas de tarifa y sus detalles
====================================

.. admonition:: Ruta en Odoo
   :class: tip

   Pestaña Reglas Tarifa de la Tarifa · TMS › Administración › Opciones de Tarifa › Detalle de regla de tarifa

Modelo Odoo: ``tms.pricelist.item.zone``. La línea dice cuándo aplica un precio; sus detalles fijan el importe por zona, rango y vehículo.

Línea de tarifa (tms.pricelist.item.zone)
-----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre de la línea.
   * - Tarifa / Versión
     - Relación
     - La tarifa y la versión a la que pertenece la línea. Obligatorias.
   * - Tarifa Base
     - Relación con Tarifa base
     - Qué magnitud se mide para aplicar los detalles.
   * - Aplicar
     - Selección
     - Sobre qué se calcula: Orden, Tramo, Parada o Viaje. Obligatorio.
   * - Producto
     - Relación con Producto (TMS)
     - El producto con el que se crea la línea de venta o de compra. Obligatorio.
   * - Tipo Órden, Tipo Servicio, Tipo Transportista, Tipo Destinatario, Tipo Planning, Tipo de parada, Hub
     - Relaciones
     - Las condiciones de aplicación. Vacío significa «cualquiera»; informado, la línea sólo aplica si la operación coincide.
   * - ¿Conv. vol.? / Kg x m3
     - Sí/No / Número
     - Activa el peso volumétrico: se compara el peso real con el volumen multiplicado por este factor y se tarifica el mayor.
   * - Seguimiento pasivo
     - Sí/No
     - En una tarifa de compra, si la línea sigue a la de venta.
   * - Notas
     - Texto
     - Notas internas.
   * - Detalles
     - Lista de detalles
     - Los importes.

Detalle (tms.pricelist.item.zone.detail)
----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Descripción
     - Texto
     - Texto que llevará la línea económica generada.
   * - Zonas de localización origen / destino
     - Listas de Áreas geográficas
     - Entre qué áreas de la zona de tarifa aplica el detalle. Vacío es cualquiera.
   * - Zona Geográfica
     - Relación con Área geográfica
     - Para suplementos de tipo Geo: el área extra que dispara el precio.
   * - Desde / Hasta
     - Número
     - El rango de la magnitud de la tarifa base en el que aplica el detalle.
   * - Añadir/Quitar
     - Número
     - Ajuste sobre la magnitud antes de aplicar el precio.
   * - Precio Unitario / Precio Forfait / Porcentaje
     - Importe / Importe / Número
     - El precio por unidad de la magnitud, o el precio cerrado, o el porcentaje sobre otra base.
   * - Mínimo / Máximo
     - Importe
     - Importe mínimo y máximo facturable del detalle.
   * - Aplicación del Precio
     - Selección
     - Sobre qué se aplica el precio: Peso, Volumen, Bulto, Pallets, Metros, Cantidad, Precio Forfait, Km, Horas, Reembolso, Costes de envío o Zona geográfica.
   * - Tipo Vehículo
     - Lista de Categorías de vehículo
     - Restringe el detalle a unas categorías de vehículo.
   * - Clientes / Transportistas
     - Listas de Contactos
     - Restringe el detalle a unos clientes o transportistas concretos.
   * - Producto
     - Relación con Producto
     - Producto del detalle, si difiere del de la línea. Obligatorio.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_4_economic-configuration`.
