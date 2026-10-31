# Auditoría, regresión y decisión de liberación — ALIMENTA-IA

## 1. Trazabilidad RF → ticket → rama → commit → PR → prueba → resultado

| Requisito | Ticket | Rama | Commit | PR | Casos de prueba | Resultado |
|---|---|---|---|---|---|---|
| RF-01, RF-03, RNF-01 | GH-01 | `feature/GH-01-registro-lotes` | `feat(GH-01): registro y validacion de lotes` | Pendiente de confirmar (URL) | `test_produccion.py` (7 pruebas) | Aprobadas |
| RF-02, RF-04 | GH-02 | `feature/GH-02-indicadores` | `feat(GH-02): indicadores y tablero de calidad` | Pendiente de confirmar (URL) | `test_calidad.py` (4 pruebas) | Aprobadas |
| RF-05, RNF-03 | GH-03 | `feature/GH-03-detector-ia` | `feat(GH-03): detector IA, datos sinteticos y evaluacion` | Pendiente de confirmar (URL) | `test_detector_ia.py` (5 pruebas) | Aprobadas |
| RNF-02, RNF-04 | GH-04 | `docs/GH-04-auditoria-release` | `docs(GH-04): auditoria y notas de version` | Pendiente de confirmar (URL) | Revisión manual (checklist) | Ver sección 3 |
| RNF-03 (D-02) | GH-05 | `test/GH-05-pruebas-scripts` | `test(GH-05): pruebas de scripts y cobertura` | Pendiente de confirmar (URL) | `test_scripts.py` (5 pruebas) | Aprobadas |

## 2. Pruebas de regresión

Suite completa ejecutada con `python -m pytest -q`: **21 pruebas, 21 aprobadas, 0 fallidas**, con 97 % de cobertura de líneas (ejecución del 29/10/2026 en entorno Python 3.13, scikit-learn 1.9.1, pytest 9.1.1). Las 5 pruebas añadidas en GH-05 cubren los scripts `app.py`, `generar_datos.py` y `evaluar_ia.py`.

Registro de defectos del taller:

| ID | Descripción | Severidad | Estado |
|---|---|---|---|
| D-01 | El generador de datos sintéticos creaba lotes etiquetados como atípicos con valores normales (etiquetas incorrectas, que reducían artificialmente el recall) | Mayor | Cerrado (generador corregido antes de reportar métricas) |
| D-02 | Los scripts `app.py`, `generar_datos.py` y `evaluar_ia.py` no tenían pruebas automáticas (cobertura global de líneas 52 %) | Menor | Cerrado en GH-05 (cobertura 97 %) |

Defectos críticos abiertos: **0**.

## 3. Checklist de auditoría

- [x] Requisitos versionados (`docs/requisitos.md`)
- [x] Ramas y commits con convención (según `docs/plan_configuracion.md`)
- [ ] PR revisados y vinculados a tickets — **Pendiente de confirmar** en GitHub
- [x] Pruebas ejecutadas con evidencia (16/16)
- [x] Dependencias y datos reproducibles (`requirements.txt`, CSV con semilla 42; prueba de reproducibilidad)
- [x] Sin secretos ni datos sensibles (búsqueda de patrones de tokens/claves sin resultados; `.gitignore` excluye `.env`, `*.key`, `*.pem`)
- [x] Reporte de métricas y análisis (`docs/plan_medicion.md`)
- [ ] Tag y notas de release coherentes — **Pendiente**: se crea tras integrar los PR

## 4. Decisión de liberación

Criterios: cero defectos críticos abiertos (cumple), pruebas obligatorias aprobadas (cumple), PR revisados (**pendiente**).

**Decisión: aplazar la creación del tag `v1.0.0` hasta que los PR GH-01 a GH-05 estén revisados e integrados en `main`.** Cuando eso ocurra y la suite siga en verde, se aprueba el release. Esta decisión debe actualizarse con las URL de los PR y el responsable que firma.
