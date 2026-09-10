6.5 Flujos del taller
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Mantenimiento › Órdenes de trabajo (botón **Close Order**) y Carga
   masiva de service; botón **Bulk Preventive Service** en la ficha del vehículo.

Tres flujos cubren el trabajo diario del taller: cerrar una orden, registrar de una vez todos los
trabajos de un service, y dar de alta o de baja una unidad.

6.5.1 Cerrar una orden de trabajo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_5_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_5_workshop-flows_01_cerrar-orden.png
      :alt: Asistente de cierre de una orden de trabajo

      El cierre de una orden: fecha y kilometraje obligatorio.

Es el flujo crítico, porque es donde entra el kilometraje real. El mecánico abre la orden y
pulsa **Close Order**, o la arrastra a la etapa Realizada; en los dos casos aparece el asistente
de cierre con la fecha (hoy) y el **kilometraje**, obligatorio. Al confirmar:

#. El kilometraje se registra en el odómetro único como una lectura de origen Mantenimiento,
   vinculada a la orden. Pasa por la detección de anomalías como cualquier otra.
#. La orden queda en la etapa Realizada con su fecha de cierre y su kilometraje.
#. El motor recalcula las reglas de preventivo del vehículo: la del trabajo cerrado vuelve a al
   día con su nuevo último realizado, y las demás se actualizan con el kilometraje nuevo.

Si la lectura resulta anómala (un retroceso, un salto), la orden **se cierra igual**: el sistema
avisa con una notificación de que la lectura ha quedado pendiente de validar en la pantalla de
anomalías, y no bloquea al mecánico. Cerrar una orden sin vehículo (una tarea general del
taller) no pide kilometraje.

6.5.2 Carga masiva de service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_5_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_5_workshop-flows_02_carga-masiva.png
      :alt: Asistente de carga masiva de service

      La carga masiva: una fecha y un kilometraje para todos los trabajos marcados de la unidad.

Un service preventivo son muchos trabajos a la vez sobre la misma unidad. En vez de cerrar diez
órdenes, el taller usa la **Carga masiva de service**, desde el menú o desde el botón de la
ficha del vehículo: elige la unidad, la fecha y el kilometraje, y marca en la lista de sus
reglas activas qué trabajos se han hecho. Al confirmar, el sistema registra **una sola lectura
de odómetro** compartida por todos, y por cada trabajo marcado cierra una orden en Realizada con
ese kilometraje.

Dos detalles importan. Si un trabajo marcado ya tenía una orden **abierta** (el pendiente que
generó la tarea diaria), el sistema **cierra esa orden** en lugar de crear otra; si la dejara
abierta, el motor no volvería a generar nunca el pendiente de ese trabajo. Y en los trabajos
por días, la orden cerrada arranca la recurrencia nativa, de modo que Odoo crea la siguiente
con la fecha desplazada. Los trabajos sin marcar no generan nada.

6.5.3 Alta y baja de unidades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una unidad nueva es un vehículo nuevo en la Flota de Odoo, con su categoría, su matrícula y su
configuración. Para que entre en el preventivo hay que darle sus reglas, una por trabajo, en la
pantalla de Reglas de preventivo; hasta entonces el motor no la evalúa y los indicadores de
odómetro no la cuentan. La baja es el archivo del vehículo: sale de las listas, los rankings y
las alertas y conserva su historial de órdenes y lecturas. Volver a activarlo lo devuelve
todo.
