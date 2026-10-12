A.29 Presets de optimización
============================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Presets de optimización (solo responsables)

Modelo Odoo: ``tms.ptv.preset``. Lo que el motor de optimización persigue y lo que puede violar.
Vienen cuatro de serie (Máxima calidad, Máxima rentabilidad, Balancear vehículos, Sacar todo como
sea), uno por compañía. Qué hace cada uno y cuándo elegirlo: sección 4.3.7 de
:doc:`/17.0/4_parametrization/4_3_planning-configuration`.

Los campos de la pestaña de un motor solo se envían cuando la optimización se lanza con ese motor;
las etiquetas de la interfaz están en inglés en parte.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre / Descripción
     - Texto
     - Cómo se identifica el preset en el asistente y qué hace, en una frase. Traducibles.
   * - Secuencia
     - Número
     - Orden en la lista desplegable del asistente.
   * - Motor
     - Selección (Ambos motores, solo uno u otro)
     - Con qué motor de optimización se ofrece el preset.
   * - Compañía
     - Relación con Compañía
     - A qué compañía pertenece.
   * - Casillas marcadas por defecto: Aplicar tolerancia, Permitir violar restricciones de vía,
       Permitir violar jornada, km, paradas y carga, Respetar zonas operativas
     - Sí/No y selección (No, Estricto, Preferido)
     - Lo que el asistente marca al elegir el preset. El planificador puede cambiarlas en cada
       lanzamiento; lo que se ejecuta son las casillas de la ejecución.
   * - Coste de salir de la zona
     - Importe
     - Con «Respetar zonas operativas» en Preferido, lo que cuesta asignar una Parada a un vehículo
       que no tiene su zona permitida. Uno por preset, no por zona.
   * - Duración de la búsqueda (s) / Parar sin mejora tras (s)
     - Número
     - Cuánto busca el motor y cuándo se detiene si no mejora. Cero conserva el valor de la
       ejecución.
   * - Compacidad / Equilibrio de duración
     - Número de 0 a 1
     - Cuánto prefiere Viajes compactos y cuánto iguala la duración entre rutas. Cero conserva el
       valor de cada vehículo.
   * - Usar costes del vehículo
     - Sí/No
     - Si se envían los costes de cada vehículo o categoría. Desmarcado, o cuando un vehículo no
       tiene ninguno, se usan los del preset.
   * - Coste fijo, por hora, por km, por parada
     - Importe
     - Los costes propios del preset, cuando no se usan los del vehículo.
   * - Coste del vehículo sin usar
     - Importe
     - Lo que cuesta dejar un vehículo disponible sin ruta. Es lo que hace que «Balancear
       vehículos» saque todos los vehículos.
   * - Coste por parada sobre el reparto justo
     - Importe
     - Cero: apagado. Si no, cada vehículo paga esto por cada Parada por encima de su parte.
   * - Ignorar costes fijos
     - Sí/No
     - Envía el coste fijo a cero, de modo que usar un vehículo más no cuesta nada.
   * - Usar el coste de no planificar
     - Sí/No
     - Envía el coste de no planificar una Orden que fija el Proyecto; sin él, el motor puede dejar
       Órdenes fuera gratis.
   * - Usar el ingreso de la Orden
     - Sí/No
     - Envía el importe del Tramo como ingreso: el motor solo planifica lo que se paga. Es la base
       de «Máxima rentabilidad».
   * - Límites blandos y sus costes (hora extra, km extra, parada extra, unidad de carga extra)
     - Sí/No e importes
     - El preset está pensado para correr con la casilla de jornada marcada: jornada, km, Paradas
       y carga pasan de límites a costes por exceso con estos importes. La conducción máxima sigue
       siendo un límite duro.
   * - Calidad / Optimización premium / Ajustes del objetivo / Considerar prioridades
     - Selección y Sí/No
     - Para el motor estándar: calidad de la búsqueda (estándar o alta), si se pide la
       optimización premium (cuando la compañía la tiene), si se evitan cruces o se deja de
       minimizar el número de rutas, y si se respetan las prioridades de los transportes.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
