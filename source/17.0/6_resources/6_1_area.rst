6.1 El área y su menú
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Menú raíz **Gestión de Recursos**, con Mantenimiento, Combustible, Documentación y
   Configuración.

.. CAPTURA: 6_1_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_1_area_01_menu.png
      :alt: Menú Gestión de Recursos

      El menú Gestión de Recursos con sus cuatro bloques.

Gestión de Recursos es una aplicación propia en el menú de Odoo, separada de TMS. La usa el
taller y quien controla la flota, y agrupa lo que tiene que ver con los vehículos como recursos:
cuántos kilómetros llevan y qué mantenimiento necesitan.

El menú tiene cuatro bloques. **Mantenimiento** es el que usa el taller a diario: Indicadores,
Órdenes de trabajo, Calendario y Tablero del taller (las tres últimas son las pantallas nativas
de Odoo), Reglas de preventivo, control de revisiones («Control de service» en el menú), carga
masiva de revisiones («Carga masiva de service») y Rankings de objetivos. **Combustible** y
**Documentación** son bloques reservados, sin contenido, que solo ve el administrador.
**Configuración** reúne lo que se define una vez: anomalías de odómetro («Odometer Anomalies»
en el menú), Tareas de mantenimiento, Trabajos, Etapas de mantenimiento y Equipos de taller.

Los permisos son los de la suite. El **usuario TMS** ve el bloque Mantenimiento entero, abre y
cierra órdenes, carga revisiones y saca las salidas de taller; las reglas de preventivo las ve
pero no las edita. El **administrador TMS** ve además Configuración, edita las reglas y valida
las anomalías de odómetro. El tablero completo del taller lo ve cualquier usuario TMS, no solo
quien creó cada orden, a diferencia de lo que hace el módulo nativo por defecto.

Los catálogos y umbrales que se configuran están en :doc:`6_8_configuration`; los campos, en
:doc:`/17.0/annexes/A_19_odometro` y :doc:`/17.0/annexes/A_20_mantenimiento`.

6.1.1 Referencia técnica
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Módulo
     - Qué aporta
   * - ``tms_resources``
     - El menú raíz Gestión de Recursos y el odómetro único (extensión de ``fleet.vehicle`` y
       ``fleet.vehicle.odometer``).
   * - ``tms_maintenance``
     - El mantenimiento: reglas de preventivo, cierre con kilometraje, salidas de taller e
       indicadores. Depende de ``tms_resources`` y del módulo nativo ``maintenance``.
