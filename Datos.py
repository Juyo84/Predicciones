from bs4 import BeautifulSoup
from requests import Response
from datetime import datetime
import requests
import pandas as pd
import os

listaEquipos = [
        ("Unicaja", "UNI"),
        ("Real Madrid", "RMA"),
        ("FC Barcelona", "FCB"),
        ("Valencia Basket", "VAL"),
        ("UCAM Murcia", "MUR"),
        ("Lenovo Tenerife", "TFE"),
        ("Gran Canaria", "GCA"),
        ("Baxi Manresa", "MAN"),
        ("Baskonia", "BAS"),
        ("Joventut", "JOV"),
        ("MoraBanc Andorra", "AND"),
        ("Casademont Zaragoza", "ZAR"),
        ("Bilbao Basket", "BIL"),
        ("Bàsquet Girona", "GIR"),
        ("Covirán CB Granada", "GRA"),
        ("Breogán", "BRE"),
        ("Monbus Obradoiro", "OBR"),
        ("Zunder Palencia", "PAL")
    ]


def equipos(nombre: str, abreviadas: str) -> str:

    for equipo in listaEquipos:
        
        if equipo[0] == nombre:

            return equipo[1] 

        if equipo[1] == abreviadas:

            return equipo[0]

    return ""


def _verificarResponse(response: Response) -> bool:

    if response.status_code == 200:

        return True

    return False


def _guardarDatosDefinido(response: Response, rutaArchivo: str, numeroTabla: int, numeroColuma: int,
                          fechaGuardado: str, indice: int, nombreColumnas: tuple) -> pd.DataFrame:
    
    ruta = 'Datos//' + rutaArchivo + fechaGuardado + '.csv'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tabla = soup.find_all('table')[numeroTabla]

    columnas = tabla.find('thead').find_all('tr')[numeroColuma].find_all('th')
    datos = tabla.find('tbody').find_all('tr')

    for columna in columnas:

        nombreColumnas += (columna.text,)
    
    datosRow = []

    for row in datos:
        
        datoColumn = {}
        index = 0

        for column in row.find_all('td'):

            dato = column.text.replace('\xa0', '')
            dato = dato.replace('%', '')
            dato = dato.replace(',', '.')
            dato = dato.replace('\n', '')
            dato = dato.replace('  ', '')

            datoColumn[nombreColumnas[index]] = dato
            index += 1
        
        datosRow.append(datoColumn)

        guardarIndividual(datoColumn, nombreColumnas[indice], fechaGuardado, rutaArchivo)
        
    dfNuevo = pd.DataFrame(datosRow, columns=nombreColumnas)
    dfNuevo.to_csv(ruta, index=False, encoding='utf-8-sig')

    return dfNuevo


def _guardarDatosIndefinido(response: Response, rutaArchivo: str, numeroTabla: int, fechaGuardado: str, indice: int,
                            nombreColumnas: tuple) -> pd.DataFrame:

    ruta = 'Datos//' + rutaArchivo + fechaGuardado + '.csv'
    soup = BeautifulSoup(response.text, 'html.parser')

    tabla = soup.find_all('table')[numeroTabla]

    datos = tabla.find('tbody').find_all('tr')
    
    datosRow = []
    
    for row in datos:
        
        datoColumn = {}
        index = 0

        for column in row.find_all('td'):

            dato = column.text.replace('\xa0', '')
            dato = dato.replace('%', '')
            dato = dato.replace(',', '.')
            dato = dato.replace('\n', '')
            dato = dato.replace('  ', '')
            
            datoColumn[nombreColumnas[index]] = dato
            index += 1

        datosRow.append(datoColumn)
        
        guardarIndividual(datoColumn, nombreColumnas[indice], fechaGuardado, rutaArchivo)

    dfNuevo = pd.DataFrame(datosRow, columns=nombreColumnas)
    dfNuevo.to_csv(ruta, index=False, encoding='utf-8-sig')

    return dfNuevo


def _responseEstadisticaAvzJugadores(ruta: str, fechaGuardado: datetime) -> pd.DataFrame:

    url = 'https://www.rincondelmanager.com/smgr/avanzadas.php'
    response = requests.get(url)

    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 3, 0, fechaGuardado, 0, ())
        return dfGuardado

    return pd.DataFrame


def _responseTirosJugadores(ruta: str, fechaGuardado: datetime) -> pd.DataFrame:

    url = 'https://www.rincondelmanager.com/smgr/porcentajes_tiro.php'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 3, 1, fechaGuardado, 0, ('Jug', 'Jugador', 'Eq'))
        return dfGuardado

    return pd.DataFrame


def _responseEstadisticaAvzEquipos(ruta: str, fechaGuardado: datetime) -> pd.DataFrame:

    url = 'https://www.rincondelmanager.com/smgr/avanzadas_equipo.php'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 0, 0, fechaGuardado, 0, ())
        return dfGuardado

    return pd.DataFrame


def _responseTirosEquipos(ruta: str, fechaGuardado: datetime) -> pd.DataFrame:

    url = 'https://www.rincondelmanager.com/smgr/porcentajes_tiro_equipo.php'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 0, 1, fechaGuardado, 0, ("Eq",))
        return dfGuardado

    return pd.DataFrame


def _responseClasificacion(ruta: str, fechaGuardado: datetime) -> pd.DataFrame:

    url = 'https://www.sport.es/resultados/baloncesto/acb/clasificacion-liga.html'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosIndefinido(response, ruta, 2, fechaGuardado, 0, ('Equipo', 'PJ', 'PG', 'PP', 'PF', 'PC', 'DIF'))
        return dfGuardado

    return pd.DataFrame


def _responseLesionados(ruta: str, fechaGuardado: datetime) -> pd.DataFrame:

    url = ''
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        #_guardarDatosDefinido()
        return True

    return pd.DataFrame


def _responseEstadisticaACB(ruta: str, temporada: int, fechaGuardado: datetime) -> pd.DataFrame:
    
    url = 'https://www.acb.com/estadisticas-equipos/valoracion/temporada_id/' + str(temporada)
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosIndefinido(response, ruta, 0, fechaGuardado, 1, ("PosVal", "Equipo", "PJ", "Min", "PT%", "T3C", "T3I", "T3%", "T2C", "T2I", "T2%", "T1C", "T1I", "T1%", "RbOf%", "RbDf%", "RbT%", "Asi%", "Rob%", "Per%", "TapF%", "TapC%", "Mates%", "FaltasC%", "FaltasR%", "Val"))
        return dfGuardado

    return pd.DataFrame


def responseInfluenciaBajaJugador(nombreJugador: str, fecha: str) -> pd.DataFrame:

    nombre = nombreJugador.split(" ")
    
    url = 'https://www.rincondelmanager.com/smgr/baja.php?nombre=' + nombre[0] + '%20' + nombre[1]
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosIndefinido(response, "Jugadores//Lesionados//InflueciaBaja" + nombreJugador + "_" + fecha, 0,
                                                                                    ("Jugador", "Minutos sin el",
                                                                                    "Minutos con el", "Minutos dif",
                                                                                    "Anotacion sin el", "Anotacion con el",
                                                                                    "Anotacion dif", "Valoracion con el",
                                                                                    "Valoracion sin el", "Valoracion dif"))
        return dfGuardado

    return pd.DataFrame


def obtenerDatosGenerales(fechaGuardado: str) -> bool:
    
    temporada: int

    fecha: datetime = datetime.strptime(fechaGuardado, "%d-%m-%Y")
    fechaInicio: datetime = datetime(fecha.year, 9, 1)

    if fecha >= fechaInicio:
    
        temporada = fecha.year

    else:

        temporada = fecha.year - 1

    ruta = 'Jugadores//General//EstadisticaAvanzadaJugadores_'
    _responseEstadisticaAvzJugadores(ruta, fechaGuardado)

    ruta = 'Jugadores//General//TirosJugadores_'
    _responseTirosJugadores(ruta, fechaGuardado)

    ruta = 'Equipos//General//EstadisticaAvanzadaEquipos_'
    _responseEstadisticaAvzEquipos(ruta, fechaGuardado)

    ruta = 'Equipos//General//Clasificacion_'
    _responseClasificacion(ruta, fechaGuardado)
    
    ruta = 'Equipos//General//EstadisticaACB_'
    _responseEstadisticaACB(ruta, 2023, fechaGuardado)
    
    ruta = ''
    #_responseLesionados()

    ''' DATOS REPETIDOS/INECESARIOS
    
        ruta = 'Equipos//General//TirosEquipos_'
        _responseTirosEquipos(ruta, fechaGuardado)

    '''
    
    return True


def guardarIndividual(datos: dict, indice: str, fecha: str, rutaArchivo: str) -> bool:
    
    columnaBusqueda = datos[indice]
    
    rutaEquipo = 'Datos//' + rutaArchivo.replace('General', 'Equipo') + columnaBusqueda + '.csv'
    rutaJugador = 'Datos//' + rutaArchivo.replace('General', 'Jugador') + columnaBusqueda + '.csv'
    
    dfGeneral: pd.DataFrame

    datos[indice] = fecha
    registro = pd.DataFrame([datos])
    datos[indice] = columnaBusqueda
    
    if os.path.exists(rutaEquipo):
        
        dfGeneral = pd.read_csv(rutaEquipo)
        rutaGuardado = rutaEquipo
    
    elif os.path.exists(rutaJugador):

        dfGeneral = pd.read_csv(rutaJugador)
        rutaGuardado = rutaJugador

    else:

        if rutaArchivo.find('Jugadores') == 0:

            rutaGuardado = rutaJugador

        elif rutaArchivo.find('Equipos') == 0:

            rutaGuardado = rutaEquipo

        else:

            return False
        
        registro.to_csv(rutaGuardado, index=False)

        return True
    
    if fecha in dfGeneral[indice].values:

        for columna in dfGeneral.columns:
            
            tipo_columna = dfGeneral[columna].dtype

            if pd.api.types.is_float_dtype(tipo_columna):
                
                valor = float(registro[columna].iloc[0])

            elif pd.api.types.is_integer_dtype(tipo_columna):

                valor = int(registro[columna].iloc[0])

            elif pd.api.types.is_string_dtype(tipo_columna):

                valor = str(registro[columna].iloc[0])

            else:

                valor = registro[columna].iloc[0]
            
            dfGeneral.loc[dfGeneral[indice] == fecha, columna] = valor
            dfGeneral.to_csv(rutaGuardado, index=False)

    else:

        registro = pd.concat([dfGeneral, registro], ignore_index=True)
        registro.to_csv(rutaGuardado, index=False)

    return True


def guardarPartido(fecha: datetime, casa: str, casaPuntaje: float, casaPorcentaje: float,
                   visitante: str, visitantePuntaje: float, visitantePorcentaje: float,
                   ganadorPrediccion: str) -> bool:

    rutaBusqueda = 'Datos//Resultados//Resultados.csv'

    datosPartido: dict = {"Fecha": fecha,
                          "Casa": casa,
                          "Casa Puntaje": casaPuntaje,
                          "Casa Porcentaje": casaPorcentaje,
                          "Visitante": visitante,
                          "Visitante Puntaje" : visitantePuntaje,
                          "Visitante Porcentaje" : visitantePorcentaje,
                          "Ganador Prediccion" : ganadorPrediccion,
                          "Ganador Final" : "POR ASIGNAR",
                          "Ganancia": -1}
    
    dfNuevo = pd.DataFrame([datosPartido])

    if os.path.exists(rutaBusqueda):
        
        dfExistente = pd.read_csv(rutaBusqueda)
        datosActualizados = pd.concat([dfExistente, dfNuevo], ignore_index=True)
        datosActualizados.to_csv(rutaBusqueda, index=False)
    
    else:

        dfNuevo.to_csv(rutaBusqueda, index=False)
    
    return True


def guardarGanador(fecha: datetime, casa: str, visitante: str, ganadorFinal: str) -> bool:
    
    rutaBusqueda = "Datos//Resultados//Resultados.csv"
    
    if not os.path.exists(rutaBusqueda):
    
        return False


    porcentajePrediccion: float
    ganancias: float
    dfExistente: pd.DataFrame = pd.read_csv(rutaBusqueda)

    ganadorPrediccion: str = dfExistente.loc[(dfExistente["Fecha"] == fecha) & (dfExistente["Casa"] == casa) & (dfExistente["Visitante"] == visitante) & (dfExistente["Ganador Final"] == "POR ASIGNAR"),
                                             "Ganador Prediccion"][0]

    if ganadorPrediccion == ganadorFinal:

        if ganadorPrediccion == casa:

            porcentajePrediccion = dfExistente.loc[(dfExistente["Fecha"] == fecha) & (dfExistente["Casa"] == casa) & (dfExistente["Visitante"] == visitante) & (dfExistente["Ganador Final"] == "POR ASIGNAR"),
                                                   "Casa Porcentaje"][0]

        elif ganadorPrediccion == visitante:

            porcentajePrediccion = dfExistente.loc[(dfExistente["Fecha"] == fecha) & (dfExistente["Casa"] == casa) & (dfExistente["Visitante"] == visitante) & (dfExistente["Ganador Final"] == "POR ASIGNAR"),
                                                   "Visitante Porcentaje"][0]

        else:

            return False

    else:
        
        porcentajePrediccion = 0

        return

    ganancias = porcentajePrediccion * 100

    dfExistente.loc[(dfExistente["Fecha"] == fecha) & (dfExistente["Casa"] == casa) & (dfExistente["Visitante"] == visitante) & (dfExistente["Ganador Final"] == "POR ASIGNAR"),
                    "Ganancia"] = ganancias
    dfExistente.loc[(dfExistente["Fecha"] == fecha) & (dfExistente["Casa"] == casa) & (dfExistente["Visitante"] == visitante) & (dfExistente["Ganador Final"] == "POR ASIGNAR"),
                    "Ganador Final"] = ganadorFinal
    
    dfActualizado = pd.DataFrame(dfExistente)
    dfActualizado.to_csv(rutaBusqueda, index=False)

    return True


def getPartidosResultados() -> list:

    rutaBusqueda: str = "Datos//Resultados//Resultados.csv"
    dfBusqueda: pd.DataFrame
    partidos: list = []

    indice = 0

    if not os.path.exists(rutaBusqueda):

        return partidos

    dfBusqueda = pd.read_csv(rutaBusqueda)
    dfBusqueda = dfBusqueda.loc[(dfBusqueda["Ganador Final"] != "POR ASIGNAR")]

    partidos = dfBusqueda.values.tolist()

    for partido in partidos:

        datoString = partido[0] + "\t" + partido[1] + "\t" + str(partido[2]) + "\t" + str(partido[3]) + "\t" + partido[4] + "\t" + str(partido[5]) + "\t\t" + str(partido[6]) + "\t\t" + partido[7] + "\t\t" + partido[8] + "\t\t" + str(partido[9])

        partidos[indice] = datoString
        indice += 1

    partidos = ["Fecha\t\tCasa\t# Casa\t% Casa\tVisita\t# Visita\t% Visita\tPrediccion\tGanador\t\tGanancia"] + partidos

    return partidos


