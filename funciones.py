def crear_contrasena():
    global contra_almacenada
    contra_almacenada = input("Ingrese la contraseña que va a crear: ")
    print("Contraseña creada con éxito! ")

def validar_contra():
    if contra_almacenada == "":
        print("No se ha creado una contraseña aún ")
    else: 
        contra_usuario = input("Introduce la contraseña para validar: ")
        if contra_almacenada.lower() == contra_almacenada.lower():
            print("Contraseña correcta! ")
        else:
            print("Contraseña incorrecta :( ")
