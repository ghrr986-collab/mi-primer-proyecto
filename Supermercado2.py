import random



#generador de codigo    


def generar_codigo(nombre):
    letras = ""
    contador = 0
    
    for caracter in nombre:
        if contador < 2:
            letras = letras + caracter
            contador += 1

    letras  = letras.upper()
    numero_aleatorio = random.randint(100, 999)

    codigo_final = letras + str(numero_aleatorio)
    return codigo_final





supermercado = {
    "Leche": 
                {"precio": 1100, "stock": 20, "codigo": ""},
    "Pan de molde": 
                {"precio": 2200, "stock": 15, "codigo": ""},
    "Queso laminado": 
                {"precio": 3800, "stock": 12, "codigo": ""},
    "Fideos": 
                {"precio": 850, "stock": 40, "codigo": ""},
    "Atun en conserva": 
                {"precio": 1400, "stock": 28, "codigo": ""}
}

supermercado_actualizado = {}
for clave_nombre in supermercado:
    datos_producto = supermercado[clave_nombre]
    
    
    codigo_real = generar_codigo(clave_nombre)
    datos_producto["codigo"] = codigo_real
    
    supermercado_actualizado[codigo_real] = datos_producto
    codigo_real = generar_codigo(clave_nombre)

    datos_producto["codigo"] = codigo_real

    supermercado_actualizado[codigo_real] = datos_producto       #Arreglar orden de como se mnuestran el print



#eliminar el producto, igual arreglar el orden de como se muestra


def quitar_producto(nombre):
    if nombre in supermercado:

        del supermercado[nombre]
        print(f"El producto *{nombre}* se elimino correctamente")
        print(supermercado)


    else:
        print(f"El producto *{nombre}* no se ha encontrado en la base de datos")




#mostrar el inventario disponible, arreglar la actualizacion no se muestran los porductos agregados recientemente 

def mostrar_stock(inventario):
    print("Stock de inventario")


    for nombre in inventario:
        
        stock_actual = inventario[nombre]["stock"]
        
        print(f"- {nombre}: {stock_actual} unidades")


encendido = True

while encendido:
    try:
        print("Menu de gestiones")
        print("1. Generador de codigo")
        print("2.Agregar producto")
        print("3.Quitar producto")
        print("4. Mostrar stock")
        print("5. salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "5":
            print("Cerrando el sistema")
            encendido = False
    except ValueError:
        print("Porfavor solo seleccione opciones disponibles ")
        


#Orden todavia bo arreglado

        elif opcion == "1":

            for clave_nombre in supermercado:
                
                codigo_listo = generar_codigo(clave_nombre)

                print(f"Producto: {clave_nombre} = Código asignado: {codigo_listo}")

    #Arreglado
        elif opcion == "2":
            print("Agregar producto")
            
        
            nombre_valido = False
            while not nombre_valido:
                nuevo_nombre = input("Ingrese el nombre del producto: ")
                
                
                if nuevo_nombre.isnumeric():
                    print("Error: El nombre del producto no puede ser un número. Usa letras.")
            
                elif nuevo_nombre in supermercado:
                    print("Error: el producto ya existe en la base de datos.")
            
                else:
                    nombre_valido = True 

            
            datos_validos = False
            while not datos_validos:
                try:
                    nuevo_precio = int(input("Ingrese el valor del producto: "))
                    nuevo_stock = int(input(f"Ingrese el stock de {nuevo_nombre}: "))
                    
                    datos_validos = True
                except ValueError:
                    
                    print("Error: Por favor ingresa SOLO NÚMEROS para el precio y el stock.")
        
            codigo_nuevo = generar_codigo(nuevo_nombre)
            
            supermercado[nuevo_nombre] = {
                "precio": nuevo_precio,
                "stock": nuevo_stock,
                "codigo": codigo_nuevo
            }
            
            print(f"\nEl producto '{nuevo_nombre}' fue agregado con éxito a la base de datos.")
            print("Este es el nuevo inventario de productos:")
            print("__________________________________________")
            print(supermercado)
            print("__________________________________________")
            

        elif opcion == "3":
            
            print("------Eliminar producto------")

            nombre_eliminar = input("Que producto desea eliminar: ")

            quitar_producto(nombre_eliminar)


    #Ahora si se muestran
        elif opcion == "4":

            mostrar_stock(supermercado)

        
      
