

#####################################################################################################
import requests
from bs4 import BeautifulSoup
def conseguir_url(url,textobusq):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'col-12 col-md-8'}) #Segun la estructura html de la pagina
            #los links a necesitar se encuentran en la class = d23_content-section
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and href.startswith('https://www.ambito.com/'+textobusq+'/'):
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


        titulo = soup.find('div', class_='col-12 col-md-8 detail-news__main-column')
        if titulo:
                titulo = titulo.find('h1').text.strip()
        else:
                titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento


        #obtener subtitulo de la noticia
        resumen = soup.find('div', class_='col-12 col-md-8 detail-news__main-column')
        if resumen:
                resumen = resumen.find('h2').text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

        div_contenido = soup.find('div', class_='col-12 col-md-8 detail-news__main-column')


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



import requests
from bs4 import BeautifulSoup

def web_scrapping_div(links):
    elementodiv=[]
    
    url = links
    response = requests.get(url)
    html = response.text
        
    # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

    soup = BeautifulSoup(html,'html.parser')

    div_contenido = soup.find_all('span', class_='drop-down-menu__navigation-link')
        
    listdiv = []

    if div_contenido:

        for div_element in div_contenido:
            elementodiv = div_element.find('a')
            texto = elementodiv.get_text(strip=True)
            listdiv.append(texto)
    else:
            print("No se encontró el div de contenido.")

    return listdiv




import funciones
funciones.clear_screen()#Borra pantalla



textobusq=input('Ingrese el la seccion de noticias: ')#ingresar economia,politica,sociedad o algunos de la barra menos ultimas noticias


url='https://www.ambito.com/contenidos/'+textobusq+'.html'
lista_de_noticias=conseguir_url(url,textobusq)
lista_de_noticias = list(set(lista_de_noticias))
lista_de_noticias = [noticia for noticia in lista_de_noticias if noticia is not None]
lista_de_noticias.sort()


print(lista_de_noticias)


url_base = 'https://www.ambito.com'
lista_url_completa=[] #la url completa de las noticias va estar formado por el url base + cada link de
#la lista de noticias

print('Accediendo a todas las paginas de https://www.ambito.com ...\n')
for noticia in lista_de_noticias:
    lista_url_completa.append(noticia)
#######################################################################


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


listdiv=web_scrapping_div(url_base)
listdiv.remove('Últimas noticias')
print(listdiv)