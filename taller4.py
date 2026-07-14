veterinario = {}

def registrar_mascota():
    print("Registro de mascota")
    rut = input("Cual es su rut: ")
    if rut in veterinario:
        print("Error el rut ya esta registrado")
    else:

        especie = input("Cual es la especie de su mascota: ")
        nombre = input(f"Cual es el nombre de su {especie}: ")
        edad = input(f"Cual es la edad de {nombre}: ")
        print("Registro exitoso")
        

        veterinario[rut] = {
            "especie": especie,
            "nombre": nombre,
            "edad": edad
        }
def consultar_mascota():
    print("Mascotas")
    rut_buscador = input("Ingrese el rut por el cual esta registrado la mascota: ")
    if rut_buscador in veterinario:
        print(f"Nombre de la mascota: {veterinario[rut_buscador]['nombre']}")
    else:
        print("El rut no esta registrado")

def dar_de_alta():
    print("Dar de alta")
    rut_alta = input("Ingrese el rut del dueño de la mascota que quiera dar de alta: ")
    if rut_alta in veterinario:
        del veterinario[rut_alta]
    else:
        print("El rut no esta registrado")


def mostrar_todas():
    if not veterinario:
        print("No hay ninguna mascota registrada")
    else:
            for rut, datos in veterinario.items():
               print(f"RUT Dueño: {rut} | Nombre: {datos['nombre']} | Especie: {datos['especie']} | Edad: {datos['edad']}")



encendido = True

while encendido:

        print("Veterinario")
        print("1. Registrar mascota")
        print("2.Consultar por una mascota")
        print("3. Dar de alta a una mascota")
        print("4. Ver todas las mascotas del veterinario")
        print("5.SALIR")

        opcion = input("Seleccione una opcion: ")

        if opcion == "5":
            encendido = False
            print("Apagando el sistema")

        elif opcion == "1":
            registrar_mascota()
           