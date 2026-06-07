encendido = True
ventas = {
   "Pedrito": [15000, 20000, 18000],
   "Ana": [22000, 30000],
   "Luis": [10000, 12000, 15000] 
}
while encendido:
    print("--- MENÚ DE VENTAS ---")
    print("1. Registrar venta")
    print("2. Ver ventas de un vendedor")
    print("3. Ver total vendido por vendedor")
    print("4. Mostrar vendedor con más ventas")
    print("5. Salir")

    opcion = input("Eliga una opcion: ").strip()
    if opcion == "1":
        nombre = input("Ingresa el nombre del vendedor: ")
        monto = int(input("Ingresa el monto de la venta: "))
        if nombre in ventas:
            ventas[nombre].append(monto)
        else:
            ventas[nombre] = [monto]
            print("Venta registrada con éxito.")
    elif opcion == "2":
        nombre = input("Ingresa el nombre del vendedor: ")
        if nombre in ventas:
            print("Ventas de", nombre, ":", ventas[nombre])
        else:
            print("Ese vendedor no existe.")
    elif opcion == "3":
        print("\n--- Total de ventas ---")
        for vendedor, lista_ventas in ventas.items():
            total = sum(lista_ventas)
            print(vendedor, "vendió: $", total)
    elif opcion == "4":
        mejor_vendedor = ""
        max_ventas = 0
        for vendedor, lista_ventas in ventas.items():
            total_actual = sum(lista_ventas)
            if total_actual > max_ventas:
                max_ventas = total_actual 
                mejor_vendedor = vendedor

        print("Mejor vendedor:", mejor_vendedor, "con $", max_ventas)
    elif opcion == "5":
        print("Saliendo del sistema...")
        encendido = False
        
    else:
        print("Opción no válida. Intenta de nuevo.")