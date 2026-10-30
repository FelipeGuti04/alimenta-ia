"""Detector de lotes atipicos con IsolationForest (RF-05).

AVISO: las alertas son apoyo analitico orientativo. No sustituyen controles
de inocuidad, evaluacion de laboratorio ni decisiones de profesionales.
"""
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

AVISO = ("Alerta orientativa generada por un modelo estadistico sobre datos "
         "sinteticos. No indica por si sola defecto ni riesgo sanitario.")
SEMILLA = 42
PARAMETROS = {"n_estimators": 200, "contamination": 0.1, "random_state": SEMILLA}


def _features(df):
    tasa = 100 * df["defectuosas"] / df["producidas"]
    return np.column_stack([df["producidas"], df["temperatura"], tasa])


class DetectorAnomalias:
    def __init__(self, **params):
        self.params = {**PARAMETROS, **params}
        self.scaler = StandardScaler()
        self.modelo = IsolationForest(**self.params)

    def entrenar(self, df):
        X = self.scaler.fit_transform(_features(df))
        self.modelo.fit(X)
        return self

    def predecir(self, df) -> np.ndarray:
        """Devuelve 1 si el lote es atipico, 0 si es normal."""
        X = self.scaler.transform(_features(df))
        return (self.modelo.predict(X) == -1).astype(int)


def evaluar(y_real, y_pred) -> dict:
    y_real, y_pred = np.asarray(y_real), np.asarray(y_pred)
    tp = int(((y_real == 1) & (y_pred == 1)).sum())
    fp = int(((y_real == 0) & (y_pred == 1)).sum())
    fn = int(((y_real == 1) & (y_pred == 0)).sum())
    tn = int(((y_real == 0) & (y_pred == 0)).sum())
    recall = tp / (tp + fn) if (tp + fn) else float("nan")
    precision = tp / (tp + fp) if (tp + fp) else float("nan")
    return {"TP": tp, "FP": fp, "FN": fn, "TN": tn,
            "recall": recall, "precision": precision}
