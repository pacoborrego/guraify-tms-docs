4.1 Configuración operativa
---------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › Ajustes, bloque **Datos auxiliares**: «Tipos de servicios», Tipos de
   Orden, «Tipos de parada», Tipos de Destinatario, «Tipos de transportista» y Tipos de
   Reembolso. Cada enlace del bloque abre la lista del catálogo, desde la que se crean, se
   modifican y se archivan los registros.

La configuración operativa son seis catálogos pequeños que clasifican lo que se mueve por el
sistema: el servicio que se vende, la Orden, la Parada, el Destinatario, el Transportista y la
forma de cobrar un Reembolso. Ninguno lleva precios ni horarios, pero casi todos los procesos
los usan como criterio: el Tipo de Orden decide qué lado de un Tramo es el hub y cuál el
cliente; el Tipo de Parada, qué Paradas se pueden planificar; los tipos de servicio, de
destinatario y de transportista son condiciones de las Líneas de tarifa y filtros del
Proyecto. Por eso se configuran antes que el resto del capítulo y se cambian poco después.

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_01_datos-auxiliares.png
   :align: center
   :alt: Panel de Datos auxiliares en Ajustes

   El bloque «Datos auxiliares» de TMS › Configuración › Ajustes, punto de entrada a los seis
   catálogos.

Cada maestro se describe aquí por lo que decide el cliente y por dónde se nota después. Detrás
de los seis catálogos vienen tres configuraciones que no son catálogos pero se hacen al principio:
la marca de la compañía (4.1.7), los contactos con su papel en el TMS (4.1.8) y los conductores
con su acceso a la app (4.1.9). La lista completa de campos de cada pantalla está en el
:doc:`anexo A </17.0/annexes/index>`.

4.1.1 Tipos de Servicio
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_02_tipos-servicio-lista.png
   :align: center
   :alt: Lista de Tipos de Servicio

   Lista de Tipos de Servicio: productos, Tipos de Orden compatibles y variables logísticas de
   cada uno.

El Tipo de Servicio (``tms.service.type``) clasifica el servicio de transporte que se vende:
carga completa, grupaje, distribución urbana, entrega con compromiso horario, larga distancia,
movimiento interno. Es la dimensión comercial de la Orden y el puente entre lo que se hace y
lo que se factura: cada Orden, cada Tramo y cada Viaje llevan un tipo de servicio, y las
Líneas de tarifa lo usan para dar precios distintos a servicios distintos.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué servicios existen
     - Una operativa con precios, plazos o exigencias distintas merece un tipo propio; dos
       servicios que se cobran y se planifican igual no. Cada tipo es un criterio más que la
       tarifa y el Proyecto tendrán que contemplar.
   * - Productos
     - Los productos TMS con los que se relaciona el servicio. Es obligatorio informar al
       menos uno y solo se admiten productos marcados como Producto TMS (ver
       :doc:`4_4_economic-configuration`). El producto que finalmente lleva cada línea
       económica lo fija la Línea de tarifa.
   * - Tipos de Orden compatibles
     - Con qué Tipos de Orden se puede combinar el servicio. Sirve de referencia al
       configurar el Proyecto y las tarifas.
   * - Variables logísticas
     - Las casillas Bultos, Cantidad, Metros y Palés dicen qué magnitudes intervienen en
       el servicio. Al añadir mercancía a un Tramo, el sistema solo ofrece las Reglas de tarifa
       que miden alguna de las magnitudes marcadas (ver :doc:`4_2_logistic-configuration`).

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_03_tipos-servicio-form.png
   :align: center
   :alt: Formulario de un Tipo de Servicio

   Formulario de un Tipo de Servicio con sus variables logísticas.

El tipo de servicio aparece después en tres sitios. En el **Proyecto**, la lista de servicios
activados limita los que se pueden elegir en sus Órdenes, uno de ellos se propone por
defecto, y un servicio aparte tarifica la recogida a domicilio (ver
:doc:`4_5_project-configuration`). En las **Líneas de tarifa**, el servicio es una de las
condiciones que deciden si la línea aplica (ver :doc:`4_4_economic-configuration`). Y en las
**Franjas horarias**, cada franja puede limitarse a unos servicios (ver
:doc:`4_3_planning-configuration`). Campos en :doc:`/17.0/annexes/A_23_tipos-servicio`.

4.1.2 Tipos de Orden
~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_04_tipos-orden.png
   :align: center
   :alt: Lista de Tipos de Orden

   Lista de Tipos de Orden: las cuatro marcas de comportamiento y los porcentajes de carga y
   descarga.

El Tipo de Orden (``tms.shipment.type``) define el comportamiento logístico de la Orden dentro
de la red: si es una entrega desde el hub, una recogida hacia el hub, un servicio directo
entre dos puntos del cliente o una operación de hub. Mientras el Tipo de Servicio dice qué se
vende, el Tipo de Orden dice cómo circula la mercancía.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - La marca de comportamiento
     - Cada tipo lleva una de las cuatro marcas: **Entrega**, **Recogida**, **Directo** o
       **Hub**. Al crear un Tramo con ese tipo, el sistema propone qué lado es el del cliente
       y cuál el del hub o la agencia del Proyecto (en una entrega se carga en el hub; en una
       recogida se descarga en él; en un directo los dos lados son del cliente; en una
       operación de hub los dos lados son el hub). Al validar la Orden, esa misma marca decide
       qué Tipo de Parada recibe cada lado y con qué otros Tramos puede compartir Parada (ver
       :doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`).
   * - Activo Carga % y Activo Descarga %
     - Cómo se reparte el ingreso de un Tramo entre su Parada de carga y su Parada de
       descarga. Los dos porcentajes deben sumar el 100 %; el sistema no guarda el registro si
       no lo hacen. Es la segunda mitad de la :term:`División de ventas` (ver
       :doc:`/17.0/8_economic-administration/8_2_sales-split`).
   * - Punto de Recogida Habitual
     - Marca el tipo con el que el sistema crea la Orden de recogida a domicilio cuando el
       Proyecto trabaja con punto de recogida en casa del cliente. Tiene que existir uno, o el
       cierre del Manifiesto se detiene.
   * - Imagen y color
     - El icono que acompaña a la Orden y al Tramo en las listas, para reconocer el tipo de un
       vistazo.

El Tipo de Orden no crea los Tramos: los crea el usuario, o el fichero, o la integración. Lo
que hace es decidir cómo se interpretan. Después aparece como condición en las Líneas de
tarifa y en sus detalles, y en el Proyecto como lista de tipos admitidos y tipo por defecto.
El Manifiesto cuenta sus Órdenes por tipo (entregas, recogidas, directos y operaciones de hub).
Campos en :doc:`/17.0/annexes/A_24_tipos-orden`.

4.1.3 Tipos de Parada
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_05_tipos-parada.png
   :align: center
   :alt: Lista de Tipos de Parada

   Lista de Tipos de Parada: seis registros, cada uno con una única marca activa.

El Tipo de Parada (``tms.stop.type``) dice qué papel juega una Parada en la operativa. A
diferencia de los otros catálogos, aquí el cliente no decide cuántos registros hay: el modelo
define **seis papeles**, cada registro lleva exactamente uno y no puede haber dos registros de
la misma compañía con el mismo papel. Los seis papeles son **Operaciones de Hub** (la entrada o
la salida de mercancía en un hub), **Punto de Recogida** (la carga de una recogida a
domicilio), **Parada de Ruta** (la parada en casa del cliente, la que se planifica y se
reparte), **Recogida Directo** y **Entrega Directo** (los dos lados de un servicio directo) y
**Paradas Optimizador** (las paradas de inicio y fin que genera el optimizador; no son eventos
ejecutables).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Nombre, descripción e imagen de cada papel
     - Es lo único que el cliente adapta: cómo se llama cada tipo en su casa y con qué icono
       lo ven el planificador en las listas y el conductor en la app. El papel no se cambia:
       al marcar una casilla se desmarcan las demás.
   * - Que existan los seis, en cada compañía
     - El sistema busca cada papel por su marca cuando lo necesita: al validar una Orden
       asigna Parada de Ruta, Operaciones de Hub, Punto de Recogida o los dos directos según el
       Tramo; al optimizar crea las paradas de inicio y fin con el papel de optimizador. Lo
       busca primero en la compañía del registro. Si a esa compañía le falta un papel, usa el
       de otra compañía y lo deja anotado como aviso en el registro del servidor: funciona, pero
       la Parada queda con un tipo ajeno. Cada compañía nueva necesita sus seis.

El papel condiciona lo que se puede hacer con la Parada. Solo las Paradas de Ruta y las
directas se asignan a un Viaje, se envían a una agencia o se reprograman; las de hub las crea
y las quita el propio Viaje, y las de optimizador quedan fuera de la secuenciación y de los
documentos de carga. Cómo se asigna el tipo al validar y qué estados recorre después la
Parada está en :doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`. Campos en
:doc:`/17.0/annexes/A_25_tipos-parada`.

4.1.4 Tipos de Destinatario
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_06_tipos-destinatario.png
   :align: center
   :alt: Lista de Tipos de Destinatario

   Lista de Tipos de Destinatario.

El Tipo de Destinatario (``tms.receiper.type``) segmenta a quién se entrega: empresa o
particular, comercio, hostelería, gran superficie, punto de conveniencia. Es un catálogo
libre, sin comportamiento propio, cuyo valor está en lo que permite condicionar.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué segmentos existen
     - Solo merecen un tipo los segmentos que cambian el precio o la operativa (una entrega a
       particular con franja estrecha frente a una entrega a un almacén). Cada segmento es una
       condición más que las tarifas pueden usar.

El tipo se informa en la Orden y lo heredan sus Tramos y su Viaje. El Proyecto lista los
tipos que admite y propone uno por defecto; las Líneas de tarifa lo usan como condición para
que el mismo servicio tenga precios distintos según a quién se entregue (ver
:doc:`4_4_economic-configuration` y :doc:`4_5_project-configuration`). Campos en
:doc:`/17.0/annexes/A_26_tipos-destinatario`.

4.1.5 Tipos de Transportista
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_07_tipos-transportista.png
   :align: center
   :alt: Lista de Tipos de Transportista

   Lista de Tipos de Transportista.

El Tipo de Transportista (``tms.carrier.type``) clasifica a quien ejecuta el transporte:
flota propia, transportista con contrato estable, transportista para picos de demanda,
agencia. Como el anterior, es un catálogo libre que sirve de condición.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué clases de transportista existen
     - Las que se pagan o se asignan de forma distinta. El tipo no sustituye a la marca de
       flota propia del contacto, que es la que decide si el Viaje genera Orden de compra (ver
       :doc:`/17.0/8_economic-administration/8_1_active-passive-margin`).

El tipo se informa en la Orden, en el Tramo y en el Viaje, y el asistente **Asignar a viaje**
permite fijarlo al crear el Viaje. El Proyecto lista los tipos que admite y propone uno por
defecto; las Líneas de tarifa lo usan como condición, de modo que un mismo recorrido puede
costar distinto según la clase de transportista que lo haga (ver
:doc:`4_4_economic-configuration` y :doc:`/17.0/5_operational-flows/5_2_trip-generation`).
Campos en :doc:`/17.0/annexes/A_27_tipos-transportista`.

4.1.6 Tipos de Reembolso
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/4_parametrization/4_1_operational-configuration_08_tipos-reembolso.png
   :align: center
   :alt: Lista de Tipos de Reembolso

   Lista de Tipos de Reembolso.

El Tipo de Reembolso (``tms.cashvalue.type``) es la forma de cobro de un :term:`Reembolso`:
en metálico, con TPV propio o del cliente, con cheque bancario. No es el importe ni el estado
del cobro; es la modalidad con la que el conductor debe cobrarlo.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - Qué formas de cobro existen
     - Las que la empresa acepta en la entrega. Cada Reembolso de un Tramo lleva una, y el
       conductor la ve en la app junto al importe, así que el nombre debe entenderse en la
       calle («Efectivo», «TPV», «Cheque»).

El tipo se elige al dar de alta el Reembolso en el Tramo, viaja con él a la app y queda en el
registro del cobro, con lo que la administración puede agrupar lo cobrado por modalidad. El
ciclo completo del Reembolso está en :doc:`/17.0/8_economic-administration/8_6_refunds` y el
cobro en la calle, en el :doc:`Manual del conductor </17.0/10_manual_app/index>`. Campos en
:doc:`/17.0/annexes/A_28_tipos-reembolso`.

4.1.7 Marca de la compañía
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   Ajustes › Usuarios y compañías › Compañías › la compañía › pestaña **Marca**

.. CAPTURA: 4_1_09 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_1_operational-configuration_09_marca.png
      :alt: Pestaña Marca de la ficha de la compañía

      La pestaña Marca: logos, paleta de día y de noche, tipografía, dominio y remitente.

Cada compañía tiene su **marca**: lo que lleva su nombre ante el conductor, el cargador y el
Destinatario. No es un catálogo sino una pestaña de la ficha de la compañía, pero se configura al
principio, como los catálogos, porque la app del conductor y el DeCA la necesitan desde el primer
día. Si una instalación tiene varias compañías, cada una lleva la suya.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Quién la usa
   * - Logo de la aplicación y **Paleta de día** (colores principal, secundario y terciario, de
       estado y neutros)
     - La app del conductor, que los recibe al iniciar sesión.
   * - Logo horizontal
     - El encabezado del DeCA y de la hoja de ruta que lo acompaña; sin él, se usa el logo de la
       compañía.
   * - Nombre del remitente de mensajería
     - El remitente que lee el Destinatario en los avisos por correo, SMS y WhatsApp
       (:doc:`/17.0/11_notifications/index`); vacío, el nombre de la compañía.
   * - Dominio de Connect
     - La dirección desde la que se servirá la torre de control de la compañía, y con ella el
       enlace de seguimiento de los avisos (cuya página todavía no existe).
   * - Favicon, **Tipografía** y **Paleta de noche (opcional)**
     - Reservados para la torre de control y las páginas de seguimiento. Hoy no los lee nadie:
       la app no recibe la tipografía ni la paleta de noche.

Los colores se escriben en hexadecimal (#1A2B3C). Campos en :doc:`/17.0/annexes/A_32_marca`.

.. _contactos-tms:

4.1.8 Contactos TMS
~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Maestros › Operaciones: **Contactos**, **Hubs**, **Agencias** · TMS › Maestros ›
   Recursos Humanos › **Conductores** · TMS › Administración › Maestros: **Clientes**,
   **Proveedores** · en la ficha, pestañas **Propiedades TMS** y **Horarios TMS**

.. CAPTURA: 4_1_10 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_1_operational-configuration_10_contacto-hub.png
      :alt: Pestaña Propiedades TMS de un hub

      La pestaña Propiedades TMS de un hub: sus marcas, la información de acceso y la
      geolocalización.

En el TMS todo el que interviene es un contacto de Odoo: el cliente, el transportista, la agencia,
el hub, el conductor y la persona a la que se entrega. Lo que hace que un contacto cumpla un papel
son unas **marcas** en su ficha, y cada menú del TMS enseña los contactos de un papel:

.. list-table::
   :header-rows: 1
   :widths: 22 38 40

   * - Papel
     - Marca en la ficha (pestaña Propiedades TMS)
     - Dónde se ven
   * - Cliente
     - **Cliente/transportista TMS**, y cliente en Odoo
     - Administración › Maestros › Clientes. Tiene Proyectos y recibe las facturas.
   * - Transportista
     - **Cliente/transportista TMS**, y proveedor en Odoo; **Transportista de flota propia** si
       conduce gente de la casa
     - Administración › Maestros › Proveedores. Recibe las órdenes de compra de los Viajes (no
       si es flota propia, ver :doc:`/17.0/8_economic-administration/8_1_active-passive-margin`).
   * - Agencia
     - **Agencia** (solo empresas)
     - Maestros › Operaciones › Agencias. Recibe los arrastres (:doc:`/17.0/3_functional-architecture/3_2_6_legs-and-stops`).
   * - Hub
     - **Hub** (solo empresas)
     - Maestros › Operaciones › Hubs. Origen y destino de los Tramos de hub y de los Viajes.
   * - Contacto de carga o descarga
     - **Contacto**, con sus **Clientes relacionados**
     - Maestros › Operaciones › Contactos. Es la dirección de una Parada y, en una entrega, el
       Destinatario. Casi siempre llega por la importación.
   * - Conductor
     - **Es Conductor**, con su **Transportista** (obligatorio)
     - Maestros › Recursos Humanos › Conductores. Ver 4.1.9.

Un mismo contacto puede tener varias marcas (un hub que también es agencia). Fuera de las marcas,
la ficha del contacto decide:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decisión
     - Efecto
   * - **Alias** (cabecera)
     - El nombre corto con el que lo identifican las importaciones (el transportista o el
       conductor de un fichero se buscan por alias), el que sale en la hoja de ruta y en el
       listado de etiquetas, y el «Nombre breve» del cliente en la lista de facturas.
   * - **Dirección completa** (cabecera, en los contactos)
     - La dirección tal como llegó en el fichero, antes de normalizarla.
   * - **Secuencia autofactura** (transportistas)
     - El contador de las autofacturas de compra del transportista, que forma su referencia.
   * - INFORMACIÓN DE CONTACTO: **Prioridad**
     - La prioridad con que el optimizador y la secuenciación tratan sus Paradas.
   * - INFORMACIÓN DE CONTACTO: **Dificultad Parking**, **Ascensor**, **Plantas a subir**
     - Entran en el cálculo del tiempo de servicio de sus Paradas
       (:ref:`17.0/4_parametrization/4_3_planning-configuration:4.3.5 Tiempos de servicio`). Un
       cuarto piso sin ascensor tarda más que una planta baja.
   * - INFORMACIÓN DE CONTACTO: **Autorizado a Dejar en Puerta**, **Coste de Peaje/Tasa por
       Acceso**
     - Informativos: hoy no los lee ningún cálculo.
   * - GEOLOCALIZACIÓN
     - Las coordenadas, su precisión y el tipo de localización
       (:ref:`17.0/1_introduction/1_4_technological-architecture:1.4.3.1 Geocodificación de direcciones`).
       Sin coordenadas buenas, ninguna Parada del contacto se planifica bien.
   * - **Horarios TMS**: Tiempo por recogida y Tiempo por entrega (min)
     - Los minutos que el optimizador y la secuenciación reservan en cada recogida o entrega en
       el contacto.
   * - **Horarios TMS**: MAÑANA y TARDE
     - El horario por defecto de mañana y de tarde y, día a día, si abre y de qué hora a qué hora.
       Son las ventanas que PTV respeta para hubs y clientes al secuenciar y optimizar, y las
       horas por defecto de carga y descarga.

La pestaña Propiedades TMS tiene además el grupo **TACÓGRAFO** de los conductores, que solo se
lee (lo rellena la telemática), el grupo **AVISOS** (:doc:`/17.0/11_notifications/11_4_recipient`)
y, para los responsables, la audiencia del portal del contacto. La cabecera lleva los botones
**Reglas TMS** y, en los conductores, **Historial de vehículos**. Campos en
:doc:`/17.0/annexes/A_34_contacto`.

.. _conductores-app:

4.1.9 Conductores y acceso a la app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Maestros › Recursos Humanos › Conductores · Ajustes › Usuarios y compañías › Usuarios ›
   el usuario, campo **Funciones de la aplicación TMS** · TMS › Configuración › App › **Roles de
   la app** y **Tokens de dispositivo**

.. CAPTURA: 4_1_11 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_1_operational-configuration_11_usuario-roles.png
      :alt: Ficha de un usuario con sus funciones de la aplicación TMS

      El usuario de un conductor con su rol de la app.

Para que un conductor trabaje con la app hacen falta tres cosas en Odoo, y las tres tienen que
apuntar a la misma persona: su **contacto** de conductor, un **usuario** unido a ese contacto y
un **rol de la app** en ese usuario.

**1. El contacto conductor.** Un contacto con **Es Conductor** marcado y su **Transportista**
(obligatorio: la propia compañía si es flota propia). El campo Conductor del Viaje solo ofrece
contactos marcados así. En el conductor se ponen también, si hacen falta, sus **Horas de
Conducción** y su **Factor de velocidad del conductor**
(:ref:`17.0/4_parametrization/4_3_planning-configuration:4.3.6 Horas de conducción`); el botón
**Historial de vehículos** enseña con qué vehículos ha hecho sus Viajes.

**2. El usuario.** Un usuario de Odoo, de portal (basta para la app y no ve el resto de Odoo) o
interno, cuyo contacto es el contacto del conductor. Su **correo** es el usuario con el que entra
en la app. Al crearlo, Odoo envía la invitación **Activar cuenta**, con la que el conductor crea
su contraseña; si la pierde, se le envía otra (:doc:`/17.0/10_manual_app/10_1_application-access`).

**3. El rol de la app.** El campo **Funciones de la aplicación TMS** del usuario dice qué hace en
la app y, con ello, qué pestañas ve:

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Rol (Roles de la app)
     - Pestañas
   * - Repartidor
     - Panel, Mapas, Chat, Perfil: el conductor
   * - Operario Hub
     - Panel, Escanear, Perfil: quien trabaja en el almacén
   * - Jefe de Tráfico · Destinatario · Cliente
     - Panel y Perfil

Un usuario puede tener varios roles; alguien que reparte y escanea en el hub necesita Repartidor y
Operario Hub. Los cinco roles vienen con el módulo. **Sin rol, la app entra pero no enseña ninguna
pestaña**, y no avisa. Un rol creado a mano en Roles de la app, sin su código interno, se comporta
igual.

**Qué ve en la app.** Su Viaje del día: el despachado o en curso en el que su contacto es el
Conductor (:doc:`/17.0/5_operational-flows/5_4_app-execution`). Un Viaje planificado y sin
despachar no le aparece.

**Tokens de dispositivo.** Cada vez que alguien inicia sesión en la app, Odoo crea un token para
ese teléfono, y la lista **Tokens de dispositivo** enseña de quién es, qué **versión de la app**
tiene y cuándo se usó por última vez. **Revocar** lo anula: la próxima vez que se abra la app en
ese teléfono, pedirá iniciar sesión de nuevo (un teléfono perdido, un conductor que se va). Hoy
las demás llamadas de la app todavía se aceptan sin token, para no dejar fuera a los teléfonos con
versiones antiguas; el parámetro del sistema ``tms_app.enforce_token`` lo vuelve obligatorio
cuando todas estén al día.

.. CAPTURA: 4_1_12 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/4_parametrization/4_1_operational-configuration_12_tokens.png
      :alt: Lista de tokens de dispositivo con su versión de la app

      Tokens de dispositivo: un teléfono por fila, con su versión de la app y su último uso.

**Cuando «la app no funciona».**

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - Síntoma
     - Qué mirar
   * - No entra: «Credenciales inválidas»
     - El correo y la contraseña del usuario, que el usuario esté activo y que haya activado la
       cuenta. Se le puede reenviar la invitación.
   * - Entra, pero no hay pestañas abajo
     - El usuario no tiene rol, o tiene uno sin código interno (creado a mano).
   * - Le falta Escanear, o le sobra
     - Escanear es del rol Operario Hub; el Repartidor no la tiene.
   * - Entra, pero no ve su ruta
     - Que su contacto sea el **Conductor** del Viaje (y no otro contacto con el mismo nombre) y
       que el Viaje esté **despachado**.
   * - Ve cosas de otra versión o le falla algo que a otros no
     - La versión de la app en su token: puede que tenga que actualizarla.
   * - Le sale de golpe la pantalla de inicio de sesión
     - Su token se ha revocado, o se ha desactivado su usuario.

Si nada de eso explica el fallo, el registro de actividad de la API (:doc:`/17.0/7_edi-integrations/7_7_integration-best-practices`)
y los envíos que no llegaron (la app los sube a Odoo con **Limpiar errores**, ver
:doc:`/17.0/10_manual_app/10_8_end-of-day`) dicen qué le respondió Odoo.

