"""Evaluacion del detector: separa entrenamiento/evaluacion y reporta metricas."""
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from detector_ia import PARAMETROS, SEMILLA, DetectorAnomalias, evaluar

CSV = Path(__file__).resolve().parent.parent / "data" / "lotes_ejemplo.csv"


def main():
    df = pd.read_csv(CSV)
    train, test = train_test_split(df, test_size=0.3, random_state=SEMILLA, stratify=df["atipico"])
    det = DetectorAnomalias().entrenar(train)
    m = evaluar(test["atipico"], det.predecir(test))
    print(f"Semilla={SEMILLA} parametros={PARAMETROS}")
    print(f"Entrenamiento={len(train)} lotes, evaluacion={len(test)} lotes "
          f"({int(test['atipico'].sum())} atipicos reales)")
    print(m)
    return m


if __name__ == "__main__":
    main()
