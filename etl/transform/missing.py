from datetime import date
from statistics import mean
import logging

logger = logging.getLogger(__name__)


def fill_missing_with_avg(
    rows: list[tuple[str, str, date]],
    window: int = 3,
) -> list[tuple[str, float, date]]:
    """
    rows: lista de tuplas (series_id, value_str, date) ORDENADA por fecha ascendente.
    Reemplaza "n.d." con el promedio de los últimos `window` valores válidos previos.
    Si no hay ningún valor previo disponible, descarta la fila (no hay con qué promediar).
    """
    result = []
    history: list[float] = []

    for series_id, value_str, dt in rows:
        if value_str == "n.d.":
            if not history:
                logger.warning("Sin datos previos para imputar %s en %s, se descarta", series_id, dt)
                continue
            imputed = round(mean(history[-window:]), 4)
            result.append((series_id, imputed, dt))
            history.append(imputed)
        else:
            value = float(value_str)
            result.append((series_id, value, dt))
            history.append(value)

    return result