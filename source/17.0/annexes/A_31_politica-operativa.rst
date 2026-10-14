A.31 Política operativa
=======================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › bloque Operación › Políticas operativas · Proyecto › pestaña
   Operación

Modelo Odoo: ``tms.operations.policy``. Una política para la compañía (sin Proyecto) y, como
mucho, una por Proyecto, que gana a la de la compañía. La leen los usuarios del TMS y la cambian
los responsables. Sin ninguna, se aplican los valores por defecto de la tabla.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Compañía / Proyecto
     - Relación
     - El alcance (grupo **Alcance**). Sin Proyecto, es la política de la compañía.
   * - Recálculo de ETA
     - Selección
     - **Desactivado**, **Al cerrar una parada** (por defecto), **Cada N minutos**, **Al cerrar
       una parada y cada N minutos** o **Al desviarse del plan** (``eta_recompute_mode``).
   * - Intervalo de recálculo (min)
     - Número
     - Cada cuántos minutos en los modos por intervalo; 15 por defecto.
   * - Intervalo mínimo (min)
     - Número
     - Tiempo mínimo entre dos recálculos del mismo Viaje; 5 por defecto.
   * - Umbral de desviación (min)
     - Número
     - Aparece con el modo Al desviarse del plan; hoy no lo usa ningún cálculo.
   * - Tope diario de llamadas
     - Número
     - Recálculos como máximo por Viaje y día; 0 es sin tope.
   * - Pedir costes de peaje
     - Sí/No
     - Si el cálculo de ruta pide los peajes a PTV (grupo **Resultados del routing**).
   * - Esquema de emisiones
     - Selección
     - Ninguno, EN 16258:2012 o ISO 14083:2023 (por defecto). Un solo esquema por cálculo.
   * - Reparto de CO2
     - Selección
     - **Por distancia** (por defecto) o **Por número de paradas**.
   * - Enriquecimiento del routing
     - Etiquetas
     - Los bloques adicionales que se piden a PTV sobre la ruta (grupo **Enriquecimiento**). El
       catálogo está en Ajustes › Operación › Bloques de resultado del routing.
   * - Geocerca de llegada (m)
     - Número
     - Radio que cuenta como llegada a la Parada para el conector de telemática; 150 por
       defecto. El Tipo de Parada puede tener el suyo (grupo **Geocercas**).
   * - Sin evento tras el ETA (min)
     - Número
     - Alarma de la torre de control; 30 por defecto. Reservado.
   * - Vehículo parado (min)
     - Número
     - Alarma de la torre de control; 20 por defecto. Reservado.
   * - Desviación de ruta (km)
     - Número
     - Alarma de la torre de control y umbral del modo Al desviarse del plan: una posición a más
       de esta distancia de la siguiente Parada pide un recálculo; 2 por defecto.
   * - Viaje sin empezar (min)
     - Número
     - Alarma de la torre de control; 15 por defecto. Reservado.
   * - Visibilidad de la posición del vehículo
     - Selección
     - **Siempre**, **Solo cuando es la siguiente parada** (por defecto) o **Solo cuenta atrás,
       sin posición**: lo que verá el Destinatario (grupo **Privacidad del destinatario**).
       Reservado.
   * - El destinatario puede reprogramar / cambiar la dirección
     - Sí/No
     - Lo que podrá hacer el Destinatario desde su página de seguimiento. Reservado.

«Reservado»: el campo se guarda, pero ningún proceso lo lee todavía; es para la torre de control.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
