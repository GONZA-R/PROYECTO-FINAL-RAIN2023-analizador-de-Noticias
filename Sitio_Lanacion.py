import funciones
#####################################################################################################

import requests
from bs4 import BeautifulSoup
def conseguir_url(url,textobusq):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'sidebar__main'}) #Segun la estructura html de la pagina
            #los links a necesitar se encuentran en la class = d23_content-section
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href  and textobusq+'/' in href and not href.startswith('https://www.lanacion.com.ar/'+textobusq):
                    #if href and 'autos' not in href and 'campo' not in href and 'economia/' in href and not href.startswith('https://www.lanacion.com.ar/economia'):

                    #if href and 'economia/' in href:
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

        """
        titulo = soup.find('div', class_='col-12')

        if titulo:
            titulo = titulo.find('h1').text.strip()
        else:
            titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

        """
        
        titulo = soup.find('h1', class_='com-title --font-primary --sixxl --font-extra')


        if titulo:
            titulo = titulo.text.strip()
        else:
            titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento


        #obtener subtitulo de la noticia
        resumen = soup.find('h2', class_='com-subhead --bajada --m-xs-')


        if resumen:
            resumen = resumen.text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento



       



        div_contenido = soup.find('div', class_='col-deskxl-10 offset-deskxl-1 col-desksm-11')


        # Crear una lista para almacenar los párrafos
            
        lista_parrafos = []

        if div_contenido:
            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            for parrafo in parrafos:
                texto = parrafo.get_text()
                lista_parrafos.append(texto)
            pass

        else:
            print("No se encontró el div de contenido.")
            
        
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos}) 
    return noticias



#####################################################################################################
funciones.clear_screen()#Borra pantalla

textobusq=input('Ingrese el la seccion de noticias: ')#ingresar economia,politica,sociedad o algunos de la barra menos ultimas noticias

url='https://www.lanacion.com.ar/'+textobusq+'/'
lista_de_noticias=conseguir_url(url,textobusq)
lista_de_noticias = list(set(lista_de_noticias))
lista_de_noticias.sort()

url_base = 'https://www.lanacion.com.ar'

lista_url_completa=[] #la url completa de las noticias va estar formado por el url base + cada link de
#la lista de noticias

print('Accediendo a todas las paginas de https://www.lanacion.com.ar ...\n')
for noticia in lista_de_noticias:
    lista_url_completa.append(url_base+noticia)
#######################################################################

patron = 'https://www.lanacion.com.ar/'+textobusq+'/'

lista_url_completa= [url for url in lista_url_completa if url.startswith(patron)]
print(lista_url_completa)



list_dic_noticias=web_scraping(lista_url_completa)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes





for noticia in list_dic_noticias:
    resumen_actual = noticia['contenido']
    nuevo_resumen = ' '.join(resumen_actual)

    nuevo_resumen = funciones.eliminar_caracteres(nuevo_resumen)
    nuevo_resumen = nuevo_resumen.split()
    nuevo_resumen = funciones.eliminar_numeros_lista(nuevo_resumen)
    nuevo_resumen = [elemento.lower() for elemento in nuevo_resumen]
    nuevo_resumen = list(filter(None, nuevo_resumen))
    nuevo_resumen = funciones.eliminar_stopwords(nuevo_resumen)
    nuevo_resumen = funciones.eliminar_caracteres_unicos(nuevo_resumen)
    noticia['contenido'] = nuevo_resumen


elemento=list_dic_noticias[0]
print('\n'+elemento['titulo'])
print('\n')
print(elemento['contenido'])


listdiv=nombres = [
    'Últimas noticias',
    'Tránsito y transporte',
    'Clima',
    'Política',
    'Economía',
    'Dólar Hoy',
    'Propiedades',
    'El Mundo',
    'Sociedad',
    'Buenos Aires',
    'Seguridad',
    'Educación',
    'Cultura',
    'Comunidad',
    'Salud',
    'Ciencia',
    'Deportes',
    'Turismo',
    'Tecnologia'
]
print(listdiv)


