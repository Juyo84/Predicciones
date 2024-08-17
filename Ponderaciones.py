import Datos as datos
import pandas as pd
import os

v1ponderacionesClasificacion: tuple = (0, 0, 2.0643, -0.9042, 4.2429, -4.0499, 0.0240)
v1ponderacionesEstadisticasACB: tuple = (0, 0, 0, 0, 4.2370, 4.1024, 4.4097, 3.9550, 4.3736, 4.2633, 4.1770, 4.1346, 4.3482, 4.2622, 3.8219, 4.0761, 4.3814, 3.9844, 4.0944, -3.8629, 3.5117, -3.4541, 2.8067, -4.2647, 4.4632, 3.7303)
v1ponderacionesEstadisticaAvanzadaEquipos: tuple = (0, 0, 0, 2.8294, 2.9707, 2.9645, 5.2800, 0.3885, 2.6500, 2.6838, 2.5633, 2.1888, 2.4585, 3.3975, 2.5017, 2.5095, 2.9330)

v1ponderacionesEstadisticaAvanzadaJugadores: tuple = (0, 0, 0, 0, 0, 4.8073, 0.0216, 0.0192, 7.3569, 7.1093, 1.5836, 1.3296, 0.0186, 0.0111, 0.0140, 0.1567, 0.0216, 0.0052, 0.0489, 0.0921, -0.0711)
v1ponderacionesTirosJugador: tuple = (0, 0, 0, 11.5041, 13.6191, 0.0559, 13.4676, 22.7927, 0.0449, 4.3669, 11.4313, 0.0507)

#VERSION 1:
#1.2733	-0.5577	2.6170	-2.4980	0.0148
#2.6134	2.5304	2.7199	2.4395	2.6977	2.6296	2.5764	2.5503	2.6820	2.6290	2.3574	2.5142	2.7025	2.4576	2.5255	-2.3827	2.1661	-2.1305	1.7312	-2.6305	2.7530	2.3009
#2.8294	2.9707	2.9645	5.2800	0.3885	2.6500	2.6838	2.5633	2.1888	2.4585	3.3975	2.5017	2.5095	2.9330

#4.8073	    0.0216	0.0192	7.3569	7.1093	1.5836	1.3296	0.0186	0.0111	0.0140	0.1567	0.0216	0.0052	0.0489	0.0921	-0.0711
#11.5041	13.6191	0.0559	13.4676	22.7927	0.0449	4.3669	11.4313	0.0507


#VERSION 2:
#1.6000	-1.0427	0.2567	-0.2367	33.3467
#6.0827	4.0400	31.3300	0.0614	5.9350	42.4200	0.1200	5.9100	22.5200	0.1680	1.6829	2.8580	3.9530	2.9429	3.4067	-3.5075	2.4150	-0.9933	2.6150	-11.4700	11.0700	22.0460
#15.5280	5.9880	5.6335	0.9510	2.9700	0.1500	0.0720	0.1120	0.5633	0.2133	0.0650	0.1280	0.2420	0.2240

#16.5020	0.0463	    0.0413	8.4180	    8.1347	    2.2650	2.2820	0.0640	    0.0380	0.0400	0.6725	0.0925	0.0300	0.0840	0.1580	-0.1220
#197.4500	233.7500	0.4800	231.1500	391.2000	0.2567	74.9500	196.2000	0.2900

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
    ponderacion += _ponderacionUltimoRegistro(ruta, v1ponderacionesClasificacion)
    
    ruta = 'Datos//Equipos//Equipo//EstadisticasACB_' + equipo + '.csv'
    ponderacion += _ponderacionUltimoRegistro(ruta, v1ponderacionesEstadisticasACB)

    ruta = 'Datos//Equipos//Equipo//EstadisticaAvanzadaEquipos_' + equipo + '.csv'
    ponderacion += _ponderacionUltimoRegistro(ruta, v1ponderacionesEstadisticaAvanzadaEquipos)

    return ponderacion


