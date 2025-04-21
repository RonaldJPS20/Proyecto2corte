import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class TestHeadlessDemoQA(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://demoqa.com/text-box")
        self.driver.implicitly_wait(5)

    def test_text_box(self):
        driver = self.driver
        driver.find_element(By.ID, "userName").send_keys("Ronald")
        driver.find_element(By.ID, "userEmail").send_keys("ronapossu6@gmail.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Cl 79 Enorte #98-45")
        driver.find_element(By.ID, "permanentAddress").send_keys("Bogota")

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(1)

        driver.find_element(By.ID, "submit").click()

        time.sleep(1)
        output = driver.find_element(By.ID, "output").text

        print("Salida del formulario:", output)

        self.assertIn("Ronald", output)
        self.assertIn("ronapossu6@gmail.com", output)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
