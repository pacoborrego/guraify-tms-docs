11.1 Qué es y qué no hace todavía
---------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › **Avisos**: Workflows, Mensajes enviados, Enlaces de seguimiento ·
   pestaña **Avisos** de la Orden · grupo **AVISOS** de la pestaña Propiedades TMS del contacto

Un :term:`Aviso` es un mensaje automático sobre una entrega concreta. Lo dispara un evento de la
Parada (se planifica, el conductor llega, se entrega) o una hora (el día anterior, cuando el ETA
está cerca), lo decide un :term:`Flujo de aviso` y lo envía una tarea programada por el canal que
toque. Cada aviso, enviado o no, queda como una fila en la Orden, con su estado y, si no salió, el
motivo.

11.1.1 Los quince disparadores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Disparador (en la interfaz)
     - Cuándo salta
   * - Orden recibida
     - Cuando existe la Parada de la Orden, que es cuando el pedido se convierte en un transporte
       (puede ser minutos después de recibirse).
   * - Planificado para una fecha
     - Cuando la Parada entra en un Viaje.
   * - Viaje iniciado
     - En un lote diario, a la hora del flujo (20:00 por defecto), sobre los Viajes despachados
       ese día; se repite cada hora las veces que diga el flujo para los despachados después.
   * - Eres el siguiente
     - Cuando el conductor cierra una Parada, al Destinatario de la siguiente.
   * - ETA dentro de N minutos
     - Cuando el ETA de la Parada está a menos de N minutos. No con un ETA caducado.
   * - Vehículo llegado
     - Cuando el conductor marca que está en la Parada.
   * - Entregado · Entregado con reservas · Orden Fallida · Reprogramado · Devuelto
     - Cuando la Parada se cierra con ese resultado, desde la app o desde la oficina.
   * - Dirección cambiada
     - Cuando cambia la dirección de la Parada.
   * - El día anterior
     - A la hora del flujo (18:00 por defecto), sobre las Paradas del día siguiente.
   * - Reembolso pendiente
     - En un barrido diario, a la hora del flujo (9:00 por defecto), sobre las Paradas con un
       Reembolso sin cobrar; se repite cada día hasta que se cobra.
   * - Prueba de entrega disponible
     - Cuando la app sube una prueba de entrega del tipo que diga el flujo (por defecto, la
       firma). Una foto no es una prueba de entrega, ni lo que se sube a mano desde la oficina.

Los quince están en el selector; el sistema no envía ninguno hasta que alguien crea su flujo.

11.1.2 Lo que todavía no hace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **La página del enlace de seguimiento no existe.** Cada aviso puede llevar un enlace personal
  (``https://<dominio>/t/<código>``) y el TMS lo genera, lo guarda, lo caduca y cuenta sus
  accesos, pero la página que debería abrir es de la torre de control, que no está terminada. Hasta
  entonces, conviene desmarcar **Enlace de seguimiento** en los flujos o no poner la variable en la
  plantilla.
- **La cuenta real de WhatsApp está pendiente.** El canal se ha probado de punta a punta con la
  cuenta de pruebas de Meta; para producción hay que registrar un número en la cuenta real de la
  compañía y volver a aprobar las plantillas en ella (:doc:`11_2_channels`).
- **Algunas pantallas salen en inglés**: el menú **Workflows** y los campos de Esendex en Ajustes.
