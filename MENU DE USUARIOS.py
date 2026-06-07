usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

while True:
    try:
        print("1.Menu de inicio")
        print("2.Inicio se sesion")
        print("3.Salir")


        opcion = int(input("Seleccione una opcion: "))


        if opcion == 1:

            if usuario1 is None and usuario2 is None and usuario3 is None:
                print("Error, tiene que registrar un usuario")
            else:
                registro_usuario = input("Ingrese un usuario")
                registro_contraseña = input("Ingrese la contraseña")

                if (registro_usuario == usuario1 and registro_contraseña == contraseña1) or (registro_usuario == usuario2 and registro_contraseña == contraseña2) or (registro_usuario == usuario3 and registro_contraseña == contraseña3):
                    
                    print(f"{registro_usuario}, Bienvenido")

                    while True:
                        print("Menu de usuario")
                        print("1.Realizar llamada")
                        print("2.Enviar correo")
                        print("3.Cerra sesion")

                        opcion_usuario = int(input("Seleccione un opcion: "))

                        if opcion_usuario == 1:
                            num = input("Ingrese el numero (Tiene que comenzar en 9): ")
                            if len(num) == 9 and num[0] == "9":
                                print("Llamando")
                            else:
                                print("Numero invalido")
                        
                        elif opcion_usuario == 2:
                            correo = input("Correo para: ")
                            mensaje = input("Mensaje: ")
                            arroba = False
                            for caracter in correo:
                                if caracter == "@":
                                    chek_arroba = True
                            if chek_arroba:
                                print("Mensaje enviado")  
                            else:
                                print("Correo invalido")

                        elif opcion_usuario == 3:
                            print("Saliendo del sistema")

                        else:
                            print("Opcion invalida seleccione una de las 3 porfavor")
    
    except ValueError:
        print("Error solo ingrese numeros porfavor")     

                        




