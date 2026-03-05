2.4 Integrated Economic Model
=============================

One of the defining characteristics of Guraify TMS is the native structural integration
between operational execution and financial impact.

Unlike traditional TMS architectures where logistics and accounting are loosely connected
through reconciliation processes, Guraify TMS embeds financial logic directly into
the operational model.

This integration is not an afterthought — it is a foundational design principle.

2.4.1 Revenue Generation (Asset)
--------------------------------

Revenue originates at the **Order** level.

The Order represents the commercial commitment with the customer,
and therefore constitutes the revenue-generating entity.

Revenue characteristics:

- Generated automatically through Pricing Rules or predefined tariffs.
- May apply flat pricing or calculated pricing logic.
- Can be segmented per Leg if operational structure requires it.
- Fully linked to the operational context that generated it.

Revenue is not an aggregated external figure.
It is a structural consequence of the logistics model.

Each revenue line is traceable to:

- Customer
- Project
- Service type
- Operational unit (Order / Leg)

2.4.2 Cost Generation (Liability)
---------------------------------

Cost originates at the **Trip** level.

The Trip represents the real execution assigned to a carrier or resource,
and therefore constitutes the cost-generating entity.

Cost characteristics:

- Generated through carrier settlement logic.
- May be fixed, variable, distance-based, or hybrid.
- Can be divided across Stops depending on configured allocation model.

The Trip acts as the cost container because it represents
a real-world route executed by a physical resource.

2.4.3 Multidimensional Prorated Allocation
------------------------------------------

This is one of the system’s strongest differentiators.

Guraify TMS does not restrict financial analysis to Order or Trip level.

Both revenue and cost can be prorated across all structural dimensions:

- Order
- Leg
- Stop
- Trip

This enables:

- Revenue generated at Order level to be proportionally distributed to its Legs.
- Cost generated at Trip level to be proportionally allocated to its Stops.
- Margin calculation at micro-operational granularity.

Allocation Criteria
^^^^^^^^^^^^^^^^^^^

Proration can be configured using one or multiple measurable variables:

- Weight
- Volume
- Package count
- Pallets
- Linear meters
- Distance (Km)
- Composite formulas (e.g., Km + Weight)
- Equal distribution

This flexibility allows the economic model to adapt to:

- Full truckload operations
- Groupage
- Last-mile
- Multihub scenarios
- Mixed transport structures

2.4.4 Margin Analysis Across Dimensions
---------------------------------------

Thanks to structural decoupling and multidimensional allocation,
margin can be computed across multiple axes:

- Order
- Leg
- Stop
- Trip
- Project
- Customer
- Planning route
- Geographic zone
- Service type
- Any configured analytic dimension

This enables advanced strategic analysis, such as:

- Which geographic zones are truly profitable?
- Which service types generate sustainable margins?
- Which customers generate volume but low profitability?
- Which Stops degrade route efficiency?
- Which carriers optimize cost per kilometer or per package?

Strategic Outcome
^^^^^^^^^^^^^^^^^

The combination of:

Structured Operations + Automated Pricing + Prorated Allocation

Transforms the system from a traditional TMS into
an advanced operational profitability intelligence platform.

