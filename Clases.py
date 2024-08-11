import pandas as pd

Clasificacion: dict = {
    "equipo": str,
    "partidosJugados": int,
    "partidosGanados": int,
    "partidosPerdidos": int,
    "puntosFavor": int,
    "puntosContra": int,
    "puntosDiferencial": int
}


AvanzadaEquipo: dict = {

    "equipo": str,
    "partidosJugados": int,
    "minutos": float,
    "ritmo": float,
    "eficienciaOfensiva": float,
    "eficienciaDefensiva": float,
    "eficienciaNeta": float,
    "diferenciaPuntos": float,
    "porcentajeReboteDefensivos": int,
    "porcentajeReboteOfensivos": int,
    "porcentajeReboteTotal": int,
    "asistenciaPorPerdida": float,
    "porcentajeAsistencias": int,
    "porcentajeTapones": int,
    "porcentajeTiroReal": int,
    "eficienciaTiro": float,
    "eficienciaTiroRival": float

}


AvanzadaJugador: dict = {
    
    "jug": str,
    "jugador": str,
    "equipo": str,
    "partidosJugados": int,
    "minutos": int,
    "ritmo": int,
    "porcentajePosesiones": int,
    "porcentajePosesionesLanzados": int,
    "eficienciaOfensiva": int,
    "eficienciaDefensiva": int,
    "eficienciaNeta": int,
    "influencia": int,
    "porcentajeReboteDefensiva": int,
    "porcentajeReboteOfensiva": int,
    "porcentajeReboteTotal": int,
    "asistenciaPorPerdida": int,
    "porcentajeAsistencias": int,
    "porcentajeTapones": int,
    "porcentajeTiroReal": int,
    "eficienciaTiro": int,
    "eficienciaTiroRival": int

}


TirosEquipo: dict = {
    
    "equipo": str,
    "tirosLibresAnotados": int,
    "tirosLibresLanzados": int,
    "porcentajeTirosLibres": float,
    "tiros2Anotados": int,
    "tiros2Lanzados": int,
    "porcentajeTiros2": float,
    "tiros3Anotados": int,
    "tiros3Lanzados": int,
    "porcentajeTiros3": float

}


TirosJugador: dict = {
    
    "jug": str,
    "jugador": str,
    "equipo": str,
    "tirosLibresAnotados": int,
    "tirosLibresLanzados": int,
    "porcentajeTirosLibres": float,
    "tiros2Anotados": int,
    "tiros2Lanzados": int,
    "porcentajeTiros2": float,
    "tiros3Anotados": int,
    "tiros3Lanzados": int,
    "porcentajeTiros3": float

}


InfluenciaBaja: dict = {
    
    "jugador": str,
    "minutosSinEl": float,
    "minutosConEl": float,
    "minutosDiferencial": float,
    "anotacionSinEl": float,
    "anotacionConEl": float,
    "anotacionDiferencial": float,
    "valoracionSinEl": float,
    "valoracionConEl": float,
    "valoracionDiferencial": float

}


EstadisticaACB: dict = {
    
    "posicionValoracion": int,
    "equipo": str,
    "partidosJugados": int,
    "minutosJugados": float,
    "porcentajePuntosTotal": float,
    "tiros3Anotados": float,
    "tiros3intendados": float,
    "porcentajeTiros3": float,
    "tiros2Anotados": float,
    "tiros2Intentados": float,
    "porcentajeTiros2": float,
    "tirosLibresAnotados": float,
    "tirosLibresIntenados": float,
    "porcentajeTirosLibres": float,
    "porcentajeRebotesOfensivos": float,
    "porcentajeRebotesDefensivos": float,
    "porcentajeRebotes": float,
    "porcentajeAsistencias": float,
    "porcentajeRobos": float,
    "porcentajePerdidas": float,
    "porcentajeTaponesFavor": float,
    "porcentajeTaponesContra": float,
    "porcentajeMates": float,
    "porcentajeFaltasCometidas": float,
    "porcentajeFaltasRecibidas": float,
    "valoracion": float

}


def _getClase(tipoClase: str) -> dict | None:

    if tipoClase == 'Clasificacion':

        clase = Clasificacion

    elif tipoClase == 'AvanzadaEquipo':

        clase = AvanzadaEquipo

    elif tipoClase == 'AvanzadaJugador':

        clase = AvanzadaJugador

    elif tipoClase == 'TirosJugador':

        clase = TirosJugador

    elif tipoClase == 'TirosEquipo':

        clase = TirosEquipo

    elif tipoClase == 'InfluenciaBaja':

        clase = InfluenciaBaja

    elif tipoClase == 'EstadisticaACB':

        clase = EstadisticaACB

    else:

        return None
    
    return clase


def setDatosClases(tipoClase: str, rutaArchivo: str) -> list:
    
    dfClase = pd.read_csv("Datos//" + rutaArchivo + ".csv")
    listaClase: list = []

    clase = _getClase(tipoClase)


    for _, row in dfClase.iterrows():

        claseAgregar = clase
        columnas = tuple(claseAgregar.keys())
        indice = 0
    
        for dato in row:
            
            if str(dato).isnumeric():
                
                claseAgregar[columnas[indice]] = float(str(dato))

            else:

                claseAgregar[columnas[indice]] = str(dato)

            indice += 1

        listaClase.append(claseAgregar)

    return listaClase



