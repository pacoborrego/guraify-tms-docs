A.34 Contacto TMS y acceso a la app
===================================

.. admonition:: Ruta en Odoo
   :class: tip

   Ficha del contacto › pestañas Propiedades TMS y Horarios TMS · ficha del usuario · TMS ›
   Configuración › App

Modelo Odoo: ``res.partner`` (y ``res.users`` y ``tms.app.device.token`` para la app). Los campos
que el TMS añade al contacto de Odoo, agrupados como en la ficha.

A.34.1 Cabecera
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Alias
     - Texto
     - Nombre corto: lo buscan las importaciones y lo usan la hoja de ruta, el listado de
       etiquetas y la lista de facturas (``tms_alias``).
   * - Dirección completa
     - Texto
     - La dirección tal como llegó en el fichero (``tms_checkout_address_original``). Solo en los
       contactos.
   * - Secuencia autofactura
     - Número
     - Contador de las autofacturas de compra del transportista (``sequence_autoinvoice``).

A.34.2 Pestaña Propiedades TMS
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Agencia · Hub
     - Sí/No
     - El contacto es una agencia o un hub. Solo en empresas (``tms_is_agency``, ``tms_is_hub``).
   * - Contacto
     - Sí/No
     - Es una dirección de carga o descarga (``tms_is_contact``).
   * - Es Conductor
     - Sí/No
     - Es un conductor (``tms_is_driver``).
   * - Cliente/transportista TMS
     - Sí/No
     - Es un cliente o un transportista del TMS (``is_tms_partner``).
   * - Clientes Relacionados
     - Relación
     - Los clientes de los que es dirección. Solo en los contactos.
   * - Transportista
     - Relación
     - El transportista del conductor; obligatorio en los conductores (``tms_carrier_id``).
   * - Horas de Conducción · Factor de velocidad del conductor
     - Relación · Número
     - Solo en los conductores; ver A.12.
   * - Transportista de flota propia
     - Sí/No
     - Sus Viajes no generan orden de compra ni coste de compra (``tms_is_own_fleet``).
   * - Audiencia del portal · manual
     - Selección
     - Solo responsables; ver la Guía del integrador.
   * - Prioridad
     - Estrellas
     - Prioridad de sus Paradas en la optimización y la secuenciación (``tms_priority``).
   * - Dificultad Parking · Ascensor · Plantas a Subir
     - Estrellas · Sí/No · Número
     - Entran en el tiempo de servicio de sus Paradas.
   * - Autorizado a Dejar en Puerta · Coste de Peaje/Tasa por Acceso
     - Sí/No
     - Informativos.
   * - Latitud · Longitud · Precisión · Tipo Localización
     - Número · Texto
     - La geolocalización del contacto (GEOLOCALIZACIÓN).
   * - Grupo TACÓGRAFO
     - Solo lectura
     - Estado y tiempos restantes de conducción y de trabajo del conductor, cuando los manda la
       telemática.
   * - Grupo AVISOS
     - —
     - Ver :doc:`A_33_avisos`.

A.34.3 Pestaña Horarios TMS
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Tiempo por Recogida en min · Tiempo por entrega en min
     - Número
     - Minutos que se reservan en cada recogida o entrega en el contacto.
   * - MAÑANA y TARDE: inicio y fin por defecto
     - Hora
     - El horario habitual.
   * - MAÑANA y TARDE: cada día de la semana
     - Sí/No y horas
     - Si abre ese día por la mañana o por la tarde, y de qué hora a qué hora.

A.34.4 Usuario y app
--------------------

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Funciones de la aplicación TMS
     - Etiquetas (``res.users.role_ids``)
     - Los roles de la app del usuario: Repartidor, Operario Hub, Jefe de Tráfico, Destinatario,
       Cliente.
   * - Rol de la app: nombre y código
     - Texto (``tms_app.role``: ``name``, ``app_id``)
     - El código es lo que entiende la app (``driver``, ``hub_operation``, ``fleet_manager``,
       ``receiper``, ``client``). Un rol sin código no habilita nada.
   * - Token de dispositivo
     - ``tms.app.device.token``
     - Uno por inicio de sesión: dispositivo, usuario, contacto, **Versión de la app**, activo,
       último uso y fecha de revocación. Botón **Revocar**.
   * - Token obligatorio
     - Parámetro del sistema
     - ``tms_app.enforce_token``: con valor ``1``, la app no puede llamar a Odoo sin un token
       válido. Por defecto, desactivado.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`.
