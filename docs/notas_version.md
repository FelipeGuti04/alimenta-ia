# Notas de versión — v1.0.0 (primera versión educativa)

Estado: **borrador**, se publica cuando los PR estén integrados (ver `docs/auditoria_release.md`).

## Incluye

- Registro de lotes con validación de cantidades y código único (GH-01).
- Tasa de defectos, historial filtrable y tablero de texto (GH-02).
- Detector de lotes atípicos con IsolationForest, dataset sintético de 46 lotes y evaluación con límites documentados (GH-03).
- Documentos de calidad, medición, configuración y auditoría (GH-04).
- Pruebas de los scripts de apoyo (GH-05).

## Calidad

- 21 pruebas, 21 aprobadas; cobertura de líneas 97 %.
- Defectos abiertos: 0 (D-01 y D-02 cerrados).

## Limitaciones conocidas

- Datos 100 % sintéticos; las métricas de IA no son extrapolables a datos reales.
- Recall de evaluación 0,50 sobre solo 2 atípicos; no concluyente.
- Las alertas de IA son orientativas y no sustituyen controles de inocuidad.
