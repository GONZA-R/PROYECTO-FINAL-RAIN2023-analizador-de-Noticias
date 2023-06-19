import funciones
#####################################################################################################

import requests
from bs4 import BeautifulSoup
def conseguir_url(url,textobusq):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div',class_= ['channel__featured max-width-md','channel__wrapper max-width-md']) #Segun la estructura html de la pagina
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and href.startswith('https://www.perfil.com/noticias/'+textobusq+'/'):
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


        titulo = soup.find('div', class_='article__header max-width-md')
        if titulo:
                titulo = titulo.find('h1').text.strip()
        else:
                titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento


        #obtener subtitulo de la noticia
        resumen = soup.find('div', class_='article__header max-width-md')
        if resumen:
                    
                resumen = resumen.find('h2').text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

        div_contenido = soup.find('div', class_='article__wrapper')


        # Crear una lista para almacenar los párrafos
            
        lista_parrafos = []

        if div_contenido:

            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            for parrafo in parrafos:
                texto = parrafo.get_text()
                lista_parrafos.append(texto)

        else:
            print("No se encontró el div de contenido.")
        
        
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos}) 

    return noticias



#####################################################################################################

funciones.clear_screen()#Borra pantalla

textobusq=input('Ingrese el la seccion de noticias: ')#ingresar economia,politica,sociedad o algunos de la barra menos ultimas noticias


url='https://www.perfil.com/seccion/'+textobusq
lista_de_noticias=conseguir_url(url,textobusq)
lista_de_noticias = list(set(lista_de_noticias))
lista_de_noticias = [noticia for noticia in lista_de_noticias if noticia is not None]
lista_de_noticias.sort()


url_base = 'https://www.perfil.com/'

lista_url_completa=[] #la url completa de las noticias va estar formado por el url base + cada link de
#la lista de noticias

print('Accediendo a todas las paginas de https://www.perfil.com/ ...\n')
for noticia in lista_de_noticias:
    lista_url_completa.append(noticia)
#######################################################################
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



import requests
from bs4 import BeautifulSoup

def web_scrapping_div(links):
    listdiv=[]
    
    url = links
    response = requests.get(url)
    html = response.text
        
    # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

    soup = BeautifulSoup(html,'html.parser')

    side_menu_group = soup.find('ul', class_='side-menu__group')

    div_no = side_menu_group.find_all('ul', class_='side-menu__topics')
    for div in div_no:
        div.decompose()


    links = side_menu_group.find_all('a')

    for link in links:
        listdiv.append(link.text.strip())

    return listdiv



elemento=list_dic_noticias[0]
print('\n'+elemento['titulo'])
print('\n')
print(elemento['contenido'])

listdiv=web_scrapping_div(url_base)
#listdiv.remove('Últimas noticias')


# Elementos a eliminar
elementos_eliminar = ['Último momento', 'Ahora', 'Columnistas', 'Opinión', 
                       'CARAS', 'Exitoina', 'Videos', 'Críticas', 'Córdoba', 'Reperfilar', 'Business', 
                       'Empresas y Protagonistas', 'Noticias', 'Caras', 'Exitoina', 'Vivo', 'Caras', 'Noticias', 
                       'Weekend', 'Fortuna', 'Parabrisas', 'Rouge', 'Hombre', 'Supercampo', 'Luz', 'Look', 'Mía', 'Lunateen', 
                       'BATimes', 'Radio Perfil en vivo', 'Net', 'Canal E','Ocio']

# Eliminar los elementos de la lista
for elemento in elementos_eliminar:
    if elemento in listdiv:
        listdiv.remove(elemento)

print(listdiv)

