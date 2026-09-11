6 Gestión de Recursos
=====================

Este capítulo describe el área **Gestión de Recursos** del TMS: el kilometraje de la flota y el
mantenimiento de los vehículos. Es el área que usa el taller, no el departamento de tráfico, y
por eso vive en su propio menú raíz.

La tesis del área es la misma que la del resto del sistema: usar lo que Odoo ya tiene y
construir solo lo que no existe. El vehículo de la Flota de Odoo es el elemento mantenible; las
órdenes de trabajo, las etapas, el calendario, el tablero del taller y la recurrencia por tiempo
son las del módulo nativo de Mantenimiento. Lo que Odoo no sabe hacer en ningún módulo, y aquí
se construye, son dos cosas: un **odómetro único** con control de calidad, en el que confluyen
todas las lecturas de kilometraje, y el **disparo del mantenimiento preventivo por kilómetros**.

.. mermaid::

   flowchart LR
       L["Lecturas de km<br/>taller · combustible · app · telemetría"] --> O["Odómetro único<br/>anomalías y validación"]
       O --> R["Reglas de preventivo<br/>por km y por días"]
       R -->|umbral cruzado| P["Orden de trabajo<br/>pendiente"]
       P --> C["Cierre con km"]
       C --> O
       O --> S["Control de revisiones<br/>dos niveles"]
       R --> W["Salidas de taller<br/>orden impresa · WhatsApp · rankings"]
       R --> K["Indicadores"]

.. toctree::
   :maxdepth: 1

   6_1_area
   6_2_odometer
   6_3_maintenance-model
   6_4_preventive-rules
   6_5_workshop-flows
   6_6_outputs
   6_7_kpis
   6_8_configuration
