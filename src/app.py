"""Punto de entrada por linea de comandos: python src/app.py"""
from pathlib import Path

import pandas as pd

from calidad import resumen_lotes, tablero_texto
from detector_ia import AVISO, DetectorAnomalias, evaluar
from produccion import RegistroLotes

DATOS = Path(__file__).resolve().parent.parent / "data" / "lotes_ejemplo.csv"


def cargar_registro(ruta=DATOS) -> RegistroLotes:
    df = pd.read_csv(ruta)
    reg = RegistroLotes()
    for r in df.itertuples():
        reg.registrar(r.codigo, pd.to_datetime(r.fecha).date(), r.producto,
                      int(r.producidas), int(r.defectuosas), float(r.temperatura))
    return reg


def main():
    reg = cargar_registro()
    print(tablero_texto(reg.historial()))
    df = pd.read_csv(DATOS)
    det = DetectorAnomalias().entrenar(df)
    df["alerta"] = det.predecir(df)
    print(f"\nLotes marcados como atipicos: {int(df['alerta'].sum())}")
    print(df.loc[df["alerta"] == 1, ["codigo", "producto", "producidas", "defectuosas", "temperatura"]].to_string(index=False))
    print("\n" + AVISO)


if __name__ == "__main__":
    main()
