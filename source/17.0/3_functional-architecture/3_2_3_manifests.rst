3.2.3 Manifiestos
=================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Manifiestos

El Manifiesto EDI (``tms.edi.manifest``) es la entidad intermedia entre la ingesta de
demanda en volumen y la estructura operativa. Agrupa los datos recibidos —de un fichero o
de la Bandeja de Entrada API— en un área de trabajo donde se importan, se revisan y se
validan antes de convertirse en Órdenes.

3.2.3.1 Origen
--------------

Un Manifiesto puede alimentarse de dos formas:

- **Por fichero**: se crea el Manifiesto, se selecciona el cliente y el **Fichero EDI**
  (``tms.edi.file``, que define el mapeo de columnas) y se importa un fichero XLSX/CSV. Se
  admiten Manifiestos **sin cliente** (cliente vacío y solo Fichero EDI).
- **Por integración**: los datos llegan por API REST a la Bandeja de Entrada API
  (``tms_int.api.inbox``) y desde ahí se agrupan en un Manifiesto (ver
  :doc:`3_2_4_api-inbox`).

3.2.3.2 La pantalla del Manifiesto
----------------------------------

La cabecera del Manifiesto ofrece las acciones principales: **Nueva expedición** (añadir
una expedición manual al manifiesto), **Importar fichero** (abrir el asistente de
importación), **Cerrar Manifiesto** y **Abrir Manifiesto** (reabrir uno cerrado).

Además, dos **botones mágicos** (*smart buttons*) resumen el estado del manifiesto y
permiten actuar sobre él:

- **Stops**: número de Paradas asociadas; abre su listado.
- **Normalizar** (*To Normalize*): número de contactos de carga/descarga **pendientes de
  normalizar**; al pulsarlo, abre la lista de esos contactos para corregirlos. Es el
  indicador que avisa de por qué un manifiesto **no podrá cerrarse** (ver
  :ref:`manifiesto-normalizacion`).

3.2.3.3 Importación y cierre
----------------------------

Ni la importación ni el cierre son instantáneos: ambos se apoyan en **colas** que procesan
tareas programadas (``ir.cron``) cada **5 minutos**, lo que evita bloquear la interfaz con
ficheros grandes. El usuario siempre puede **forzar** el paso desde la pantalla.

El Manifiesto recorre cuatro estados:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Estado
     - Significado
   * - Abierto (``open``)
     - Recibiendo y acumulando datos; admite revisión.
   * - En cola (``in_queue``)
     - A la espera de que la tarea programada lo procese.
   * - Procesando (``processing``)
     - El sistema está materializando su contenido.
   * - Cerrado (``closed``)
     - Procesado: su contenido se ha convertido en estructura operativa.

**Importación.** Al importar un fichero, su contenido entra en cola y el Manifiesto pasa a
*En cola*; la tarea **«Compute File Imports in Queue»** lo procesa cada 5 minutos. El
usuario puede adelantarlo con el botón **«Validar e importar»** del asistente.

**Cierre.** Cuando el Manifiesto ya tiene expediciones, aparece **«Cerrar Manifiesto»**. Al
cerrarlo, su contenido se materializa en la estructura operativa —Orden (``sale.order``),
Tramos (``tms.shipment.leg``) y Paradas (``tms.stop``)—. El cierre también se procesa
mediante una cola (tarea **«Compute Close Manifest»**, cada 5 minutos). Un Manifiesto
cerrado puede reabrirse con **«Abrir Manifiesto»**.

.. _manifiesto-normalizacion:

3.2.3.4 Normalización de contactos
----------------------------------

El cierre del Manifiesto **se bloquea si quedan contactos sin normalizar**: el sistema
exige resolver antes todas las direcciones de carga y descarga, porque una dirección
incompleta o de baja calidad afecta a la geocodificación, la planificación y la ejecución.

Un contacto (``res.partner`` de carga o descarga) se considera **pendiente de normalizar**
cuando se cumple alguno de estos criterios:

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Criterio
     - Detalle
   * - Sin coordenadas
     - Latitud o longitud a 0 (``partner_latitude`` / ``partner_longitude``).
   * - Geolocalización de baja calidad
     - Puntuación de geocodificación insuficiente (``tms_geo_score`` < 80).
   * - Solo a nivel de código postal
     - La geolocalización resuelve únicamente el código postal, no la dirección exacta
       (``tms_geo_location_type`` = ``POSTAL_CODE``).
   * - Sin franjas horarias
     - Si el proyecto **no** usa "horarios informados", el contacto sin ninguna ventana de
       apertura definida también se marca para normalizar.

El botón mágico **Normalizar** lleva directamente a la lista de estos contactos; una vez
corregidos (coordenadas válidas y, en su caso, horarios), el Manifiesto ya puede cerrarse.

.. CAPTURA: 3_2_3_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_01_manifiesto.png
      :alt: Formulario de un Manifiesto EDI con su estado

      Formulario de un Manifiesto EDI (``tms.edi.manifest``) con sus estados y botones.

.. CAPTURA: 3_2_3_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_02_botones-magicos.png
      :alt: Botones mágicos del Manifiesto (Stops y Normalizar)

      Botones mágicos del Manifiesto: **Stops** y **Normalizar** (contactos pendientes).
