from datetime import date

import pytest

from calidad import resumen_lotes, tablero_texto, tasa_defectos
from produccion import Lote


def _lotes():
    return [Lote("L1", date(2026, 1, 1), "Arepa", 200, 6, 70.0),
            Lote("L2", date(2026, 1, 2), "Galleta", 300, 3, 71.0)]


def test_tasa_defectos():  # RF-02
    assert tasa_defectos(200, 6) == 3.0


def test_tasa_invalida():  # RF-02 / RNF-01
    with pytest.raises(ValueError):
        tasa_defectos(0, 0)


def test_resumen():  # RF-04
    r = resumen_lotes(_lotes())
    assert r["lotes"] == 2 and r["producidas"] == 500 and r["defectuosas"] == 9
    assert r["tasa_global"] == 1.8
    assert r["tasa_por_lote"]["L1"] == 3.0


def test_tablero_muestra_conteo():  # RF-04
    assert "Lotes registrados : 2" in tablero_texto(_lotes())
