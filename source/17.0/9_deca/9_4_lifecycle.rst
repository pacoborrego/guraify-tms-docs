9.4 El documento y su ciclo de vida
-----------------------------------

.. admonition:: Ruta en Odoo
   :class: tip

   TMS › Operaciones › DeCA › **Documentos** · botón **Generar DeCA** del Tramo · botón **Emitir
   DeCA del viaje** del Viaje · **Despachar** el Viaje

.. CAPTURA: 9_4_01 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/9_deca/9_4_lifecycle_01_documentos.png
      :alt: Lista de documentos DeCA con sus estados

      Los documentos DeCA: referencia, transportista, fecha, estado y URL activa.

9.4.1 Cómo nace
~~~~~~~~~~~~~~~

Un DeCA nace de tres maneras, y las tres pasan por el mismo motor:

- **Al despachar el Viaje** (:doc:`/17.0/5_operational-flows/5_4_app-execution`), si la ficha
  del Proyecto dispara al despachar: por cada Tramo obligado de las Paradas que la ficha señala
  se crea el borrador (uno por Tramo o uno por Viaje, según la agrupación) y, con la emisión
  automática, se **emite por cola** en los segundos siguientes. El despacho **nunca se queda
  esperando ni se bloquea** por el DeCA: si algo falla, el Viaje sale despachado igual, con una
  nota en su historial y una actividad para el Responsable DeCA. Si la tarea programada de
  emisión está apagada, se emite en línea.
- **Desde el Viaje**, con **Emitir DeCA del viaje**: lo mismo, a mano y emitiendo en el acto.
  Pulsarlo dos veces no duplica nada.
- **Desde el Tramo**, con **Generar DeCA**: un borrador para ese Tramo, evaluando la obligación
  en ese momento.

El borrador toma una **foto** de los datos a)–h) al crearse y la **reconstruye desde sus Tramos al
emitir**: lo que se teclee a mano en la cabecera o en líneas generadas no sobrevive (la matrícula
se pone en el Viaje, no en el documento), y la emisión se niega si un Tramo ya no va en su Viaje.
Nunca hay dos DeCA vigentes para un Tramo.

9.4.2 Emitir
~~~~~~~~~~~~

**Emitir** es una sola operación: comprueba que no falta nada, genera el PDF con su QR, lo guarda
y sella el documento. Lo que puede faltar lo dice todo junto: un remolque sin matrícula, un
cargador sin nombre o dirección, una URL pública que no es HTTPS y, sobre todo, el **peso**. Un
Tramo con peso cero bloquea la emisión nombrándolo; un Responsable DeCA puede escribir en el
borrador un **peso declarado** para ese Tramo, aparte del medido y con traza, y entonces vale el
declarado. Si el servicio ya ha empezado y la compañía bloquea la emisión tardía, un Usuario
recibe el error y un Responsable un asistente que pide el motivo. Si algo falla, el borrador se
queda como estaba.

9.4.3 Los estados
~~~~~~~~~~~~~~~~~

.. mermaid::

   flowchart LR
       B["Borrador"] -->|"Emitir"| I["Emitido"]
       I -->|"Revisar"| M["Modificado"]
       M -->|"Revisar"| M
       I & M -->|"Anular"| C["Anulado"]
       I & M -->|"URL desactivada<br/>(fin del servicio + N días)"| X["Caducado"]
       C -. "Emitir nuevo<br/>desde este" .-> B
       I & M -. "Emitir nuevo<br/>desde este<br/>(anula el original)" .-> B

Un documento que no es borrador está **congelado**: ni la cabecera, ni las líneas, ni el estado
se pueden tocar fuera de las tres acciones que siguen, y el PDF emitido no se vuelve a generar.
El estado nunca vuelve a Borrador; solo los borradores se pueden borrar, y un DeCA no se puede
duplicar.

**Revisar** (botón *Revisar*). Para corregir lo que la norma permite modificar: matrícula,
remolque, fecha, observaciones, y en cada línea el destino y el peso. El asistente pide el motivo;
el PDF vigente pasa al **historial** como revisión, con su huella, y el nuevo se genera con la
**misma URL** y el mismo QR: el inspector siempre descarga la versión vigente y el historial
conserva las anteriores. El documento queda *Modificado*. Cambiar el cargador o el transportista
no es una revisión: el asistente remite a anular y emitir uno nuevo.

**Anular** (botón *Anular DeCA*, Responsable DeCA, motivo obligatorio). El documento queda
*Anulado* y se conserva, su URL responde «documento anulado» y sus Tramos quedan libres para
generar otro. Se puede anular también con el servicio empezado, con una confirmación: es el camino
que la FAQ del Ministerio admite cuando cambia el transportista o el vehículo.

**Emitir nuevo desde este**. Crea un borrador con los mismos Tramos y datos frescos,
enlazado al original. Desde un documento emitido o modificado, emitir el nuevo anula el original;
desde uno anulado, simplemente lo sustituye. Es el camino cuando cambia el cargador, el
transportista o el vehículo.

**Caducado** lo pone el sistema cuando desactiva la URL del QR, pasados los días que la compañía
fija tras el fin del servicio; el documento y su PDF siguen consultables en Odoo hasta cumplir la
retención, y después también: el control de retención cuenta, nunca borra.

9.4.4 El DeCA sigue a su Viaje
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un DeCA emitido no cambia porque cambie el Viaje: queda **desactualizado** (y así lo dice su
ficha y la lista Tramos sin DeCA) si un Tramo sale del Viaje o el Viaje cambia de transportista
o de vehículo; lo que toca es anular y emitir el nuevo. Si se **revierte el despacho**
(:doc:`/17.0/3_functional-architecture/3_2_2_trips`), los borradores que estaban en cola salen de
ella y los documentos vigentes **no se anulan solos**: si el Viaje vuelve a salir con el mismo
camión y transportista siguen valiendo, y el nuevo despacho no genera otros; el Responsable DeCA
recibe una actividad para revisarlos.

Cuando el Viaje lo hace un vehículo que no está en la flota, el Viaje lleva la **matrícula
externa**, la del remolque y los **equipos externos** de manipulación: el DeCA los usa en f), g) y
en la paquetería como si fueran de la flota.

.. CAPTURA: 9_4_02 — descomentar el figure cuando esté la imagen
   .. figure:: /_static/img/9_deca/9_4_lifecycle_02_documento-emitido.png
      :alt: Ficha de un DeCA emitido

      Un DeCA emitido: cargador, transportista, vehículo, líneas, URL pública y los botones
      Revisar, Anular y Emitir nuevo desde este.
