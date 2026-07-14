clave_secreta = "python123"
acceso_consedido = False
while not acceso_consedido:
    contraseña_us = input("Ingrese la contraseña: ")
    if contraseña_us == clave_secreta:
        print("¡Acceso concedido!")
        acceso_consedido = True
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
