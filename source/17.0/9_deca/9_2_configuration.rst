9.2 Configuración
-----------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes, bloques **DeCA** y **Parcel Service (art. 2.1.d)** · ficha del
   Proyecto, pestaña **DeCA** (solo Responsable DeCA). Algunas etiquetas están en inglés en la
   interfaz.

La configuración tiene dos niveles. La **compañía** dice si usa el DeCA y fija lo que es igual
para todos sus documentos. El **Proyecto** puede llevar una **ficha DeCA** que manda sobre lo que
el sistema deduciría por sí solo; sin ficha, decide la **regla automática**. Quien configura solo
decide dos cosas de verdad: quién es el cargador y quién el transportista en cada operativa, y
qué Proyectos son paquetería.

9.2.1 La compañía
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Activar el DeCA
     - Con la casilla apagada ningún Tramo de la compañía está obligado y nada se genera: una
       compañía que no opera en España no nota el módulo.
   * - URL pública
     - El origen HTTPS al que apuntan los QR (``https://deca.miempresa.es``). Vacía, se usa la
       dirección base de Odoo. Se fija **antes** de emitir: la URL va dentro del QR del PDF, que
       no se regenera; cambiarla después deja los QR impresos apuntando al dominio viejo. Una
       URL que no sea HTTPS se acepta para trabajar en local, con aviso.
   * - Desactivar la URL a los N días
     - Cuántos días después del fin del servicio deja de responder la URL del QR (7 por defecto).
       El documento y el PDF se conservan.
   * - Retención (días)
     - Cuánto se guarda como mínimo el documento y sus PDF (365 por defecto, lo que exige la
       norma). Una tarea semanal cuenta lo que ha cumplido la retención; **nunca borra**.
   * - Bloquear la emisión tardía
     - Si un DeCA se puede emitir una vez empezado el servicio. Activo por defecto: solo un
       Responsable DeCA puede emitir tarde, dejando el motivo en el historial.
   * - Límite de descargas por minuto
     - Cuántas veces por minuto se puede descargar un documento desde su URL antes de que el
       sistema responda «vuelve en un minuto» (60 por defecto; 0 lo desactiva). Protege el
       servidor sin estorbar a un inspector.
   * - Umbrales de paquetería y equipos de manipulación
     - Si la compañía aplica la exención de paquetería (art. 2.1.d) y con qué cifras: bultos y
       palés máximos por expedición, peso máximo por bulto (opcional) y qué equipamientos del
       vehículo cuentan como medios de manipulación de palés (una transpaleta). Sin la casilla,
       ningún Proyecto queda exento por paquetería salvo que lleve sus propios umbrales.
   * - Endpoint JSON
     - Sirve también los datos a)–h) en formato de datos, para la futura obligación europea
       (eFTI). Apagado por defecto.

9.2.2 La ficha DeCA del Proyecto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 9_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/9_deca/9_2_configuration_01_ficha-proyecto.png
      :alt: Pestaña DeCA de un Proyecto

      La ficha DeCA de un Proyecto: cargador, transportista efectivo, disparo, agrupación y envío.

El Proyecto de la Orden (no el del transportista) puede llevar una ficha DeCA. Con la casilla
**DeCA por proyecto** encendida, la ficha manda; apagada, el Tramo se resuelve con la regla
automática de 9.2.3. Lo que decide la ficha:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Exención
     - Ninguna (se evalúan las reglas), transporte internacional (CMR), paquetería (se evalúa el
       art. 2.1.d con los umbrales de la ficha o de la compañía), vehículo sin autorización de
       transporte, o exención manual con su motivo. Una exención fija exime a todos los Tramos
       del Proyecto.
   * - Umbrales de paquetería propios
     - Bultos y palés máximos y peso por bulto del Proyecto, por encima de los de la compañía.
   * - Cargador contractual
     - El contacto que figura como cargador (letra a). Si el Viaje está subcontratado, el
       cargador es siempre la propia compañía, porque es quien contrata al transportista
       efectivo, aunque la ficha nombre a otro.
   * - Transportista efectivo
     - **Nuestra compañía** (flota propia), **el transportista del Viaje** o **automático**
       (según el Viaje). Una ficha que diga «nuestra compañía» en un Viaje subcontratado, o al
       revés, no emite: el documento señala la incoherencia con el Proyecto, el Viaje y el
       transportista.
   * - Marca del PDF
     - Si el PDF lleva la marca de la compañía o el logotipo del cargador (el operador
       logístico, como la hoja de ruta).
   * - Tipos de parada
     - Qué Paradas del Viaje despachado hacen que sus Tramos generen DeCA (las de entrega, las
       de recogida…).
   * - Disparador y Emitir automáticamente
     - **Al despachar** el Viaje (por defecto) o solo **a mano**. Con *Emitir automáticamente*,
       el despacho emite; sin ella, deja borradores para que alguien los revise y emita.
   * - Agrupación
     - **Un documento por Tramo** o **un documento por Viaje** (un DeCA con todos los Tramos del
       Viaje que compartan cargador, transportista y Proyecto).
   * - Naturaleza, observaciones y permiso especial
     - Lo que se escribe en d) y h) cuando el Tramo no lo dice: la naturaleza por defecto de la
       mercancía (si el Tramo no tiene categorías de carga), las observaciones y el permiso
       especial de circulación.
   * - QR en el manifiesto
     - Si la hoja de ruta del Viaje lleva el QR del DeCA en su cabecera (:doc:`9_5_outputs`).
   * - Envío por correo y por webhook
     - A quién se manda el documento al emitirlo, revisarlo o anularlo: al transportista, al
       cargador y a otros contactos, con una plantilla de correo; y a una dirección web del
       cliente, con autenticación (ninguna, token o firma HMAC), con la URL sola o con el PDF
       dentro, y un número de reintentos.
   * - Responsable del DeCA
     - El usuario que recibe una actividad cuando algo falla sin nadie delante: una emisión en
       cola que no sale, un Viaje despachado con Tramos sin DeCA, un despacho revertido con
       documentos vigentes.

9.2.3 La regla automática
~~~~~~~~~~~~~~~~~~~~~~~~~

Sin ficha, el sistema deduce cargador y transportista del Viaje y de la planificación de la
Orden, y clasifica el Tramo en uno de cuatro **casos**:

.. list-table::
   :header-rows: 1
   :widths: 34 22 22 22

   * - Situación
     - Transportista efectivo
     - Cargador contractual
     - Caso
   * - El Viaje lo hace un transportista externo
     - El del Viaje
     - La propia compañía
     - Cliente directo u operador logístico, subcontratado
   * - Flota propia y la planificación tiene un operador logístico que no somos nosotros
     - La propia compañía
     - El operador
     - Operador logístico, flota propia
   * - Flota propia sin operador
     - La propia compañía
     - El cliente de la Orden
     - Cliente directo, flota propia

Flota propia es el transportista marcado como tal o el contacto de la propia compañía. Un Viaje
**sin transportista** no tiene caso ni partes: el Tramo sigue siendo obligado y no se puede
generar hasta asignarlo (con una ficha que diga «nuestra compañía» sí, porque el transportista se
conoce sin Viaje). Sin ficha, la agrupación es un documento por Tramo, no se envía nada por correo
ni webhook, y la hoja de ruta lleva el QR.

Campos de la ficha, de la compañía y del documento en :doc:`/17.0/annexes/A_30_deca`.
