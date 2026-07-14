def validar_lista_numeros():
    while True:
        try:
            
            entrada = input("Ingrese una lista de números enteros separados por espacios: ")
            elementos = entrada.split()


            if elementos:
                numeros_enteros = [int(item) for item in elementos]
                return numeros_enteros
            else:
                print("La lista no puede estar vacía. Intente nuevamente")

        except ValueError:
            print("Error")
            
def clasificar_pares_impares(lista_numeros):
    pares = []
    impares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)

        else:
            impares.append(numero)
    return pares, impares
if __name__ == "__main__":
    lista_validada = validar_lista_numeros()
    
    lista_pares, lista_impares = clasificar_pares_impares(lista_validada)
    print(" Resultados del Programa ")
    print(f"Números pares identificados: {lista_pares}")
    print(f"Números impares identificados: {lista_impares}")
