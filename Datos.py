import Clases as clase
from bs4 import BeautifulSoup
from requests import Response
from datetime import datetime
import requests
import pandas as pd
import os

def equipos(nombre: str, abreviadas: str):

    equipos = [
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

    for equipo in equipos:
        
        if equipo[0] == nombre:

            return equipo[1] 

        if equipo[1] == abreviadas:

            return equipo[0]

    return ""


def _verificarResponse(response: Response):

    if response.status_code == 200:

        return True

    return False


def _guardarDatosDefinido(response: Response, rutaArchivo: str, numeroTabla: int, numeroColuma: int,
                          fechaGuardado: str, nombreColumnas: tuple):
    
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
        indice = 0

        for column in row.find_all('td'):

            dato = column.text.replace('\xa0', '')
            dato = dato.replace('%', '')
            dato = dato.replace(',', '.')
            dato = dato.replace('\n', '')
            dato = dato.replace('  ', '')

            datoColumn[nombreColumnas[indice]] = dato
            indice += 1
        
        datosRow.append(datoColumn)

        guardarIndividual(datoColumn, nombreColumnas[0], fechaGuardado, rutaArchivo)
        
    dfNuevo = pd.DataFrame(datosRow, columns=nombreColumnas)
    dfNuevo.to_csv(ruta, index=False, encoding='utf-8-sig')

    return dfNuevo


def _guardarDatosIndefinido(response: Response, rutaArchivo: str, numeroTabla: int, fechaGuardado: str,
                            nombreColumnas: tuple):

    ruta = 'Datos//' + rutaArchivo + fechaGuardado + '.csv'
    soup = BeautifulSoup(response.text, 'html.parser')

    tabla = soup.find_all('table')[numeroTabla]

    datos = tabla.find('tbody').find_all('tr')
    
    datosRow = []

    for row in datos:
        
        datoColumn = {}
        indice = 0

        for column in row.find_all('td'):

            dato = column.text.replace('\xa0', '')
            dato = dato.replace('%', '')
            dato = dato.replace(',', '.')
            dato = dato.replace('\n', '')
            dato = dato.replace('  ', '')

            datoColumn[nombreColumnas[indice]] = dato
            indice += 1

        datosRow.append(datoColumn)
        
        guardarIndividual(datoColumn, nombreColumnas[0], fechaGuardado, rutaArchivo)

    dfNuevo = pd.DataFrame(datosRow, columns=nombreColumnas)
    dfNuevo.to_csv(ruta, index=False, encoding='utf-8-sig')

    return dfNuevo


def _responseEstadisticaAvzJugadores(ruta: str, fechaGuardado: datetime):

    url = 'https://www.rincondelmanager.com/smgr/avanzadas.php'
    response = requests.get(url)

    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 3, 0, fechaGuardado, ())
        return dfGuardado

    return False


def _responseTirosJugadores(ruta: str, fechaGuardado: datetime):

    url = 'https://www.rincondelmanager.com/smgr/porcentajes_tiro.php'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 3, 1, fechaGuardado, ('Jug', 'Jugador', 'Eq'))
        return dfGuardado

    return False


def _responseEstadisticaAvzEquipos(ruta: str, fechaGuardado: datetime):

    url = 'https://www.rincondelmanager.com/smgr/avanzadas_equipo.php'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 0, 0, fechaGuardado, ())
        return dfGuardado

    return False


def _responseTirosEquipos(ruta: str, fechaGuardado: datetime):

    url = 'https://www.rincondelmanager.com/smgr/porcentajes_tiro_equipo.php'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosDefinido(response, ruta, 0, 1, fechaGuardado, ("Eq",))
        return dfGuardado

    return False


def _responseClasificacion(ruta: str, fechaGuardado: datetime):

    url = 'https://www.sport.es/resultados/baloncesto/acb/clasificacion-liga.html'
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        dfGuardado = _guardarDatosIndefinido(response, ruta, 2, fechaGuardado, ('Equipo', 'PJ', 'PG', 'PP', 'PF', 'PC', 'DIF'))
        return dfGuardado

    return False


def _responseLesionados(ruta: str, fechaGuardado: datetime):

    url = ''
    response = requests.get(url)
    
    if(_verificarResponse(response)):

        #_guardarDatosDefinido()
        return True

    return False


def responseInfluenciaBajaJugador(nombreJugador: str, fecha: str):

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

    return False


def setDatosClases(clase: clase, rutaArchivo: str):
    
    dfClase = pd.read_csv("Datos//" + rutaArchivo + ".csv")
    listaClase: list = []
    
    for _, row in dfClase.iterrows():
        
        datosRow = tuple(row)
        claseAgregar = clase()

        claseAgregar.setDatos(datosRow)
        listaClase.append(claseAgregar)

    return listaClase


def obtenerDatosGenerales(fechaGuardado: str):
    
    ruta = 'Jugadores//Fecha//EstadisticaAvanzadaJugadores_'
    _responseEstadisticaAvzJugadores(ruta, fechaGuardado)

    ruta = 'Jugadores//Fecha//TirosJugadores_'
    _responseTirosJugadores(ruta, fechaGuardado)

    ruta = 'Equipos//Fecha//EstadisticaAvanzadaEquipos_'
    _responseEstadisticaAvzEquipos(ruta, fechaGuardado)

    ruta = 'Equipos//Fecha//TirosEquipos_'
    _responseTirosEquipos(ruta, fechaGuardado)

    ruta = 'Equipos//Fecha//Clasificacion_'
    _responseClasificacion(ruta, fechaGuardado)
    
    #_responseLesionados()


def guardarIndividual(datos: dict, indice: str, fecha: str, rutaArchivo: str):
    
    columnaBusqueda = datos[indice]

    rutaJugador = 'Datos//' + rutaArchivo.replace('Fecha', 'Jugador') + columnaBusqueda + '.csv'
    rutaEquipo = 'Datos//' + rutaArchivo.replace('Fecha', 'Equipo') + columnaBusqueda + '.csv'

    dfGeneral: pd.DataFrame

    if os.path.exists(rutaEquipo):

        dfGeneral = pd.read_csv(rutaEquipo)
        rutaGuardado = rutaEquipo
    
    elif os.path.exists(rutaJugador):

        dfGeneral = pd.read_csv(rutaJugador)
        rutaGuardado = rutaJugador

    else:

        datos[indice] = fecha
        registro = pd.DataFrame([datos])
        datos[indice] = columnaBusqueda

        if rutaArchivo.find('Jugadores') == 0:

            rutaGuardado = rutaJugador

        elif rutaArchivo.find('Equipos') == 0:

            rutaGuardado = rutaEquipo

        else:

            return
        
        registro.to_csv(rutaGuardado, index=False)
        return
    
    datos[indice] = fecha
    registro = pd.DataFrame([datos])
    datos[indice] = columnaBusqueda
    
    registro = pd.concat([dfGeneral, registro], ignore_index=True)
    registro.to_csv(rutaGuardado, index=False)


