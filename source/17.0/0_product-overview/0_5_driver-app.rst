La app del conductor
--------------------

El conductor no entra en Odoo. Trabaja con una aplicación en su móvil, Android o iPhone, que
le muestra su viaje y le pide sólo lo que hace falta en cada parada. Todo lo que hace en la
app llega al backoffice en el momento.

.. figure:: /_static/img/10_manual_app/10_2_route_01_dashboard.png
   :alt: Pantalla principal de la app del conductor con la lista de paradas
   :width: 320px

   La ruta del día: paradas ordenadas, con hora prevista y estado.

Qué hace el conductor con ella
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Ve su ruta**: las paradas del viaje en orden, con dirección, franja horaria, hora estimada
  de llegada y qué hay que cargar o entregar en cada una.
- **Avisa de que ha llegado** y de que empieza, con la posición del móvil registrada.
- **Escanea los bultos** con la cámara, uno a uno o en ráfaga, y la app le dice al instante si
  falta alguno o sobra alguno.
- **Recoge la prueba de entrega**: firma del destinatario en la pantalla o fotografía del
  albarán firmado.
- **Cobra reembolsos** y registra si se ha cobrado todo, una parte o nada.
- **Reporta incidencias**: bulto dañado, destinatario ausente, rechazo, dirección incorrecta.
  Cada incidencia lleva su motivo y, si hace falta, su foto.
- **Cierra la parada** con un resultado: completada, con reservas o fallida.

Qué recibe el backoffice
~~~~~~~~~~~~~~~~~~~~~~~~

Cada acción del conductor actualiza la Parada, el Tramo y la Orden en Odoo en el momento. El
planificador ve avanzar los viajes en pantalla, las listas cambian de color según el estado y
la puntualidad, la prueba de entrega queda adjunta a la Orden y disponible para el cliente, y
las incidencias abren el circuito que tenga configurado el proyecto. No hay que esperar a que
el conductor vuelva ni a que nadie pase datos a mano.

Cuando no hay cobertura
~~~~~~~~~~~~~~~~~~~~~~~

La app guarda lo que el conductor hace y lo envía cuando recupera la red. Si algo no llega a
Odoo, queda en una cola visible para el conductor, que puede reintentarlo. Lo que el servidor
rechaza por una regla de negocio (por ejemplo, un bulto que no pertenece a esa parada) se le
avisa al momento con un mensaje claro, para que lo corrija allí mismo.

Con la marca de la empresa
~~~~~~~~~~~~~~~~~~~~~~~~~~

El logotipo, los colores y la tipografía de la app se configuran en Odoo por compañía. El
conductor de cada empresa ve la app con la imagen de su empresa, aunque varias compartan la
misma instalación.

.. seealso::

   El :doc:`Manual del conductor </17.0/10_manual_app/index>` explica la app pantalla a
   pantalla, para entregárselo a los conductores.
