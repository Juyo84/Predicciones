from bs4 import BeautifulSoup
from requests import Response
from datetime import datetime
import requests
import pandas as pd
import os

listaEquipos = [
    ('Baskonia',                'BAS', 'Baskonia'),
    ('BAXI Manresa',            'MAN', 'Baxi Manresa'),
    ('Barca',                   'FCB', 'FC Barcelona'),
    ('Bàsquet Girona',          'GIR', 'Bàsquet Girona'),
    ('Casademont Zaragoza',     'ZAR', 'Casademont Zaragoza'),
    ('Coviran Granada',         'COV', 'Covirán CB Granada'),
    ('Dreamland Gran Canaria',  'GCA', 'Gran Canaria'),
    ('Joventut Badalona',       'JOV', 'Joventut'),
    ('La Laguna Tenerife',      'CAN', 'Lenovo Tenerife'),
    ('MoraBanc Andorra',        'AND', 'MoraBanc Andorra'),
    ('Monbus Obradoiro',        'OBR', 'Monbus Obradoiro'),
    ('Real Madrid',             'RMA', 'Real Madrid'),
    ('Río Breogán',             'BRE', 'Breogán'),
    ('Surne Bilbao Basket',     'BLB', 'Bilbao Basket'),
    ('UCAM Murcia',             'MUR', 'UCAM Murcia'),
    ('Unicaja',                 'UNI', 'Unicaja'),
    ('Valencia Basket',         'VBC', 'Valencia Basket'),
    ('Zunder Palencia',         'PAL', 'Zunder Palencia')
]


def equipos(equipoCambiar: str, busqueda: int) -> str:

    for equipo in listaEquipos:
        
        for nombreEquipo in equipo:
        
            if nombreEquipo.lower() == equipoCambiar.lower():

                return equipo[busqueda]

    return ""


def _verificarResponse(response: Response) -> bool:

    if response.status_code == 200:

        return True

    return False


def _guardarDatosDefinido(response: Response, rutaArchivo: str, numeroTabla: int, numeroColuma: int,
                          fechaGuardado: str, indice: int, nombreColumnas: tuple) -> pd.DataFrame:
    
    ruta = 'Datos//' + rutaArchivo + '.csv'
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

        _guardarIndividual(datoColumn, nombreColumnas[indice], fechaGuardado, rutaArchivo)
        
    dfNuevo = pd.DataFrame(datosRow, columns=nombreColumnas)
    dfNuevo.to_csv(ruta, index=False, encoding='utf-8-sig')

    return dfNuevo


def _guardarDatosIndefinido(response: Response, rutaArchivo: str, numeroTabla: int, fechaGuardado: str, indice: int,
                            nombreColumnas: tuple) -> pd.DataFrame:

    ruta = 'Datos//' + rutaArchivo + '.csv'
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
        
        _guardarIndividual(datoColumn, nombreColumnas[indice], fechaGuardado, rutaArchivo)

    dfNuevo = pd.DataFrame(datosRow, columns=nombreColumnas)
    dfNuevo.to_csv(ruta, index=False, encoding='utf-8-sig')

    return dfNuevo


def _guardarCalendario(response: Response, rutaArchivo: str) -> pd.DataFrame:

    ruta = 'Datos//' + rutaArchivo + '.csv'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    '''
    meses = ("Sep", "Oct", "Nov",
             "Dic", "Ene", "Feb",
             "Mar", "Abr", "May",
             "Jun", "Ago")
    
    fechasInicio: str =  soup.find('div', class_='float-right fechas mayusculas').text

    mesInicial: int = 0

    for mes in meses:

        if (mes in fechasInicio):

            mesInicial = meses.index(mes)
            break
    '''
    
    partidos = soup.find_all('article', class_='partido previa')

    datosRow = []

    '''
    fechaAnterior: int = 0
    fecha: str = '00'
    '''

    for partido in partidos:

        equipoCasa: str = partido.find_all('div')[0].find('span', class_='nombre_corto').text
        equipoVisitante: str = partido.find_all('div')[5].find('span', class_='nombre_corto').text

        fecha = partido.find_all('div')[2].find_all('span')[0].text
        fecha = fecha.replace(' - ', '')
        
        '''
            fechaActual = int(fecha[-2] + fecha[-1])
            
            if fechaAnterior > fechaActual:

                mesInicial += 1

                if mesInicial > len(meses):

                    mesInicial = 0

            fecha = meses[mesInicial] + " " + fecha
        '''
        
        hora: str = partido.find_all('div')[2].find_all('span')[2].text

        datoColumn = {'Fecha': fecha, 'Hora': hora, 'Casa': equipoCasa, 'Visitante': equipoVisitante}
        datosRow.append(datoColumn)

        '''
        fechaAnterior = fechaActual
        '''

    dfNuevo = pd.DataFrame(datosRow, columns=["Fecha", "Hora", "Casa", "Visitante"])
    dfNuevo.to_csv(ruta, index=False, encoding='utf-8-sig')

    return dfNuevo
    

def _responseCalendario(ruta: str) -> pd.DataFrame:

    url = 'https://www.acb.com/calendario/'
    response = requests.get(url)

    if(_verificarResponse(response)):

        dfGuardado = _guardarCalendario(response, ruta)
        return dfGuardado

    return pd.DataFrame


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


def _guardarIndividual(datos: dict, indice: str, fecha: str, rutaArchivo: str) -> bool:
    
    columnaBusqueda = datos[indice]

    rutaJugador = 'Datos//' + rutaArchivo.replace('General', 'Jugador') + columnaBusqueda + '.csv'

    columnaBusqueda = equipos(columnaBusqueda, 1)
    rutaEquipo = 'Datos//' + rutaArchivo.replace('General', 'Equipo') + columnaBusqueda + '.csv'
    
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
    
    ruta = 'Equipos//General//Calendario_'
    _responseCalendario(ruta)

    ruta = ''
    #_responseLesionados()

    ''' DATOS REPETIDOS/INECESARIOS
    
        ruta = 'Equipos//General//TirosEquipos_'
        _responseTirosEquipos(ruta, fechaGuardado)

    '''
    
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


_responseCalendario('Equipos//General//Calendario_')