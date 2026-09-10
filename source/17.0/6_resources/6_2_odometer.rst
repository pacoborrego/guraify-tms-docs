6.2 El odómetro único
---------------------

.. admonition:: Ruta en Odoo
   :class: tip

   Pestaña **Odometer (TMS)** de la ficha del vehículo (TMS › Maestros › Equipos › Vehículos) y
   Gestión de Recursos › Configuración › Odometer Anomalies.

.. CAPTURA: 6_2_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_2_odometer_01_pestana-vehiculo.png
      :alt: Pestaña Odometer (TMS) de un vehículo

      La pestaña de odómetro del vehículo: lectura actual, origen, antigüedad y km por día.

El kilometraje de un vehículo llega de muchos sitios: lo anota el taller al cerrar una orden,
viene en el albarán de cada carga de combustible, lo captura el conductor en la app, lo envía
la telemática. Si cada fuente escribiera por su cuenta, habría series distintas y nadie sabría
cuál manda. El TMS resuelve eso con **una sola serie por vehículo** y **un solo punto de
entrada**: toda lectura, venga de donde venga, pasa por el mismo registro, la misma detección
de anomalías y la misma validación.

La serie es el odómetro nativo de la Flota de Odoo (``fleet.vehicle.odometer``), extendido con
el origen de cada lectura, su estado de validación y su anomalía. Un vehículo puede medirse en
kilómetros o, si es una máquina, en **horas de motor**; el tipo de contador se elige en el
vehículo y cambia las reglas que se aplican.

6.2.1 Qué lleva cada lectura
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cada lectura registra el vehículo, la fecha, el valor y tres datos que el TMS añade. El
**origen**: Manual, Mantenimiento (el cierre de una orden de trabajo), Importación de
combustible, Combustible manual, App del conductor o Telemetría, con el registro concreto del
que salió cuando lo hay. La **referencia externa**: el identificador de la lectura en el sistema
de origen (el albarán de la gasolinera, el identificador del proveedor de telemetría), que
hace que volver a importar la misma lectura no la duplique. Y el **estado de validación**:
Válida, Borrador (pendiente de revisar) o Rechazada. Sólo las lecturas válidas cuentan para el
kilometraje actual, el ritmo de km por día y las estimaciones.

6.2.2 La detección de anomalías
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Al registrar una lectura, el sistema la compara con la serie válida del vehículo y aplica
cuatro reglas, en este orden; la primera que se cumple decide:

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Anomalía
     - Cuándo se marca
   * - Fecha futura
     - La fecha de la lectura es posterior a hoy.
   * - Duplicada
     - Ya existe una lectura válida con la misma fecha y el mismo valor.
   * - Retroceso
     - El valor es menor que una lectura válida anterior o de la misma fecha. El cuentakilómetros
       no va hacia atrás.
   * - Salto inverosímil
     - El incremento desde la última lectura válida, repartido por los días transcurridos, supera
       el máximo de kilómetros por día de la compañía (1.500 por defecto). No se aplica a los
       contadores de horas de motor.

Una lectura con anomalía **no se rechaza ni se pierde**: entra en estado Borrador, con la nota
de qué regla saltó, la lectura válida anterior con la que se comparó y la diferencia entre
ambas. Mientras esté en borrador no cuenta. Ninguna lectura escapa al control: también las que
Odoo crea por su cuenta desde los servicios de flota pasan por la detección y nacen con su
origen.

6.2.3 La pantalla de anomalías
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. CAPTURA: 6_2_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/6_resources/6_2_odometer_02_anomalias.png
      :alt: Pantalla de anomalías de odómetro

      Las lecturas pendientes de revisar, agrupadas por vehículo, con la anterior válida y la
      diferencia.

La pantalla **Odometer Anomalies** lista las lecturas en borrador agrupadas por vehículo, con
el tipo de anomalía, el origen, la lectura anterior válida y la diferencia. El administrador
decide lectura a lectura: **Validar** la incorpora a la serie y recalcula el resumen del
vehículo y las reglas de preventivo que dependen de él; **Rechazar** la aparta para siempre,
conservándola como historial. La pantalla filtra por anomalía y por origen, y la ficha del
vehículo tiene un botón inteligente con el número de anomalías pendientes que abre la misma
lista filtrada.

6.2.4 El resumen en el vehículo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La ficha del vehículo muestra, en la pestaña de odómetro, la **lectura actual**: el último
valor válido, su fecha, su origen y cuántos días tiene. Muestra también el **ritmo de km por
día**, calculado sobre la serie válida, el tipo de contador y la referencia del dispositivo de
telemetría si lo hay. Estos datos los actualiza el propio registro de lecturas, no un cálculo
permanente, así que están al día en el momento en que entra o se valida una lectura.

Con la serie válida el sistema puede además **estimar el kilometraje en una fecha** en la que
no hubo lectura, por interpolación entre las dos más cercanas o por extrapolación con el ritmo
de km por día. La estimación viene con una confianza: **alta** si coincide exactamente con una
lectura, **media** si se ha interpolado o extrapolado. Es lo que usa el motor de preventivo
cuando una orden de trabajo antigua no trae el kilometraje real (ver
:doc:`6_4_preventive-rules`). Un vehículo sin ninguna lectura válida no tiene kilometraje, no
cero: el sistema lo trata como dato ausente en todas partes.

Campos de la lectura y del resumen en :doc:`/17.0/annexes/A_19_odometro`.
