"""Indicadores de calidad de produccion (RF-02, RF-04)."""
from produccion import Lote, validar_lote


def tasa_defectos(producidas: int, defectuosas: int) -> float:
    """RF-02: (defectuosas / producidas) x 100."""
    return validar_lote(producidas, defectuosas)


def resumen_lotes(lotes: list[Lote]) -> dict:
    """RF-04: conteo de lotes y tasa de defectos global y por lote."""
    total_prod = sum(l.producidas for l in lotes)
    total_def = sum(l.defectuosas for l in lotes)
    return {
        "lotes": len(lotes),
        "producidas": total_prod,
        "defectuosas": total_def,
        "tasa_global": round(tasa_defectos(total_prod, total_def), 2) if total_prod else 0.0,
        "tasa_por_lote": {l.codigo: round(tasa_defectos(l.producidas, l.defectuosas), 2) for l in lotes},
    }


def tablero_texto(lotes: list[Lote]) -> str:
    r = resumen_lotes(lotes)
    lineas = [
        "=== TABLERO ALIMENTA-IA ===",
        f"Lotes registrados : {r['lotes']}",
        f"Unidades producidas: {r['producidas']}",
        f"Unidades defectuosas: {r['defectuosas']}",
        f"Tasa global de defectos: {r['tasa_global']} %",
    ]
    return "\n".join(lineas)
