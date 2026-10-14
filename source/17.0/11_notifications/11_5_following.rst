11.5 Seguir los avisos
----------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Orden › botón y pestaña **Avisos** · TMS › Configuración › Avisos › **Mensajes enviados** y
   **Enlaces de seguimiento** · TMS › Métricas › KPIs

.. CAPTURA: 11_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/11_notifications/11_5_following_01_pestana-avisos.png
      :alt: Pestaña Avisos de una Orden con sus mensajes y estados

      La pestaña Avisos de la Orden: qué se dijo, a quién, por qué canal y cómo acabó.

Cada aviso, haya salido o no, es una fila que se ve en la pestaña **Avisos** de su Orden (y en el
botón **Avisos** de la cabecera) y en la lista **Mensajes enviados**, que abre por defecto con los
de hoy. La fila dice el disparador, el canal, el contacto, a qué número o correo, el estado y,
si no salió, el motivo.

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Estado
     - Qué significa
   * - En cola
     - Esperando a la tarea programada, que pasa cada minuto.
   * - Retenido
     - Cayó en el horario de silencio; sale cuando termina.
   * - Enviado · Entregado · Leído · Respondido
     - Salió. En WhatsApp, Odoo recibe de Meta la entrega, la lectura y la respuesta; en SMS, la
       entrega la consulta la tarea de Esendex.
   * - Fallido
     - El canal lo rechazó; el error está en la ficha (una plantilla de WhatsApp sin aprobar, un
       número que el canal no acepta).
   * - Omitido
     - No se envió, con su motivo: los del destinatario (:doc:`11_4_recipient`), **Ya avisado**
       (dentro del tiempo de no repetir), **Horario de silencio** (si el flujo omite),
       **Canal no instalado**, **No está en la lista blanca de pruebas** (:doc:`11_6_go-live`).

**Reintentar**, en la lista o en la ficha, vuelve a poner en cola un aviso fallido u omitido una
vez corregida la causa. **Abrir la orden** lleva a la Orden en su formulario del TMS.

**Enlaces de seguimiento.** Cada Orden con avisos que lo llevan tiene su enlace, que dura 30 días
desde la fecha de la entrega, se puede revocar y cuenta cuántas veces se ha abierto. Se ve en la
misma pestaña Avisos y en la lista Enlaces de seguimiento. La página que abre todavía no existe
(:doc:`11_1_what-it-is`).

**La alarma de la cola.** El motor de indicadores
(:doc:`/17.0/8_economic-administration/8_8_control-reporting`) trae dos indicadores, solo para el
equipo interno: **Avisos atascados en cola**, los avisos que llevan más de 10 minutos en cola, con
objetivo cero; y **Avisos enviados**, el total del periodo. Si el primero no es cero, la tarea
programada no está corriendo y nadie está recibiendo nada: es la alarma que hay que mirar.
