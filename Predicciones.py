import Ponderaciones as ponderacion
import Datos as datos
from datetime import datetime

def prediccion(fecha: datetime, equipoCasa: str, equipoVisitante: str) -> tuple:

    diferencia: float
    ganador: tuple

    casa = 0
    visitante = 0

    totalCasa = ponderacion.totalPonderacionEquipo(equipoCasa)
    totalVisitante = ponderacion.totalPonderacionEquipo(equipoVisitante)

    totalJugadoresCasa = ponderacion.totalPonderacionJugadores(equipoCasa)
    totalJugadoresVisitante = ponderacion.totalPonderacionJugadores(equipoVisitante)

    casa += totalCasa + totalJugadoresCasa
    visitante += totalVisitante + totalJugadoresVisitante

    if casa > visitante:

        diferencia = casa - visitante

        ganador = (equipoCasa, diferencia)

    elif visitante > casa:

        diferencia = visitante - casa

        ganador = (equipoVisitante, diferencia)

    else:

        ganador = ("EMPATE", 0)

    datos.guardarPartido(fecha, equipoCasa, casa, 0, equipoVisitante, visitante, 0, ganador[0])
    
    return ganador


