import Ponderaciones as ponderacion

def prediccion(equipoCasa: str, equipoVisitante: str) -> tuple:

    diferencia: float

    totalCasa = ponderacion.totalPonderacionEquipo(equipoCasa)
    totalVisitante = ponderacion.totalPonderacionEquipo(equipoVisitante)

    if totalCasa > totalVisitante:

        diferencia = totalCasa - totalVisitante

        return (equipoCasa, diferencia)

    elif totalVisitante > totalCasa:

        diferencia = totalVisitante - totalCasa

        return (equipoVisitante, diferencia)
    
    return ("EMPATE", 0)


