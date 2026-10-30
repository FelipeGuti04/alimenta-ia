# Plan de medición y análisis — ALIMENTA-IA

Se separan cuatro ámbitos. Los **defectos del software** (fallas en el código) no se confunden con las **unidades defectuosas de fábrica** (dato del dominio).

## Definición de indicadores

| Ámbito | Indicador | Fórmula / método | Fuente | Periodicidad | Responsable | Meta de clase |
|---|---|---|---|---|---|---|
| Producto (software) | Aprobación de pruebas | pruebas aprobadas / ejecutadas × 100 | pytest | Cada PR y release | QA | 100 % |
| Producto (software) | Cobertura de requisitos | RF con pruebas / RF totales × 100 | `docs/requisitos.md` | Cierre de sesión 3 y 4 | Resp. medición | ≥ 90 % |
| Proceso | PR revisados | PR aprobados / PR integrados × 100 | GitHub | Cada integración | Resp. configuración | 100 % |
| Proyecto | Cumplimiento de tareas | tareas terminadas / comprometidas × 100 | Tablero de tareas | Fin de cada sesión | Product Owner | ≥ 80 % |
| Producción | Tasa de defectos | defectuosas / producidas × 100 | `data/lotes_ejemplo.csv` | Por lote | QA | Analizar tendencia (sin meta industrial real) |
| IA | Recall de anomalías | TP / (TP + FN) | Dataset sintético etiquetado | Por entrenamiento | QA | Reportar valor y limitaciones |

## Resultados obtenidos (medidos al ejecutar el código)

| Indicador | Valor obtenido | Meta | Interpretación | Acción correctiva |
|---|---|---|---|---|
| Aprobación de pruebas | 21/21 = 100 % | 100 % | Cumple | Ninguna |
| Cobertura de requisitos | 9/9 = 100 % (5 RF + RNF-01 y RNF-03 con prueba; RNF-02 y RNF-04 se verifican por auditoría) | ≥ 90 % | Cumple | Ninguna |
| Cobertura de líneas (pytest-cov) | 97 % global (138/142 líneas); 100 % en `produccion.py`, `calidad.py` y `detector_ia.py` | Sin meta de clase | Las 4 líneas sin cubrir son los bloques `if __name__ == "__main__"` de los scripts. Antes de GH-05 la cobertura era 52 % | Ninguna |
| PR revisados | Pendiente de confirmar (depende de los PR creados en GitHub) | 100 % | — | — |
| Cumplimiento de tareas | Pendiente de confirmar (tablero del equipo) | ≥ 80 % | — | — |
| Tasa de defectos (global) | 1358 / 45 376 = 2,99 %. Por producto: Arepa 2,25 %, Bocadillo 3,32 %, Galleta 3,36 % | Tendencia | Datos sintéticos; la diferencia entre productos no tiene significado industrial | Ninguna |
| IA — recall | Ver sección siguiente | Reportar | Ver limitaciones | Ver limitaciones |

## Evaluación del detector de IA

- Dataset sintético: 46 lotes, 6 atípicos etiquetados (generados con semilla 42 en `src/generar_datos.py`).
- Modelo: `IsolationForest` (n_estimators = 200, contamination = 0,1, random_state = 42) sobre producidas, temperatura y tasa de defectos, escaladas con `StandardScaler`.
- Evaluación con separación entrenamiento/evaluación (70/30, estratificada, semilla 42): 32 lotes de entrenamiento y 14 de evaluación.

| Conjunto | TP | FP | FN | TN | Recall | Precisión |
|---|---|---|---|---|---|---|
| Evaluación (14 lotes) | 1 | 0 | 1 | 12 | 0,50 | 1,00 |
| Dataset completo (46 lotes, informativo) | 5 | 0 | 1 | 40 | 0,83 | 1,00 |

### Limitaciones

- El conjunto de evaluación contiene solo 2 atípicos reales, por lo que el recall de 0,50 equivale a 1 de 2 y no es estadísticamente concluyente.
- Las cifras del dataset completo usan datos con los que se entrenó el modelo; sirven como referencia, no como estimación de desempeño.
- Los atípicos son sintéticos y se generaron a propósito; con datos reales el desempeño puede ser muy distinto.
- Una primera versión del generador producía "atípicos" con valores normales (mal etiquetados); se corrigió el generador antes de reportar estos resultados. No se ajustaron los parámetros del modelo para mejorar las métricas.
- Una alerta indica una observación apartada del comportamiento esperado; no implica por sí sola defecto ni riesgo sanitario.
