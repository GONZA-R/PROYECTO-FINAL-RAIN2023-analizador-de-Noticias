import requests
from bs4 import BeautifulSoup

def web_scraping(links):
    noticias = []
    
    url = links
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    titulo = soup.find('div', class_='section-2-col article-header')
    titulo = titulo.find('h1').text.strip()

    #obtener subtitulo de la noticia
    resumen = soup.find('div', class_='section-2-col article-header')
    resumen = resumen.find('h2').text.strip()

    print(titulo)
    print(resumen)
            

    # Buscar el div con la clase "article-main-content article-text"
    #div_contenido = soup.find('div', class_='article-main-content article-text')
    div_contenido = soup.find('div', class_=['article-main-content article-text','article-main-content article-text no-main-image'])


    # Crear una lista para almacenar los párrafos
        
    lista_parrafos = []

    if div_contenido:
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
    
    img_principales = soup.find('div', {'class': 'section-2-col article-main-image'})
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
        #guardar_noticias(nombre_noticia,noticia)
        if i>=10:
            break
        else:
            pass
    return noticias



# Ejemplo de uso
url = 'https://www.pagina12.com.ar/557819-sin-colectivos-en-el-interior'
#url = 'https://www.pagina12.com.ar/557660-general-motors-produce-mas'
web_scraping(url)
