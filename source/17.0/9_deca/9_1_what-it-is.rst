9.1 Qué es y a quién obliga
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › DeCA · pestaña **DeCA** del Tramo · botón **Emitir DeCA del viaje** del
   Viaje

El :term:`DeCA` es el documento de control que la Orden FOM/2861/2012 exige en el transporte
público de mercancías por carretera en España. Desde el **5 de octubre de 2026**, por la
Resolución de 5 de junio de 2026, tiene que ser **electrónico**: un PDF de como mucho 5 MB con un
**código QR** que lleve a una dirección pública desde la que descargarlo, generado **antes de que
empiece el servicio**, con cada versión conservada cuando se modifica, y guardado al menos **un
año**. El conductor no lleva papel: el inspector escanea el QR y descarga el documento.

9.1.1 El Tramo es la carta de porte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En el TMS no hay que teclear un DeCA: el :term:`Tramo` ya es la carta de porte, el movimiento de
una mercancía de un punto de carga a uno de descarga. El documento se monta con lo que el Tramo y
su Viaje ya saben, y lo que la norma pide en sus ocho letras sale de ahí:

.. list-table::
   :header-rows: 1
   :widths: 10 36 54

   * - Letra
     - Dato
     - De dónde sale
   * - a)
     - **Cargador contractual**: quien contrata el transporte
     - La configuración (9.2): la propia compañía cuando subcontrata, el operador logístico o el
       cliente cuando transporta con flota propia
   * - b)
     - **Transportista efectivo**: quien lo ejecuta
     - El transportista del Viaje; la propia compañía, si es flota propia
   * - c)
     - Origen y destino
     - Los contactos de carga y descarga del Tramo, con su dirección
   * - d)
     - Naturaleza y **peso bruto** de la mercancía
     - Las categorías de carga del Tramo (o lo que diga el Proyecto) y el peso del Tramo en kilos;
       bultos y palés acompañan como información
   * - e)
     - Fecha del transporte
     - La del Viaje
   * - f), g)
     - Matrícula del vehículo y del remolque
     - El vehículo y los remolques del Viaje; si el Viaje lo hace un vehículo ajeno a la flota, las
       matrículas externas que se anotan en el Viaje
   * - h)
     - Permiso especial de circulación y observaciones
     - La ficha DeCA del Proyecto

Un DeCA puede recoger **un Tramo o varios del mismo Viaje**: «agrupar» es llevar en un documento
los Tramos que comparten cargador, transportista y Proyecto, cada uno como una línea con su origen,
su destino y su peso. La cabecera (quién, con qué y cuándo) sale del Viaje; cada línea, de su
Tramo. Un Tramo directo con dos Paradas es una sola línea.

9.1.2 Quién lo usa
~~~~~~~~~~~~~~~~~~

Dos permisos propios, dentro de los del TMS. El **Usuario DeCA** ve los documentos, genera
borradores, los emite y los descarga. El **Responsable DeCA** configura la ficha de los Proyectos y
hace lo que deja huella legal: declarar un peso que falta, emitir tarde con un motivo, revisar,
anular y desactivar una URL. El responsable del TMS es también Responsable DeCA. La ficha DeCA de
un Proyecto solo la edita un Responsable, y eso lo comprueba el servidor, no solo la pantalla.

Lo que el módulo **no** hace: no sustituye a la carta de porte internacional (CMR), que es una
exención; no decide por sí solo qué es paquetería (aplica el criterio literal del Ministerio, con
los umbrales que cada compañía fija, ver :doc:`9_3_obligation`); y no borra nunca un documento,
ni siquiera anulado.
