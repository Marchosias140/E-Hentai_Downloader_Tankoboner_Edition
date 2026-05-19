# Press F12 and selec the Console option, paste this '[...document.querySelectorAll('a')].map(a => a.href);' as it will show you all the links.

# Quick quoter with commas: ^(.*)$ then "$1" then $1,

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
import time

# Lista de URLs de galerías
urls = [



]

# Carpeta para guardar imágenes
os.makedirs("Scraped_Images", exist_ok=True)

# Inicializar navegador (ejemplo con Chrome)
driver = webdriver.Chrome()

for url in urls:
    driver.get(url)
    time.sleep(2)  # Espera breve para que cargue el contenido dinámico

    # Obtener el HTML renderizado
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Buscar todas las etiquetas <img>
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        # Manejo de URLs relativas
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = url.rstrip("/") + src

        # Filtrar por extensiones
        if src.lower().endswith((".webp", ".jpg", ".jpeg")):
            filename = os.path.join("Scraped_Images", os.path.basename(src))
            try:
                img_data = requests.get(src).content
                with open(filename, "wb") as f:
                    f.write(img_data)
                print(f"Downloaded {filename}")
            except Exception as e:
                print(f"Failed to download {src}: {e}")

# Cerrar navegador
driver.quit()