import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

class TestDemoQA(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        headless_mode = False  # Cambia a True si quieres que corra sin abrir ventana
        if headless_mode:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_formulario_registro_usuario(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        driver.find_element(By.ID, "firstName").send_keys("Juan")
        driver.find_element(By.ID, "lastName").send_keys("Pérez")
        driver.find_element(By.ID, "userEmail").send_keys("juanperez@test.com")
        driver.find_element(By.XPATH, "//label[text()='Male']").click()
        driver.find_element(By.ID, "userNumber").send_keys("1234567890")
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        modal_title = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
        self.assertIn("Thanks for submitting the form", modal_title)

    def test_carga_y_descarga_archivo(self):
        driver = self.driver
        driver.get("https://demoqa.com/upload-download")

        # Crear archivo temporal
        file_path = os.path.abspath("holamundo.txt")
        with open(file_path, "w") as f:
            f.write("Contenido de prueba para subir")

        # Subir archivo
        driver.find_element(By.ID, "uploadFile").send_keys(file_path)
        uploaded_text = driver.find_element(By.ID, "uploadedFilePath").text
        self.assertIn("holamundo.txt", uploaded_text)

        # Descargar archivo
        driver.find_element(By.ID, "downloadButton").click()
        time.sleep(2)  # Espera a que se descargue

    def test_alertas(self):
        driver = self.driver
        wait = self.wait
        driver.get("https://demoqa.com/alerts")

        # Alerta simple
        driver.find_element(By.ID, "alertButton").click()
        try:
            wait.until(EC.alert_is_present())
            driver.switch_to.alert.accept()
        except TimeoutException:
            self.fail("❌ La alerta simple no apareció.")

        # Alerta con retardo
        driver.find_element(By.ID, "timerAlertButton").click()
        try:
            wait.until(EC.alert_is_present())
            driver.switch_to.alert.accept()
        except TimeoutException:
            self.fail("❌ La alerta con retardo no apareció.")

        # Alerta de confirmación
        driver.find_element(By.ID, "confirmButton").click()
        try:
            wait.until(EC.alert_is_present())
            driver.switch_to.alert.dismiss()
        except TimeoutException:
            self.fail("❌ La alerta de confirmación no apareció.")

        # Alerta tipo prompt
        driver.find_element(By.ID, "promtButton").click()
        try:
            wait.until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.send_keys("Hola Mundo")
            alert.accept()
            resultado = driver.find_element(By.ID, "promptResult").text
            self.assertIn("Hola Mundo", resultado)
        except TimeoutException:
            self.fail("❌ La alerta tipo prompt no apareció.")

    def test_text_box_modo_headless(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        driver.find_element(By.ID, "userName").send_keys("Test User")
        driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Calle Falsa 123")
        driver.find_element(By.ID, "permanentAddress").send_keys("Ciudad Imaginaria")
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)
        driver.find_element(By.ID, "submit").click()
        output = driver.find_element(By.ID, "output").text
        self.assertIn("Test User", output)
        self.assertIn("test@example.com", output)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reportes',
        report_name='reporte_demoqa',
        report_title='Pruebas Selenium DemoQA',
        combine_reports=True,
        add_timestamp=True
    ))