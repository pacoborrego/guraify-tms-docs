6.7 Indicadores
---------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Mantenimiento › Indicadores y Tablero del taller.

.. CAPTURA: 6_7_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_7_kpis_01_indicadores.png
      :alt: Lista de indicadores de mantenimiento

      Los indicadores de mantenimiento, con su valor y el acceso al listado que los explica.

Los indicadores de mantenimiento no tienen un tablero propio: se registran en el **motor de
indicadores** de la suite, el mismo que usan los tableros del TMS, y se ven en el menú
Indicadores filtrados por mantenimiento. Cada indicador muestra su valor calculado sobre los
datos vivos y, al pulsarlo, abre la lista de registros que lo componen. El **Tablero del taller**
es el nativo de Odoo, con los contadores de órdenes pendientes, de alta prioridad, bloqueadas y
sin planificar de cada equipo de taller.

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - Indicador
     - Qué cuenta
   * - Preventivos vencidos / por vencer / al día
     - Reglas de preventivo por estado: progreso desde el 100 %, entre el 85 % y el 100 %, y por
       debajo del 85 %.
   * - Service de combustible vencido / Service completo vencido
     - Unidades con cada nivel del control de service vencido.
   * - Unidades con órdenes abiertas
     - Unidades con al menos una orden de trabajo sin cerrar.
   * - Unidades sin odómetro
     - Unidades del perímetro de mantenimiento sin ninguna lectura válida.
   * - Unidades sin lectura reciente
     - Unidades del perímetro cuya última lectura tiene más días de los que fija el parámetro.
   * - Kilometraje estimado
     - Porcentaje de las reglas evaluadas que usan un kilometraje estimado en vez de real. Es la
       medida de cuánto falta por capturar: cada orden que se cierra con su kilometraje lo baja.
   * - MTBF y MTTR de la flota
     - Media de días entre fallos y de días de reparación de las unidades, calculados por el
       módulo nativo sobre las órdenes correctivas.

El **perímetro de mantenimiento** son las unidades con al menos una regla de preventivo activa:
la población que el motor evalúa. Los indicadores de odómetro se cuentan sobre él y no sobre
toda la flota de Odoo, porque una unidad sin reglas no está en el preventivo y su falta de
lectura no es accionable. El indicador de kilometraje estimado es el que más dice del proyecto:
mientras sea alto, el preventivo se calcula sobre estimaciones, y bajarlo es exactamente para lo
que existen el cierre con kilometraje, la app del conductor y la telemetría.
