"""Modulo de registro de lotes (RF-01, RF-03, RNF-01)."""
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Lote:
    codigo: str
    fecha: date
    producto: str
    producidas: int
    defectuosas: int
    temperatura: float


def validar_lote(producidas: int, defectuosas: int) -> float:
    """Valida cantidades y devuelve la tasa de defectos (%).

    Rechaza: producidas <= 0, defectuosas negativas o defectuosas > producidas.
    """
    if producidas <= 0 or defectuosas < 0 or defectuosas > producidas:
        raise ValueError("Cantidades invalidas")
    return 100 * defectuosas / producidas


class RegistroLotes:
    """Registro en memoria de lotes con codigo unico."""

    def __init__(self):
        self._lotes: dict[str, Lote] = {}

    def registrar(self, codigo: str, fecha: date, producto: str,
                  producidas: int, defectuosas: int, temperatura: float) -> Lote:
        if not codigo or not codigo.strip():
            raise ValueError("El codigo de lote es obligatorio")
        if not producto or not producto.strip():
            raise ValueError("El producto es obligatorio")
        if codigo in self._lotes:
            raise ValueError(f"El lote {codigo} ya existe")
        validar_lote(producidas, defectuosas)
        lote = Lote(codigo, fecha, producto, producidas, defectuosas, temperatura)
        self._lotes[codigo] = lote
        return lote

    def historial(self, producto: str | None = None) -> list[Lote]:
        lotes = sorted(self._lotes.values(), key=lambda l: (l.fecha, l.codigo))
        if producto is None:
            return lotes
        return [l for l in lotes if l.producto.lower() == producto.lower()]
