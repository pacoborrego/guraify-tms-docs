Reporte
--------

Datos de la parada
~~~~~~~~~~~~~~~~~~~

Cuando pulses sobre una parada, accederás a la pantalla de detalle.

En esta pantalla encontrarás toda la información necesaria para trabajar la parada, tanto si es una carga como una entrega.

.. image:: /_static/images/Parada_Report_Inicio.PNG
   :width: 300px
   :align: center



**Estructura de la pantalla**


La pantalla está organizada en dos niveles:

- Encabezado con la tarjeta de la parada seleccionada

- Lista de los pedidos de cliente vinculados a esta parada

- Pie con los botones de acción.


**Información general de la parada**


Es exactamente lo mismo que las tarjetas de parada en la vista Viaje.

.. seealso::

   Ver sección: :ref:`section-paradas-info`


**Lista de Órdenes**


A continuación de la información de la parada, verás una lista de las órdenes vinculadas a la parada. Cada tarjeta que ves en la pantalla representa a una orden.

Una misma parada puede tener:

- Una sola orden


- Varias órdenes agrupadas del mismo destinatario


- Varias órdenes agrupadas de diferentes destinatarios

.. image:: /_static/images/Parada_Report_Botones_Exito.PNG
   :width: 300px
   :align: center


**Información de cada orden**


En cada tarjeta podrás ver:

.. image:: /_static/images/Orden_Card.png
   :width: 300px
   :align: center



1. En la Fila Superior:

   a. Referencia de la orden  
   b. Nombre del receptor o destinatario  
   c. Cliente  

2. A continuación:

   a. Teléfono de contacto (si está disponible)  
   b. Dirección completa  

3. Detalle de la mercancía:

   a. Cantidad de bultos  
   b. Tipo de bulto  
   c. Descripción  
   d. Peso (kg)  
   e. Volumen  


Información adicional

En algunos casos puede aparecer una zona resaltada dentro de la tarjeta.

Aquí se muestran:

- Observaciones

- Instrucciones especiales

- Información importante de la orden

- Si hay o no reembolso a cobrar antes de entregar

.. important::

   Lee siempre las observaciones antes de trabajar la parada.  
   Pueden afectar a cómo debes realizar la carga o la entrega.



**Pie de acciones**

En la parte inferior de la pantalla encontrarás el panel de acciones.

.. image:: /_static/images/Parada_Footer.png
   :width: 300px
   :align: center


Estructura del footer

El footer está compuesto por tres elementos:

- Acceso a navegación (izquierda)

- Botón central (centro)

- Menú de acciones (derecha)


**Menú de acciones**

En la parte derecha encontrarás un icono de tres puntos.

Al pulsarlo se abrirá un menú con acciones disponibles.

.. image:: /_static/images/Parada_Acciones.png
   :width: 300px
   :align: center


Opciones disponibles:

- Reiniciar


----

**Acción: Reiniciar**

.. image:: /_static/images/parada_accion.png
   :width: 300px
   :align: center


.. warning::

   Utiliza esta opción solo si necesitas repetir el proceso de la parada.


**Flujo operativo de una parada**

1. Inicio → El conductor inicia el desplazamiento

2. He llegado  → El conductor confirma llegada a la ubicación

3. Reporte → El conductor reporta el resultado de la parada 

.. note::
   Los botones cambian según el estado de la parada.


Reportar una parada
~~~~~~~~~~~~~~~~~~~~

**Flujo estándar (sin incidencias)**

A continuación se describe el flujo habitual cuando una parada se realiza correctamente, sin incidencias.

.. _section-2:


**1. Inicio del desplazamiento**


Una vez seleccionada la parada, el conductor debe pulsar el botón Inicio.
Esta acción indica al sistema que el conductor está en camino hacia el destino.

· Además, puede activar procesos automáticos como:
· Notificación al destinatario (preaviso de entrega)
· Actualización del estado en tiempo real

.. image:: /_static/images/Parada_Report_Inicio.PNG
   :width: 300px
   :align: center


**2. Llegada a la parada**


Al llegar al destino, el conductor debe pulsar el botón He llegado.

Esto registra la llegada a la ubicación y permite continuar con el proceso de la parada.



.. image:: /_static/images/Parada_Report_He_Llegado.PNG
   :width: 300px
   :align: center



**3. Revisión de la parada**


Antes de iniciar la operación, el conductor debe revisar la información disponible:

- Número de bultos

- Dirección

- Nombre del destinatario

- Observaciones e instrucciones

- POD Físico (albarán) o POD Digital

.. important::

   Lee siempre las observaciones antes de realizar la operación.



.. _section-3:

**4. Documentación**

Si la parada requiere POD físico, preparar albarán.

- El conductor debe preparar el albarán correspondiente antes de realizar la entrega

**5. Localización de los bultos**


El conductor debe localizar los bultos dentro del vehículo.

Para facilitar esta tarea, puede utilizar la funcionalidad de escaneo disponible en la app, haciendo clic encima del icono que se encuentra en el Pie a la izquierda de los botones de Éxito.

Al activarla:

- Se abre la cámara del dispositivo

- Al enfocar las etiquetas:

- Verde → el bulto pertenece a la parada

- Rojo → el bulto no pertenece a la parada

- Se muestra en pantalla el número de bultos pendientes de localizar

Esto permite asegurar que se entregan únicamente los bultos correctos.

.. list-table::

   * - .. image:: /_static/images/ScanMatrix_Step_1.png
         :width: 200px
     - →
     - .. image:: /_static/images/ScanMatrix_Step_2.png
         :width: 200px
     - →
     - .. image:: /_static/images/ScanMatrix_Step_3.png
         :width: 200px

**6. Confirmación de bultos**


Una vez localizados los bultos:

- El conductor los transporta hasta el destinatario

- Realiza la entrega

En ese momento, debe pulsar el botón OK (color verde).

Al pulsar OK, la aplicación cambia automáticamente a la pantalla de verificación de bultos.

.. image:: /_static/images/Bultos_Lista_Scan_Off.png
   :width: 300px
   :align: center




**Información de cada bulto**

Cada tarjeta contiene la siguiente información:

.. image:: /_static/images/Bulto_Card.png
   :width: 300px
   :align: center



1. Primera línea:

   a. Iconos que indican el tipo de bulto

   b. Referencia del bulto (visible en la etiqueta física)

   c. Nombre o logotipo del cliente

   c. Nombre o logotipo del cliente

2. Segunda línea:

   a. Estado  
   b. Descripción  
   c. Tipo  

3. Tercera línea:

   a. Nombre del destinatario

   b. Código postal y localidad
   b. Código postal y localidad

---

.. important::
    Esta información ayuda a identificar físicamente los bultos (tipo de caja, etiquetas, logotipos, etc.).

   


**Validación de los bultos**

El objetivo de esta pantalla es confirmar que todos los bultos han sido correctamente entregados.

Existen dos formas de validación:

1. Validación manual

   a. El conductor puede marcar manualmente cada bulto

   b. Esto indica que el bulto ha sido entregado correctamente

2. Validación mediante escaneo

   a. El conductor puede utilizar la funcionalidad de escaneo

   b. Para ello, debe pulsar el icono de escáner

   c. Se activará la cámara del dispositivo

   d. Al escanear la etiqueta:

      i. El sistema marcará automáticamente el bulto correspondiente

.. image:: /_static/images/Bultos_Lista_Scan_On.png
   :width: 300px
   :align: center


**Indicador de progreso**

En la parte inferior de la pantalla se muestra un contador:
	•	Número de bultos confirmados
	•	Número total de bultos de la parada

.. image:: /_static/images/Bultos_Lista_Footer.png
   :width: 300px
   :align: center



Esto permite al conductor saber en todo momento cuántos bultos faltan por validar.

Esta pantalla permanecerá activa hasta que el número de bultos confirmados sea igual al total

Cuando se hayan confirmado todos los bultos:
El contador desaparecerá
Se habilitará el botón Siguiente

Este botón permite continuar con el proceso de confirmación de la parada.


.. important::

   Debes confirmar todos los bultos antes de continuar.


**7. Confirmación de la entrega (POD)**


El método de confirmación depende del tipo de POD:

**POD físico**

.. list-table::
   :align: center

   * - .. image:: /_static/images/Parada_Report_POD_Phisical_Pre_Scan.PNG
         :width: 300px
     - →
     - .. image:: /_static/images/Parada_Report_POD_Phisical_Post_Scan.PNG
         :width: 300px


**POD digital**

- El conductor solicita los datos del receptor:
  
  - Nombre  
  - Documento identificativo (DNI / NIE / equivalente)

- El destinatario firma directamente en la pantalla del dispositivo

.. list-table::

   * - .. image:: /_static/images/parada_report_pre_sign_digital.png
         :width: 300px

     - →

     - .. image:: /_static/images/Parada_Report_POD_Digital_Post_Sign.PNG
         :width: 300px


**8. Finalización**

Una vez completada la firma:

- La parada queda reportada

- Desaparece de la lista de pendientes

- El sistema registra la operación como completada

.. note::

   Este es el flujo estándar de trabajo.  
   En los siguientes apartados se describen los casos especiales (reserva, incidencias, etc.).


Reportar un reembolso
~~~~~~~~~~~~~~~~~~~~~~

En determinadas paradas, antes de finalizar la entrega, es necesario gestionar un reembolso. Esto implica que el conductor debe cobrar un importe al destinatario como parte del proceso operativo.

**Cómo identificar un reembolso**

Si una parada tiene reembolso, el sistema mostrará una indicación visual dentro de la orden.

.. image:: /_static/images/Reembolso_Step_1.png
   :width: 300px
   :align: center


Ejemplo:

“Reembolso - CONTADO - 100 €”

Esto indica que el conductor debe cobrar dicho importe antes de completar la entrega.


.. important::

   No completes la entrega sin haber realizado previamente el cobro.


**Cuándo se gestiona el reembolso**

El reembolso se gestiona automáticamente durante el flujo de reporte de la parada.

Al pulsar el botón OK para confirmar la entrega, y antes de acceder a la captura del POD, la aplicación mostrará la pantalla específica de gestión de reembolso.

.. image:: /_static/images/Reembolso_Step_2.png
   :width: 300px
   :align: center


**Qué debes hacer**

Si el cobro se realiza correctamente, el conductor debe seleccionar la opción correspondiente:

- Cobrado

Existen otras opciones como:

- Cobrado en parte  
- No cobrado  

Estas opciones están destinadas a la gestión de incidencias y se detallarán en secciones posteriores.


**Continuación del proceso**

Una vez confirmado el reembolso:

- El flujo operativo continúa con normalidad  
- Se accede al proceso de captura del POD  

Dependiendo del caso, el POD podrá ser:

- Firma digital en el dispositivo  
- Escaneo de albarán físico  


.. tip::

   Realiza siempre el cobro antes de confirmar la acción en la aplicación.



Reportar incidencias
~~~~~~~~~~~~~~~~~~~~

**Reportar incidencias durante la carga**

Durante el proceso de carga, el conductor debe verificar el estado físico de los bultos antes de incorporarlos al vehículo.

En caso de detectar cualquier anomalía, el sistema permite registrar una incidencia en ese mismo momento, garantizando la trazabilidad desde origen.


**Tipos de incidencia en carga**

Existen dos situaciones principales:

- El bulto se puede entregar
- El bulto no se puede entregar 

Para registrar estas incidencia nos iremos encima del bulto en la aplicacion 

.. image:: /_static/images/Reporte_carga_1.png
   :width: 300px
   :align: center



Y clicaremos en el boton que nos aparece abajo que dice : **Reportar Problema**

.. image:: /_static/images/Reporte_carga_2.png
   :width: 300px
   :align: center



Al clicar , observaremos que nos aparecen dos opcciones dependiendo de en que estado se encuentre el bulto reportaremos si se entrega o si no se entrega

.. image:: /_static/images/Reporte_carga_3.png
   :width: 300px
   :align: center


**Bulto transportable con incidencia (Reserva)**

Se utiliza cuando el bulto puede continuar en el proceso, pero presenta algún tipo de anomalía.

Ejemplos habituales:

- Embalaje dañado  
- Golpes visibles  
- Deterioro externo  

En estos casos, el conductor debe:

- Reportar la incidencia durante la carga  
- Seleccionar el bulto afectado  
- Registrar la incidencia  
- Adjuntar una imagen como evidencia  





.. important::

   Es obligatorio adjuntar una imagen cuando el bulto presenta daños visibles.  
   Esto permite evitar incidencias y reclamaciones posteriores.


**Bulto no transportable (KO)**

Se utiliza cuando el bulto no puede ser cargado y no debe continuar en el transporte.

Ejemplos habituales:

- Daño grave  
- Producto incorrecto  
- Problemas que impiden su manipulación  

En estos casos, el conductor debe:

- Reportar la incidencia durante la carga  
- Seleccionar el bulto afectado  
- Indicar el motivo  
- Confirmar que el bulto no se carga  




.. warning::

   Un bulto marcado como KO no debe cargarse en el vehículo bajo ningún concepto.


**Importante**

El registro de incidencias en carga permite:

- Mantener la trazabilidad del bulto  
- Evitar errores en la entrega  
- Garantizar una correcta gestión posterior  


.. note::

   Las incidencias deben registrarse en el momento en que se detectan.


**Reportar incidencias durante la entrega**

Durante el proceso de entrega, pueden producirse situaciones en las que la operación no se realiza en condiciones estándar. En estos casos, el sistema permite registrar incidencias directamente desde la pantalla de validación de bultos.

Al escanear un bulto, la aplicación mostrará las opciones de reporte disponibles:

- Entrega OK (sin incidencias)  
- Entrega con incidencia (Reserva)  
- No entregado (KO)  


**Entrega con incidencia (Reserva)**

Se utiliza cuando el bulto ha sido entregado, pero no en las condiciones inicialmente previstas.

Ejemplos habituales:

- Entrega a un vecino  
- Entrega en portería o recepción  
- Mercancía dejada en la puerta  
- Entrega en un punto distinto al destinatario original  

En estos casos, el conductor debe:

- Seleccionar el bulto escaneado  
- Elegir la opción de entrega con incidencia (Reserva)  
- Seleccionar el tipo de incidencia dentro de la app  
- Adjuntar una imagen como evidencia (portería, ubicación, número de puerta, etc.)  


.. image:: /_static/images/reporte_entrega.png
   :width: 300px
   :align: center


.. important::

   Es obligatorio adjuntar una imagen que evidencie el lugar de entrega.  
   Esto garantiza la trazabilidad y evita reclamaciones posteriores.


**Entrega no realizada (KO)**

Se utiliza cuando la entrega no ha podido completarse.

Opciones habituales disponibles en la app:

- Destinatario ausente  
- Entrega cancelada  
- Mercancía no localizada en el vehículo  
- Otros motivos operativos  

En estos casos, el conductor debe:

- Seleccionar el bulto correspondiente  
- Elegir la opción KO  
- Indicar el motivo de la incidencia  
- Confirmar el reporte  


.. image:: /_static/images/reporte_entrega_4.png
   :width: 300px
   :align: center


.. warning::

   Un bulto reportado como KO implica que la entrega no se ha realizado y deberá gestionarse posteriormente.


**Importante**

El correcto registro de incidencias en entrega permite:

- Mantener la trazabilidad completa de la operación  
- Informar en tiempo real al sistema  
- Evitar errores en la gestión posterior  


.. note::

   Selecciona siempre el tipo de incidencia que mejor represente la situación real de la entrega.

   **Reportar incidencias de reembolso**

Durante el proceso de entrega, puede ocurrir que el reembolso no se complete correctamente. En estos casos, el sistema permite registrar una incidencia asociada al cobro.

Cuando se accede a la pantalla de reembolso, la aplicación mostrará dos opciones principales:

- No pagado  
- Pagado a medias  


**Reembolso no pagado (KO)**

Se utiliza cuando el destinatario no realiza ningún pago.

En este caso, el conductor debe:

- Seleccionar la opción **No pagado**  
- Indicar el motivo correspondiente  

Ejemplos habituales:

- El cliente rechaza el pago  
- El cliente no dispone de dinero  
- El cliente no acepta el importe  


.. warning::

   Un reembolso marcado como no pagado implica que la entrega no ha sido cobrada y deberá gestionarse posteriormente.


**Reembolso pagado parcialmente (Reserva)**

Se utiliza cuando el destinatario realiza un pago parcial del importe.

En este caso, el conductor debe:

- Seleccionar la opción **Pagado a medias**  
- Indicar la cantidad abonada  
- Especificar el motivo por el cual no se ha realizado el pago completo  

.. list-table::

   * - .. image:: /_static/images/IMG_1021.png
         :width: 200px

     - →

     - .. image:: /_static/images/IMG_1020.png
         :width: 200px


Esto permite al sistema reflejar la situación real del cobro y facilitar su gestión posterior.


.. important::

   Es fundamental registrar correctamente el importe recibido para evitar descuadres en la liquidación.


**Importante**

El registro correcto de incidencias de reembolso permite:

- Mantener la trazabilidad económica de la operación  
- Evitar errores en la facturación  
- Facilitar la gestión administrativa posterior  


.. note::

   Selecciona siempre la opción que refleje con mayor precisión la situación real del cobro.