
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.find_element(By.ID, "firstName").send_keys("Juan")
driver.find_element(By.ID, "lastName").send_keys("Pérez")
driver.find_element(By.ID, "userEmail").send_keys("juanperez@test.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
driver.find_element(By.ID, "submit").click()

time.sleep(5)
driver.quit()
