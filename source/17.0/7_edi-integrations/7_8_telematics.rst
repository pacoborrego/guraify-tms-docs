7.8 Telemática
--------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › **Telemática**: Proveedores, Dispositivos, Señales, Lecturas, Eventos

El conector de telemática es la puerta por la que el TMS recibe lo que saben los vehículos: dónde
están, cuántos kilómetros llevan, a qué temperatura va la carga, qué le queda al conductor de
jornada, qué avería ha saltado. Odoo no habla con cada proveedor de telemática: describe qué
proveedores, dispositivos y señales hay, y recibe las lecturas ya normalizadas.

7.8.1 Estado: hecho en Odoo, sin datos todavía
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Todo lo que se describe aquí existe y está probado en Odoo, pero **hoy no entra ningún dato**:

- El **servicio intermedio** que tiene que consultar a los proveedores, normalizar sus señales y
  entregarlas a Odoo (el «hub» de la torre de control) **no está construido**.
- La **app del conductor**, que puede ser su propio proveedor de posición, **todavía no envía su
  posición**: el endpoint que la espera (7.8.3) existe, pero la app no lo llama.

Mientras tanto, el ETA se recalcula desde la última Parada cerrada
(:doc:`/17.0/5_operational-flows/5_4_app-execution`), la geocerca y el tacógrafo no tienen
efecto, y la planificación funciona exactamente como sin telemática. Encenderla es: que la app
envíe su posición, o que el servicio intermedio exista y se configure un proveedor real.

7.8.2 El modelo
~~~~~~~~~~~~~~~

.. CAPTURA: 7_8_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_8_telematics_01_proveedor.png
      :alt: Ficha del proveedor de telemática de la app del conductor con su mapeo

      El proveedor «app del conductor», el que viene de serie, con su mapeo de la posición.

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Pieza
     - Qué es
   * - **Proveedor**
     - Una fuente de telemática: su código, su **Modo de entrega** (el servicio intermedio
       pregunta al proveedor; el proveedor llama al servicio; o empuja datos sin parar, como la
       app), cada cuánto se le pregunta y la **integración** (:doc:`7_3_api-integrations`) donde
       viven su dirección y sus credenciales. La app no tiene integración: se identifica con el
       token de su dispositivo.
   * - **Dispositivo**
     - Una unidad concreta: su identificador en el proveedor y a quién pertenece, un **vehículo**,
       un **conductor** o los dos (uno sin ninguno de los dos no se puede crear), con su vigencia
       y su prioridad. Un vehículo puede tener varios a la vez (la caja negra y el móvil del
       conductor, o dos proveedores mientras se cambia de uno a otro). Un dispositivo fuera de su
       vigencia no recibe nada.
   * - **Señal**
     - El vocabulario común: posición, odómetro, horas de motor, temperatura, tacógrafo, avería,
       frenada brusca… Cada una con su unidad, su tipo, qué hace el TMS con ella y su **Política
       de persistencia** (abajo). Añadir una señal es una fila, no un desarrollo.
   * - **Mapeo de señales**
     - Cómo llama cada proveedor a cada señal, y el factor y el desfase para pasarla a la unidad
       común.
   * - **Lectura**
     - Un valor que ha merecido guardarse. Las lecturas se purgan periódicamente.
   * - **Evento**
     - Un hito: entrada en una geocerca, excursión de temperatura, avería, frenada. No se purgan:
       son lo que leerá la torre de control.

El módulo trae **20 señales** y el proveedor **app del conductor** con el mapeo de la posición.

7.8.3 Las dos puertas
~~~~~~~~~~~~~~~~~~~~~

Hay dos formas de entregar datos a Odoo. Las dos acaban en el mismo punto de aterrizaje, que hace
lo mismo con cada lectura venga de donde venga.

**El servicio intermedio.** Es un usuario técnico de Odoo con una clave de API: se autentica en
``/web/session/authenticate`` y reutiliza la sesión. **El usuario técnico necesita zona horaria**:
«los Viajes de hoy» son los de su día. Los cuatro endpoints son JSON-RPC (``type='json'``) y
exigen sesión:

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Endpoint
     - Qué hace
   * - ``/tms_int/telematics/config``
     - Todo lo que el servicio necesita en una llamada: proveedores con sus credenciales ya
       resueltas (un token con caducidad; los secretos no salen nunca de Odoo), dispositivos,
       mapeos, el intervalo mínimo entre posiciones y las **geocercas** de las Paradas de los
       Viajes en curso y de los despachados con fecha de hoy. Con ``since``, solo lo que ha
       cambiado.
   * - ``/tms_int/telematics/readings``
     - Un lote de lecturas normalizadas: ``provider_code``, ``external_id``, ``signal``,
       ``value``, ``recorded_at`` (y ``lat``, ``lon``, ``compartment_ref`` según la señal).
       Responde cuántas aterrizaron y cuántas se descartaron.
   * - ``/tms_int/telematics/events``
     - Hitos que el servicio ya ha detectado: geocercas, encendido, excursiones, averías. Una
       desviación de ruta o una parada demasiado larga piden un recálculo del ETA.
   * - ``/tms_int/telematics/positions``
     - La última posición de cada Viaje en curso, aparte, porque es la que más volumen trae.

**La app del conductor.** ``POST /app/telematics/position`` con el token de su dispositivo
(:ref:`17.0/4_parametrization/4_1_operational-configuration:4.1.9 Conductores y acceso a la app`),
siempre obligatorio en esta ruta: sin token responde 401. Cuerpo:
``{"positions": [{"lat": …, "lon": …, "recorded_at": …, "accuracy": …}]}``, como mucho 100 por
llamada.

7.8.4 Volumen e idempotencia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La telemática es lo que más volumen puede meter en Odoo, y en junio de 2026 la app tumbó el
servidor con reintentos. Las defensas no son opcionales:

- **Lotes de 500 como máximo.** Un lote mayor responde con un **413** de verdad (no un error
  dentro de una respuesta 200): el servicio tiene que partirlo.
- **Una lectura repetida no se duplica.** Dispositivo, señal y hora identifican una lectura: la
  base de datos rechaza la segunda. Reenviar un lote es seguro.
- **Una posición no crea una fila.** Actualiza la última posición conocida del Viaje (y la
  sobrescribe), como mucho una cada 120 segundos por Viaje (parámetro
  ``tms_int.telematics_position_min_gap_s``). Lo que llega antes se descarta, pero se responde
  como aceptado, para que quien envía no lo reintente.
- **Cada señal guarda solo lo necesario**, según su política de persistencia: **No guardar**
  (posición, velocidad, rumbo: solo cuenta el efecto), **al cambiar** (los sí/no, el
  tacógrafo), **como mucho una vez por intervalo** (temperatura y consumo, cada 15 minutos) o
  **al moverse más que un umbral** (nivel de combustible, batería). La serie completa es del
  servicio intermedio, no de Odoo.
- **Una lectura mala no tumba el lote**: se descarta y las demás siguen.
- Cada lote deja su entrada en el registro de actividad de la API (:doc:`7_7_integration-best-practices`),
  con el contenido completo solo si algo se descartó.

7.8.5 Qué hace el TMS con cada señal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Señal
     - Efecto
   * - Posición
     - Última posición del Viaje (pestaña ETA y ruta). Al entrar en la **geocerca de llegada** de
       una Parada (150 m o lo que diga la :ref:`politica-operativa` o el Tipo de Parada) registra
       la llegada; con el modo de recálculo «Al desviarse del plan», pide un recálculo del ETA si
       el vehículo está lejos de la siguiente Parada.
   * - Odómetro, horas de motor
     - Una lectura del odómetro único del vehículo, por el mismo punto que el taller o la app
       (:doc:`/17.0/6_resources/6_2_odometer`), con origen Telemetría.
   * - Temperatura
     - Se compara con el rango de la clase de temperatura del compartimento (grupo **Cadena de
       frío** de la ficha de la temperatura, mínimo y máximo en °C). Fuera de rango: evento y nota
       en las Órdenes del Viaje. Una clase con los dos límites a cero no se juzga.
   * - Tacógrafo
     - El grupo TACÓGRAFO del conductor: lo que le queda de conducción y de trabajo. Lo usan el
       cálculo de ruta y OptiFlow para colocar las pausas, solo si el dato es de la última hora y
       del mismo día (parámetro ``tms.tacho_freshness_minutes``): uno caducado es peor que
       ninguno.
   * - Avería (código de diagnóstico)
     - Evento y una orden de mantenimiento, **una por avería**, no una por cada vez que se
       reporta.
   * - Frenada brusca, exceso de velocidad y otros
     - Solo el evento.

7.8.6 Configurar un proveedor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Una **integración** (:doc:`7_3_api-integrations`) con la dirección y las credenciales del
   proveedor.
#. El **proveedor**, con su modo de entrega y esa integración.
#. Los **dispositivos**: uno por unidad, con su identificador en el proveedor y su vehículo y/o
   conductor. La referencia de telemetría del vehículo
   (:doc:`/17.0/annexes/A_19_odometro`) es solo una pista para darlos de alta: la autoridad es el
   dispositivo.
#. Los **mapeos** de las señales que dé el proveedor.
#. El **usuario técnico** del servicio intermedio, con clave de API y zona horaria.
#. Para la cadena de frío, el rango en °C de cada clase de temperatura; para la llegada por
   geocerca, el radio en la política operativa.

Un endpoint de una integración con proveedores de telemática **no se puede programar como tarea
periódica**: haría una llamada al proveedor por vehículo desde el mismo servidor que atiende a los
usuarios. Odoo lo rechaza y la ficha del proveedor lo avisa.
