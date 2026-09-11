5.7 Facturación
---------------

.. admonition:: Ruta en Odoo
   :class: tip

   Botón **Crear factura** en la Orden y en el Viaje · TMS › Administración › Transacciones
   (Líneas de Orden de Venta, Líneas de Orden de Compra, Lista de facturas)

.. CAPTURA: 5_7_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/5_operational-flows/5_7_invoicing_01_factura.png
      :alt: Facturación

      Generación de la factura al cliente y de la factura del transportista.

La facturación es el último paso del ciclo y el más cercano al Odoo estándar: las facturas son
las facturas de Odoo, con su contabilidad, sus impuestos y sus vencimientos. Lo que añade el
TMS es el punto de partida (la Orden confirmada y la :term:`Orden de compra` confirmada en el
cierre) y una forma de agrupar las líneas pensada para el transporte.

5.7.1 Factura al cliente
~~~~~~~~~~~~~~~~~~~~~~~~

Se factura desde la Orden (``sale.order``) confirmada con el botón estándar **Crear factura**,
una a una o seleccionando varias en la lista. El asistente de Odoo incorpora un campo propio,
**Modo de facturación TMS** («Modo factura» en el formulario), con dos opciones:

- **Grupo TMS por producto, servicio y zona**, la opción por defecto. Las líneas de venta de
  todas las Órdenes seleccionadas del mismo cliente se consolidan en una sola factura, con una
  línea por cada combinación de producto, servicio y zona de tarifa. El cliente recibe un
  documento compacto y cada línea de la factura conserva el enlace a las líneas de venta que la
  componen.
- **Estándar Odoo**, una factura por Orden con sus líneas tal cual.

El asistente permite además fijar la **fecha de factura**. También se puede facturar desde la
lista de **Líneas de Orden de Venta**: seleccionando líneas de varias Órdenes y pulsando
**Crear factura agrupada** se facturan solo esas líneas, siempre que pertenezcan a Órdenes
confirmadas, tengan cantidad pendiente y no estén ya facturadas. Para corregir una línea ya
facturada, **Línea de abono** genera la rectificativa.

5.7.2 Factura del transportista
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La factura del transportista (una «factura de proveedor», en el nombre nativo de Odoo) se
registra desde el Viaje (``tms.trip``) con **Crear factura**, sobre uno o varios Viajes a la
vez. El sistema exige que cada Viaje tenga su Orden de compra y que esta tenga líneas
pendientes de facturar; si alguno no cumple, lo dice y no crea nada. El cierre del Viaje ya
dejó la Orden de compra confirmada con las cantidades recibidas y a facturar fijadas, así que
la factura sale con los importes de la liquidación. La lista de **Líneas de Orden de Compra**
ofrece los mismos botones **Crear factura agrupada** y **Línea de abono** que la de venta.

5.7.3 Qué cambia al facturar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Control
     - Efecto
   * - Línea de venta ya facturada
     - No se vuelve a facturar; el sistema la rechaza.
   * - Viaje sin Orden de compra
     - No puede generar la factura del transportista.
   * - Orden de compra sin líneas pendientes
     - No procede facturar; el sistema lo indica con el nombre del Viaje.
   * - Orden o Viaje facturados
     - Quedan protegidos: no se reabren ni se vuelven a tarificar (ver
       :doc:`5_5_trip-closing`).

El **estado de facturación** queda visible en la Orden y en el Viaje, y en el indicador KPI de
la Orden (:doc:`5_8_kpi-indicators`). Con él se organiza el trabajo del cierre económico:
Órdenes confirmadas pendientes de facturar, Viajes completados pendientes de liquidar y
diagnósticos de tarifa pendientes de resolver antes de facturar (:doc:`5_6_settlement`).
Facturado el último documento, el ciclo de la Orden queda cerrado con trazabilidad completa
entre lo que se ejecutó y lo que se cobró y se pagó.
