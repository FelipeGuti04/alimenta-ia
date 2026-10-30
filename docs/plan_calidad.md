# Plan de calidad — ALIMENTA-IA

## Objetivos de calidad y controles

| Objetivo de calidad | Control preventivo | Prueba o evidencia | Responsable | Criterio de aceptación |
|---|---|---|---|---|
| Evitar registros inválidos | Validación de entradas en `validar_lote`; revisión de código | `tests/test_produccion.py` (reporte pytest) | Desarrollador / QA | 100 % de pruebas de validación aprobadas |
| Asegurar cambios trazables | Ramas `feature/GH-xx`, commits convencionales, PR con ticket | Historial Git, PR revisados | Resp. configuración | 100 % de PR revisados y vinculados a ticket |
| Detectar fallas de IA | Semilla y parámetros documentados, evaluación con etiquetas, advertencia de uso orientativo | `src/evaluar_ia.py`, `docs/plan_medicion.md` | QA | Recall/precisión reportados con sus limitaciones |
| Reproducibilidad | `requirements.txt`, CSV versionado, semilla fija | `test_reproducible_con_semilla` | Resp. medición | Misma salida en dos ejecuciones |

## Pruebas

- Unitarias con pytest (`python -m pytest -q`).
- Regresión: se reejecuta toda la suite antes de cada PR y antes del release.
- Revisión de código: checklist en el PR (ver `docs/auditoria_release.md`).

## Gestión de defectos

Registro en GitHub Issues con severidad (crítico / mayor / menor) y estado (abierto / en corrección / cerrado).

## Criterios de salida (liberación)

1. Cero defectos críticos abiertos.
2. Pruebas obligatorias aprobadas.
3. Todos los PR integrados revisados.
4. Sin secretos ni datos reales en el repositorio.

## Alcance y límites

Los datos son sintéticos. Las alertas de IA son apoyo analítico y no sustituyen controles de inocuidad, evaluación de laboratorio ni decisiones de profesionales responsables.
