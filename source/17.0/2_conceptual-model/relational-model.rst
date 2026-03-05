2.6 Conceptual Relational Model
===============================

The Conceptual Relational Model defines how the core entities of Guraify TMS
are structurally linked.

Its objective is to formalize cardinalities and dependencies between:

- Order
- Leg
- Stop
- Trip

This model represents the logical foundation upon which the technical
architecture of the system is built.

2.6.1 Core Entities
-------------------

ORDER
^^^^^

Represents the commercial service commitment.

- Generates revenue
- May contain multiple Legs
- Linked to Customer and Project
- Defines pricing logic

LEG
^^^

Operational unit belonging to an Order.

- Defines origin and destination
- Generates Stops
- Carries goods and time constraints

STOP
^^^^

Physical operational event derived from a Leg.

- Pickup / Delivery / Hub / Technical event
- Minimum planning unit
- Assigned to a Trip

TRIP
^^^^

Operational execution unit.

- Groups multiple Stops
- Assigned to carrier/resource
- Generates cost

2.6.2 Structural Cardinalities
------------------------------

The conceptual relational structure can be represented as:

ORDER (1) ──────── (N) LEG  
LEG (1) ──────── (N) STOP  
STOP (N) ──────── (1) TRIP


ORDER → LEG (1:N)
^^^^^^^^^^^^^^^^^

- One Order may contain multiple Legs.
- Each Leg belongs exclusively to one Order.

This is a strong structural dependency.
If the Order is removed, its Legs lose logical meaning.

LEG → STOP (1:N)
^^^^^^^^^^^^^^^^

- A Leg generates at least two Stops (load and unload).
- Additional Stops may exist in complex logistics scenarios.

This is a strong structural dependency.
Stops cannot exist without their parent Leg.

STOP → TRIP (N:1)
^^^^^^^^^^^^^^^^^^

- A Stop belongs to exactly one Trip during operational execution.
- A Trip groups multiple Stops.

This represents an operational assignment dependency,
not a hierarchical construction dependency.


2.6.3 Indirect ORDER ↔ TRIP Relationship
-----------------------------------------

There is no direct structural relation between Order and Trip.

However, an indirect relationship exists through Stops:

- A Trip may contain Stops originating from multiple Orders.
- An Order may be distributed across multiple Trips.

Conceptually, this results in an indirect N:M relationship
between Order and Trip.

This behavior is especially relevant in:

- Groupage operations
- Last-mile scenarios
- Multi-client planning
- Multi-hub operations

This structural decoupling is intentional and enables
operational flexibility and economic independence.


2.6.4 Structural vs Operational Dependencies
--------------------------------------------

The model defines two types of dependencies:

Strong Structural Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Leg depends on Order.
- Stop depends on Leg.

If the parent entity is deleted, child entities lose logical validity.

These relationships represent hierarchical construction
of the logistics structure.

Weak Operational Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Stop is assigned to Trip.
- Trip does not structurally depend on a specific Order.

This allows:

- Replanning
- Trip reassignment
- Dynamic optimization
- Separation between revenue and cost


2.6.5 Architectural Impact
--------------------------

This relational architecture enables:

1. Operational scalability
2. Event-based advanced planning
3. Grouping of multiple Orders into a single Trip
4. Multidimensional economic allocation
5. Independence between invoicing and execution

The structural separation between:

Commercial Commitment (Order)

and

Operational Execution (Trip)

is only possible due to this relational architecture.

This decoupled model allows Guraify TMS
to scale from simple direct-load operations
to complex multi-hub and large-scale last-mile scenarios.
