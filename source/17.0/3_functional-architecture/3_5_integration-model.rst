3.5 Modelo de integración
-------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI

El modelo de integración define los mecanismos mediante los cuales el TMS intercambia
información con sistemas externos: la entrada de demanda por fichero o por API, el envío de
estados y documentos a los sistemas de los clientes y la recepción de eventos de plataformas
logísticas. Lo que entra se convierte directamente en Órdenes, Tramos y Paradas, y lo que sale
se construye a partir de esas mismas entidades. Los canales y su encuadre tecnológico están en
:doc:`/17.0/1_introduction/1_4_technological-architecture`; aquí se nombran las piezas con las
que se configuran.

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Mecanismo
     - Qué hace
   * - :term:`Definición de fichero`
     - Describe cómo leer el fichero de un cliente (columnas, transformaciones) para importarlo
       en un Manifiesto.
   * - Integración API
     - Un sistema externo con el que se habla: la dirección de su servidor, la autenticación y
       sus Endpoints.
   * - Endpoint (punto de conexión)
     - Cada llamada concreta, entrante o saliente, con su método, su dirección y su mapeo de
       datos.
       Los entrantes reciben webhooks; los salientes envían estados y documentos.
   * - Patrón
     - Plantilla con la que se construye el mensaje de salida a partir de la Orden, el Tramo o
       la Parada, campo a campo y con las mismas transformaciones que la importación.
   * - :term:`Bandeja de entrada API`
     - Donde se depositan las Órdenes que llegan por API antes de pasar al Manifiesto.
   * - Funciones preestablecidas
     - Transformaciones reutilizables que se aplican a los campos al importar y al construir
       los mensajes de salida.
   * - Automatizaciones
     - Acciones automáticas y tareas programadas que disparan los envíos y procesan las colas.

.. admonition:: Dónde se detalla
   :class: important

   Este apartado es solo el encuadre arquitectónico. El funcionamiento completo de cada
   mecanismo (configuración, mapeo, transformaciones, patrones, webhooks, acciones automáticas
   y buenas prácticas) se desarrolla en la :doc:`Guía del integrador
   </17.0/7_edi-integrations/index>`. Los contratos de la API REST pública viven en la pasarela
   de API y no se duplican aquí.
