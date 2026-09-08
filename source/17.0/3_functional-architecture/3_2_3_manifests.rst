3.2.3 Manifiestos
=================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Manifiestos

El :term:`Manifiesto` (``tms.edi.manifest``) es la entidad intermedia entre la ingesta de
demanda en volumen y la estructura operativa. Agrupa los datos recibidos, de un fichero o
de la Bandeja de entrada API, en un área de trabajo donde se importan, se revisan y se
validan antes de convertirse en Órdenes.

3.2.3.1 Origen
--------------

Un Manifiesto puede alimentarse de dos formas:

- **Por fichero**: se crea el Manifiesto, se selecciona el cliente y la
  :term:`Definición de fichero` (que dice cómo interpretar cada columna) y se importa un
  fichero XLSX o CSV. Se admiten Manifiestos **sin cliente**, sólo con Definición de fichero.
- **Por integración**: los datos llegan por API REST a la Bandeja de entrada API y desde
  ahí se agrupan en un Manifiesto (ver :doc:`3_2_4_api-inbox`).

3.2.3.2 La pantalla del Manifiesto
----------------------------------

La cabecera del Manifiesto ofrece las acciones principales: **Nueva Orden** (añadir una
Orden manual al manifiesto), **Fichero de Importación** (abrir el asistente de
importación), **Cerrar Manifiesto** y **Abrir Manifiesto** (reabrir uno cerrado).

Además, dos **botones inteligentes** resumen el estado del manifiesto y permiten actuar
sobre él:

- **Paradas**: número de Paradas asociadas; abre su listado.
- **Normalizar**: número de contactos de carga y descarga **pendientes de normalizar**; al
  pulsarlo, abre la lista de esos contactos para corregirlos. Es el indicador que avisa de
  por qué un manifiesto **no podrá cerrarse** (ver :ref:`manifiesto-normalizacion`).

3.2.3.3 Importación y cierre
----------------------------

Ni la importación ni el cierre son instantáneos: ambos se apoyan en **colas** que una tarea
programada procesa cada **cinco minutos**, lo que evita bloquear la interfaz con ficheros
grandes. El usuario puede **forzar** cada paso desde la pantalla con **Importar Fichero
Ahora** y **Cerrar Manifiesto Ahora**.

El Manifiesto recorre cuatro estados:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Abierto
     - Recibiendo y acumulando datos; admite revisión.
   * - En cola de espera
     - A la espera de que la tarea programada lo procese.
   * - Procesando
     - El sistema está materializando su contenido.
   * - Cerrado
     - Procesado: su contenido se ha convertido en estructura operativa.

**Importación.** Al importar un fichero, su contenido entra en cola y el Manifiesto pasa a
*En cola de espera*. El usuario puede adelantarlo con el botón **Validar e importar** del
asistente.

**Cierre.** Cuando el Manifiesto ya tiene órdenes, aparece **Cerrar Manifiesto**. Al
cerrarlo, su contenido se materializa en la estructura operativa: Órdenes, Tramos y
Paradas. Un Manifiesto cerrado puede reabrirse con **Abrir Manifiesto**. Lo que el cierre
hace con los Viajes cuando el fichero trae la asignación a viajes se describe en
:doc:`/17.0/5_operational-flows/5_2_trip-generation`.

.. _manifiesto-normalizacion:

3.2.3.4 Normalización de contactos
----------------------------------

El cierre del Manifiesto **se bloquea si quedan contactos sin normalizar**: el sistema
exige resolver antes todas las direcciones de carga y descarga, porque una dirección
incompleta o de baja calidad afecta a la geocodificación, la planificación y la ejecución.

Un contacto de carga o descarga se considera **pendiente de normalizar** cuando se cumple
alguno de estos criterios:

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Criterio
     - Detalle
   * - Sin coordenadas
     - La localización no tiene latitud ni longitud.
   * - Geolocalización de baja calidad
     - La puntuación de la geocodificación es inferior a 80 (ver
       :ref:`17.0/1_introduction/1_4_technological-architecture:Geocodificación de direcciones`).
   * - Sólo a nivel de código postal
     - La geocodificación ha resuelto el código postal, no la dirección exacta.
   * - Sin franjas horarias
     - Si el Proyecto **no** usa "horarios informados", el contacto sin ninguna ventana de
       apertura definida también se marca para normalizar.

El botón inteligente **Normalizar** lleva directamente a la lista de estos contactos; una
vez corregidos (coordenadas válidas y, en su caso, horarios), el Manifiesto ya puede
cerrarse.

.. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_01_manifiesto.png
   :alt: Formulario de un Manifiesto con su estado

   Formulario de un Manifiesto con sus estados y botones.

.. CAPTURA: 3_2_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_02_botones-magicos.png
      :alt: Botones inteligentes del Manifiesto (Paradas y Normalizar)

      Botones inteligentes del Manifiesto: **Paradas** y **Normalizar** (contactos pendientes).
