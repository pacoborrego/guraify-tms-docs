6.8 Configuración
-----------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Configuración: Tareas de mantenimiento, Trabajos, Etapas de
   mantenimiento, Equipos de taller y anomalías de odómetro («Odometer Anomalies»). Los
   umbrales, en la ficha de la compañía.

Lo que se configura una vez, por el administrador, antes de que el taller empiece a trabajar.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Qué se configura
     - Qué decide
   * - Trabajos
     - El catálogo de lo que se hace, con la tarea, el material y el intervalo por defecto de cada
       uno, y si participa en el preventivo. Los cuatro objetivos periódicos son trabajos
       (ver :doc:`6_3_maintenance-model`) y su intervalo es el objetivo en días de los rankings y
       de la orden impresa.
   * - Tareas de mantenimiento
     - La clasificación con la que el taller filtra (ver :doc:`6_3_maintenance-model`). Los
       nombres son únicos sin distinguir mayúsculas.
   * - Etapas de mantenimiento
     - Las etapas de la orden de trabajo. Se pueden renombrar y añadir, con una regla: Pendiente
       debe ser la primera y ninguna etapa cerrada puede ir delante de ella, porque una orden
       nueva nace en la primera etapa.
   * - Equipos de taller
     - Los equipos del módulo nativo, con su técnico responsable. Cada vehículo tiene uno.
   * - Reglas de preventivo
     - Una por vehículo y trabajo, con su intervalo (ver :doc:`6_4_preventive-rules`). Es lo que
       más trabajo lleva al implantar.
   * - Umbrales de la compañía
     - El máximo de kilómetros por día para detectar saltos inverosímiles; los intervalos de la
       revisión de combustible y de la completa y el margen de aviso (ver
       :doc:`6_4_preventive-rules`); y el nombre corto con el que se firman los textos de
       WhatsApp.
   * - Días sin lectura reciente
     - A partir de cuántos días sin lectura válida un vehículo cuenta en el indicador «sin
       lectura reciente» (30 por defecto). Es un parámetro técnico del sistema, no un campo de
       la compañía; su nombre está en :doc:`/17.0/annexes/A_20_mantenimiento`.
   * - Configuración del vehículo
     - En cada vehículo: el tipo de contador (kilómetros u horas de motor), la configuración de
       ejes o carrocería que se imprime junto al tipo, y la referencia de su dispositivo de
       telemetría.

Los datos históricos (vehículos, reglas, trabajos realizados, lecturas de odómetro y pendientes)
no se cargan desde la interfaz: los carga el consultor en la implantación con un script de
importación que se ejecuta desde la consola de Odoo, respeta el punto de entrada único del
odómetro y deja el kilometraje como estimado donde el histórico no lo traía. Campos de todos
estos maestros en :doc:`/17.0/annexes/A_19_odometro` y :doc:`/17.0/annexes/A_20_mantenimiento`.
