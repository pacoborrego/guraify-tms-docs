A.30 DeCA
=========

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes, bloques **DeCA** y **Parcel Service (art. 2.1.d)** · ficha del
   Proyecto, pestaña **DeCA** · TMS › Operaciones › DeCA › Documentos

Modelos Odoo: ajustes en ``res.company``, ficha en ``project.project``, documento en
``tms.deca.document`` y su línea ``tms.deca.document.line``. Qué decide el cliente y cómo
funciona: :doc:`capítulo 9 </17.0/9_deca/index>`. Varias etiquetas están en inglés en la
interfaz; se indica la española que usa esta documentación.

A.30.1 Ajustes de la compañía
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - DeCA (activar)
     - Sí/No
     - Si los Tramos de la compañía se evalúan. Apagado, nada se genera.
   * - URL pública
     - Texto
     - El origen HTTPS al que apuntan los QR. Vacío, la dirección base de Odoo. Un aviso señala
       cuando la URL en uso no es HTTPS.
   * - Desactivar la URL a los (días)
     - Número
     - Días tras el fin del servicio en que la URL del QR deja de responder (7).
   * - Retención (días)
     - Número
     - Retención mínima del documento y sus PDF (365). El control semanal cuenta, nunca borra.
   * - Bloquear la emisión tardía
     - Sí/No
     - Si solo un Responsable DeCA, con motivo, puede emitir con el servicio empezado (activo).
   * - Límite de descargas por minuto
     - Número
     - Descargas por minuto que admite un token desde una misma dirección (60; 0 desactiva).
   * - Endpoint JSON
     - Sí/No
     - Sirve también ``/deca/<token>/json`` con los datos a)–h) (apagado).
   * - Umbrales de paquetería (activar)
     - Sí/No
     - Si se evalúa la exención del art. 2.1.d con los umbrales de la compañía.
   * - Paquetería: bultos máximos / palés máximos / peso máximo por bulto (kg)
     - Número
     - Los umbrales de la condición «expedición pequeña». El peso por bulto es opcional.
   * - Paquetería: equipos de manipulación
     - Relación con Equipamiento
     - Los equipamientos del vehículo que hacen manipulable una expedición con palés
       (transpaleta).

A.30.2 Ficha DeCA del Proyecto
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - DeCA por proyecto
     - Sí/No
     - Si esta ficha manda (plan A). Apagada, el Tramo se resuelve con la regla automática.
   * - Exención
     - Selección
     - Ninguna (se evalúan las reglas), Transporte internacional (CMR), Paquetería (se evalúa el
       art. 2.1.d), Vehículo sin autorización de transporte, Exención manual.
   * - Motivo de la exención
     - Texto
     - Obligatorio con la exención manual.
   * - Umbrales de paquetería propios y sus tres cifras
     - Sí/No y números
     - Umbrales del Proyecto por encima de los de la compañía.
   * - Cargador contractual
     - Relación con Contacto
     - El cargador (letra a). En un Viaje subcontratado el cargador es siempre la propia compañía.
   * - Transportista efectivo
     - Selección (Nuestra compañía, Transportista del viaje, Automático)
     - Quién figura como transportista (letra b). Una incoherencia con el Viaje impide emitir.
   * - Marca del PDF
     - Selección (Marca de la compañía, Logotipo del cargador)
     - Con qué marca sale el PDF.
   * - Tipos de parada
     - Relación con Tipo de Parada
     - Las Paradas del Viaje despachado cuyos Tramos generan DeCA.
   * - Disparador
     - Selección (Al despachar, Manual)
     - Cuándo se genera.
   * - Emitir automáticamente
     - Sí/No
     - Si el despacho emite o solo deja borradores.
   * - Agrupación
     - Selección (Un documento por tramo, Un documento por viaje)
     - Cuántos documentos salen de un Viaje.
   * - Naturaleza de la mercancía / Observaciones por defecto / Permiso especial de circulación
     - Texto
     - Lo que se escribe en d) y h) cuando el Tramo no lo aporta.
   * - QR en el manifiesto
     - Sí/No
     - Si la hoja de ruta lleva el QR del DeCA (activo).
   * - Enviar por correo electrónico, plantilla, al transportista, al cargador, destinatarios
       extra
     - Sí/No, relaciones
     - El envío por correo de cada evento, con el PDF adjunto.
   * - Enviar por webhook, URL, autenticación, secreto, contenido, reintentos
     - Sí/No, texto, selecciones, número
     - El envío por webhook: URL HTTPS, autenticación (ninguna, token, firma HMAC-SHA256),
       contenido (solo URL, URL y PDF) y reintentos (5). El secreto solo lo ven los administradores.
   * - Enviar al emitir / al revisar / al anular
     - Sí/No
     - Qué eventos se envían (emitir y revisar, por defecto).
   * - Responsable del DeCA
     - Relación con Usuario
     - Quién recibe las actividades cuando algo falla sin nadie delante.

A.30.3 El documento y sus líneas
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Referencia
     - Texto
     - ``DECA/<año>/<número>``, de una secuencia compartida entre compañías.
   * - Estado
     - Selección
     - Borrador, Emitido, Modificado, Anulado, Caducado (la URL del QR se desactivó al cumplirse
       los días tras el fin del servicio).
   * - Cargador contractual (nombre, NIF, dirección) · Transportista efectivo (nombre, NIF)
     - Contacto y textos
     - La foto de las partes tomada al emitir.
   * - Vehículo, Matrícula, Matrícula del remolque, Fecha del transporte, Permiso especial,
       Observaciones
     - Relación, textos, fecha
     - La cabecera: f), g), e) y h). Matrícula, remolque, fecha y observaciones se pueden
       revisar.
   * - Inicio y fin del servicio
     - Fecha y hora
     - Cuándo empieza el servicio (decide la emisión tardía) y cuándo termina (decide la
       desactivación de la URL).
   * - Líneas: Expedición, Origen, Destino, Naturaleza, Peso (kg), Peso declarado (kg), Bultos,
       Palés, Entregado
     - Relaciones, textos, números
     - Una por Tramo. El peso que vale es el medido o, si falta, el declarado por un Responsable.
       Destino y peso se pueden revisar.
   * - URL pública, URL activa, Desactivada el
     - Texto, Sí/No, fecha
     - La dirección del QR y su vigencia.
   * - Emitido el / por, Revisión, PDF, SHA-256 del PDF, Prueba de emisión
     - Fecha, usuario, número, adjunto, textos
     - La evidencia de la emisión. El PDF no se regenera.
   * - Caso DeCA, Origen de la configuración, Proyecto, Viaje
     - Selecciones y relaciones
     - Con qué regla se resolvió (ficha del proyecto o regla automática) y de dónde viene.
   * - Membrete, Responsable
     - Selección y usuario
     - La marca del PDF y quién recibe los avisos.
   * - Motivo, fecha y autor de la anulación
     - Texto, fecha, usuario
     - Solo en un documento anulado.
   * - Retención hasta
     - Fecha
     - Cuándo se cumple la retención mínima.
   * - Pestañas Historial, Envíos y Accesos
     - Listas
     - Las revisiones con su PDF anterior, los intentos de correo y webhook, y las descargas
       desde la URL pública.
