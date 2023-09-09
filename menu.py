import os
import sys
import keyboard # pip install keyboard, en la terminal para descargar el import

import functions as funciones

# --------------- Limpiar consola ---------------

def limpiarConsola():  
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
    
limpiarConsola()

# ----------- Finalizar cada opción -------------

def finalizarPrograma():
    
    print("\n" + "Presiona (Ctrl) para regresar el menú. \n")
    
    while True:
        
        if keyboard.is_pressed("ctrl"):
            limpiarConsola()
            break
            mostrar_menu()

# ---------------- ------------- ----------------        

def mostrar_menu():

    print("\n" + " ------------ MENÚ DE OPCIONES ------------ ")
    print("|                                          |")
    print("|  1. Registrar usuario                    |")
    print("|  2. Rentar bicicleta                     |")
    print("|  3. Consultar listado de usuarios        |")
    print("|  4. Consultar listado de los prestamos   |")
    print("|  5. Salir                                |")
    print("|                                          |")
    print(" ---------------- ---- -------------------- \n")
    
opcion = "0"

while opcion != "5":

    mostrar_menu()
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
    
        limpiarConsola()

        print("Has seleccionado la Opción 1. ( Registrar usuario ) \n")

        funciones.registrarUsuario() # <-- Llamamos la función registrar usuarios
    
        finalizarPrograma()

    elif opcion == "2":
        
        limpiarConsola()
        
        print("Has seleccionado la Opción 2. ( Rentar bicicleta ) \n")

        funciones.registrarRenta() # <-- Llamamos la función rentar bicicletas

        finalizarPrograma()

    elif opcion == "3":
        
        limpiarConsola()
        
        print("Has seleccionado la Opción 3. ( Consultar listado de usuarios ) \n")

        funciones.consultarUsuarios() # <-- Llamamos la función ver usuarios registrados

        finalizarPrograma()
        
    elif opcion == "4":
    
        limpiarConsola()
        
        print("Has seleccionado la Opción 4. ( Consultar listado de los prestamos ) \n")

        funciones.consultarRentas() # <-- Llamamos la función ver prestamos realizados

        finalizarPrograma()
    
    elif opcion == "5":
        
        limpiarConsola()
        
        print("\n" + "Saliendo del programa... \n \n")
        sys.exit()

    else:
        
        limpiarConsola()
        
        print("\n" + "Opción no válida. Por favor, selecciona una opción del menú. \n")

# ---------------- ------------- ----------------  


    