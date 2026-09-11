La app del conductor
--------------------

El conductor no entra en Odoo. Trabaja con una aplicación en su móvil, Android o iPhone, que
le muestra su Viaje y le pide solo lo que hace falta en cada Parada.

.. figure:: /_static/img/10_manual_app/10_2_route_01_dashboard.png
   :alt: Pantalla principal de la app del conductor con la lista de paradas
   :width: 320px

   La pantalla principal: las Paradas del Viaje en orden, con hora prevista y estado.

Qué hace el conductor con ella
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Ve su Viaje**: las Paradas en orden, con dirección, franja horaria, hora estimada de
  llegada y qué hay que cargar o entregar en cada una.
- **Avisa de que ha llegado** y de que empieza la carga o la entrega, con la posición del
  móvil registrada.
- **Escanea los Bultos** con la cámara, uno a uno o en ráfaga, y la app le dice al instante si
  falta alguno o sobra alguno.
- **Recoge la prueba de entrega (POD)**: firma del destinatario en la pantalla o fotografía
  del albarán firmado.
- **Cobra reembolsos** y registra si se ha cobrado todo, una parte o nada.
- **Reporta incidencias**: bulto dañado, destinatario ausente, rechazo, dirección incorrecta.
  Cada incidencia lleva su motivo y, si hace falta, su foto.
- **Cierra la Parada** con un resultado: Completada, Con reservas o Fallida.

Qué recibe la oficina
~~~~~~~~~~~~~~~~~~~~~

Cada acción del conductor actualiza la Parada, el Tramo y la Orden en Odoo en el momento. El
planificador ve avanzar los Viajes en pantalla, las listas cambian de color según el estado y
la puntualidad, la POD queda adjunta a la Orden y disponible para el cliente, y las
incidencias quedan registradas en la Parada con su motivo, para que la oficina actúe. No hay
que esperar a que el conductor vuelva ni a que nadie pase datos a mano.

Cuando no hay cobertura
~~~~~~~~~~~~~~~~~~~~~~~

La app guarda lo que el conductor hace y lo envía cuando recupera la red. Si algo no llega a
Odoo, queda en una cola visible para el conductor, que puede reintentarlo. Lo que Odoo no
acepta (por ejemplo, un bulto que no pertenece a esa Parada) se le indica al instante con un
mensaje claro, para que lo corrija allí mismo.

Con la marca de la empresa
~~~~~~~~~~~~~~~~~~~~~~~~~~

El conductor ve la app con el logotipo y los colores de su empresa, aunque varias compartan la
misma instalación (ver :doc:`Qué incluye <0_4_what-it-includes>`).

.. seealso::

   El :doc:`Manual del conductor </17.0/10_manual_app/index>` explica la app pantalla a
   pantalla, para entregárselo a los conductores.
