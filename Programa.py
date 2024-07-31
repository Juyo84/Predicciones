import Datos as datos
from datetime import datetime
from os import system
import time

fecha: datetime = datetime.now()
fechaMostrar = fecha.strftime('%d-%m-%Y')

def menu():

    system("cls")

    print("BIENVENIDO AL PROGRAMA\t\tFecha: " + fechaMostrar + "\n")
    print("1. Realizar prediccion")
    print("2. Predicciones automaticas")
    print("3. Lista de predicciones")
    print("4. Actualizar datos")
    print("5. Salir")

    seleccion = input()
    system("cls")
        
    if seleccion == '1' or seleccion.lower() == 'prediccion' or seleccion.lower() == 'pre':

        input()

    elif seleccion == '2' or seleccion.lower() == 'automatico' or seleccion.lower() == 'auto':

        input()

    elif seleccion == '3' or seleccion.lower() == 'lista' or seleccion.lower() == 'lis':

        input()

    elif seleccion == '4' or seleccion.lower() == 'actualizar' or seleccion.lower() == 'act':

        actualizar()

    elif seleccion == '5' or seleccion.lower() == 'salir' or seleccion.lower() == 'sal':

        print("\t\tSALIENDO DEL SISTEMA")
        
        time.sleep(2)
        system("cls")
        
        return

    else:

        print("\t\tSELECCIONE UNA OPCION DEL MENU\n")
        time.sleep(2)

    menu()


def actualizar():

    system("cls")

    print("BIENVENIDO AL PROGRAMA\t\tFecha: " + fechaMostrar + "\n")
    print("\t\tActualizando datos...")
    
    datos.obtenerDatosGenerales(fechaMostrar)

    system("cls")

    print("BIENVENIDO AL PROGRAMA\t\tFecha: " + fechaMostrar + "\n")
    print("\t\tDatos actualizados")
    time.sleep(2)


def inicio():

    actualizar()
    menu()


inicio()
