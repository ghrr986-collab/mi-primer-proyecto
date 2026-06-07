opcion = -1
import math
print("CALCULADOR ")

while opcion != 0:
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4.dividir")
    print("5.raiz cuadrada")
    print("0. salir")
    
    opcion = int(input("elige una opcion: "))
    
    if opcion == 1:
        x1 = int(input("ingrese un numero: "))
        x2 = int(input("ingrese otro numero: "))
        rel = x1 + x2
        print(f"EL RESULTADO DE {x1} + {x2} = {rel}")

    if opcion == 2:
        x1 = int(input("ingrese un numero: "))
        x2 = int(input("ingrese otro numero: "))
        rel = x1 - x2
        print(f"EL RESULTADO DE {x1} - {x2} = {rel}")
    if opcion == 3:
        x1 = int(input("ingrese un numero: "))
        x2 = int(input("ingrese otro numero: "))
        rel = x1 * x2
        print(F"EL RESULTADO DE {x1} X {x2} = {rel}")
    if opcion == 4:
        try:
            x1 = int(input("ingrese un numero: "))
            x2 = int(input("ingrese otro numero: "))
            rel = x1 / x2
            print (f"EL RESULTADO DE {x1} / {x2} = {rel}")
        
        except ZeroDivisionError:
            print(" ERROR NO SE PUEDE DIVIDIR POR 0")
    if opcion == 5:
        x = int(input("ingrese un numero: "))
        rel = math.sqrt(x)
        print(f"LA RAIZ CUADRADA DE {x} ES  {rel}")
    if opcion == 0:
        print("SALIENDO DE LA CALCULADORA")
    

