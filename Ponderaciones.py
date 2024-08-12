import Datos as datos
import pandas as pd
import os

ponderacionesClasificacion: tuple = (0, 0, 2.0643, -0.9042, 4.2429, -4.0499, 0.0240)
ponderacionesEstadisticasACB: tuple = (0, 0, 0, 0, 4.2370, 4.1024, 4.4097, 3.9550, 4.3736, 4.2633, 4.1770, 4.1346, 4.3482, 4.2622, 3.8219, 4.0761, 4.3814, 3.9844, 4.0944, -3.8629, 3.5117, -3.4541, 2.8067, -4.2647, 4.4632, 3.7303)
ponderacionesEstadisticaAvanzadaEquipos: tuple = (0, 0, 0, 2.8294, 2.9707, 2.9645, 5.2800, 0.3885, 2.6500, 2.6838, 2.5633, 2.1888, 2.4585, 3.3975, 2.5017, 2.5095, 2.9330)

#VERSION 1:
#1.2733	-0.5577	2.6170	-2.4980	0.0148
#2.6134	2.5304	2.7199	2.4395	2.6977	2.6296	2.5764	2.5503	2.6820	2.6290	2.3574	2.5142	2.7025	2.4576	2.5255	-2.3827	2.1661	-2.1305	1.7312	-2.6305	2.7530	2.3009
#2.8294	2.9707	2.9645	5.2800	0.3885	2.6500	2.6838	2.5633	2.1888	2.4585	3.3975	2.5017	2.5095	2.9330

#VERSION 2:
#1.6000	-1.0427	0.2567	-0.2367	33.3467
#6.0827	4.0400	31.3300	0.0614	5.9350	42.4200	0.1200	5.9100	22.5200	0.1680	1.6829	2.8580	3.9530	2.9429	3.4067	-3.5075	2.4150	-0.9933	2.6150	-11.4700	11.0700	22.0460
#15.5280	5.9880	5.6335	0.9510	2.9700	0.1500	0.0720	0.1120	0.5633	0.2133	0.0650	0.1280	0.2420	0.2240

def _ponderacionUltimoRegistro(ruta: str, ponderaciones: tuple) -> float:

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
    ponderacion += _ponderacionUltimoRegistro(ruta, ponderacionesClasificacion)
    
    ruta = 'Datos//Equipos//Equipo//EstadisticasACB_' + equipo + '.csv'
    ponderacion += _ponderacionUltimoRegistro(ruta, ponderacionesEstadisticasACB)

    ruta = 'Datos//Equipos//Equipo//EstadisticaAvanzadaEquipos_' + equipo + '.csv'
    ponderacion += _ponderacionUltimoRegistro(ruta, ponderacionesEstadisticaAvanzadaEquipos)

    return ponderacion


