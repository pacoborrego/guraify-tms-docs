6.8 Configuración
-----------------

.. admonition:: Ruta en Odoo
   :class: tip

   Gestión de Recursos › Configuración: Tareas de mantenimiento, Trabajos, Etapas de
   mantenimiento, Equipos de taller y Odometer Anomalies. Los umbrales, en la ficha de la
   compañía.

Lo que se configura una vez, por el administrador, antes de que el taller empiece a trabajar.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Qué se configura
     - Qué decide
   * - Trabajos
     - El catálogo de lo que se hace, con la tarea, el material y el intervalo por defecto de cada
       uno, y si participa en el preventivo. Los cuatro objetivos periódicos son trabajos, y su
       intervalo es el objetivo en días de los rankings y de la orden impresa.
   * - Tareas de mantenimiento
     - La clasificación con la que el taller filtra: Preventivo, Taller, Reparación, Gomería,
       Lavado... Los nombres son únicos sin distinguir mayúsculas.
   * - Etapas de mantenimiento
     - Las etapas de la orden de trabajo. Se pueden renombrar y añadir, con una regla: Pendiente
       debe ser la primera y ninguna etapa cerrada puede ir delante de ella, porque una orden
       nueva nace en la primera etapa.
   * - Equipos de taller
     - Los equipos del módulo nativo, con su técnico responsable. Cada vehículo tiene uno.
   * - Reglas de preventivo
     - Una por vehículo y trabajo, con su intervalo (ver :doc:`6_4_preventive-rules`). Es lo que
       más trabajo lleva al implantar: el cliente de referencia partió de setecientas cuarenta.
   * - Umbrales de la compañía
     - El máximo de kilómetros por día para detectar saltos inverosímiles (1.500); los intervalos
       del service de combustible (15.000) y completo (30.000) y el margen de aviso (1.500); y la
       firma corta con la que se firman los textos de WhatsApp.
   * - Configuración de la unidad
     - En cada vehículo: el tipo de contador (kilómetros u horas de motor), la configuración de
       ejes o carrocería que se imprime junto al tipo, y la referencia de su dispositivo de
       telemetría.

Los datos históricos del cliente (unidades, reglas, realizados, lecturas de odómetro, pendientes
y objetivos) se cargan con una herramienta de importación propia de la implantación, que
respeta el punto de entrada único del odómetro y deja el kilometraje estimado donde el
histórico no lo traía. Campos de todos estos maestros en
:doc:`/17.0/annexes/A_19_odometro` y :doc:`/17.0/annexes/A_20_mantenimiento`.
