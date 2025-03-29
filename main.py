from menu import menu_principal
from funciones import validar_contra, crear_contrasena

def ejecutar_programa():
    while True:
        op = menu_principal()
    
        match op: 
            case "1":
                crear_contrasena()
            case "2":
                validar_contra()
            case "3":
                print("Hasta luego! ")
                break
            case _:
                print("Por favor ingrese una opción válida ")