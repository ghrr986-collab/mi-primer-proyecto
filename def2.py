alumnos = {}

def agregar_nuevo_alumno(nombre):
    if nombre in alumnos:
        print(f"El alumno {nombre} ya existe en el sistema")
    else:
        alumnos[nombre] = []
        print(f"El alumno ha sido registrado con exito")

def agregar_nota(nombre, nota):
    if nombre in alumnos:
        alumnos[nombre].append(nota)
        print(f"nota agregada con exito a {nombre}")
    
    else:
        print(f"Error, alumno {nombre}, no esta registrado en el sistema")


def mostrar_reporte():
    print("\n--- REPORTE DE NOTAS ---")

    if len(alumnos) == 0:
        print("Aun no hay alumnos registrados en el sistema")
        return
    
    for alumno, notas in alumnos.items():

        if len(notas) > 0:
            promedio = sum(notas) / len(notas)
            print(f"Estudiante: {alumno} | Notas: {notas} | Promedio: {promedio:.1f}")
        else:
            print(f"Estudiante: {alumno} | Notas: Sin calificaciones registradas.")



continuar = True 
try:
    while continuar:
        print("\n" + "="*25)
        print("      MENÚ PRINCIPAL")
        print("="*25)
        print("1. Agregar alumno")
        print("2. Agregar nota a un alumno")
        print("3. Mostrar reporte completo")
        print("4. Salir")

        opcion = input("Elije una opcion (del 1 al 4): ")


        if opcion == "1":
            nom = input("Ingrese el nombre del alumno: ")
            agregar_nuevo_alumno(nom)
        
        elif opcion == "2":
            nom = input("Ingresa el nombre del alumno: ")
            calificacion = float(input("Ingrese la nota: "))
            agregar_nota(nom, calificacion)
        
        elif opcion == "3":
            mostrar_reporte()

        elif opcion =="4":
            print("Saliendo del sistema")
            continuar = False

        else:
            print("opcion invalida")
except ValueError:
    print("Solo numeros porfavor")
