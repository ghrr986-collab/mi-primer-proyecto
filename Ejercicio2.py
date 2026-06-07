habitaciones_disponibles = 50
ht_oc = 0
star = True


while star:
    try:    
        print("===MENÚ PRINCIPAL===")
        print("1. Habitaciones disponibles")
        print("2. Realizar check-in")
        print("3. Realizar check-out")
        print("4. historial de ocupaciones")
        print("5. Salir")
        opcion = int(input("Seleccione una opcion: "))
        
        
            
        if opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima")
            star = False
        elif opcion == 1:
            print(f"Habitaciones disponible {habitaciones_disponibles}")
                
        elif opcion == 2:
            h_usada = int(input("¿Cauntas habitaciones desea reservar?: "))
            if h_usada > 0 and h_usada <= habitaciones_disponibles:
                print("El registro se completo con exito")
                habitaciones_disponibles -= h_usada
                ht_oc += h_usada
            else:
                print("El numero tiene que ser positivo y mayor a 0 y aparte no tiene que superar el numero total de habitaciones")

        elif opcion == 3:
            c_habitaciones = int(input("Cuantas habitaciones desea cancelar: "))
            if c_habitaciones > 0 and c_habitaciones <= ht_oc:
                print("Se cancelo exitosamente ")
                habitaciones_disponibles += c_habitaciones
                ht_oc -= c_habitaciones
        elif opcion == 4:
            print(f"Total de ocupacion de habitaciones {ht_oc}")

        else:
                print("Seleccione una opcion valida (1,2,3,4,5)")        
    except ValueError:
        print("Error critico, solo numeros y opciones disponibles porfavor")