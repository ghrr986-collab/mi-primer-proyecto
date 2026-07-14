num1 = int(input("numero 1:"))
num2 = int(input("numero 2:"))
valor = 0
while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion:"))
    if opcion == 1:
        valor = num1 + num2
        print("El resultado es:", valor)
    elif opcion == 2:
        valor = num1 - num2
        print("El resultado es:", valor)
    elif opcion == 3:
        valor = num1 * num2
        print("El resultado es:", valor)
    elif opcion == 4:
        if num2 != 0:
            valor = num1 / num2
            print("El resultado es:", valor)
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opcion no valida, por favor intente de nuevo.")

