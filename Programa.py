import Datos as datos
import Predicciones as prediccion
from datetime import datetime
from os import system
import time

def _menu(estadoActualizacion: bool):

    system("cls")
    
    fecha: datetime = datetime.now()
    fechaMostrar = fecha.strftime('%d-%m-%Y')
    
    if estadoActualizacion:

        print("BIENVENIDO AL PROGRAMA\t\tFecha: " + fechaMostrar + "\n")
        print("1. Realizar prediccion")
        print("2. Predicciones automaticas")
        print("3. Lista de predicciones")
        print("4. Actualizar datos")
        print("5. Salir")

    else:

        print("BIENVENIDO AL PROGRAMA\t\tFecha: " + fechaMostrar + "\tDATOS NO ACTUALIZADOS" + "\n")
        print("1. Realizar prediccion")
        print("2. Predicciones automaticas")
        print("3. Lista de predicciones")
        print("4. Actualizar datos")
        print("5. Salir")
        
    seleccion = input()
    system("cls")
        
    if seleccion == '1' or seleccion.lower() == 'prediccion' or seleccion.lower() == 'pre':

        _prediccion()

    elif seleccion == '2' or seleccion.lower() == 'automatico' or seleccion.lower() == 'auto':

        input()

    elif seleccion == '3' or seleccion.lower() == 'lista' or seleccion.lower() == 'lis':

        _listaPredicciones()

    elif seleccion == '4' or seleccion.lower() == 'actualizar' or seleccion.lower() == 'act':

        estadoActualizacion = _actualizar()

    elif seleccion == '5' or seleccion.lower() == 'salir' or seleccion.lower() == 'sal':

        print("\t\tSALIENDO DEL SISTEMA")
        
        time.sleep(2)
        system("cls")
        
        return

    else:

        print("\t\tSELECCIONE UNA OPCION DEL MENU\n")
        time.sleep(2)

    _menu(estadoActualizacion)


def _actualizar() -> bool:

    system("cls")
    
    fecha: datetime = datetime.now()
    fechaMostrar = fecha.strftime('%d-%m-%Y')
    
    print("ACTUALIZACION DE DATOS\t\tFecha: " + fechaMostrar + "\n")
    print("\t\tActualizando datos...")
    
    try:
    
        datos.obtenerDatosGenerales(fechaMostrar)

    except Exception:
        
        system("cls")
        
        print("ACTUALIZACION DE DATOS\t\tFecha: " + fechaMostrar + "\n")
        print("\t\tError al actualizar...")
        time.sleep(3)
        
        return False        

    system("cls")

    print("ACTUALIZACION DE DATOS\t\tFecha: " + fechaMostrar + "\n")
    print("\t\tDatos actualizados")
    time.sleep(2)

    return True


def _prediccion():
    
    fecha: datetime = datetime.now()
    fechaMostrar = fecha.strftime('%d-%m-%Y')

    verificar = False

    while not verificar:

        system("cls")

        print("PREDICCION\t\tFecha: " + fechaMostrar + "\n")
        print("Equipo de Casa:")

        casa = datos.equipos(input(), 1)

        system("cls")

        if casa == 'Otro':

            print("PREDICCION\t\tFecha: " + fechaMostrar + "\n")
            print("\t\tNo se encontro el equipo...")

            time.sleep(1)
            
        else:

            verificar = True

    verificar = False

    while not verificar:
        
        system("cls")

        print("PREDICCION\t\tFecha: " + fechaMostrar + "\n")
        print("Equipo de Visitante:")

        visitante = datos.equipos(input(), 1)

        system("cls")

        if visitante == 'Otro':

            print("PREDICCION\t\tFecha: " + fechaMostrar + "\n")
            print("\t\tNo se encontro el equipo...")

            time.sleep(1)

        elif visitante == casa:

            print("PREDICCION\t\tFecha: " + fechaMostrar + "\n")
            print("\t\tEquipo asginado en Casa...")

            time.sleep(1)

        else:

            verificar = True

    print("PREDICCION\t\tFecha: " + fechaMostrar + "\n")
    print("\t\tHaciendo calculos...")

    resultado = prediccion.prediccion(fechaMostrar, casa, visitante)

    system("cls")

    ganador = datos.equipos(resultado[0], 0)
    puntaje = str(round(resultado[1], 4))

    print("PREDICCION\t\tFecha: " + fechaMostrar + "\n")
    print("\t\tGanador: " + ganador + "\n\t\tPuntaje: " + puntaje)

    input()


def _listaPredicciones():

    system("cls")

    fecha: datetime = datetime.now()
    fechaMostrar = fecha.strftime('%d-%m-%Y')
    
    print("LISTA DE PREDICCIONES\t\tFecha: " + fechaMostrar + "\n")
    
    resultados: list = datos.getPartidosResultados()

    if resultados.__len__() > 0:

        for resultado in resultados:

            print(resultado)

    else:

        print("\t\tSin Registros\n")
    
    input("\nPresione cualquier boton para continuar...")


def inicio():

    system("cls")

    print("¿DESEA ACTUALIZAR LOS DATOS?")
    print("1. Si")
    print("2. No\n")

    res = input()

    if res.lower() == '1' or res.lower() == 'si':

        estadoActualizacion: bool = _actualizar()
        _menu(estadoActualizacion)

    elif res.lower() == '2' or res.lower() == 'no':

        _menu(False)

    else:
        
        print("\t\tSELECCIONE UNA OPCION\n")
        time.sleep(2)
        
        inicio()

inicio()