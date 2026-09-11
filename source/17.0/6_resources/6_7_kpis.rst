6.7 Indicadores
---------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Mantenimiento › Indicadores y Tablero del taller.

.. CAPTURA: 6_7_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_7_kpis_01_indicadores.png
      :alt: Lista de indicadores de mantenimiento

      Los indicadores de mantenimiento, con su valor y el acceso al listado que los explica.

Los indicadores de mantenimiento son indicadores configurables del motor de indicadores de la
suite (ver :doc:`/17.0/8_economic-administration/8_8_control-reporting`), filtrados por
mantenimiento en el menú Indicadores; cada uno abre, al pulsarlo, la lista de registros que lo
componen. El **Tablero del taller** es el nativo de Odoo, con los contadores de órdenes
pendientes, de alta prioridad, bloqueadas y sin planificar de cada equipo de taller.

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - Indicador
     - Qué cuenta
   * - Preventivos vencidos / por vencer / al día
     - Reglas de preventivo por estado: progreso desde el 100 %, entre el 85 % y el 100 %, y por
       debajo del 85 %.
   * - Revisión de combustible vencida / Revisión completa vencida («Service de combustible
       vencido», «Service completo vencido»)
     - Vehículos con cada nivel del control de revisiones vencido.
   * - Vehículos con órdenes abiertas («Unidades con órdenes abiertas»)
     - Vehículos con al menos una orden de trabajo sin cerrar.
   * - Vehículos sin odómetro («Unidades sin odómetro»)
     - Vehículos del perímetro de mantenimiento sin ninguna lectura válida.
   * - Vehículos sin lectura reciente («Unidades sin lectura reciente»)
     - Vehículos del perímetro cuya última lectura tiene más días que el umbral configurado
       (30 por defecto; ver :doc:`6_8_configuration`).
   * - Reglas con km estimado
     - Porcentaje de las reglas evaluadas que usan un kilometraje estimado en vez de real. Es la
       medida de cuánto falta por capturar: cada orden que se cierra con su kilometraje lo baja.
   * - MTBF y MTTR de la flota
     - Tiempo medio entre fallos (MTBF) y tiempo medio de reparación (MTTR), en días, como media
       de los vehículos que tienen el dato. Los calcula el módulo nativo sobre las órdenes
       correctivas cerradas; sin correctivas cerradas el indicador queda «Sin datos».

El **perímetro de mantenimiento** son los vehículos con al menos una regla de preventivo activa:
la población que el motor evalúa. Los indicadores de odómetro se cuentan sobre él y no sobre
toda la flota de Odoo, porque un vehículo sin reglas no está en el preventivo y su falta de
lectura no es accionable. El indicador de kilometraje estimado es el que más dice de la
implantación: mientras sea alto, el preventivo se calcula sobre estimaciones, y bajarlo es
exactamente para lo que existen el cierre con kilometraje, la app del conductor y la
telemetría.
