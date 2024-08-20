import Ponderaciones as ponderacion
import Datos as datos
from datetime import datetime
import pandas as pd
import os

def prediccion(fecha: datetime, equipoCasa: str, equipoVisitante: str) -> tuple:

    diferencia: float
    ganador: tuple

    casa = 0
    visitante = 0

    totalCasa = ponderacion.totalPonderacionEquipo(equipoCasa)
    totalVisitante = ponderacion.totalPonderacionEquipo(equipoVisitante)

    #totalJugadoresCasa = ponderacion.totalPonderacionJugadores(equipoCasa)
    #totalJugadoresVisitante = ponderacion.totalPonderacionJugadores(equipoVisitante)

    #casa += totalCasa + totalJugadoresCasa
    #visitante += totalVisitante + totalJugadoresVisitante

    casa = totalCasa
    visitante = totalVisitante

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


def prediccionAutomatica(fechaActual: datetime) -> bool:

    rutaCalendario = 'Datos//Equipos//General//Calendario_.csv'

    if os.path.exists(rutaCalendario):

        dfPartidos: pd.DataFrame = pd.read_csv(rutaCalendario)

        for partido in range(0, len(dfPartidos), 1):
        
            fecha = dfPartidos.values[partido][0]
            casa = dfPartidos.values[partido][2]
            visitante = dfPartidos.values[partido][3]

            prediccion(fecha, casa, visitante)

        return True

    else:

        return False
    

