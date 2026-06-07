capacidad_maxima = 20
espacios_disponibles = 20
cont_auto = 0
cont_moto = 0
cont_camionetas = 0
acu_dinero = 0
total_vehiculos = 0
while True:
    print("1.Registro entrada vehiculo")
    print("2. Registro salida de vehiculo")
    print("3.Visualizar el estado del estacionamiento")
    print("4.Reporte general del estacionamiento")
    print("5.Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion =="5":
        print("Cerrando el sistema")
        break
    elif opcion == "1":
        print("Registro de entrada")
        if espacios_disponibles > 0:
            tipo = input("Que tipo de auto es (camioneta, auto, moto): ").lower()
            if tipo == "auto":
                cont_auto += 1
                espacios_disponibles -= 1
                print("Auto registrado con exito")
            elif tipo == "moto":
                cont_moto += 1
                espacios_disponibles -= 1
                print("Moto registrada con exito")
            elif tipo == "camioneta":
                cont_camionetas += 1
                espacios_disponibles -= 1
                print("Camioneta registrada con exito")
            else:
                print("Tipo de vehiculo no disponible")
        else:
            print("Estacionamiento lleno")
    
    elif opcion == "2":
        print("Registro de salida")
        
        tipo_de_salida = input("Que tipo de auto sale: ").lower()
        if tipo_de_salida == "auto":
            if cont_auto > 0:
                
                horas = int(input("Ingrese la cantidad de horas"))
                if horas > 0:
                    total_pagar = horas * 3000
                    cont_auto -= 1
                    espacios_disponibles += 1
                    acu_dinero += total_pagar
                    total_vehiculos += 1
                    print("--BOLETA--")
                    print(f"Tipo de vehiculo: AUTO ")
                    print(f"Horas de estacionamiento: {horas}")
                    print(f"Total a pagar: ${total_pagar}")
                    print("--GRACIAS--")

                else:
                    print("Las horas del vehiculo deben ser mayor a 0")
            else:
                print("Error, no hay autos registrados")
       
        elif tipo_de_salida == "moto":
            if cont_moto > 0:
                

                horas = int(input("Ingrese la cantidad de horas: "))
                if horas > 0:
                    total_pagar = horas * 1500
                    cont_moto -= 1
                    espacios_disponibles += 1
                    acu_dinero += total_pagar
                    total_vehiculos += 1
                    print("--BOLETA--")
                    print("Tipo de auto: Moto")
                    print(f"Horas de estancionamiento {horas}")
                    print(f"Total a pagar ${total_pagar}")
                    print("--GRACIAS--")
                else:
                    print("las horas deben ser mayor a 0")



            else:
                print("Error, mo hay motos registradas")
        elif tipo_de_salida == "camioneta":
            if cont_camionetas > 0:
                

                horas = int(input("Ingrese la cantidad de horas: "))
                if horas > 0:
                    total_pagar = horas * 4000
                    cont_camionetas -= 1
                    espacios_disponibles += 1
                    acu_dinero += total_pagar
                    total_vehiculos += 1
                    print("--BOLETA--")
                    print("Tipo de auto: Camioneta")
                    print(f"Horas de estancionamiento {horas}")
                    print(f"Total a pagar ${total_pagar}")
                    print("--GRACIAS--")
                else:
                    print("Las horas deben ser mayor a 0")
                


            else:
                print("Error, no hay camionetas registradas")
        else:
            print("Tipo de vehiculo no disponible")

    elif opcion == "3":
        print("Visualizar estado")
        estacionamientos_utilizados = capacidad_maxima - espacios_disponibles
        print(f"Estacionamientos uilizados: {estacionamientos_utilizados}")
        print(f"Espacios disponibles: {espacios_disponibles}")
        print(f"Capacidad maxima: {capacidad_maxima}")
        print("Detalle de vehiculos:")
        print(f"-Autos: {cont_auto}")
        print(f"-Motos: {cont_moto}")
        print(f"-Camionetas: {cont_camionetas}")
    
    elif opcion == "4":
        print("Reporte general")
        print(f"-Vehiculos totales: {total_vehiculos}")
        print(f"Dinero del dia de hoy: ${acu_dinero}")






    else:
        print("Opcion no valida")
