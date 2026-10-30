from datetime import date

import pytest

from produccion import RegistroLotes, validar_lote


def test_validar_lote_normal():  # RF-01
    assert validar_lote(200, 6) == 3.0


def test_cero_producidas():  # RNF-01
    with pytest.raises(ValueError):
        validar_lote(0, 0)


def test_negativos():  # RNF-01
    with pytest.raises(ValueError):
        validar_lote(100, -1)
    with pytest.raises(ValueError):
        validar_lote(-10, 0)


def test_defectuosas_mayores_que_producidas():  # RNF-01
    with pytest.raises(ValueError):
        validar_lote(100, 101)


def test_registrar_y_codigo_unico():  # RF-01
    r = RegistroLotes()
    r.registrar("L1", date(2026, 1, 1), "Arepa", 100, 2, 70.0)
    with pytest.raises(ValueError):
        r.registrar("L1", date(2026, 1, 2), "Arepa", 100, 2, 70.0)


def test_codigo_y_producto_obligatorios():  # RF-01
    r = RegistroLotes()
    with pytest.raises(ValueError):
        r.registrar("", date(2026, 1, 1), "Arepa", 100, 2, 70.0)
    with pytest.raises(ValueError):
        r.registrar("L2", date(2026, 1, 1), " ", 100, 2, 70.0)


def test_historial_filtra_por_producto():  # RF-03
    r = RegistroLotes()
    r.registrar("L1", date(2026, 1, 1), "Arepa", 100, 2, 70.0)
    r.registrar("L2", date(2026, 1, 2), "Galleta", 100, 3, 70.0)
    assert [l.codigo for l in r.historial("arepa")] == ["L1"]
    assert len(r.historial()) == 2
