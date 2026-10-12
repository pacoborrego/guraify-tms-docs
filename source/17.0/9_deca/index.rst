9 DeCA: el documento de control del transporte
==============================================

Este capítulo describe el módulo **DeCA** del TMS, que emite el **documento electrónico de
control administrativo** que la normativa española exige en el transporte público de mercancías
por carretera. Es un módulo opcional: lo instala quien opera en España y lo configura una vez por
compañía y, cuando hace falta, por Proyecto.

La tesis es la de siempre: no inventar nada que el TMS ya tenga. El DeCA no es un documento
nuevo que haya que teclear; es la **carta de porte que el Tramo ya representa**, con los datos
que el Viaje aporta (quién transporta, con qué vehículo, qué día) y los que el Tramo lleva (de
dónde a dónde, qué y cuánto pesa), congelados en un PDF con un código QR que un inspector puede
descargar en carretera sin credenciales. El TMS decide qué Tramos lo necesitan, lo emite al
despachar el Viaje, lo entrega a quien tenga que llevarlo y conserva cada versión el tiempo que
la norma manda.

.. mermaid::

   flowchart LR
       L["Tramo<br/>¿obligado o exento?"] -->|"obligado"| B["Borrador<br/>uno por Tramo o por Viaje"]
       T["Despachar el Viaje"] --> B
       B -->|"Emitir"| D["DeCA emitido<br/>PDF con QR · URL pública"]
       D --> E["Envío<br/>correo · webhook"]
       D --> M["Hoja de ruta<br/>con el QR"]
       D -->|"Revisar"| D
       D -->|"Anular + nuevo a partir de este"| B

.. toctree::
   :maxdepth: 1

   9_1_what-it-is
   9_2_configuration
   9_3_obligation
   9_4_lifecycle
   9_5_outputs
   9_6_operations
