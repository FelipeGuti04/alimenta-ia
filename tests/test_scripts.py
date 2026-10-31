"""Pruebas de los scripts de apoyo: app, generar_datos y evaluar_ia (cierra D-02)."""
from pathlib import Path

import pandas as pd

import app
import evaluar_ia
import generar_datos

CSV = Path(__file__).resolve().parent.parent / "data" / "lotes_ejemplo.csv"


def test_generar_datos_reproduce_csv_versionado(tmp_path):  # RNF-03
    salida = tmp_path / "lotes.csv"
    generar_datos.generar(ruta=salida)
    assert salida.read_text(encoding="utf-8") == CSV.read_text(encoding="utf-8")


def test_generar_datos_estructura(tmp_path):
    salida = tmp_path / "lotes.csv"
    generar_datos.generar(ruta=salida)
    df = pd.read_csv(salida)
    assert len(df) == 46 and int(df["atipico"].sum()) == 6
    assert (df["defectuosas"] <= df["producidas"]).all()  # RNF-01


def test_cargar_registro_lee_todos_los_lotes():  # RF-01, RF-03
    reg = app.cargar_registro(CSV)
    assert len(reg.historial()) == 46


def test_main_imprime_tablero_y_advertencia(capsys):  # RF-04, RF-05
    app.main()
    salida = capsys.readouterr().out
    assert "TABLERO ALIMENTA-IA" in salida
    assert "Lotes registrados : 46" in salida
    assert "riesgo sanitario" in salida


def test_evaluar_ia_reporta_metricas():  # RF-05
    m = evaluar_ia.main()
    assert m["TP"] + m["FN"] == 2  # 2 atipicos reales en la evaluacion
    assert m["FP"] == 0
