from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

descargas_path = os.path.abspath("descargas")
if not os.path.exists(descargas_path):
    os.makedirs(descargas_path)

chrome_options = Options()
prefs = {
    "download.default_directory": descargas_path,
    "download.prompt_for_download": False,
    "directory_upgrade": True
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/upload-download")
driver.maximize_window()

file_path = os.path.abspath("holamundo.txt")
with open("holamundo.txt", "w") as f:
    f.write("Contenido de prueba para subir")

driver.find_element(By.ID, "uploadFile").send_keys(file_path)
time.sleep(1)

driver.find_element(By.ID, "downloadButton").click()
time.sleep(3)

driver.quit()

print(f"Archivo descargado en: {descargas_path}")

