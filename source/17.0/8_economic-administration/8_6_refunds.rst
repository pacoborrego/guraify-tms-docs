8.6 Reembolsos
--------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Administración › Reembolsos; pestaña de reembolsos de la Orden; TMS › Configuración ›
   Ajustes › Datos auxiliares › Tipos de Reembolso.

Un :term:`Reembolso` es dinero que el conductor cobra al destinatario en la entrega por cuenta
del cliente: un cobro contra entrega, una tasa, un pago acordado en el momento de recibir la
mercancía. El TMS lo trata como una entidad propia (``tms.shipment.refund``) porque su vida es
distinta de la de la Orden: hay que saber cuánto había que cobrar, cuánto cobró el conductor,
cuánto ingresó en la empresa y cuánto se ha devuelto al cliente, y dónde está cada diferencia.
La forma de cobro (efectivo, tarjeta, cheque...) se elige de un catálogo propio, los **Tipos de
Reembolso** de los datos auxiliares.

.. CAPTURA: 8_6_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/8_economic-administration/8_6_refunds_01_lista.png
      :alt: Lista de Reembolsos con estados y saldos

      Reembolsos: importe, cobrado, ingresado, pagado y los dos saldos.

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Estado
     - Significado
   * - Borrador
     - Creado con la Orden, pendiente de ejecutar. Es el único estado en que se puede borrar.
   * - En proceso
     - La Parada en la que se cobra está en ejecución.
   * - Cobrado
     - El conductor ha cobrado en la entrega y lo ha registrado en la app, con el importe real.
   * - Ingresado
     - El conductor ha entregado el dinero en la empresa.
   * - Pagado
     - Se ha devuelto al cliente.
   * - Rechazado / Cancelado
     - El destinatario no pagó, o el reembolso se anuló.

El reembolso entra en la economía por dos vías. Su importe se suma en la Orden y en el Viaje,
y las líneas de tarifa pueden aplicar un precio sobre él (aplicación del precio «Reembolso»),
que es cómo se cobra al cliente la gestión del cobro. Y el conductor lo cobra en la app al
cerrar la Parada, con el importe efectivamente recibido, que es el que arranca la cadena de
saldos. La lista de Reembolsos de Administración, con sus filtros por estado y por conductor,
es la herramienta de cuadre de caja. Campos en :doc:`/17.0/annexes/A_21_economico`.
