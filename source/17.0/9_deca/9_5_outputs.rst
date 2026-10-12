9.5 Salidas: el PDF, la URL pública, el envío y la hoja de ruta
---------------------------------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Botones **Descargar PDF**, **Reenviar** y **Desactivar URL** del documento · pestañas
   **Envíos**, **Historial** y **Accesos** · Imprimir › Manifiesto de transporte del Viaje

9.5.1 El PDF
~~~~~~~~~~~~

.. CAPTURA: 9_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/9_deca/9_5_outputs_01_pdf.png
      :alt: PDF de un DeCA emitido con su QR

      El DeCA emitido: datos del transporte, QR, cargador, transportista y las expediciones.

El documento es un PDF A4 vertical, en español, con el orden que fija la Resolución: título y
referencia, datos del transporte (fecha, matrículas, permiso especial), el **QR** de 40 mm con la
URL escrita debajo, cargador, transportista, las expediciones con origen, destino, naturaleza y
peso, los totales, las observaciones, la fecha de emisión (y la de la última modificación), el
historial de revisiones, la nota legal y el pie. Lleva el membrete que diga la ficha del Proyecto
(la marca de la compañía o el logotipo del cargador). Se genera con tipografías del sistema y
todo lo que necesita dentro, para que salga igual tenga o no el servidor acceso a nada más.

El PDF emitido es **inmutable**: es un adjunto que no se vuelve a generar, que nadie puede borrar
ni sustituir, con su huella (SHA-256) y la prueba de emisión guardadas en el documento. **Descargar
PDF** devuelve ese fichero. Una revisión guarda el PDF anterior en el historial y genera el nuevo;
el documento guarda ambos.

9.5.2 La URL pública
~~~~~~~~~~~~~~~~~~~~

El QR lleva a ``https://<dominio>/deca/<token>``. Esa dirección es **pública y el token es toda
la autorización**, como exige la norma: el inspector la abre sin credenciales, sin cookies y sin
nada que ejecutar, y recibe el PDF guardado, nunca uno nuevo. Responde «no existe» a un token
desconocido, «documento anulado» o «URL desactivada» cuando toca, y «vuelve en un minuto» por
encima del límite de descargas por token y dirección. Cada descarga queda en la pestaña
**Accesos** del documento (fecha, dirección, navegador, resultado).

La URL deja de responder sola a los N días del fin del servicio (ajuste de la compañía), o a
mano con **Desactivar URL** (Responsable DeCA). El documento y el PDF se conservan hasta cumplir
la retención.

9.5.3 El envío
~~~~~~~~~~~~~~

Si la ficha del Proyecto lo pide, emitir, revisar o anular un DeCA lo **envía** a quien tenga que
llevarlo: por **correo** al transportista, al cargador y a los contactos que se indiquen, con el
PDF guardado adjunto; y por **webhook** a la dirección del cliente, con la URL sola o con el PDF
dentro, autenticado con un token o una firma HMAC. Nada sale en el momento: cada evento deja un
intento en la pestaña **Envíos** y una tarea programada lo manda en los segundos siguientes; un
webhook que falla se reintenta con esperas crecientes hasta el número de reintentos de la ficha
y, si se rinde, lo anota en el historial. Un envío fallido **no toca el documento**. **Reenviar**
repite el envío del evento vigente (uno por canal cada minuto). Sin ficha de Proyecto no se envía
nada: el documento se descarga desde Odoo o desde su URL.

9.5.4 La hoja de ruta
~~~~~~~~~~~~~~~~~~~~~

La hoja de ruta del Viaje (Imprimir › Manifiesto de transporte, ver
:doc:`/17.0/5_operational-flows/5_4_app-execution`) es de todo el TMS y no sabe nada del DeCA.
Cuando la compañía del Viaje tiene el DeCA activo, el módulo le añade lo suyo: el DeCA del Viaje
y su **QR** en la cabecera (si la ficha del Proyecto lo pide), las tarjetas del cargador y del
transportista, una columna **DeCA** por línea con «Exento» o «DeCA pendiente» donde corresponda,
las letras a)–h) junto a cada dato, el permiso especial, las observaciones y la nota legal; y la
hoja sale en el idioma del DeCA. Es lo que el conductor lleva en la cabina cuando no hay
smartphone, y lo que el muelle imprime al despachar.
