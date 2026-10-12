9.6 Operación diaria y despliegue
---------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › DeCA: **Documentos**, **Tramos sin DeCA**, **Envíos** y **Registro de
   accesos** (los dos últimos, Responsable DeCA) · TMS › Configuración › Técnico › Acciones
   programadas

9.6.1 El día a día
~~~~~~~~~~~~~~~~~~

Con la ficha configurada, el DeCA no pide trabajo: despachar el Viaje lo emite y lo envía. Lo que
el equipo mira es:

- **Tramos sin DeCA**, agrupados por Viaje: los Tramos obligados sin documento vigente o con el
  documento desactualizado, con el motivo. Es la lista que hay que dejar vacía antes de que
  salgan los Viajes del día; una **alerta diaria** avisa al Responsable DeCA de los Tramos de
  hoy que siguen sin DeCA.
- **Documentos**, con los filtros *Por emitir* (borradores que el despacho dejó sin emitir),
  *Emitidos hoy*, *Revisados*, *Anulados*, *Caducados*, *URL activa* y *Envío fallido*, y
  agrupados por transportista, estado, fecha, caso o Viaje.
- **Envíos**: cada intento de correo o webhook, con su resultado, para saber si el cliente
  recibió lo suyo.

Cinco tareas programadas sostienen el ciclo: la emisión en cola (que el despacho despierta; su
intervalo de diez minutos es la red de seguridad), el envío de correos y webhooks (igual, cada
cinco minutos), la desactivación diaria de las URL cuyo servicio terminó, el control semanal de
retención (cuenta, nunca borra) y la alerta diaria de Tramos sin DeCA. Con la tarea de emisión
apagada el despacho emite en línea; con la de envío apagada, los envíos esperan.

9.6.2 Lo que tiene que haber en el servidor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El PDF se emite igual en cualquier instalación; lo que necesita el servidor es que **el QR
funcione en carretera**. El detalle, con los ejemplos de configuración, está en el ``README`` del
módulo; lo que un administrador tiene que tener delante:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Qué
     - Por qué
   * - Una sola base por dominio (``db_name`` o ``dbfilter``)
     - El inspector llega sin sesión: Odoo elige la base solo por la configuración. Si ve varias
       y ningún filtro deja exactamente una, toda URL ``/deca/…`` responde «no existe».
   * - ``proxy_mode`` detrás del proxy inverso, que reenvíe las cabeceras de origen
     - El límite de descargas es por dirección del cliente y el registro de accesos guarda esa
       dirección; sin él, todos los inspectores comparten la IP del proxy.
   * - Dominio público en HTTPS con certificado válido (Ajustes › TMS › DeCA › URL pública)
     - Es lo que va dentro del QR y lo que la norma exige. Se fija antes de emitir el primero.
   * - ``/deca/*`` sin nada delante
     - Ni autenticación, ni captcha, ni redirección a login, ni caché del PDF, ni geobloqueo. El
       límite de frecuencia lo pone Odoo.
   * - ``wkhtmltopdf`` 0.12.6 con Qt parcheado y una tipografía del sistema (Arial, Helvetica o
       Liberation Sans)
     - Sin él la emisión falla con un error claro y el documento se queda en borrador.

Tras desplegar, se comprueba desde fuera de la red con un documento emitido: la URL devuelve el
PDF cuya huella coincide con la del documento, un token inventado da «no existe», y el acceso
aparece en la pestaña Accesos con la dirección pública desde la que se hizo.

9.6.3 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Concepto
     - Modelo o campo
   * - El documento, sus líneas, sus revisiones, sus envíos y sus accesos
     - ``tms.deca.document``, ``tms.deca.document.line``, ``tms.deca.document.revision``,
       ``tms.deca.delivery.log``, ``tms.deca.access.log``
   * - Estados del documento
     - ``state``: ``draft``, ``issued``, ``modified``, ``cancelled``, ``expired``
   * - La obligación en el Tramo
     - ``tms.shipment.leg``: ``deca_required``, ``deca_required_reason``, ``deca_exemption``,
       ``deca_manual_exemption``, ``deca_operation_type``, ``deca_document_id``,
       ``deca_state``; en vivo, ``deca_missing`` y ``deca_missing_reason``
   * - Caso y origen de la configuración
     - ``deca_case`` (``direct_own``, ``direct_subcontracted``, ``operator_own``,
       ``operator_subcontracted``), ``deca_config_source`` (``project`` plan A, ``default``
       plan B)
   * - Vehículo ajeno a la flota
     - ``tms.trip``: ``deca_external_plate``, ``deca_external_trailer_plate``,
       ``deca_external_equipment_ids``
   * - Ficha del Proyecto y ajustes de la compañía
     - ``project.project.deca_*``, ``res.company.deca_*``
       (:doc:`/17.0/annexes/A_30_deca`)
   * - Permisos
     - grupos ``tms_deca.group_deca_user`` y ``tms_deca.group_deca_manager``
   * - URL pública
     - ``GET`` / ``HEAD`` ``/deca/<token>`` (público; ``/deca/<token>/json`` si el endpoint JSON
       está activo)
   * - Tareas programadas
     - «DeCA: issue queued documents», «DeCA: send e-mails and webhooks», «DeCA: deactivate
       expired URLs», «DeCA: retention check», «DeCA: alert on today's legs without a DeCA»
   * - Secuencia de referencias
     - ``DECA/<año>/<número>``, compartida entre compañías
