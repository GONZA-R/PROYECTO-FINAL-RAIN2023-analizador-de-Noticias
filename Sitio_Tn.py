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
            divs = soup.find_all('div',class_= 'content-container') #Segun la estructura html de la pagina
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and  'economia' in href:
                        urls_noticias.append(href)
                            
            return urls_noticias
#####################################################################################################
import requests
from bs4 import BeautifulSoup


def web_scraping(links):
    noticias = []
    for link in links:
        url = link
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')


        titulo = soup.find('div', class_='col-content')
        if titulo:
                titulo = titulo.find('h1').text.strip()
        else:
                titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento





        #obtener subtitulo de la noticia
        resumen = soup.find('div', class_='article__headline-byline-container')
        if resumen:
                    
                resumen = resumen.find('h2').text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento



        div_contenido = soup.find('div', class_='default-article-color article__body article__article')


        # Crear una lista para almacenar los párrafos
            
        lista_parrafos = []

        if div_contenido:

            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            for parrafo in parrafos:
                texto = parrafo.get_text(strip=True)
                lista_parrafos.append(texto)

        else:
            print("No se encontró el div de contenido.")
            


        img_principales = soup.find('picture', class_='responsive-image')
  
        if img_principales:
            img_principales = img_principales.find_all('img')
        else:
            img_principales = None
        url_imagen_principal = [img['src'] for img in img_principales] if img_principales else []

        
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos,'url_imagenes':url_imagen_principal}) 
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

url='https://tn.com.ar/economia/'
lista_de_noticias=conseguir_url(url)
lista_de_noticias = list(set(lista_de_noticias))
lista_de_noticias = [noticia for noticia in lista_de_noticias if noticia is not None]
lista_de_noticias.sort()


url_base = 'https://tn.com.ar'
lista_url_completa=[] #la url completa de las noticias va estar formado por el url base + cada link de
#la lista de noticias

print('Accediendo a todas las paginas de https://tn.com.ar ...\n')
for noticia in lista_de_noticias:
    lista_url_completa.append(url_base+noticia)
#######################################################################

dic_noticias=web_scraping(lista_url_completa)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes

#contenido de los parrafos y lista de imagenes para guardar todo en un documento de texto

with open('Lista de URLs.txt', 'w') as file:#Va a guardar la lista en un archivo de texto para 
    #visualizar mejor con que links se va a trabajar
    file.write('\n'.join(lista_url_completa))



print("\nSe genero un archivo de texto...\n")

