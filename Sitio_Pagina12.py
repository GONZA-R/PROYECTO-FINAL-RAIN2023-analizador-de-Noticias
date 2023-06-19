import funciones


import requests
from bs4 import BeautifulSoup
def conseguir_url(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'article-item__content'}) #Segun la estructura html de la pagina
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
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


        titulo = soup.find('div', class_='section-2-col article-header')
        titulo = titulo.find('h1').text.strip()

        #obtener subtitulo de la noticia
        resumen = soup.find('div', class_='section-2-col article-header')
        resumen = resumen.find('h2').text.strip()


        div_contenido = soup.find('div', class_=['article-main-content article-text','article-main-content article-text no-main-image'])
        lista_parrafos = []


        if div_contenido:
            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')
              # Crear una lista para almacenar los párrafos
            

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


url='https://www.pagina12.com.ar/secciones/'+textobusq
lista_de_noticias=conseguir_url(url)
lista_de_noticias = list(set(lista_de_noticias))
lista_de_noticias.sort()


url_base = 'https://www.pagina12.com.ar'

lista_url_completa=[] #la url completa de las noticias va estar formado por el url base + cada link de
#la lista de noticias

print('Accediendo a todas las paginas de https://www.pagina12.com.ar ...\n')
for noticia in lista_de_noticias:
    lista_url_completa.append(url_base+noticia)
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

        # Encontrar el div con la clase "p12-dropdown-column"
    div_dropdown = soup.find('div', class_='p12-dropdown-column')

    if div_dropdown:
        # Encontrar todos los elementos <a> dentro del div
        a_tags = div_dropdown.find_all('a')

        # Extraer los textos de los elementos <a>
        listdiv = [tag.text for tag in a_tags]
        #listdiv.append(textos)
    return listdiv



elemento=list_dic_noticias[0]
print('\n'+elemento['titulo'])
print('\n')
print(elemento['contenido'])

listdiv=web_scrapping_div(url_base)

elementos_eliminar=['Buenos Aires12', 'Líbero', 'Buenos Aires12', 'Rosario12', 'Salta12', 'Catamarca12', 'La Rioja12', 'Negrx', 'Audiovisuales',
  'Plástica', 'Soci@s', 'La ventana', 'Contratapa', 'Diálogos', 'Recordatorios', 'Edición impresa']

# Eliminar los elementos de la lista
for elemento in elementos_eliminar:
    if elemento in listdiv:
        listdiv.remove(elemento)

print(listdiv)