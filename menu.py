#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por 
# el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def menu_principal():
    menuPrincipal = """"
============================================
************ Bienvenido usuario ************
============================================
 * Por favor seleccione la opción que desea:

1. Crear una nueva contraseña
2. Validar contraseña guardada
3. Salir

============================================
"""
    print(menuPrincipal)
    return input ("Por favor ingrese su opción: ")