# Auditoría, regresión y decisión de liberación — ALIMENTA-IA

Equipo: Felipe Gutierrez (Desarrollador, Responsable de configuración y medición) y Camilo Ossa (Product Owner y Responsable QA).

## 1. Trazabilidad RF → ticket → rama → commit → PR → prueba → resultado

| Requisito | Ticket | Rama | Commit | PR | Casos de prueba | Resultado |
|---|---|---|---|---|---|---|
| RF-01, RF-03, RNF-01 | GH-01 | `feature/GH-01-registro-lotes` | `feat(GH-01): registro y validacion de lotes` | [#1](https://github.com/FelipeGuti04/alimenta-ia/pull/1) | `test_produccion.py` (7 pruebas) | Aprobadas |
| RF-02, RF-04 | GH-02 | `feature/GH-02-indicadores` | `feat(GH-02): indicadores y tablero de calidad` | [#2](https://github.com/FelipeGuti04/alimenta-ia/pull/2) | `test_calidad.py` (4 pruebas) | Aprobadas |
| RF-05, RNF-03 | GH-03 | `feature/GH-03-detector-ia` | `feat(GH-03): detector IA, datos sinteticos y evaluacion` | [#3](https://github.com/FelipeGuti04/alimenta-ia/pull/3) | `test_detector_ia.py` (5 pruebas) | Aprobadas |
| RNF-02, RNF-04 | GH-04 | `docs/GH-04-auditoria-release` | `docs(GH-04): auditoria y notas de version` | [#4](https://github.com/FelipeGuti04/alimenta-ia/pull/4) | Revisión manual (checklist) | Ver sección 3 |
| RNF-03 (D-02) | GH-05 | `test/GH-05-pruebas-scripts` | `test(GH-05): pruebas de scripts y cobertura` | [#5](https://github.com/FelipeGuti04/alimenta-ia/pull/5) | `test_scripts.py` (5 pruebas) | Aprobadas |
| RNF-02 (D-03) | GH-06 | `docs/GH-06-cierre-documental` | `docs(GH-06): cierre documental` | [#6](https://github.com/FelipeGuti04/alimenta-ia/pull/6) | Revisión manual (checklist) | Ver sección 3 |

### Revisión de los PR

| PR | Integrado en `main` por | Registro de la revisión en GitHub |
|---|---|---|
| #1 | Camilo Ossa | Revisión con comentario «Aprobado», antes de integrar |
| #2 | Camilo Ossa | Ninguno |
| #3 | Camilo Ossa | Ninguno |
| #4 | Camilo Ossa | Ninguno |
| #5 | Camilo Ossa | Revisión con comentario «Revisado», antes de integrar |

Según el revisor (Camilo Ossa), los cinco PR fueron revisados antes de integrarse. Solo #1 y #5 tienen constancia en GitHub. En #2, #3 y #4 no se dejó comentario ni aprobación por un error humano, y una vez integrados GitHub no permitió añadirlos. Esta diferencia se registra como el defecto D-03 y no se corrige con evidencia posterior.

## 2. Pruebas de regresión

Suite completa ejecutada con `python -m pytest -q`: **21 pruebas, 21 aprobadas, 0 fallidas**, con 97 % de cobertura de líneas (ejecución del 29/10/2026 en entorno Python 3.13, scikit-learn 1.9.1, pytest 9.1.1). Las 5 pruebas añadidas en GH-05 cubren los scripts `app.py`, `generar_datos.py` y `evaluar_ia.py`.

Registro de defectos del taller:

| ID | Descripción | Severidad | Estado |
|---|---|---|---|
| D-01 | El generador de datos sintéticos creaba lotes etiquetados como atípicos con valores normales (etiquetas incorrectas, que reducían artificialmente el recall) | Mayor | Cerrado (generador corregido antes de reportar métricas) |
| D-02 | Los scripts `app.py`, `generar_datos.py` y `evaluar_ia.py` no tenían pruebas automáticas (cobertura global de líneas 52 %) | Menor | Cerrado en GH-05 (cobertura 97 %) |
| D-03 | Los PR #2, #3 y #4 se integraron sin revisión registrada en GitHub: el botón de integrar no exige aprobación y el revisor no dejó comentario, aunque según él los revisó | Menor (proceso) | Abierto y aceptado con salvedad; acción preventiva: regla de protección de rama que exija 1 aprobación |

Defectos críticos abiertos: **0**. Defectos abiertos en total: **1** (D-03, menor, de proceso).

## 3. Checklist de auditoría

- [x] Requisitos versionados (`docs/requisitos.md`)
- [x] Ramas y commits con convención (según `docs/plan_configuracion.md`)
- [~] PR revisados y vinculados a tickets: **parcial**. 5 de 5 revisados según el revisor; 2 de 5 con registro en GitHub (ver D-03)
- [x] Pruebas ejecutadas con evidencia (21/21)
- [x] Dependencias y datos reproducibles (`requirements.txt`, CSV con semilla 42; prueba de reproducibilidad)
- [x] Sin secretos ni datos sensibles (búsqueda de patrones de tokens/claves sin resultados; `.gitignore` excluye `.env`, `*.key`, `*.pem`)
- [x] Reporte de métricas y análisis (`docs/plan_medicion.md`)
- [ ] Tag y notas de release coherentes: **pendiente**, se crea tras integrar GH-06

## 4. Decisión de liberación

| Criterio de salida | Resultado |
|---|---|
| Cero defectos críticos abiertos | Cumple (0) |
| Pruebas obligatorias aprobadas | Cumple (21/21) |
| Todos los PR integrados revisados | Cumple con salvedad: registro verificable en 2 de 5 (D-03) |
| Sin secretos ni datos reales | Cumple |

**Decisión propuesta: aprobar la liberación de v1.0.0 con una salvedad (D-03).** Condición: integrar el PR #6 y crear el tag `v1.0.0` sobre `main`. Acción preventiva para próximos cambios: activar en GitHub una regla de protección de la rama `main` que exija al menos una aprobación antes de integrar.

| Rol | Nombre | Firma |
|---|---|---|
| Elaborado por (Desarrollador y Responsable de configuración) | Felipe Gutierrez | La firma se estampa en el informe en Word |
| Aprobado por (Product Owner y Responsable QA) | Camilo Ossa | La firma se estampa en el informe en Word |
