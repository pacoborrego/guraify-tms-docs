2.1 Structural Logic of the System
==================================

Guraify TMS is designed around a fundamental principle:

**Structurally separate the commercial service request from its real logistics execution.**

The entire transport operation is structured around four primary entities:

ORDER → LEG → STOP → TRIP

Each entity fulfills a specific and differentiated role within the operational and financial workflow.

2.1.1 The Order
---------------

Order Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Order represents the digital version of the customer’s commercial request.
Conceptually, it answers the question:

"What service must be provided and later invoiced?"

Order Main Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Represents the operational contract with the customer
- Contains administrative and commercial information
- Determines invoicing logic
- Links project, pricing model, and tariff rules

Key Characteristics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- May contain one or multiple legs
- Linked to a customer and project
- Generates sales lines
- Activates pricing rules
- Inherits configuration from the project

Order Structural Principle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An Order is not a route.  
It is a service commitment.

2.1.2 The Leg
-------------

Leg Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Leg is the operational unit within an Order.

If the Order answers "what", the Leg answers:

"From where to where is the service performed?"

Each Leg contains:

- Load location
- Unload location
- Goods information
- Applicable pricing rules
- Time constraints

Leg Main Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decomposes complex Orders into independent logistics operations.

Conceptual Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Door-to-door service → 1 Order / 1 Leg
- Hub transfer → 1 Order / 2 Legs
- Mass last-mile → 1 Order / multiple Legs
- Rescheduling → additional Leg added
- Inter-hub transfers → additional Leg

Leg Structural Principle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Leg is the unit that generates Stops.

2.1.3 The Stop
--------------

Stop Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Stop represents a physical event in real operations.

It may be:

- Pickup
- Delivery
- Hub entry
- Hub exit
- Technical stop
- Route change

Automatic Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an Order is validated:

- The system analyzes the Legs
- Automatically generates required Stops
- Links them to their respective Leg

In bulk imports, the system groups Legs automatically when:

- Same customer
- Same location
- Compatible time window

Stop Main Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Stop is the minimum planning unit.

Route optimizers do not operate on Orders — they operate on Stops.

2.1.4 The Trip
--------------

Trip Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Trip represents the digital assignment of work to a carrier.

It answers:

"What set of stops will a resource execute on a real route?"

Trip Main Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Groups Stops
- Represents an executable route
- Generates purchase order to carrier
- Triggers economic settlement

Trip Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Trips can be created:

- Manually (filtering and grouping stops)
- Automatically via route optimization (PTV)

Trip Structural Principle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Order represents revenue.  
The Trip represents cost.
