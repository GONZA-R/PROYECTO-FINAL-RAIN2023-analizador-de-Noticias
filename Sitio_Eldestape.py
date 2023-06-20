import funciones
import requests
from bs4 import BeautifulSoup

#####################################################################################################

def conseguir_url(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'contenedor notas_seccion_ grid'}) #Segun la estructura html de la pagina
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    urls_noticias.append(href)
                    
                            
            return urls_noticias
#####################################################################################################


def web_scraping(links,textobusq,url_base):
    noticias = []
    for link in links:
        url = link
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        titulo = soup.find('h1', class_='titulo')
        if titulo:
            titulo = titulo.text.strip()
        
        #obtener subtitulo de la noticia
        resumen = soup.find('h2', class_='intro')
        if resumen:
            resumen = resumen.text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

        div_contenido = soup.find('div', class_='nota_contenido')

        # Crear una lista para almacenar los párrafos
            
        lista_parrafos = []

        if div_contenido:

            div_no = div_contenido.find_all('div', class_='cont-boton')
            for div in div_no:
                div.decompose()

            div_no = div_contenido.find_all('div', class_='link_nota_propia')
            for div in div_no:
                div.decompose()

            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            for parrafo in parrafos:

                texto = parrafo.get_text()
                lista_parrafos.append(texto)
            pass

        else:
            print("")
            
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos,'sitio':'El Destape','url_sitio':url_base,'seccion':textobusq,'link':link}) 
        
    return noticias

#####################################################################################################
def web_scrapping_div(links):
    listdiv=[]
    url = links
    response = requests.get(url)
    html = response.text
    # O cualquier valor por defecto que desees asignar si no se encuentra el elemento
    soup = BeautifulSoup(html, 'html.parser')
    ul_elements = soup.find('ul',class_='menu menu__mobile')

    for ul in ul_elements:
        a_elements = ul.find_all('a')
        for a in a_elements:
            texto = a.text.strip()
            listdiv.append(texto)
    ul_elements = soup.find('ul',class_='menu2')

    for ul in ul_elements:
        a_elements = ul.find_all('a')
        for a in a_elements:
            texto = a.text.strip()
            listdiv.append(texto)
    # Elementos a eliminar
    elementos_eliminar = ['#ATR', 'Secciones editoriales', 'Videos', 'Radio', 'Programación']
    # Eliminar los elementos de la lista
    for elemento in elementos_eliminar:
        if elemento in listdiv:
            listdiv.remove(elemento)
    listdiv=funciones.procesar_lista(listdiv)   
    return listdiv


def obtener_lista_url_completa(url_base):
    lista_url_completa = []
    textobusq=""
    textobusq = input('\nIngrese la sección de noticias: ')###Es con el item selecionado
    url = url_base+'/seccion/' + textobusq + '/'

    lista_de_noticias = conseguir_url(url)
    lista_de_noticias = list(set(lista_de_noticias))
    lista_de_noticias.sort()

    lista_url_completa = [url_base + noticia for noticia in lista_de_noticias]
    lista_url_completa = [url for url in lista_url_completa if url.startswith('https://www.eldestapeweb.com/' + textobusq)]

    return lista_url_completa,textobusq



url_base = 'https://www.eldestapeweb.com'

lista_url_completa,textobusq = obtener_lista_url_completa(url_base)

listdiv=web_scrapping_div(url_base)

list_dic_noticias=web_scraping(lista_url_completa,textobusq,url_base)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes

funciones.procesar_noticias(list_dic_noticias)

indice_invertido = funciones.crear_indice_invertido(list_dic_noticias)

funciones.buscar_y_mostrar_noticias(indice_invertido)


