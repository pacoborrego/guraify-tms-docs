7.2.2 Transformaciones Python
=============================

Las transformaciones Python aportan la flexibilidad necesaria para adaptar datos que no
encajan mediante una correspondencia directa de campos. Se aplican tanto en el mapeo de
entrada como en la construcción de los patrones de salida.

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Configuración › EDI › Funciones preestablecidas

Contexto de ejecución
---------------------

El código de transformación se ejecuta en un entorno controlado que expone un conjunto
acotado de variables y librerías: ``value`` (el valor del campo en curso), ``row`` (el
registro actual), ``rows`` (el conjunto completo de datos, útil en funciones de
agregación) y las librerías estándar ``json``, ``re`` y ``datetime``. El resultado de la
transformación se devuelve asignándolo a la variable ``result``.

Funciones preestablecidas
-------------------------

El catálogo de funciones preestablecidas (``tms_int.preset.function``) reúne las
transformaciones más habituales para no tener que reescribir código en cada
integración. Al seleccionar una función en un mapeo (campo ``preset_function_id``), su
código de ejemplo se copia automáticamente al campo ``python_code`` del mapeo, donde
puede ajustarse a la necesidad concreta. Las funciones que requieren parámetros
(índices de columna, diccionarios de correspondencia, valores por defecto) los declaran
al inicio del código mediante marcadores que el consultor sustituye.

.. CAPTURA: 7_2_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/7_edi-integrations/7_2_2_python-transformations_01_lista-funciones.png
      :alt: Catálogo de funciones preestablecidas

      Catálogo de funciones preestablecidas.

Las funciones cargadas por defecto (fichero ``tms_int/data/tms_int_preset_function.xml``)
son las siguientes:

Extract First Hour
~~~~~~~~~~~~~~~~~~

Extrae la **primera** hora en formato ``HH:MM`` que aparezca en el valor. Si no se
encuentra ninguna, devuelve ``00:00``. Útil cuando el campo de origen mezcla texto y
horarios (p. ej. de ``"Inicio a las 08:30 y fin a las 17:45"`` extrae ``08:30``).

Extract Second Hour
~~~~~~~~~~~~~~~~~~~

Variante de la anterior que extrae la **segunda** hora ``HH:MM`` del valor; si no
existe, devuelve ``00:00``. Típicamente se usa en pareja con *Extract First Hour* para
separar el inicio y el fin de una franja horaria contenida en un mismo campo.

Extract Substring
~~~~~~~~~~~~~~~~~

Extrae una subcadena del valor a partir de una posición de inicio y una longitud, que
se indican como parámetros en el código. Si los parámetros no son válidos, devuelve
cadena vacía (p. ej. de ``"Hello, World!"`` con inicio 7 y longitud 5 extrae
``World``).

Format Date to DD/MM/YYYY
~~~~~~~~~~~~~~~~~~~~~~~~~

Convierte el valor a una cadena con formato ``DD/MM/YYYY`` cuando representa una fecha
válida (objeto fecha o texto que contenga una fecha). Si el valor no es interpretable
como fecha, lo devuelve sin cambios.

Extract and Match
~~~~~~~~~~~~~~~~~

Combina extracción y correspondencia: toma una subcadena del valor (inicio y longitud
parametrizables) y la busca como clave en un diccionario de correspondencias definido
en el código, devolviendo el valor asociado. Útil para traducir códigos embebidos en
referencias (p. ej. de ``"ABCDEFGH"`` extraer ``CDE`` y resolverlo contra el
diccionario).

Match Value
~~~~~~~~~~~

Busca el valor completo como clave en un diccionario de correspondencias y devuelve el
valor asociado, o nulo si no hay coincidencia. Es la opción directa para mapear
catálogos cerrados (códigos de servicio, tipos de bulto, provincias…) entre el sistema
externo y Odoo.

Custom Code
~~~~~~~~~~~

Plantilla en blanco para escribir lógica a medida cuando ninguna función del catálogo
encaja. Da acceso a todo el contexto de ejecución (``value``, ``row``, ``rows`` y las
librerías disponibles). Ver :ref:`funciones-personalizadas`.

Sum Parcel
~~~~~~~~~~

Función de **agregación**: suma una columna numérica (peso, volumen, bultos…) de todas
las filas del dataset (``rows``) que comparten el identificador de expedición y de
bulto de la fila actual. Los índices de las columnas (valor a sumar, identificador de
expedición e identificador de bulto) se indican como parámetros. Es la forma de
totalizar líneas de detalle en ficheros donde cada bulto llega en una fila.

Count Parcel
~~~~~~~~~~~~

Complementaria de la anterior: **cuenta** cuántas filas del dataset comparten el
identificador de expedición y de bulto de la fila actual. Sirve para calcular el número
de bultos de una expedición a partir de sus líneas de detalle.

Convert to Uppercase
~~~~~~~~~~~~~~~~~~~~

Convierte el valor a mayúsculas. Útil para normalizar matrículas, códigos o referencias
antes de compararlos o almacenarlos.

Convert to Lowercase
~~~~~~~~~~~~~~~~~~~~

Convierte el valor a minúsculas, típicamente para normalizar correos electrónicos o
identificadores insensibles a mayúsculas.

Trim Whitespace
~~~~~~~~~~~~~~~

Elimina los espacios en blanco al inicio y al final del valor. Recomendable de forma
sistemática en ficheros generados a mano o exportados de hojas de cálculo.

Extract Digits
~~~~~~~~~~~~~~

Extrae todos los dígitos numéricos del valor y los concatena (p. ej. de ``"Order1234"``
obtiene ``1234``). Útil para limpiar referencias que mezclan prefijos de texto con
numeración.

Default Value
~~~~~~~~~~~~~

Devuelve un valor por defecto (parametrizable en el código) cuando el valor original
está vacío o no existe. Es la manera estándar de garantizar que un campo obligatorio
del modelo siempre reciba contenido.

Calculate Percentage
~~~~~~~~~~~~~~~~~~~~

Calcula un porcentaje del valor numérico recibido, con el porcentaje parametrizable en
el código (p. ej. el 10 % de 200 es 20). Útil para recargos, descuentos o repartos
proporcionales durante la ingesta.

.. _funciones-personalizadas:

Creación de funciones personalizadas
------------------------------------

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
la variable ``result`` — por ejemplo, ``result = str(value).upper()``. Los parámetros
configurables se declaran como variables al inicio del código, siguiendo la convención
de los marcadores ``<INTEGER>`` o similares que usan las funciones de serie.

Prueba de funciones
-------------------

El asistente de prueba (``tms_int.preset.function.test.wizard``) permite ejecutar una
función con un valor de ejemplo y comprobar su salida antes de incorporarla a un mapeo
de producción. Para los mapeos, existe además la prueba inline descrita en
:doc:`7_2_1_field-mapping`. Es muy recomendable validar así cualquier función nueva o
modificada antes de aplicarla a datos reales.

Seguridad
---------

La ejecución del código está restringida: el entorno no expone ``__import__`` ni acceso
a módulos arbitrarios, de modo que las transformaciones quedan limitadas a las
variables y librerías del contexto. Esta restricción evita que un mapeo mal diseñado o
malicioso pueda comprometer el sistema.
