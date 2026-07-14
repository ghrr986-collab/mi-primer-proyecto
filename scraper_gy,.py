import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Iniciando extractor optimizado de Zen Store...")

url = "https://zenstorechile.com/collections/all"

#
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta = requests.get(url, headers=headers)
sopa = BeautifulSoup(respuesta.text, 'html.parser')


tarjetas_productos = sopa.find_all('div', class_='card__content')

lista_nombres = []
lista_precios = []

for tarjeta in tarjetas_productos:
    
    titulo_el = tarjeta.find('h3', class_='card__heading')
    
    
    precio_el = tarjeta.find('span', class_='price-item--sale')
    if not precio_el:
        precio_el = tarjeta.find('span', class_='price-item--regular')
        
    
    if titulo_el and precio_el:
        nombre_limpio = titulo_el.text.strip()
        precio_limpio = precio_el.text.strip()

        if precio_limpio and "/" not in precio_limpio and "por" not in precio_limpio:
            lista_nombres.append(nombre_limpio)
            lista_precios.append(precio_limpio)


datos = {
    'Prenda': lista_nombres,
    'Precio': lista_precios
}


tabla = pd.DataFrame(datos)
tabla = tabla.drop_duplicates()

tabla.to_excel('ropagym_zenstore_PERFECTO.xlsx', index=False)

print("¡Éxito total! Se ha generado 'ropagym_zenstore_PERFECTO.xlsx' sin desfases.")