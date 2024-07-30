import Datos as datos
from datetime import datetime
from os import system

fecha: datetime = datetime.now()
fechaMostrar = fecha.strftime('%d-%m-%Y')

def inicio():

    system("cls")

    print("BIENVENIDO AL PROGRAMA\t\tFecha: " + fechaMostrar + "\n")
    print("\t\tActualizando datos...")
    
    datos.obtenerDatosGenerales(fecha)

    print("\t\tDatos ya actualizados")
    system("cls")
    
    print("BIENVENIDO AL PROGRAMA\t\tFecha: " + fechaMostrar + "\n")
    print("1. Realizar prediccion")
    print("2. Predicciones automaticas")
    print("3. Lista de predicciones")
    print("4. Salir")

    seleccion = input()
    system("cls")
        
    if seleccion == '1' or seleccion.lower() == 'prediccion' or seleccion.lower() == 'pre':

        input()

    elif seleccion == '2' or seleccion.lower() == 'automatico' or seleccion.lower() == 'auto':

        input()

    elif seleccion == '3' or seleccion.lower() == 'lista' or seleccion.lower() == 'lis':

        input()

    elif seleccion == '4' or seleccion.lower() == 'salir' or seleccion.lower() == 'sal':

        print("\t\tSISTEMA FINALIZADO")
        
        input()
        system("cls")
        
        return

    else:

        input("\t\tSELECCIONE UNA OPCION DEL MENU\n")

    inicio()


inicio()




