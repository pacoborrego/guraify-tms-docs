Preguntas frecuentes
--------------------

**¿Necesito Odoo para usar Guraify TMS?**
   Sí. Guraify TMS es un conjunto de módulos de Odoo 17 y trabaja sobre sus ventas, compras,
   contabilidad, contactos, flota y proyectos. Si su empresa ya usa Odoo 17, se instala encima.
   Si no, la implantación incluye Odoo.

**¿Qué edición de Odoo, en la nube o en mi servidor, y con qué licencia?**
   Estos aspectos se tratan directamente con Guraify según cada proyecto. Consulte con Guraify
   o con su distribuidor.

**¿Puedo usarlo sin el motor de PTV?**
   Sí. Sin contrato PTV el sistema funciona con planificación manual y el mapa se muestra
   sobre OpenStreetMap. Lo que requiere PTV es la optimización automática de rutas, la
   secuenciación y el cálculo de distancias y horas estimadas de llegada con red viaria
   profesional.

**¿Sirve para varias empresas a la vez?**
   Sí. Odoo es multiempresa y el TMS respeta esa separación: cada compañía ve sus datos, y la
   app del conductor y las comunicaciones llevan la marca de cada una. Un distribuidor puede
   operar varios clientes en una misma instalación.

**¿En qué idiomas está?**
   La interfaz del TMS está en español (España y Argentina) e inglés, sobre un Odoo que se
   puede usar en cualquiera de sus idiomas. La app del conductor está en español e inglés.
   Esta documentación está en español.

**¿Qué necesitan los conductores?**
   Un móvil Android o iPhone con la app instalada, un usuario y la dirección del servidor de
   su empresa. No necesitan usuario de Odoo ni formación en Odoo.

**¿Qué pasa si el conductor pierde la cobertura?**
   La app guarda lo que hace y lo envía al recuperar la red. Lo que no consigue enviar queda
   en una cola visible que el conductor puede reintentar.

**¿Cómo empiezan a entrar las órdenes de mis clientes?**
   Por el canal que ya usen: un fichero Excel o CSV con su formato, una integración por API o
   webhooks desde su sistema, o el formulario de Odoo para lo puntual. Definir el formato de
   un fichero de cliente es una tarea de configuración, no de programación.

**¿Mis clientes pueden ver el estado de sus envíos?**
   Sí. Por integración, recibiendo los estados y la prueba de entrega en su sistema; por
   consulta, preguntando por su referencia; o por el portal, entrando con su usuario.

**¿Cómo se migra desde otro sistema?**
   Los datos maestros (clientes, transportistas, conductores, vehículos, direcciones) y las
   órdenes en curso se cargan con la misma importación de ficheros que se usa en el día a día.
   El entorno de demostración sirve para ensayar la carga antes de hacerla en real.

**¿Se puede probar antes de decidir?**
   Sí. Hay un entorno de demostración con configuración completa y datos inventados que se
   instala en minutos. Consulte con Guraify o con su distribuidor.

**¿Quién da soporte y cómo se actualiza?**
   Se acuerda en cada proyecto. Consulte con Guraify o con su distribuidor.

**¿Dónde está la documentación técnica?**
   En esta misma web: el :doc:`Manual de implantación </17.0/1_introduction/index>` para
   consultores, la :doc:`Guía del integrador </17.0/7_edi-integrations/index>` para técnicos
   de integración y el :doc:`Manual del conductor </17.0/10_manual_app/index>` para los
   conductores.
