3.5 Modelo de integración
-------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI

El modelo de integración define los mecanismos mediante los cuales el TMS intercambia
información con sistemas externos. Estas integraciones permiten automatizar la entrada de
demanda, sincronizar información con otros sistemas empresariales y facilitar la
interoperabilidad con plataformas logísticas, transformando los datos externos
directamente en entidades nativas del sistema (Orden, Tramo, Parada, Viaje) sin crear
estructuras paralelas.

Todos los mecanismos los gestiona el módulo de integraciones (``tms_int``):

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Mecanismo
     - Qué hace
   * - :term:`Definición de fichero`
     - Describe cómo leer el fichero de un cliente (columnas, transformaciones) para
       importarlo en un Manifiesto.
   * - Integración API
     - Un sistema externo con el que se habla: dirección, autenticación y sus endpoints.
   * - Endpoint
     - Cada llamada concreta, entrante o saliente, con su método, su ruta y su mapeo de
       datos. Los entrantes reciben webhooks; los salientes envían estados y documentos.
   * - :term:`Bandeja de entrada API`
     - Donde se depositan las Órdenes que llegan por API antes de pasar al Manifiesto.
   * - Automatizaciones
     - Acciones automáticas y tareas programadas que disparan los envíos y procesan las
       colas.

.. admonition:: Dónde se detalla
   :class: important

   Este apartado es sólo el encuadre arquitectónico. El funcionamiento completo de cada
   mecanismo (configuración, mapeo, transformaciones, webhooks, acciones automáticas y
   buenas prácticas) se desarrolla en la :doc:`Guía del integrador
   </17.0/7_edi-integrations/index>`. Los contratos de la API REST pública viven en la
   pasarela de API y no se duplican aquí.
