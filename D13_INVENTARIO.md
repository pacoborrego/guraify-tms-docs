# D13 — Inventario para limpiar el historial (13/10/2026)

Fichero de trabajo, no se sube. Copia de seguridad: `~/Backups/tms-docs-mirror-261013.git` (clon espejo, 107 MB).

Historial: 260 rutas de imagen han existido alguna vez; 98 siguen en el árbol. El `.git` pesa 107 MB.

## 1. Rutas que ya no están en el árbol y se borran del historial entero

**a) `source/_static/images/`** — 56 imágenes, las capturas antiguas a pantalla completa con datos reales, incluidas las 8 de `_originals_pre_anonimization/`.

**b) Capturas rechazadas o renombradas en `source/_static/img/`** — 10:

- `source/_static/img/4_parametrization/4_5_project-configuration_04_app.png`
- `source/_static/img/5_operational-flows/5_11_kpi-indicators_01_kpi-parada.png`
- `source/_static/img/5_operational-flows/5_11_kpi-indicators_02_kpi-orden.png`
- `source/_static/img/5_operational-flows/5_1_order-creation_02_validar.png`
- `source/_static/img/5_operational-flows/5_7_invoicing_01_factura.png`
- `source/_static/img/7_edi-integrations/7_2_1_field-mapping_02_selector-campo.png`
- `source/_static/img/7_edi-integrations/7_2_2_python-transformations_01_lista-funciones .png`
- `source/_static/img/7_edi-integrations/7_2_file-import_02_validacion .png`
- `source/_static/img/7_edi-integrations/7_4_endpoint-configuration_01_endpoint .png`
- `source/_static/img/7_edi-integrations/_7_3_01-apis_integration.png`

**c) `venv/`** — un entorno de Python que se subió entre marzo y mayo de 2026 (8.328 ficheros, 98 de ellas imágenes de temas). No son datos personales, pero es la mayor parte del peso del repositorio; se aprovecha para quitarlo.

Se conserva `source/_static/design/configuracion_operativa_inicial.png` (un diagrama de mayo, sin datos).

## 2. Versiones antiguas de imágenes que siguen en el árbol — 25

Son las primeras versiones de capturas que después se rehicieron (lote de María del 15/09, primeras capturas activadas en D1). Se borran solo esas versiones; la actual de cada fichero se queda.

- `source/_static/img/5_operational-flows/5_1_order-creation_01_orden-nueva.png` (blob `04320fbe3e`)
- `source/_static/img/4_parametrization/4_1_operational-configuration_03_tipos-servicio-form.png` (blob `09a829c87c`)
- `source/_static/img/4_parametrization/4_2_logistic-configuration_04_tipos-bulto.png` (blob `10c832d0e8`)
- `source/_static/img/4_parametrization/4_5_project-configuration_01_proyecto.png` (blob `1ff898f46d`)
- `source/_static/img/4_parametrization/4_4_economic-configuration_04_linea-tarifa.png` (blob `27c083505d`)
- `source/_static/img/4_parametrization/4_3_planning-configuration_02_areas-geograficas.png` (blob `2e36c1699c`)
- `source/_static/img/4_parametrization/4_4_economic-configuration_01_zonas-tarifarias.png` (blob `3145ef7d63`)
- `source/_static/img/0_product-overview/0_4_what-it-includes_01_tablero.png` (blob `477aecf2f8`)
- `source/_static/img/5_operational-flows/5_3_resource-assignment_01_recursos.png` (blob `4dff084068`)
- `source/_static/img/4_parametrization/4_3_planning-configuration_01_planes-transporte.png` (blob `4eb2fa362a`)
- `source/_static/img/4_parametrization/4_5_project-configuration_02_kanban-proyectos.png` (blob `5b2228bc0b`)
- `source/_static/img/4_parametrization/4_2_logistic-configuration_03_reglas-tarifa.png` (blob `5cefc0024b`)
- `source/_static/img/5_operational-flows/5_5_trip-closing_01_cierre.png` (blob `67d159ba62`)
- `source/_static/img/4_parametrization/4_5_project-configuration_03_otros-parametros.png` (blob `698682620b`)
- `source/_static/img/4_parametrization/4_3_planning-configuration_06_horas-conduccion.png` (blob `6d44856393`)
- `source/_static/img/3_functional-architecture/3_2_3_manifests_02_botones-inteligentes.png` (blob `7a0267acce`)
- `source/_static/img/4_parametrization/4_4_economic-configuration_02_tarifa.png` (blob `9245fbd848`)
- `source/_static/img/5_operational-flows/5_2_trip-generation_01_generacion-viajes.png` (blob `a3367e0868`)
- `source/_static/img/4_parametrization/4_3_planning-configuration_05_franjas-horarias.png` (blob `b5dfea7a18`)
- `source/_static/img/4_parametrization/4_4_economic-configuration_03_tarifa-base.png` (blob `be58bc6531`)
- `source/_static/img/4_parametrization/4_3_planning-configuration_04_planning.png` (blob `c41910afdf`)
- `source/_static/img/4_parametrization/4_2_logistic-configuration_02_vehiculos.png` (blob `d67d949145`)
- `source/_static/img/4_parametrization/4_3_planning-configuration_03_tiempos-servicio.png` (blob `f70920d6bd`)
- `source/_static/img/7_edi-integrations/7_2_1_field-mapping_01_lista-mapeos.png` (blob `fde28f887c`)
- `source/_static/img/5_operational-flows/5_4_app-execution_01_paradas-estado-app.png` (blob `ff3f2bc6f3`)

## 3. Lo que bloquea: 15 capturas de la app PUBLICADAS hoy con datos reales

Están en el árbol actual y en guraify.com/docs. Nombres de destinatarios, teléfonos móviles, direcciones, el nombre del conductor y su matrícula, y un nombre con DNI en la firma. Limpiar el historial sin quitarlas antes no sirve: seguirían publicadas.

- `source/_static/img/10_manual_app/10_2_route_01_dashboard.png`
- `source/_static/img/10_manual_app/10_2_route_02_dashboard-header.png`
- `source/_static/img/10_manual_app/10_2_route_03_parada-card.png`
- `source/_static/img/10_manual_app/10_3_report_01_parada-report-inicio.png`
- `source/_static/img/10_manual_app/10_3_report_02_parada-report-botones-exito.png`
- `source/_static/img/10_manual_app/10_3_report_03_orden-card.png`
- `source/_static/img/10_manual_app/10_3_report_05_parada-acciones.png`
- `source/_static/img/10_manual_app/10_3_report_06_parada-accion.png`
- `source/_static/img/10_manual_app/10_3_report_07_parada-report-he-llegado.png`
- `source/_static/img/10_manual_app/10_3_report_08_bultos-lista-scan-off.png`
- `source/_static/img/10_manual_app/10_3_report_09_bulto-card.png`
- `source/_static/img/10_manual_app/10_3_report_10_bultos-lista-scan-on.png`
- `source/_static/img/10_manual_app/10_3_report_12_reembolso-step-1.png`
- `source/_static/img/10_manual_app/10_3_report_19_scanmatrix-step-1.png`
- `source/_static/img/10_manual_app/10_3_report_25_parada-report-pod-digital-post-sign.png`

Las otras 18 de la app (invitación, entrada, botones, motivos, pantallas de foto y firma vacías) no llevan datos de terceros.


## 4. Decisión de Paco (13/10/2026)

- **Lista aprobada entera** (1, 2 y `venv/`).
- **Las 15 de la app las difumina María primero** y D13 espera a que estén en el repositorio. Cuando
  lleguen, sus versiones actuales (las de abajo) pasan a ser «versiones antiguas» y se borran del
  historial con las demás; se quedan las difuminadas.

Versiones de las 15 que se borrarán cuando María entregue las nuevas:
- `source/_static/img/10_manual_app/10_2_route_01_dashboard.png` (blob `c340e0edcf`)
- `source/_static/img/10_manual_app/10_2_route_02_dashboard-header.png` (blob `8b3fe89266`)
- `source/_static/img/10_manual_app/10_2_route_03_parada-card.png` (blob `326da319bd`)
- `source/_static/img/10_manual_app/10_3_report_01_parada-report-inicio.png` (blob `24e58b377e`)
- `source/_static/img/10_manual_app/10_3_report_02_parada-report-botones-exito.png` (blob `0610c69b12`)
- `source/_static/img/10_manual_app/10_3_report_03_orden-card.png` (blob `c5808fd7cb`)
- `source/_static/img/10_manual_app/10_3_report_05_parada-acciones.png` (blob `4dcb6b7fef`)
- `source/_static/img/10_manual_app/10_3_report_06_parada-accion.png` (blob `bd93729f23`)
- `source/_static/img/10_manual_app/10_3_report_07_parada-report-he-llegado.png` (blob `074b53618c`)
- `source/_static/img/10_manual_app/10_3_report_08_bultos-lista-scan-off.png` (blob `a501c9f8ee`)
- `source/_static/img/10_manual_app/10_3_report_09_bulto-card.png` (blob `42e5bcdf39`)
- `source/_static/img/10_manual_app/10_3_report_10_bultos-lista-scan-on.png` (blob `2c097b17b5`)
- `source/_static/img/10_manual_app/10_3_report_12_reembolso-step-1.png` (blob `cdd987580a`)
- `source/_static/img/10_manual_app/10_3_report_19_scanmatrix-step-1.png` (blob `85a5a754b7`)
- `source/_static/img/10_manual_app/10_3_report_25_parada-report-pod-digital-post-sign.png` (blob `634adb7ffc`)

## 5. Cómo se ejecutará (cuando estén las 15)

1. Comprobar que las 15 tienen versión nueva en `main` (blob distinto del de arriba) y que no queda
   nada sin commitear ni sin subir; nueva copia espejo.
2. `git filter-repo --invert-paths --path source/_static/images/ --path venv/ --path <las 10 de 1b>`
   y, en la misma pasada, `--strip-blobs-with-ids <lista>` con las 25 versiones antiguas y las 15 de
   arriba (lista en el scratchpad de la sesión: `d13/blob_ids.txt`).
3. Comprobar: ninguna de esas rutas ni blobs en `git log --all`; build con `-W` limpio; tamaño del `.git`.
4. Con el OK de Paco: `git push --force --all` y `--tags` a `origin`. María borra su clon y vuelve a
   clonar; en epartner se vuelve a clonar `/opt/tms-docs/guraify-tms-docs` y se lanza `deploy.sh`.

## 6. Lista completa de blobs para `--strip-blobs-with-ids` (40)

```
04320fbe3e949753e16dc07d82d6fefba6727528
09a829c87c811339d19adbd82f024c77f1e8f840
10c832d0e827db41146366c9629a9b7291a9ac26
1ff898f46d2f81808acaf5d0db590ed4e350432c
27c083505d5bac98de3b1d9c41879ccc01ad6f82
2e36c1699c03494ba1ee8648f0db138f02f6c0ba
3145ef7d6345b7810076af1de499add714b46a80
477aecf2f8c2f43ac6504ea60afd15bf9a6efaf1
4dff0840682ec7f519d18d08050e0788dcd62ca8
4eb2fa362ab0cf6cd626bccbaf1984d8040eba4a
5b2228bc0bdda28e10e939ac546f4a85e6cebb01
5cefc0024b8e0f55ab676d888170e2d63c0e1b2e
67d159ba62c359b6c6abc155cbd5b60021f457fd
698682620b83f33b8e2a6fcaaa8f6018464e1f23
6d44856393d28f0538131947a066bd6ffe0ec92f
7a0267acce3299755c6a7a570e80495154331c9f
9245fbd848ece425c4074093e061c06475ff6e7e
a3367e08683a05b23eec3f901ded48b33833b4be
b5dfea7a1858dd8c7abd3e344d68d9202a169fcb
be58bc653154b46c226a1367b4fbd263c752a715
c41910afdfba8d51903b69ecb1f6b110787e0c5b
d67d949145fd9ae858f5f337e0b2fedf5ead1ef1
f70920d6bd3511819d2e6f34fd82b3af6edf1855
fde28f887c26a27a9ae38fdf9f9b83b5bd5e6f1c
ff3f2bc6f3130c2f09944a37bc05df6b24c85273
c340e0edcfd81bc3123d6c114976d95d7c8a2b7d
8b3fe8926600e6f813a396e9977cdd70c4394d9d
326da319bd8fc87ccb3426cdd3e36f43ed7dbc44
24e58b377ee34484b211ef09947a4bab569cae1b
0610c69b126a4408d371084437a77f9250506772
c5808fd7cbc697afde5a2ef135049ba69a2996ed
4dcb6b7fef2d8bb9c9b57a7342c7160b4245f62f
bd93729f2393b0dbbbc6108111d2fa91d4bdb566
074b53618c7cd0e9e160deb611beb9f8faafaa94
a501c9f8eef9b43cd38f52f690f965140add4635
42e5bcdf396d6723b2731cc4fbc7d9cbf6f709e2
2c097b17b58550fdde69a90782066169232907f2
cdd987580ae511f2372a7228dd6e6e64ad1483e0
85a5a754b742561d41384a9f058e0bd34dd9ea0a
634adb7ffc70153ba252b3c81c0638bc8404461d
```
