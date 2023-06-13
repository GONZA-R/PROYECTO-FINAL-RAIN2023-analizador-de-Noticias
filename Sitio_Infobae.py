############################
#Borrar pantalla
import os
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
############################

#####################################################################################################
# Funciones punto 2

import requests
from bs4 import BeautifulSoup
def conseguir_url(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'd23_content-section'}) #Segun la estructura html de la pagina
            #los links a necesitar se encuentran en la class = d23_content-section
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and 'autor' not in href and 'infobae' not in href:
                        if href and 'economia/2023' in href:
                            urls_noticias.append(href)
            return urls_noticias
#####################################################################################################
import requests
from bs4 import BeautifulSoup

def web_scrapping(links):
    noticias = []
    for link in links:
            
        url = link
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
            
        # Obtener título de la noticia
        titulo = soup.find('h1').text.strip()

        #obtener subtitulo de la noticia
        resumen = soup.find('h2').text.strip()
            
        # Obtener contenido de la noticia
        parrafos = [p.text for p in soup.find_all("p")]


        img_principales = soup.find('div', {'class': 'd23-body-article'})
        if img_principales:
            img_principales = img_principales.find_all('img')
        else:
            img_principales = None
        url_imagen_principal = [img['src'] for img in img_principales] if img_principales else []
        
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': parrafos,'url_imagenes':url_imagen_principal}) 
    i=0
        # guardar archivo de texto de las 10 primeras noticias
    for noticia in noticias:
        i=i+1
        nombre_noticia='Noticia N° '+str(i)+'.txt'
        guardar_noticias(nombre_noticia,noticia)
        if i>=10:
            break
        else:
            pass
    return noticias

#####################################################################################################
def guardar_noticias(nombre_archivo,noticia):
    with open(nombre_archivo, 'w',encoding='utf-8') as file:
        file.write('Título: \n' + noticia['titulo'] + '\n\n')
        file.write('Resumen: \n' + noticia['resumen'] + '\n\n')
        file.write('Contenido: \n\n')
        for parrafo in noticia['contenido']:
            file.write(parrafo + '\n')
        file.write('\nURLs de las imagenes:\n\n')
        for url in noticia['url_imagenes']:
            file.write(url + '\n')
        file.write('\n')
#######################################################################


clear_screen()#Borra pantalla

url = 'https://www.infobae.com/economia/'
lista_de_noticias=conseguir_url(url)
lista_de_noticias = list(set(lista_de_noticias))
lista_de_noticias.sort()


url_base = 'https://www.infobae.com'
lista_url_completa=[] #la url completa de las noticias va estar formado por el url base + cada link de
#la lista de noticias

print('Accediendo a todas las paginas de https://www.infobae.com ...\n')
for noticia in lista_de_noticias:
    lista_url_completa.append(url_base+noticia)
#######################################################################


dic_noticias=web_scrapping(lista_url_completa)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes
#contenido de los parrafos y lista de imagenes para guardar todo en un documento de texto
with open('Lista de URLs.txt', 'w') as file:#Va a guardar la lista en un archivo de texto para 
    #visualizar mejor con que links se va a trabajar
    file.write('\n'.join(lista_url_completa))


print("\nSe genero un archivo de texto...\n")

