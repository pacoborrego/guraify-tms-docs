7.2.2 Transformaciones Python
=============================

Las transformaciones Python aportan la flexibilidad necesaria para adaptar datos que no
encajan mediante una correspondencia directa de campos. Se aplican tanto en el mapeo de
entrada como en la construcción de los patrones de salida.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Funciones preestablecidas

7.2.2.1 Contexto de ejecución
-----------------------------

El código de transformación se ejecuta en un entorno controlado que expone un conjunto
acotado de variables y librerías: ``value`` (el valor del campo en curso), ``row`` (el
registro actual), ``rows`` (el conjunto completo de datos, útil en funciones de
agregación) y las librerías estándar ``json``, ``re`` y ``datetime``. El resultado de la
transformación se devuelve asignándolo a la variable ``result``.

7.2.2.2 Funciones preestablecidas
---------------------------------

El catálogo de funciones preestablecidas (``tms_int.preset.function``) reúne las
transformaciones más habituales para no tener que reescribir código en cada
integración. Al seleccionar una función en un mapeo (campo ``preset_function_id``), su
código de ejemplo se copia automáticamente al campo ``python_code`` del mapeo, donde
puede ajustarse a la necesidad concreta. Las funciones que requieren parámetros
(índices de columna, diccionarios de correspondencia, valores por defecto) los declaran
al inicio del código mediante marcadores que el integrador sustituye.

.. figure:: /_static/img/7_edi-integrations/7_2_2_python-transformations_01_lista-funciones.png
   :alt: Catálogo de funciones preestablecidas

   Catálogo de funciones preestablecidas.

Las funciones cargadas de serie son las siguientes:

7.2.2.2.1 ``Extract First Hour`` · primera hora
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extrae la **primera** hora en formato ``HH:MM`` que aparezca en el valor. Si no se
encuentra ninguna, devuelve ``00:00``. Útil cuando el campo de origen mezcla texto y
horarios (p. ej. de ``"Inicio a las 08:30 y fin a las 17:45"`` extrae ``08:30``).

7.2.2.2.2 ``Extract Second Hour`` · segunda hora
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Variante de la anterior que extrae la **segunda** hora ``HH:MM`` del valor; si no
existe, devuelve ``00:00``. Típicamente se usa en pareja con *Extract First Hour* para
separar el inicio y el fin de una franja horaria contenida en un mismo campo.

7.2.2.2.3 ``Extract Substring`` · subcadena
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extrae una subcadena del valor a partir de una posición de inicio y una longitud, que
se indican como parámetros en el código. Si los parámetros no son válidos, devuelve
cadena vacía (p. ej. de ``"Hello, World!"`` con inicio 7 y longitud 5 extrae
``World``).

7.2.2.2.4 ``Format Date to DD/MM/YYYY`` · fecha a DD/MM/AAAA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convierte el valor a una cadena con formato ``DD/MM/YYYY`` cuando representa una fecha
válida (objeto fecha o texto que contenga una fecha). Si el valor no es interpretable
como fecha, lo devuelve sin cambios.

7.2.2.2.5 ``Extract and Match`` · extraer y emparejar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combina extracción y correspondencia: toma una subcadena del valor (inicio y longitud
parametrizables) y la busca como clave en un diccionario de correspondencias definido
en el código, devolviendo el valor asociado. Útil para traducir códigos embebidos en
referencias (p. ej. de ``"ABCDEFGH"`` extraer ``CDE`` y resolverlo contra el
diccionario).

7.2.2.2.6 ``Match Value`` · emparejar valor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Busca el valor completo como clave en un diccionario de correspondencias y devuelve el
valor asociado, o nulo si no hay coincidencia. Es la opción directa para mapear
catálogos cerrados (códigos de servicio, tipos de bulto, provincias…) entre el sistema
externo y Odoo.

7.2.2.2.7 ``Custom Code`` · código propio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plantilla en blanco para escribir lógica a medida cuando ninguna función del catálogo
encaja. Da acceso a todo el contexto de ejecución (``value``, ``row``, ``rows`` y las
librerías disponibles). Ver :ref:`funciones-personalizadas`.

7.2.2.2.8 ``Sum Parcel`` · suma de bultos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Función de **agregación**: suma una columna numérica (peso, volumen, bultos…) de todas
las filas del dataset (``rows``) que comparten el identificador de orden y de
bulto de la fila actual. Los índices de las columnas (valor a sumar, identificador de
orden e identificador de bulto) se indican como parámetros. Es la forma de
totalizar líneas de detalle en ficheros donde cada bulto llega en una fila.

7.2.2.2.9 ``Count Parcel`` · recuento de bultos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complementaria de la anterior: **cuenta** cuántas filas del dataset comparten el
identificador de orden y de bulto de la fila actual. Sirve para calcular el número
de bultos de una orden a partir de sus líneas de detalle.

7.2.2.2.10 ``Convert to Uppercase`` · a mayúsculas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convierte el valor a mayúsculas. Útil para normalizar matrículas, códigos o referencias
antes de compararlos o almacenarlos.

7.2.2.2.11 ``Convert to Lowercase`` · a minúsculas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convierte el valor a minúsculas, típicamente para normalizar correos electrónicos o
identificadores insensibles a mayúsculas.

7.2.2.2.12 ``Trim Whitespace`` · quitar espacios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Elimina los espacios en blanco al inicio y al final del valor. Recomendable de forma
sistemática en ficheros generados a mano o exportados de hojas de cálculo.

7.2.2.2.13 ``Extract Digits`` · solo dígitos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extrae todos los dígitos numéricos del valor y los concatena (p. ej. de ``"Order1234"``
obtiene ``1234``). Útil para limpiar referencias que mezclan prefijos de texto con
numeración.

7.2.2.2.14 ``Default Value`` · valor por defecto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Devuelve un valor por defecto (parametrizable en el código) cuando el valor original
está vacío o no existe. Es la manera estándar de garantizar que un campo obligatorio
del modelo siempre reciba contenido.

7.2.2.2.15 ``Calculate Percentage`` · porcentaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Calcula un porcentaje del valor numérico recibido, con el porcentaje parametrizable en
el código (p. ej. el 10 % de 200 es 20). Útil para recargos, descuentos o repartos
proporcionales durante la ingesta.

.. _funciones-personalizadas:

7.2.2.3 Creación de funciones personalizadas
--------------------------------------------

Cuando el catálogo no cubre una necesidad, hay dos vías:

**Ajustar el código en el propio mapeo.** Al elegir una función preestablecida, su
código se copia al campo ``python_code`` del mapeo; ese código es editable, por lo que
la vía más rápida es partir de la función más parecida (o de *Custom Code*) y
adaptarla. El cambio afecta solo a ese mapeo.

**Añadir una función al catálogo.** Si la transformación va a reutilizarse en varias
integraciones, conviene crear un registro nuevo en ``tms_int.preset.function`` con su
nombre, su descripción (qué hace, qué parámetros usa y un ejemplo de entrada/salida) y
su código de ejemplo. A partir de ese momento aparece en el desplegable de funciones de
cualquier mapeo, como las de serie.

.. CAPTURA: 7_2_2_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_2_python-transformations_02_funcion-detalle.png
      :alt: Detalle de una función preestablecida

      Detalle de una función preestablecida (descripción y código de ejemplo).

En ambos casos el código debe respetar el contrato del contexto de ejecución: leer el
dato de entrada de ``value`` (y, si procede, de ``row`` o ``rows``), usar únicamente
las librerías disponibles (``json``, ``re``, ``datetime``) y depositar el resultado en
la variable ``result``; por ejemplo, ``result = str(value).upper()``. Los parámetros
configurables se declaran como variables al inicio del código, siguiendo la convención
de los marcadores ``<INTEGER>`` o similares que usan las funciones de serie.

7.2.2.4 Prueba de funciones
---------------------------

El asistente de prueba (``tms_int.preset.function.test.wizard``) permite ejecutar una
función con un valor de ejemplo y comprobar su salida antes de incorporarla a un mapeo
de producción. Una vez incorporada, el mapeo tiene su propia prueba en el propio mapeo
(ver :doc:`7_2_1_field-mapping`). Es muy recomendable validar así cualquier función nueva
o modificada antes de aplicarla a datos reales.

7.2.2.5 Seguridad
-----------------

La ejecución del código está restringida: el entorno no expone ``__import__`` ni acceso
a módulos arbitrarios, de modo que las transformaciones quedan limitadas a las
variables y librerías del contexto. Esta restricción evita que un mapeo mal diseñado o
malicioso pueda comprometer el sistema.
