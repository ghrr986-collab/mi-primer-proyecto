ing_sn = 0
ing_jr = 0
total_ing = 0
star = True
while star:
    try:
        cant_ing = int(input("Cuantos ingenieros va a registrar: "))

        if cant_ing > 0:
            star = False
        else:
            print("Error el numero tiene que ser positivo y mayor que 0")

    except ValueError:
        print("ERROR ,solo tiene que ingresar numeros porfavor")


for i in range(cant_ing):
        nombre_val = False
        while nombre_val == False:
            nombre = input("Ingrese el nombre del ingeniero: ")

            if len(nombre) > 6 and " " not in nombre:
                nombre_val = True
            else:
                print("el nombre tiene que tener un minimno de 6 letras y sin espacio")
            
        
        experiencia_val = False
        while experiencia_val == False:
            try:
                experiencia = int(input("Experiencia del ingeniero: "))
                
                if experiencia > 0:
                    experiencia_val = True
                else:
                    print("Solo numeros enteros positivos")
            except ValueError:
                print("ERROR ,solo numeros porfavor")

        
        total_ing += 1
        if experiencia > 45:
            ing_sn += 1
        else:
            ing_jr += 1

print(f"El total de ingenieros en el instituto es de {total_ing}, ingenieros senior hay {ing_sn} y ingenieros juniors hay {ing_jr} ")
