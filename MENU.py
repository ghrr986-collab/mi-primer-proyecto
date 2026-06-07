usuario1 = None
contraseña = None

star_menu = True

while star_menu:

    try:
        print("1. Iniciar Sesión")
        print("2. Registrar Usuario")
        print("3. Apagar Sistema")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 3:
            print("Apagando el sistema")
            star_menu = False

        elif opcion == 2:
            print("REGISTRO DE USUARIO")
            usuario1 = input("Nombre de usuario: ")
            contraseña = input("Ingrse contraseña: ")
            print("Registro completado con exito")
        
        elif opcion == 1:
            if usuario1 is None:
                print("Porfavor registre a un usuario y una contraseña")
            else:
                print("INICIO DE SESION")
                intentos = 0

                while intentos < 3:
                    login_usuario = input("Ingrese su nombre de usuario: ")
                    pwd_login = input("Porfavor ingrese su contraseña: ")
                    if login_usuario == usuario1 and pwd_login == contraseña:
                        print("Inicio de sesion exitoso")
                        
                        while True:
                            print("Menu de opciones")
                            print("1.Enviar mails")
                            print("2.Hacer llamadas")
                            print("3.Cerra sesion")

                            op_menu = input("Seleccione una opcion: ")
                            if op_menu == "3":
                                print("Cerrando sesion")
                                break

                            elif op_menu == "1":
                                correo = input("Que destinatario tiene este mail")
                                if "@" in correo:
                                    print("Mail verificado con exito")
                                else:
                                    print("falta el @ en el destinatario")
                            
                            elif op_menu == "2":
                                numero = input("Digite el numero al que desea llamar")
                                if len(numero) == 8:
                                    print(f"Llamando a {numero}")
                                else:
                                    print("El numero tiene que tener 8 digitos ")


                        break
                    else:
                        intentos += 1
                        print("Los datos son incorrectos")
                if intentos == 3:
                    print("Sesion bloqueada por seguridad")
                    star_menu = False

        else:
            print("Seleccione una opcion del uno al tres porfavor")
    
    except ValueError:
        print("Error critico, porfavor solo ingrese solo numero y letras permitidas")