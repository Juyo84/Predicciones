import Datos as datos
import pandas as pd
import os

ponderacionesClasificacion: tuple = (0, 0, 2.0643, 0.9042, 4.2429, 4.0499, 0.0240)
ponderacionesEstadisticasACB: tuple = (0, 0, 0, 0, 4.2370, 4.1024, 4.4097, 3.9550, 4.3736, 4.2633, 4.1770, 4.1346, 4.3482, 4.2622, 3.8219, 4.0761, 4.3814, 3.9844, 4.0944, 3.8629, 3.5117, 3.4541, 2.8067, 4.2647, 4.4632, 3.7303)
ponderacionesEstadisticaAvanzadaEquipos: tuple = (0, 0, 0, 2.8294, 2.9707, 2.9645, 5.2800, 0.3885, 2.6500, 2.6838, 2.5633, 2.1888, 2.4585, 3.3975, 2.5017, 2.5095, 2.9330)


def _ponderacion(ruta: str, ponderaciones: tuple) -> float:

    total: float = 0

    if os.path.exists(ruta):
        
        dfEstadisticas: pd.DataFrame = pd.read_csv(ruta)

        total: float = 0
        columnas = dfEstadisticas.columns

        for columna in range(0, columnas.size, 1):

            dato: str = str(dfEstadisticas.values[-1][columna])

            if dato.isnumeric():
                
                total += (float(dato) * float(ponderaciones[columna]))
    
    return total


def totalPonderacionEquipo(equipo: str) -> float:

    equipo = datos.equipos(equipo, 1)
    
    ponderacion: float = 0
    ruta: str = ''

    ruta = 'Datos//Equipos//Equipo//Clasificacion_' + equipo + '.csv'
    ponderacion += _ponderacion(ruta, ponderacionesClasificacion)
    
    ruta = 'Datos//Equipos//Equipo//EstadisticasACB_' + equipo + '.csv'
    ponderacion += _ponderacion(ruta, ponderacionesEstadisticasACB)

    ruta = 'Datos//Equipos//Equipo//EstadisticaAvanzadaEquipos_' + equipo + '.csv'
    ponderacion += _ponderacion(ruta, ponderacionesEstadisticaAvanzadaEquipos)

    return ponderacion

