2.2 Entity Relationships
========================

2.2.1 Logical Structural Flow
-----------------------------

Customer requests service
↓
Order is created
↓
Legs are generated
↓
Order validation
↓
System generates Stops
↓
Stops grouped into Trips
↓
Trip assigned to resource
↓
Execution
↓
Settlement and Invoicing

2.2.2 Conceptual Separation
---------------------------

+---------+----------------------+--------------------+------------------+
| Entity  | Represents           | Operational Impact | Economic Impact  |
+=========+======================+====================+==================+
| Order   | Revenue              | Billing logic      | Invoicing        |
+---------+----------------------+--------------------+------------------+
| Leg     | Logistics operation  | Traceability       | —                |
+---------+----------------------+--------------------+------------------+
| Stop    | Physical event       | Planning           | —                |
+---------+----------------------+--------------------+------------------+
| Trip    | Executable route     | Execution          | Cost             |
+---------+----------------------+--------------------+------------------+

This separation enables:

- Scalability
- Operational flexibility
- Advanced optimization
- Real financial control

