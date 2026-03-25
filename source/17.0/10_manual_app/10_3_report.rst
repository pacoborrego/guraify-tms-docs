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