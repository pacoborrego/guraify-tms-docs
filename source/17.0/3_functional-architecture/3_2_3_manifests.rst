3.2.3 Manifiestos
-----------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › Tráfico › Manifiestos

El :term:`Manifiesto` (``tms.edi.manifest``) es la entidad intermedia entre la ingesta de
demanda en volumen y la estructura operativa. Agrupa los datos recibidos, de un fichero o de la
Bandeja de entrada API, en un área de trabajo donde se importan, se revisan y se validan antes
de convertirse en Órdenes.

3.2.3.1 Origen
~~~~~~~~~~~~~~

Un Manifiesto puede alimentarse de dos formas:

- **Por fichero**: se crea el Manifiesto, se selecciona el cliente y la
  :term:`Definición de fichero` (que dice cómo interpretar cada columna) y se importa un fichero
  XLSX o CSV. Se admiten Manifiestos **sin cliente**, solo con Definición de fichero.
- **Por integración**: los datos llegan por API REST a la Bandeja de entrada API y desde ahí se
  agrupan en un Manifiesto (ver :doc:`3_2_4_api-inbox`).

3.2.3.2 La pantalla del Manifiesto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La cabecera del Manifiesto ofrece las acciones principales: **Nueva Orden** (añadir una Orden
manual al manifiesto), **Importar fichero** (abrir el asistente de importación), **Cerrar
Manifiesto** y **Abrir Manifiesto** (reabrir uno cerrado). Cuando hay trabajo en cola aparecen
además **Importar Fichero Ahora** y **Cerrar Manifiesto Ahora**, que se explican más abajo.

Además, tres **botones inteligentes** resumen el estado del manifiesto y permiten actuar sobre
él:

- **Paradas**: número de Paradas asociadas; abre su listado.
- **Normalizar**: número de contactos de carga y descarga **pendientes de normalizar**; al
  pulsarlo, abre la lista de esos contactos para corregirlos. Es el indicador que avisa de por
  qué un manifiesto **no podrá cerrarse** (ver :ref:`manifiesto-normalizacion`).
- **Ficheros**: los ficheros importados en el Manifiesto, con su estado y su registro
  de validación.

3.2.3.3 Importación y cierre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ni la importación ni el cierre son instantáneos: ambos se apoyan en **colas** que una tarea
programada procesa cada **cinco minutos**, lo que evita bloquear la interfaz con ficheros
grandes. El Manifiesto recorre cuatro estados:

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

**Importación.** El asistente que abre **Importar fichero** comprueba que el formato del fichero
coincide con el de la Definición de fichero y, con **Validar e importar**, lo deja en cola: el
Manifiesto pasa a *En cola de espera* y la tarea programada lo importará en su siguiente
pasada. Quien no quiera esperar pulsa **Importar Fichero Ahora** en la cabecera del Manifiesto,
que solo aparece mientras está en cola: es el botón que despierta a la tarea programada para
que lo recoja en segundos, sin retener la pantalla.

Cada fichero se importa **en su propia transacción**: si uno falla (una regla de transformación
que no puede leer una columna, por ejemplo), queda en estado **Error**, en rojo en la lista de
ficheros y con el motivo en su registro de validación, y la cola sigue con el siguiente. Un
fichero en Error **no se reintenta solo**, a propósito: repetirlo cada cinco minutos sería
repetir el error. Corregido el dato, se vuelve a encolar desde el botón. Los botones, además,
avisan: si el Manifiesto no tiene fichero, si todo estaba ya encolado (y vuelven a despertar a
la tarea), y **se niegan a encolar si la tarea programada está apagada**, porque entonces nada
lo recogería. El botón **Registros API** del Manifiesto reúne en una sola lista los registros de
actividad que explican qué le pasó: el de cada fichero importado, los del propio Manifiesto y
los de sus Órdenes (el envío a la agencia o al cliente se registra por Orden); la etiqueta del
botón sale en rojo cuando alguno está en error.

.. CAPTURA: 3_2_3_03 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_03_fichero-error.png
      :alt: Lista de ficheros de un Manifiesto con uno en estado Error

      Un fichero en Error: la cola ha seguido con los demás y el motivo está en su registro.

**Cierre.** Cuando el Manifiesto ya tiene órdenes, aparece **Cerrar Manifiesto**, que también
lo encola. Al cerrarse, su contenido se materializa en la estructura operativa: Órdenes, Tramos
y Paradas, agrupando los Tramos en Paradas con el criterio de
:doc:`3_2_6_legs-and-stops`. **Cerrar Manifiesto Ahora** salta esa cola. Un Manifiesto cerrado
puede reabrirse con **Abrir Manifiesto**. Lo que el cierre hace con los Viajes cuando el fichero
trae la asignación a viajes se describe en
:doc:`/17.0/5_operational-flows/5_2_trip-generation`.

.. _manifiesto-normalizacion:

3.2.3.4 Normalización de contactos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El cierre del Manifiesto **se bloquea si quedan contactos sin normalizar**: el sistema exige
resolver antes todas las direcciones de carga y descarga, porque una dirección incompleta o de
baja calidad afecta a la geocodificación, la planificación y la ejecución. Esta tabla es la
referencia de lo que el sistema entiende por normalizar; el resto de la documentación remite a
ella.

Un contacto de carga o descarga se considera **pendiente de normalizar** cuando se cumple alguno
de estos criterios:

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Criterio
     - Detalle
   * - Sin coordenadas
     - La localización no tiene latitud ni longitud.
   * - Geolocalización de baja calidad
     - La puntuación de la geocodificación es inferior a 80 (la cascada de geocodificación se
       describe en :doc:`/17.0/1_introduction/1_4_technological-architecture`).
   * - Solo a nivel de código postal
     - La geocodificación ha resuelto el código postal, no la dirección exacta.
   * - Sin franjas horarias
     - Si el Proyecto **no** usa «horarios informados», el contacto sin ninguna ventana de
       apertura definida también se marca para normalizar.

El botón inteligente **Normalizar** lleva directamente a la lista de estos contactos; una vez
corregidos (coordenadas válidas y, en su caso, horarios), el Manifiesto ya puede cerrarse.

**Cómo se elige el contacto.** Antes de normalizar nada, la importación tiene que decidir a qué
contacto corresponde cada dirección de carga o descarga del fichero, y una dirección identifica
un sitio, no a una persona: en la misma nave pueden trabajar varias. Los candidatos salen de la
**dirección normalizada** (sin tildes, sin mayúsculas ni espacios de más, comparada con el
código postal cuando viene) y, entre ellos, gana el que **se llama como dice el fichero**. Si
nadie se llama así, el sistema **crea el contacto** con esa dirección y ese nombre, en vez de
atribuir el Tramo a un compañero con más historial; si el fichero no trae nombre, gana el de más
historial, como antes. El nombre se compara entero: «Marta Ruiz» y «Marta Ruiz García» son dos
contactos, y una errata también; es el precio de no entregar a la persona equivocada. Cuando
la Definición de fichero trabaja con clave de dirección (AddressKey), no se crean contactos: se
prefiere el que coincide en nombre y, si ninguno coincide, el de más historial.

.. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_01_manifiesto.png
   :alt: Formulario de un Manifiesto con su estado

   Formulario de un Manifiesto con sus estados y botones.

.. figure:: /_static/img/3_functional-architecture/3_2_3_manifests_02_botones-inteligentes.png
   :alt: Botones inteligentes del Manifiesto (Paradas, Normalizar y Ficheros)

   Botones inteligentes del Manifiesto: **Paradas**, **Normalizar** (contactos pendientes) y
   **Ficheros** (ficheros importados).
