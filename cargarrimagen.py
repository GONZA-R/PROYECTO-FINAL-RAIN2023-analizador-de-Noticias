from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

def cargar_y_visualizar_imagen(url,texto):
    # Obtener la imagen de la URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')

    # Agregar el párrafo de texto
    ax.text(0.5, -0.1, texto, transform=ax.transAxes,
            fontsize=12, color='red', ha='center')
    plt.show()


texto=('El reporte del organismo estadístico provincial señaló que la inflación acumulada en los cinco primeros meses del año'+'El reporte del organismo estadístico provincial señaló que la inflación acumulada en los cinco primeros meses del año'+'El reporte del organismo estadístico provincial señaló que la inflación acumulada en los cinco primeros meses del año'+'El reporte del organismo estadístico provincial señaló que la inflación acumulada en los cinco primeros meses del año')

url_imagen = 'https://media.ambito.com/p/e2cbce923430877155fa0be663ddc911/adjuntos/239/imagenes/035/981/0035981419/ypf-naftasjpg.jpg'
cargar_y_visualizar_imagen(url_imagen,texto)
