A.20 Mantenimiento: reglas, órdenes, trabajos y umbrales
========================================================

Los campos que ``tms_maintenance`` añade a la orden de trabajo nativa (``maintenance.request``), al trabajo (``fleet.service.type``) y al vehículo, y los de sus modelos propios: la regla de preventivo (``tms.maintenance.rule``) y la tarea (``tms.maintenance.task``).

Regla de preventivo (tms.maintenance.rule)
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Vehículo / Trabajo
     - Relaciones
     - La unidad y el trabajo. Obligatorios; un vehículo no puede tener dos reglas activas del mismo trabajo.
   * - Tarea / Material
     - Relación / Texto
     - Se copian del trabajo al elegirlo y se pueden cambiar.
   * - Intervalo / Tipo de intervalo
     - Número / Selección
     - Cada cuánto toca: en Kilómetros, en Días, o No aplica («no lleva»).
   * - Último realizado / Km del último realizado / Última orden
     - Fecha / Número / Relación (calculados)
     - La última orden cerrada de ese trabajo en esa unidad, su fecha y su kilometraje real si lo trajo.
   * - Consumido / Restante / Progreso
     - Número (calculados)
     - Kilómetros o días desde el último realizado, lo que falta (negativo si vencido) y el cociente sobre el intervalo.
   * - Estado
     - Selección (calculado)
     - Al día, Por vencer, Vencido o No evaluada.
   * - Confianza
     - Selección (calculado)
     - Alta si el último realizado trae kilometraje real; Media si se estimó con la serie de odómetro.
   * - Motivo de exclusión
     - Selección (calculado)
     - Por qué la regla no se evalúa: no aplica, sin historial, falta odómetro, serie insuficiente, dato incoherente.

Orden de trabajo (maintenance.request, campos TMS)
--------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Vehículo
     - Relación con Vehículo
     - La unidad mantenida. El campo Equipo del módulo nativo no se usa.
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
     - La regla de la que nació la orden, si es preventiva, y si su siguiente pendiente lo genera Odoo (días) o el motor (km).
   * - Km actual de la unidad
     - Número (calculado)
     - El kilometraje actual del vehículo, para el kanban y la lista del taller. No es el de la orden.

Trabajo (fleet.service.type, campos TMS)
----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tarea por defecto / Material por defecto
     - Relación / Texto
     - Lo que hereda una regla nueva de este trabajo.
   * - Intervalo por defecto / Tipo de intervalo por defecto
     - Número / Selección
     - El intervalo que propone a las reglas. En los cuatro objetivos periódicos es el objetivo en días.
   * - Preventivo
     - Sí/No
     - Si el trabajo participa en el motor de preventivo.

Tarea (tms.maintenance.task)
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tarea / Código
     - Texto
     - El nombre (único sin distinguir mayúsculas) y un código opcional.

Vehículo (fleet.vehicle, campos de mantenimiento)
-------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Km del último service
     - Número
     - Kilometraje del último service registrado. Vacío no es cero: significa que el último service se desconoce y el control queda Sin datos.
   * - Estado y restante del service de combustible / del service completo
     - Selección / Número
     - Al día, Por vencer, Vencido o Sin datos, y los kilómetros que faltan o sobran, por nivel.
   * - Reglas de preventivo / Órdenes
     - Listas
     - Las reglas de la unidad y su historial de órdenes.
   * - Equipo, técnico, MTBF, MTTR, próximo fallo estimado, último fallo, fecha efectiva
     - Del módulo nativo
     - La fiabilidad y la responsabilidad que aporta el comportamiento mantenible de Odoo.

Compañía (res.company)
----------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Intervalo del service de combustible / completo
     - Número
     - Kilómetros entre services de cada nivel: 15.000 y 30.000 por defecto.
   * - Margen de aviso del service
     - Número
     - Kilómetros restantes a los que un service pasa a Por vencer: 1.500 por defecto.
   * - Firma de los textos de taller
     - Texto
     - Nombre corto con el que se firman los textos de WhatsApp. Vacío usa el nombre de la compañía.

Cómo se usa y qué decide el cliente: :doc:`/17.0/6_resources/index`.
