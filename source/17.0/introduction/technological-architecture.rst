1.4 Technological Architecture
==============================

This section describes the base platform and the primary integration layers used by Guraify TMS.

1.4.1 Base Platform: Odoo
-------------------------

Guraify TMS is implemented as a suite of custom modules on top of **Odoo Enterprise 17.0**.

Key principles:

- Use Odoo as the system of record for operational, commercial, and financial data.
- Extend standard apps (Sales, Purchase, Inventory, Accounting) where required.
- Keep custom logic isolated in modules following the ``tms*`` naming convention.

1.4.2 Integration with PTV OptiFlow
-----------------------------------

PTV OptiFlow is used for route optimization and planning scenarios where sequencing and constraints
must be computed externally.

Typical pattern:

1. Export planning dataset from Odoo (stops, constraints, vehicles, time windows).
2. Send optimization request to PTV.
3. Import optimized plan (sequence, ETAs, assignments) into Odoo.
4. Persist results into TMS operational entities (Trips / Stops).

1.4.3 External Integrations (API / EDI)
---------------------------------------

The TMS supports external integrations for ingestion, updates, and traceability.

Supported patterns:

- File imports (Excel/CSV)
- API endpoints (JSON)
- Webhooks (inbound event notifications)

Design principles:

- Payload validation and mapping into internal models
- Idempotency to avoid duplicates where applicable
- Traceability event creation for relevant state transitions
- Configuration-driven endpoints (auth, headers, mapping, response processing)