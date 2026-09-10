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
cuántos kilómetros llevan, qué mantenimiento necesitan y, en fases posteriores, cuánto
combustible consumen y qué documentación tienen en vigor.

El menú tiene cuatro bloques. **Mantenimiento** es el que usa el taller a diario: Órdenes de
trabajo, Calendario y Tablero del taller (las tres pantallas nativas de Odoo), Reglas de
preventivo, Control de service, Carga masiva de service, Rankings de objetivos e Indicadores.
**Combustible** y **Documentación** están reservados para los módulos previstos y sólo los ve el
administrador mientras estén vacíos. **Configuración** reúne lo que se define una vez: Anomalías
de odómetro, Tareas de mantenimiento, Trabajos, Etapas de mantenimiento y Equipos de taller.

Los permisos son los de la suite. El **usuario TMS** ve el bloque Mantenimiento entero, abre y
cierra órdenes, carga services y saca las salidas de taller; las reglas de preventivo las ve
pero no las edita. El **administrador TMS** ve además Configuración, edita las reglas y valida
las anomalías de odómetro. El tablero completo del taller lo ve cualquier usuario TMS, no sólo
quien creó cada orden, a diferencia de lo que hace el módulo nativo por defecto.

Los dos módulos que forman el área son ``tms_resources`` (el menú raíz y el odómetro) y
``tms_maintenance`` (el mantenimiento), que depende del primero y del módulo nativo
``maintenance``. Los catálogos y umbrales que se configuran están en :doc:`6_8_configuration`;
los campos, en :doc:`/17.0/annexes/A_19_odometro` y :doc:`/17.0/annexes/A_20_mantenimiento`.
