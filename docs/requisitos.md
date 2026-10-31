# Requisitos y riesgos — ALIMENTA-IA

Caso: NutriAlimentos S.A.S. (empresa simulada). Datos 100 % sintéticos.

## Roles del equipo (Sesión 1)

| Rol | Responsable |
|---|---|
| Product Owner | Camilo Ossa |
| Desarrollador | Felipe Gutierrez |
| Responsable QA | Camilo Ossa |
| Responsable de configuración / medición | Felipe Gutierrez |

## Matriz de requisitos

| ID | Tipo | Requisito | Criterio de aceptación | Módulo | Prueba |
|---|---|---|---|---|---|
| RF-01 | Funcional | Registrar lote con código único, fecha, producto y cantidades válidas | Lote duplicado, sin código o sin producto se rechaza | `produccion.py` | `test_validar_lote_normal`, `test_registrar_y_codigo_unico`, `test_codigo_y_producto_obligatorios` |
| RF-02 | Funcional | Tasa de defectos = defectuosas / producidas × 100 | `tasa_defectos(200, 6) == 3.0` | `calidad.py` | `test_tasa_defectos`, `test_tasa_invalida` |
| RF-03 | Funcional | Consultar historial y filtrar por producto | Filtro no distingue mayúsculas; orden por fecha | `produccion.py` | `test_historial_filtra_por_producto` |
| RF-04 | Funcional | Tablero con tasa de defectos y conteo de lotes | Muestra lotes, unidades y tasa global | `calidad.py` | `test_resumen`, `test_tablero_muestra_conteo` |
| RF-05 | Funcional | Marcar lotes atípicos con IA y mostrar advertencia orientativa | Al menos un atípico detectado; advertencia visible | `detector_ia.py` | `test_detecta_al_menos_un_atipico`, `test_advertencia_de_uso_orientativo` |
| RNF-01 | No funcional | No aceptar negativos ni defectuosas > producidas | `ValueError` en esos casos | `produccion.py` | `test_cero_producidas`, `test_negativos`, `test_defectuosas_mayores_que_producidas` |
| RNF-02 | No funcional | Cada cambio integrado con ticket, PR y pruebas | Revisión en GitHub | Proceso | Auditoría (docs/auditoria_release.md) |
| RNF-03 | No funcional | Resultados reproducibles | Semilla fija, `requirements.txt`, CSV versionado | Todos | `test_reproducible_con_semilla` |
| RNF-04 | No funcional | Sin secretos ni datos reales | `.gitignore` y revisión | Repositorio | Auditoría manual |

## Riesgos priorizados (probabilidad 1–5 × impacto 1–5)

| # | Riesgo | P | I | Nivel | Control preventivo |
|---|---|---|---|---|---|
| R1 | Registro de lotes con cantidades inválidas que distorsionen indicadores | 4 | 4 | 16 | Validación en `validar_lote` + pruebas de borde |
| R2 | Cambios integrados sin trazabilidad ni revisión | 3 | 4 | 12 | Ramas, PR obligatorio, convención de commits |
| R3 | La IA genera falsas alertas o pasa por alto atípicos y se usa como decisión de inocuidad | 3 | 5 | 15 | Advertencia de uso orientativo, evaluación con etiquetas y límites documentados |

Los valores de P e I son una estimación del equipo para el ejercicio académico (Pendiente de validar con el grupo).
