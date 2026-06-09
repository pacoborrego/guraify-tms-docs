# Roadmap de migración Drive → Sphinx

Fuente de redacción histórica: Google Doc `2026_02_Manual Tecnico Guraify TMS_V01`.
Destino y fuente de verdad: `source/17.0/`.

Marca cada subsección al portarla. Orden de prioridad acordado: **7 → 6 → 8 → 3.2 ampliado**.

## Leyenda
- [x] migrado y compilando en Sphinx
- [ ] pendiente de portar
- [~] en curso

---

## Capítulo 7 — EDI e Integraciones  → `7_edi-integrations/`  **(PRIORIDAD 1)**

> Estado: **COMPLETADO (2026-06-04)**, con reestructuración por revisión del propietario
> (2026-06-04): canales de entrada = fichero (XLSX/CSV), API REST (JSON), webhooks y alta
> manual (sin "EDI" como canal); orquestación y materialización movidas de 7.1 a 7.3;
> Mapeo y Transformaciones anidados bajo 7.2 como 7.2.1/7.2.2. Prosa descriptiva + modelos,
> sin bloques de código; diagramas mermaid de flujo entrante (7.1) y saliente (7.4).
> Compila con 0 warnings nuevos.
> Nota: el cap. 7 del Google Doc estaba **vacío** (solo títulos); el contenido se redactó
> desde el código, no se portó.
> Discrepancia anotada: los guiones citaban modelos `tms.int.*`; el código define
> `tms_int.*` (guion bajo). Corregido en la prosa conforme a la regla "manda el código".

- [x] 7.1 Estrategia de Integración
- [x] 7.2 Importación de Ficheros
- [x] 7.2.1 Mapeo de Campos
- [x] 7.2.2 Transformaciones Python
- [x] 7.3 Integraciones API
- [x] 7.4 Configuración de Endpoints
- [x] 7.5 Webhooks
- [x] 7.6 Acciones Automáticas
- [x] 7.7 Buenas Prácticas de Integración

> Verificar contra módulo `tms_int` (modelos `tms_int_*`, `tms_edi_*`, `tms_api_log`).
> No duplicar contratos de API REST públicos: esos viven en el gateway (`/api/docs`).

## Capítulo 6 — Aplicación Móvil (técnica)  → `6_mobile-app/`

- [ ] 6.1 Arquitectura funcional
- [ ] 6.2 Perfil de Aplicación
- [ ] 6.3 Flujo del Conductor
- [ ] 6.4 POD Digital
- [ ] 6.5 POD Físico
- [ ] 6.6 Incidencias
- [ ] 6.7 Reembolsos
- [ ] 6.8 Escaneo Masivo y Spark Scan

> Verificar contra módulo `tms_app`. Ojo: no solapar con el cap. 10 (Manual App Conductor),
> que es guía de usuario; el cap. 6 es técnico-funcional.

## Capítulo 8 — Administración y Control Económico  → `8_administration/`

- [ ] 8.1 Modelo de Costes
- [ ] 8.2 División de Ventas
- [ ] 8.3 División de Costes
- [ ] 8.4 Órdenes de Compra Automáticas
- [ ] 8.5 Liquidación Transportistas
- [ ] 8.6 Cuenta Analítica
- [ ] 8.7 Reporting

> Verificar contra `account_move*`, `purchase_order*`, `sale_order*` en `tms`.

## Integración de 3.2 ampliado en `3_functional-architecture/`

El Doc trae al final una versión ampliada del Modelo de Datos Operativo que falta en Sphinx:

- [x] 3.2.1 Órdenes (estados, papel estructural)
- [x] 3.2.2 Viajes (creación, secuenciación/routing, relación con OC, estados en 3 dimensiones)
- [x] 3.2.3 Manifiestos (origen, cierre→estructura operativa, validaciones)
- [x] 3.2.4 API Inbox (funcionamiento, relación con Manifiesto)

> **Hecho (2026-06-04)** como 4 subficheros `3_2_N_slug.rst` con sub-toctree en
> `3_2_operational-data-model.rst`, redactados desde el código. Además se revisó todo el
> cap. 3 (títulos ES numerados, rutas UI, capturas, mermaid del árbol funcional) y se
> ampliaron 3.3 Planificación, 3.4 Tarificación y 3.5 Integración (esta remite al cap. 7).

---

*Generado: 2026-06-03.*
