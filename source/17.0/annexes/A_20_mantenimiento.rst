A.20 Mantenimiento: reglas, órdenes, trabajos y umbrales
========================================================

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Mantenimiento › Reglas de preventivo y Órdenes de trabajo · Gestión de Recursos › Configuración › Trabajos y Tareas de mantenimiento · pestaña «Maintenance (TMS)» del vehículo · umbrales en la ficha de la compañía

Modelo Odoo: ``tms.maintenance.rule`` (la Regla de preventivo) y ``tms.maintenance.task`` (la Tarea
de mantenimiento), más los campos añadidos a la orden de trabajo nativa (``maintenance.request``),
al Trabajo (``fleet.service.type``), al vehículo (``fleet.vehicle``) y a la compañía
(``res.company``). Las pantallas del área Gestión de Recursos no llevan todavía traducción y
muestran sus etiquetas en inglés; aquí se dan en español.

A.20.1 Regla de preventivo
--------------------------

La Regla de preventivo (``tms.maintenance.rule``) une un vehículo y un Trabajo con su intervalo.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Vehículo / Trabajo
     - Relaciones
     - El vehículo y el Trabajo. Obligatorios; un vehículo no puede tener dos reglas activas del
       mismo Trabajo.
   * - Tarea / Material
     - Relación / Texto
     - Se copian del Trabajo al elegirlo y se pueden cambiar.
   * - Intervalo / Tipo de intervalo
     - Número / Selección
     - Cada cuánto toca: en Kilómetros, en Días, o No aplica («no lleva»).
   * - Último realizado / Km del último realizado / Última orden
     - Fecha / Número / Relación (calculados)
     - La última orden cerrada de ese Trabajo en ese vehículo, su fecha y su kilometraje real si lo
       trajo.
   * - Consumido / Restante / Progreso
     - Número (calculados)
     - Kilómetros o días desde el último realizado, lo que falta (negativo si vencido) y el cociente
       sobre el intervalo.
   * - Estado
     - Selección (calculado)
     - Al día, Por vencer, Vencido o No evaluada.
   * - Confianza
     - Selección (calculado)
     - Alta si el último realizado trae kilometraje real; Media si se estimó con la serie de
       odómetro.
   * - Motivo de exclusión
     - Selección (calculado)
     - Por qué la regla no se evalúa: no aplica, sin historial, falta odómetro, serie insuficiente,
       dato incoherente.

A.20.2 Orden de trabajo
-----------------------

Los campos que el TMS añade a la orden de trabajo nativa (``maintenance.request``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Vehículo
     - Relación con Vehículo
     - El vehículo mantenido.
   * - Trabajo / Tarea
     - Relaciones
     - Qué se hace y cómo se clasifica.
   * - Odómetro
     - Número
     - Kilometraje en el momento del trabajo. Obligatorio para cerrar una orden con vehículo.
   * - Lectura de odómetro
     - Relación (solo lectura)
     - La lectura que generó el cierre en el odómetro único.
   * - Regla de preventivo / Tipo de intervalo
     - Relación / Selección
     - La regla de la que nació la orden, si es preventiva, y si su siguiente pendiente lo genera
       Odoo (días) o el motor (km).
   * - Km actual del vehículo
     - Número (calculado)
     - El kilometraje actual del vehículo, para las tarjetas y la lista del taller. No es el de la
       orden.

A.20.3 Trabajo
--------------

Los campos que el TMS añade al Trabajo (``fleet.service.type``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tarea por defecto / Material por defecto
     - Relación / Texto
     - Lo que hereda una regla nueva de este Trabajo.
   * - Intervalo por defecto / Tipo de intervalo por defecto
     - Número / Selección
     - El intervalo que propone a las reglas. En los cuatro objetivos periódicos es el objetivo en
       días.
   * - Preventivo
     - Sí/No
     - Si el Trabajo participa en el motor de preventivo.

A.20.4 Tarea
------------

La Tarea de mantenimiento (``tms.maintenance.task``) clasifica las órdenes.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tarea / Código
     - Texto
     - El nombre (único sin distinguir mayúsculas) y un código opcional.

A.20.5 Vehículo
---------------

Los campos de mantenimiento del vehículo (``fleet.vehicle``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Km de la última revisión
     - Número
     - Kilometraje de la última revisión registrada («Last Service Km»). Vacío no es cero: significa
       que la última revisión se desconoce y el control queda Sin datos.
   * - Estado y restante de la revisión de combustible / de la revisión completa
     - Selección / Número
     - Al día, Por vencer, Vencido o Sin datos, y los kilómetros que faltan o sobran, por nivel.
   * - Reglas de preventivo / Órdenes
     - Listas
     - Las reglas del vehículo y su historial de órdenes.
   * - Equipo, técnico, MTBF, MTTR, próximo fallo estimado, último fallo, fecha efectiva
     - Del módulo nativo
     - La fiabilidad y la responsabilidad que aporta el comportamiento mantenible de Odoo.

A.20.6 Compañía y parámetros del sistema
----------------------------------------

Los umbrales del control de revisiones y la firma de los textos viven en la compañía
(``res.company``); el umbral de lectura reciente es un parámetro del sistema
(``ir.config_parameter``).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Intervalo de la revisión de combustible / completa
     - Número
     - Kilómetros entre revisiones de cada nivel: 15.000 y 30.000 por defecto («Fuel Service
       Interval», «Full Service Interval»).
   * - Margen de aviso de la revisión
     - Número
     - Kilómetros restantes a los que una revisión pasa a Por vencer: 1.500 por defecto («Service
       Warning Margin»).
   * - Firma de los textos de taller
     - Texto
     - Nombre corto con el que se firman los textos de WhatsApp. Vacío usa el nombre de la compañía.
   * - ``tms_maintenance.odometer_stale_days``
     - Parámetro del sistema (número)
     - Días sin lectura válida a partir de los cuales un vehículo cuenta en el indicador «Unidades
       sin lectura reciente». 30 si no se define.

Cómo se usa y qué decide el cliente: :doc:`/17.0/6_resources/6_3_maintenance-model` y
:doc:`/17.0/6_resources/6_4_preventive-rules`.
