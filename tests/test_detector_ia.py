from pathlib import Path

import pandas as pd

from detector_ia import AVISO, DetectorAnomalias, evaluar

CSV = Path(__file__).resolve().parent.parent / "data" / "lotes_ejemplo.csv"


def test_dataset_sintetico_minimo():  # actividad IA: >= 30 lotes
    df = pd.read_csv(CSV)
    assert len(df) >= 30 and df["atipico"].sum() > 0


def test_reproducible_con_semilla():  # RNF-03
    df = pd.read_csv(CSV)
    a = DetectorAnomalias().entrenar(df).predecir(df)
    b = DetectorAnomalias().entrenar(df).predecir(df)
    assert (a == b).all()


def test_evaluar_metricas():
    m = evaluar([1, 1, 0, 0], [1, 0, 1, 0])
    assert m["TP"] == 1 and m["FN"] == 1 and m["FP"] == 1 and m["recall"] == 0.5


def test_advertencia_de_uso_orientativo():  # RF-05
    assert "orientativa" in AVISO and "riesgo sanitario" in AVISO


def test_detecta_al_menos_un_atipico():  # RF-05
    df = pd.read_csv(CSV)
    pred = DetectorAnomalias().entrenar(df).predecir(df)
    assert pred.sum() >= 1
