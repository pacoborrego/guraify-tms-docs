A.9 Áreas geográficas
=====================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Áreas Geográficas

Modelo Odoo: ``tms.area``. Un polígono con significado operativo o económico. Una misma entidad
sirve para cinco usos, que distingue el campo Tipo.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos
del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué
compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando
hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Nombre / Descripción
     - Texto
     - Cómo se identifica el área en listas, reglas y mapas.
   * - Tipo
     - Selección
     - Para qué sirve el área: Plan de Transporte (zona operativa), Zona Tarifa (zona de precio),
       Tarifa Extra (suplemento geográfico), «Operación Artículo» (elemento de operación) o Bajas
       emisiones.
   * - Geometría del Polígono
     - Texto (GeoJSON)
     - El polígono o multipolígono. Se dibuja sobre el mapa o se importa de OpenStreetMap; no se
       edita a mano.
   * - Latitud Centro / Longitud Centro
     - Número (calculado)
     - El centro del polígono, para centrar el mapa y calcular el área más cercana.
   * - Agencia / Hub
     - Relación con Contacto
     - La Agencia y el Hub que heredan los Tramos cuya dirección cae en el área.
   * - Plan de Transporte
     - Lista de Planes de transporte
     - Redes de las que forma parte el área (uso operativo).
   * - Zonas de Tarifa
     - Lista de Zonas de tarifa
     - Zonas de precio de las que forma parte (uso económico).
   * - Lunes … Domingo
     - Sí/No (siete casillas)
     - Días en que la zona operativa admite servicio. Una carga o descarga programada fuera de ellos
       se avisa.
   * - Franjas Horarias
     - Lista de Franjas horarias
     - Franjas de servicio válidas en el área, como referencia.
   * - Incluir filtro de dominio / Filtro de dominios excluidos
     - Texto (dominio)
     - Reglas avanzadas de inclusión y exclusión, para casos que la geometría no resuelve.
   * - Recuento de reglas
     - Número (calculado)
     - Cuántas reglas de automatización del TMS (``tms.rule``) usan el área.
   * - Vista Seguimiento
     - Mapa (calculado)
     - Previsualización del polígono.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
