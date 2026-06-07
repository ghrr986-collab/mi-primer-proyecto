pasaje_base = 95000
tarjeta_base = 5000

print ("DESCUENTO DE PASAJES")

porcetaje_pasaje = 0

distancia = int(input("CUANTA DISTANCIA VA A VIAJAR: "))
categoria = int(input("QUE CATEGORIA ES SU VIAJE: "))

if distancia >= 400:
    if categoria == 1 or categoria == 2:
        porcetaje_pasaje = 0.20
    elif categoria == 3 or categoria == 4:
        porcetaje_pasaje = 0.14
elif distancia >= 200:
    if categoria == 1 or categoria == 2:
        porcetaje_pasaje = 0.12
    elif categoria == 3 or categoria == 4:
        porcetaje_pasaje = 0.08

porcetaje_tarjeta = 0

if categoria >= 1 and categoria <= 3:
    porcetaje_tarjeta = 0.10
    if distancia > 300:
        porcetaje_tarjeta = porcetaje_tarjeta + 0.05

    pasaje_final = pasaje_base * (1 - porcetaje_pasaje)
    tarjeta_final = tarjeta_base * (1 - porcetaje_tarjeta)

    print (f"EL VALOR DEL PASAJE CON LOS DESCUENTOS ES {int(pasaje_final)}")
    print (f"EL VALOR DE LA TARJETA CON LOS DECUENTOS ES {int(tarjeta_final)} ")
