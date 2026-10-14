A.32 Marca de la compañía
=========================

.. admonition:: Ruta en Odoo
   :class: tip

   Ajustes › Usuarios y compañías › Compañías › la compañía › pestaña Marca

Modelo Odoo: ``res.company`` (módulo ``tms_branding``). La marca de cada compañía, con un solo
punto de lectura (``res.company.get_branding()``) para quien la necesite. La app del conductor lee
los campos del logo y de la paleta de día directamente.

.. list-table::
   :header-rows: 1
   :widths: 28 22 50

   * - Campo
     - Tipo
     - Qué es
   * - Logo de la aplicación
     - Imagen
     - El logo cuadrado que muestra la app del conductor (``app_logo``).
   * - Logo horizontal
     - Imagen
     - El logo ancho para encabezados: lo usan el DeCA y la hoja de ruta que lo acompaña
       (``brand_logo_horizontal``).
   * - Favicon
     - Imagen
     - El icono de pestaña del navegador de la torre de control y de las páginas de seguimiento.
       Reservado (``brand_favicon``).
   * - Paleta de día
     - Nueve colores en hexadecimal
     - Principal, secundario, terciario; de estado (éxito, aviso, peligro); neutros (claro, medio,
       oscuro). Los recibe la app (``color_primary`` … ``color_dark``).
   * - Paleta de noche (opcional)
     - Nueve colores en hexadecimal
     - Los mismos nueve para el modo oscuro. Reservado (``brand_dark_color_*``).
   * - Familia tipográfica
     - Texto
     - Lista de fuentes CSS, por ejemplo ``Inter, system-ui, sans-serif``; vacío, la de cada
       aplicación. Reservado (``brand_font_family``).
   * - Escala tipográfica (JSON)
     - Texto
     - Tamaños de los títulos y del texto, como objeto JSON con las claves h1 a h6 y body; el
       sistema rechaza un JSON mal formado. Reservado (``brand_font_scale_json``).
   * - Dominio de Connect
     - Texto
     - El nombre de host desde el que se sirve la torre de control de la compañía (por ejemplo,
       connect.e-transport.es) y el de los enlaces de seguimiento (``brand_connect_domain``).
   * - Nombre del remitente de mensajería
     - Texto
     - El remitente de los avisos al Destinatario por correo, SMS y WhatsApp; vacío, el nombre de
       la compañía (``brand_sender_name``).

«Reservado»: el campo se guarda y se sirve, pero ninguna pantalla lo usa todavía.

Cómo se usa y qué decide el cliente: :doc:`/17.0/4_parametrization/4_1_operational-configuration`.
