7.10 Indicadores y tableros para el integrador
----------------------------------------------

Los indicadores y los tableros se describen, para quien los usa, en
:doc:`/17.0/8_economic-administration/8_8_control-reporting`. Aquí está lo que necesita quien los
amplía: cómo se añade un cálculo de indicador y cómo se versiona un tablero para que viaje entre
bases.

7.10.1 Registrar un cálculo de indicador
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un indicador (``tms.kpi``) se configura desde la interfaz, pero su **cálculo** es código: una
entrada en el registro de cálculos y un método. No hay campo de código editable desde la pantalla,
a propósito: un cálculo es una consulta a la base y se revisa como cualquier otro código.

Cada módulo amplía el registro heredando ``tms.kpi`` y su método ``_kpi_registry()``:

.. code-block:: python

   class TmsKpiNotify(models.Model):
       _inherit = 'tms.kpi'

       @api.model
       def _kpi_registry(self):
           registry = super()._kpi_registry()
           registry['notify_sent'] = {
               'label': 'Avisos enviados',   # lo que se elige en «Cálculo»
               'method': '_kpi_notify_sent',  # el método que devuelve el número
               'format': 'number',            # number, percent, currency, duration
               # 'action': '_kpi_action_…',   # opcional: la lista que abre la tarjeta
           }
           return registry

       @api.model
       def _kpi_notify_sent(self, scope):
           Message = scope.env['tms.notify.message']
           return Message.search_count([...])

El método recibe un **alcance** (``scope``) con la audiencia (``internal``, ``client`` o
``carrier``), la empresa del cliente o del transportista y las fechas, y consulta con el ``env``
del usuario, de modo que las reglas de acceso (7.9.3) ya acotan lo que cuenta. ``scope.stop_domain()``
da el dominio de las Paradas del alcance. Las duraciones se devuelven en horas. Una vez
desplegado, el cálculo aparece en el selector de la ficha y el indicador se crea y se ajusta
(título, formato, objetivo, audiencias) sin más código. Así se han añadido los de mantenimiento
(:doc:`/17.0/6_resources/6_7_kpis`) y los de los avisos (:doc:`/17.0/11_notifications/11_5_following`).

7.10.2 Versionar un tablero
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un tablero creado desde la interfaz vive solo en la base donde se creó y lleva dentro cosas de esa
base: identificadores de registros en las fórmulas, filtros por empresa, menús por número. Para
que un tablero viaje con el producto (``tms_dashboard``), se guarda como fichero en el repositorio
y se sanea antes. El procedimiento completo está en el README del módulo; en resumen:

#. **Extraer** el tablero de la base donde se editó, como JSON
   (``/web/content/spreadsheet.dashboard/<id>/spreadsheet_snapshot?download=true``).
#. **Sanear** con ``tools/sanitize_dashboard.py``: quita el contexto de la sesión, reescribe las
   condiciones atadas a datos de una empresa, traduce los menús a identificadores externos, pone
   los rótulos en inglés para traducirlos y convierte las referencias a registros en posicionales.
   El informe lista bajo **REVISAR** lo que no puede arreglar solo.
#. **Construirlo para que viaje**: tablas dinámicas o referencias posicionales («el primer
   cliente»), nunca una fórmula con el identificador de un registro, que en otra base apunta a
   nada.
#. **Traducir**: los ficheros se llaman ``*_dashboard.json`` para que Odoo extraiga sus términos;
   el texto de celda va con ``_t()``.
#. **Publicar**: el fichero en ``data/`` y su registro en ``data/dashboards.xml``; se actualiza el
   módulo.
#. **Adoptar** en una base donde el tablero ya existía creado a mano: ``tools/adopt_dashboards.py``
   le pone el identificador del módulo antes de instalarlo, para no duplicarlo (guarda una copia
   del contenido anterior).

Un grupo de tableros propio del cliente sale en TMS › Operaciones › Tableros si se marca como
**Tablero TMS** en su ficha (:ref:`17.0/8_economic-administration/8_8_control-reporting:8.8.4 Tableros`).
