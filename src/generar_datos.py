"""Genera data/lotes_ejemplo.csv (datos 100% sinteticos, semilla fija)."""
import csv
from datetime import date, timedelta
from pathlib import Path

import numpy as np

SEMILLA = 42
PRODUCTOS = ["Galleta", "Arepa", "Bocadillo"]


def generar(n_normales: int = 40, n_atipicos: int = 6, ruta=None):
    rng = np.random.default_rng(SEMILLA)
    filas = []
    for i in range(n_normales):
        prod = int(rng.normal(1000, 50))
        tasa = max(rng.normal(2.0, 0.6), 0.1)
        filas.append((prod, int(round(prod * tasa / 100)), round(float(rng.normal(72, 1.5)), 1), 0))
    for i in range(n_atipicos):
        # Cada atipico se aparta claramente de lo normal en al menos una variable
        prod, tasa, temp = [(300, 12.0, 55.0), (1800, 15.0, 72.0), (1000, 14.0, 95.0),
                            (1000, 2.0, 55.0), (320, 2.0, 72.0), (1000, 13.0, 72.0)][i % 6]
        filas.append((prod, int(round(prod * tasa / 100)), round(temp, 1), 1))
    orden = rng.permutation(len(filas))
    inicio = date(2026, 1, 5)
    if ruta is None:
        ruta = Path(__file__).resolve().parent.parent / "data" / "lotes_ejemplo.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["codigo", "fecha", "producto", "producidas", "defectuosas", "temperatura", "atipico"])
        for k, idx in enumerate(orden):
            prod, dfc, temp, at = filas[idx]
            w.writerow([f"L{k+1:03d}", (inicio + timedelta(days=k)).isoformat(),
                        PRODUCTOS[k % 3], prod, dfc, temp, at])
    return ruta


if __name__ == "__main__":
    print("Generado:", generar())
