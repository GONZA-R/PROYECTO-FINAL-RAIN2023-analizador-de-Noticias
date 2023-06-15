import requests
from bs4 import BeautifulSoup

def web_scraping(links):
    noticias = []
    
    url = links
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    titulo = soup.find('div', class_='news-header')
    if titulo:
            titulo = titulo.find('h1').text.strip()
    else:
            titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento


    print(titulo)

    #obtener subtitulo de la noticia
    resumen = soup.find('div', class_='news-header')
    if resumen:
            """
            div_fecha = resumen.find('span', class_='detail-date')
            if div_fecha:
                div_fecha.extract()  # Eliminar el div "notapropia" del árbol del documento
            """
            
            resumen = resumen.find('h2').text.strip()
    else:
        resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento


    print(resumen)

    

    div_contenido = soup.find('div', class_='partner-wrapper article-page__body-row')
 

    # Crear una lista para almacenar los párrafos
        
    lista_parrafos = []

    if div_contenido:

    
        div_twitters = div_contenido.find_all('figure', class_='embed-container--type-twitter')
        for div_twitter in div_twitters:
            div_twitter.decompose()
        

        # Buscar todos los elementos <p> dentro del div
        parrafos = div_contenido.find_all('p')

        # Recorrer los elementos <p> y obtener el texto de cada uno
        for parrafo in parrafos:
            texto = parrafo.get_text(strip=True)
            lista_parrafos.append(texto)

        # Imprimir la lista de párrafos
        print(lista_parrafos)
    else:
        print("No se encontró el div de contenido.")
   


    img_principales = soup.find('picture', class_='news-image')
    

    if img_principales:
        img_principales = img_principales.find_all('img')
    else:
        img_principales = None
    url_imagen_principal = [img['src'] for img in img_principales] if img_principales else []
    

    print(url_imagen_principal)
    
    # Diccionario con cada elemento de la pagina a consultar
    noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos,'url_imagenes':url_imagen_principal}) 
    i=0
        # guardar archivo de texto de las 10 primeras noticias
    for noticia in noticias:
        i=i+1
        nombre_noticia='Noticia N° '+str(i)+'.txt'
        #guardar_noticias(nombre_noticia,noticia)
        if i>=10:
            break
        else:
            pass
    return noticias



# Ejemplo de uso
#url = 'https://www.pagina12.com.ar/557819-sin-colectivos-en-el-interior'
#url = 'https://www.pagina12.com.ar/557660-general-motors-produce-mas'
#url = 'https://www.lanacion.com.ar/economia/cuanto-aumentan-las-prepagas-en-julio-2023-nid13062023/'
url = 'https://www.eldiarioar.com/economia/alimentos-bebidas-aumentaron-inflacion-mensual-primera-vez-ano_1_10295845.html'
web_scraping(url)


