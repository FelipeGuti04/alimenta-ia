# ALIMENTA-IA

Prototipo educativo para la fábrica simulada **NutriAlimentos S.A.S.**: registro de lotes, tasa de defectos, tablero y detección de lotes atípicos con IA. Taller integrador de Administración de Proyectos de Software (UTP). **Todos los datos son sintéticos.**

> Las alertas de IA son apoyo analítico orientativo. No sustituyen controles de inocuidad, evaluación de laboratorio ni decisiones de profesionales responsables.

## Instalación y ejecución

```bash
pip install -r requirements.txt
python src/generar_datos.py   # regenera data/lotes_ejemplo.csv (semilla 42)
python src/app.py             # tablero y lotes atípicos
python src/evaluar_ia.py      # métricas del detector
python -m pytest -q           # pruebas
```

## Estructura

```
src/    produccion.py, calidad.py, detector_ia.py, app.py, generar_datos.py, evaluar_ia.py
tests/  test_produccion.py, test_calidad.py, test_detector_ia.py
data/   lotes_ejemplo.csv (sintético)
docs/   requisitos, plan de calidad, medición, configuración, auditoría y release
```

## Flujo de trabajo

Ramas `feature/GH-xx-*`, commits convencionales, Pull Request con revisión hacia `main` y release etiquetado. Ver `docs/plan_configuracion.md`.
