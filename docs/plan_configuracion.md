# Plan de gestión de la configuración — ALIMENTA-IA

## Registro de elementos de configuración (SCI)

| ID SCI | Elemento | Ubicación | Responsable | Versión / línea base |
|---|---|---|---|---|
| SCI-01 | Código fuente | `src/` | Desarrollador | v1.0.0 |
| SCI-02 | Pruebas | `tests/` | QA | v1.0.0 |
| SCI-03 | Datos sintéticos | `data/` | Resp. medición | v1.0.0 |
| SCI-04 | Documentación | `docs/` | Resp. configuración | v1.0.0 |
| SCI-05 | Dependencias | `requirements.txt` | Resp. configuración | v1.0.0 |

Línea base inicial: primer commit en `main` (`chore: estructura inicial ALIMENTA-IA`).

## Convenciones

- Ramas: `main` (estable) y `feature/GH-xx-descripcion`.
- Commits: `tipo(GH-xx): descripcion`; tipos `feat`, `fix`, `test`, `docs`, `chore`.
- Pull Request hacia `main`: ticket asociado, pruebas aprobadas y revisión antes de integrar.
- Versionado: tag anotado `vMAJOR.MINOR.PATCH`.
- Prohibido subir contraseñas, tokens o datos reales.

## Registro de cambios

| Ticket | Motivo | SCI afectados | Riesgo / impacto | Decisión | PR / evidencia |
|---|---|---|---|---|---|
| GH-01 | Registro de lotes | `src/produccion.py`, `tests/test_produccion.py` | Medio: afecta validación de datos | Aprobado si pytest pasa | Pendiente de confirmar (URL del PR) |
| GH-02 | Indicadores | `src/calidad.py`, `tests/test_calidad.py` | Bajo | Aprobado si pytest pasa | Pendiente de confirmar (URL del PR) |
| GH-03 | Detector IA | `src/detector_ia.py`, `src/evaluar_ia.py`, `data/` | Medio: uso responsable de alertas | Aprobado si pytest pasa | Pendiente de confirmar (URL del PR) |
| GH-04 | Auditoría y notas de versión | `docs/` | Bajo | Aprobado tras revisión | Pendiente de confirmar (URL del PR) |
| GH-05 | Pruebas de scripts (cierra D-02) | `src/generar_datos.py`, `tests/test_scripts.py` | Bajo: `generar()` recibe parámetro opcional `ruta` | Aprobado si pytest pasa | Pendiente de confirmar (URL del PR) |
