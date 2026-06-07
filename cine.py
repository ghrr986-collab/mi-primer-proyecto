capacidad_maxima = 30
asientos_disponibles = 30
entradas_vendidas = 0
dinero_total = 0
while True:
    print("1.Venta de entradas")
    print("2. Reporte de sala")
    print("3. salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "3":
        print("Cerrando centro de ventas")
        break
    elif opcion == "1":
        print("Venta de entrada")
        if asientos_disponibles > 0:
            persona = input("Que rango es (Adulto, Niño): ").lower()
            if persona == "adulto":
                asientos_disponibles -= 1
                entradas_vendidas += 1
                dinero_total += 5000
                print("Entrada registrada con exito")
            elif persona == "niño":
                asientos_disponibles -= 1
                entradas_vendidas += 1
                dinero_total += 3000
                print("Entrada registrada con exito")
            else:
                print("Venta no disponible")
        else:
            print("Sala de cine llena")
    elif opcion == "2":
        print("Reporte de sala")
        print(f"Asientos disponibles: {asientos_disponibles}")
        print(f"Entradas vendidas en total: {entradas_vendidas}")
        print(f"Dinero total hasta ahora: {dinero_total}")
    
    else:
        print("Error, opcion invalida (seleccione de las tres porfavor)")
