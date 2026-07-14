
import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Iniciando el rescate de datos...")


url = "http://quotes.toscrape.com/"


respuesta = requests.get(url)


sopa = BeautifulSoup(respuesta.text, 'html.parser')


citas_html = sopa.find_all('span', class_='text')
autores_html = sopa.find_all('small', class_='author')


lista_citas = []
for cita in citas_html:
    lista_citas.append(cita.text)

lista_autores = []
for autor in autores_html:
    lista_autores.append(autor.text)


datos = {
    'Frase': lista_citas,
    'Autor': lista_autores
}


tabla = pd.DataFrame(datos)
tabla.to_excel('citas_famosas.xlsx', index=False)

print("¡Listo! Revisa la carpeta donde está este script, tienes un Excel nuevo.")