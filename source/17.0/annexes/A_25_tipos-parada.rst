A.25 Tipos de Parada
====================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › «Tipos de parada»

Modelo Odoo: ``tms.stop.type``. El papel de una Parada en la operativa: operación de hub, punto de recogida, parada de ruta, recogida o entrega directa, parada del optimizador.

Además de los campos de la tabla, el maestro lleva tres de los campos comunes a los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual) y **Compañía** (a qué compañía pertenece). El nombre debe ser único dentro de cada compañía. Las seis casillas de papel son excluyentes (marcar una desmarca las demás) y cada papel solo puede estar marcado en un registro por compañía; en la lista aparecen en modo de solo lectura y se cambian desde el formulario.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre
     - Texto
     - Nombre del tipo, tal y como aparece en las Paradas, en las listas y en la app del conductor. Es traducible.
   * - Descripción
     - Texto
     - Descripción del papel. Obligatoria y traducible.
   * - Imagen
     - Imagen
     - Icono del tipo, que se muestra en las listas de Paradas y en la app del conductor.
   * - Operaciones de Hub
     - Sí/No
     - Papel de entrada o salida de mercancía en un hub. Lo reciben los lados de hub de las entregas y las recogidas.
   * - Punto de Recogida
     - Sí/No
     - Papel de carga de una recogida a domicilio en el punto de recogida del Proyecto.
   * - Parada de Ruta
     - Sí/No
     - Papel de parada en casa del cliente: la que se planifica, se asigna a un Viaje, se envía a una agencia y se reprograma.
   * - Recogida Directo
     - Sí/No
     - Papel de carga de un servicio directo. La etiqueta de la interfaz es «Recogida Directo».
   * - Entrega Directo
     - Sí/No
     - Papel de descarga de un servicio directo. La etiqueta de la interfaz es «Entrega Directo».
   * - Paradas Optimizador
     - Sí/No
     - Papel de las paradas de inicio y fin que genera el optimizador. No son eventos ejecutables y quedan fuera de la secuenciación y de los documentos de carga.
   * - Arrival Geofence (m)
     - Número entero
     - Radio en metros alrededor de la Parada que se considera llegada para el conector de telemática. A cero, se usa el radio de la política operativa. La etiqueta está sin traducir.
   * - Información
     - Texto
     - Notas internas de parametrización.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`; cómo se asigna el tipo al validar la Orden, :doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`.
