Documentación de Guraify TMS
============================

Guraify TMS es el sistema de gestión del transporte construido dentro de Odoo 17. Esta
documentación tiene cuatro recorridos, uno por tipo de lector. Empiece por el suyo.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: 🚚 Conocer Guraify TMS
        :link: 0_product-overview/index
        :link-type: doc

        Qué es, qué hace y para quién. Para clientes y distribuidores, sin tecnicismos.

    .. grid-item-card:: 🛠️ Manual de implantación
        :link: 1_introduction/index
        :link-type: doc

        Cómo funciona por dentro y cómo se configura. Para consultores y clientes avanzados.

    .. grid-item-card:: 🔌 Guía del integrador
        :link: 7_edi-integrations/index
        :link-type: doc

        Cómo entran y salen los datos: ficheros, API y webhooks. Para técnicos de integración.

    .. grid-item-card:: 📱 Manual del conductor
        :link: 10_manual_app/index
        :link-type: doc

        La app del móvil, pantalla a pantalla. Para entregar a los conductores.

Y para todos, el :doc:`glosario <glossary>`: cada término del producto, con su definición.

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Conocer Guraify TMS

   0_product-overview/index
   glossary

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Manual de implantación

   1_introduction/index
   2_conceptual-model/index
   3_functional-architecture/index
   4_parametrization/index
   5_operational-flows/index
   annexes/index

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Guía del integrador

   7_edi-integrations/index
