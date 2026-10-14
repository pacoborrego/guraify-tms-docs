7.9 Acceso de clientes y transportistas
---------------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › bloque **Audiencias externas**: **Política de campos del
   portal** y **Recalcular audiencias** · contacto › pestaña Propiedades TMS › **Audiencia del
   portal** · portal: ``/my/inboxes``

Un cliente o un transportista puede entrar en Odoo como **usuario de portal**: con su usuario y su
contraseña, sin acceso al resto del sistema, viendo solo lo suyo. Este apartado explica qué hay
preparado para que eso sea seguro y qué se puede usar hoy.

7.9.1 Estado
~~~~~~~~~~~~

**Hoy ningún cliente tiene acceso al portal.** Lo que existe:

- El **portal de Bandejas de entrada API** (``tms_portal``, 7.9.5): el cliente que envía por API
  ve lo que ha llegado, lo rechazado y los manifiestos generados. Es lo único que el portal pinta
  hoy.
- El **aislamiento** (7.9.2 a 7.9.4): reglas que limitan lo que cada usuario externo puede leer y
  la lista blanca de campos que se le pueden enseñar. Están hechas, probadas y activas, y son la
  base sobre la que leerá la torre de control; ninguna pantalla del portal las usa todavía para
  enseñar Órdenes, Viajes o Paradas.

7.9.2 La audiencia de cada contacto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La **Audiencia del portal** de una empresa dice qué es para el TMS: **Cliente**, **Transportista**,
**Ambos** o **Ninguno**. Se calcula sola:

- Cada noche, una tarea programada la recalcula para toda la base: quien tiene Órdenes del TMS es
  cliente; quien ha hecho Viajes o Tramos en los últimos **24 meses** (parámetro
  ``tms.portal_audience_months``), transportista.
- Asignar un transportista a un Viaje o a un Tramo le da la audiencia **en el acto**, para que un
  transportista nuevo no espere a la noche. Quitarla es cosa del recálculo nocturno.
- **Recalcular audiencias › Recalcular ahora**, en Ajustes, lanza el recálculo a mano.
- **Audiencia del portal (manual)**, en la ficha, la fuerza: gana a la calculada.

Las dos solo las ven los responsables. La audiencia se guarda en la empresa: un contacto de esa
empresa usa la de su empresa.

7.9.3 Qué puede leer cada audiencia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un usuario de portal solo lee (nunca crea, cambia ni borra) y solo lo de **su empresa**:

.. list-table::
   :header-rows: 1
   :widths: 26 37 37

   * - Qué
     - Un cliente ve
     - Un transportista ve
   * - Órdenes
     - Las suyas (solo las del TMS)
     - Ninguna
   * - Tramos, Paradas, Bultos, Reembolsos
     - Los de sus Órdenes
     - Los de sus Viajes y los que transporta
   * - Viajes
     - Los que llevan sus Paradas
     - Los suyos
   * - Trazabilidad
     - Solo los apuntes marcados para enseñar al cliente
     - La de lo que transporta
   * - Facturas
     - Las suyas, sin borradores (regla de Odoo)
     - Las suyas, sin borradores (regla de Odoo)
   * - Órdenes de compra
     - —
     - Las suyas (regla de Odoo)

Dos límites que conviene saber:

- **Los adjuntos no se sirven por el portal**: Odoo exige un usuario interno para leer un
  adjunto, y ninguna regla lo cambia. Las fotos y firmas de la prueba de entrega tendrán que
  servirse por otra vía cuando haga falta enseñarlas.
- **Proyectos**: con ``tms_portal`` instalado, un usuario de portal ve todos los Proyectos cuyo
  cliente es su empresa, aunque no los siga. Se ha dejado así a propósito.

7.9.4 La lista blanca de campos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 7_9_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_9_external-access_01_politica-campos.png
      :alt: Lista de la política de campos del portal agrupada por modelo

      Política de campos del portal: qué campo de qué modelo se enseña a cada audiencia.

Que un usuario externo pueda leer un registro no significa que deba ver todos sus campos: un
cliente no tiene por qué ver el coste ni el margen de su Orden, ni un transportista quién paga el
envío. La **Política de campos del portal** dice, modelo a modelo y para cliente y para
transportista, qué campos se pueden enseñar.

- **Falla cerrada**: un modelo o una audiencia que no está en la lista no enseña nada más que el
  identificador. Añadir un campo nuevo a un modelo no lo expone nunca por descuido.
- Viene sembrada con **340 filas** sobre seis modelos. Fuera, siempre: coste, margen, tarifa de
  compra, rentabilidad y los importes de venta de la Orden (el cliente ve el dinero en sus
  facturas). El transportista no recibe ni quién paga ni ningún importe.
- **Para quitar un campo se desmarca Permitido; no se borra la fila.** La semilla se repone en
  cada actualización del módulo y volvería a crear la fila borrada, pero no toca una desmarcada.
- Quien sirva datos a un externo (el portal, la torre) tiene que pasar por esta lista antes de
  enviarlos. **Hoy no la usa ninguna pantalla**: está preparada para la torre de control.

7.9.5 Dar acceso a un cliente: el portal de Bandejas de entrada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Con ``tms_portal`` instalado, el cliente que envía Órdenes por API
(:doc:`/17.0/3_functional-architecture/3_2_4_api-inbox`) puede ver en el portal sus **Bandejas de
entrada**: cada una con lo **recibido**, lo **rechazado** con su motivo, el detalle de cada línea y
los **manifiestos** que se generaron. Así comprueba él mismo si un envío llegó y por qué se
rechazó.

#. En el contacto de la empresa del cliente, o en el de la persona que va a entrar, **conceder
   acceso al portal** (la acción de Odoo en el contacto). Odoo envía la invitación para que cree
   su contraseña.
#. Comprobar que la empresa tiene su **audiencia** (7.9.2) y Proyectos con Bandeja de entrada.
#. El cliente entra en ``/my`` y ve la tarjeta de sus Bandejas de entrada (``/my/inboxes``).

Lo que el cliente ve en el portal sale de las reglas, no de filtros de cada página: si una regla
dejara de cubrir un modelo, el fallo se vería en las pruebas de aislamiento del módulo, que
recorren el portal como un usuario real de una empresa y comprueban que no aparece nada de otra.
