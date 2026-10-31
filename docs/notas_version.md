# Notas de versión — v1.0.0 (primera versión educativa)

Estado: lista para publicar con el tag `v1.0.0` una vez integrado el PR #6 (ver `docs/auditoria_release.md`).

## Incluye

- Registro de lotes con validación de cantidades y código único (GH-01).
- Tasa de defectos, historial filtrable y tablero de texto (GH-02).
- Detector de lotes atípicos con IsolationForest, dataset sintético de 46 lotes y evaluación con límites documentados (GH-03).
- Documentos de calidad, medición, configuración y auditoría (GH-04).
- Pruebas de los scripts de apoyo (GH-05).
- Cierre documental: roles, enlaces a los PR, indicadores y decisión de liberación (GH-06).

## Calidad

- 21 pruebas, 21 aprobadas; cobertura de líneas 97 %.
- Defectos críticos abiertos: 0.
- Defecto abierto: D-03 (menor, de proceso): los PR #2, #3 y #4 no tienen revisión registrada en GitHub, aunque según el revisor sí se revisaron. D-01 y D-02 están cerrados.

## Limitaciones conocidas

- Datos 100 % sintéticos; las métricas de IA no son extrapolables a datos reales.
- Recall de evaluación 0,50 sobre solo 2 atípicos; no concluyente.
- Las alertas de IA son orientativas y no sustituyen controles de inocuidad.
