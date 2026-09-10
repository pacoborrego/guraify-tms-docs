A.10 Franjas horarias
=====================

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes › Datos auxiliares › Franjas Horarias

Modelo Odoo: ``tms.time.zone``. Una ventana de servicio reutilizable, de una hora de inicio a una de fin.

Además de los campos de la tabla, el maestro lleva los cuatro campos comunes a todos los catálogos del TMS: **Secuencia** (orden en las listas), **Color** (etiqueta visual), **Compañía** (a qué compañía pertenece; vacío es compartido) y **Defecto** (el registro que el sistema propone cuando hay que elegir uno y nadie ha elegido).

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Zona Horaria
     - Texto (calculado)
     - El nombre se compone solo con el formato HH:MM - HH:MM. En la interfaz el campo se llama «Zona Horaria» aunque es una franja.
   * - Inicio / Fin
     - Hora
     - Hora de inicio y de fin de la ventana. Obligatorias.
   * - Servicio
     - Lista de Tipos de servicio
     - Tipos de servicio con los que se puede usar la franja.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_3_planning-configuration`.
