from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Ruta a tu chromedriver.exe (ajustá si lo pusiste en otro lugar)
CHROMEDRIVER_PATH = "drivers/chromedriver.exe"

# Configuramos opciones del navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Pantalla grande
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Evitar detección de bot

# Iniciar el driver con las opciones
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrir Flybondi
url = "https://www.flybondi.com/"
driver.get(url)

# Esperamos unos segundos para que cargue todo
time.sleep(5)

# Mostramos el contenido HTML de la página
print(driver.page_source)

# Cerrar el navegador (podés comentar esto para ver la página abierta)
driver.quit()
