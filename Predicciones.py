import Ponderaciones as ponderacion

def prediccion(equipoCasa: str, equipoVisitante: str) -> tuple:

    diferencia: float

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

        return (equipoCasa, diferencia)

    elif visitante > casa:

        diferencia = visitante - casa

        return (equipoVisitante, diferencia)
    
    return ("EMPATE", 0)


