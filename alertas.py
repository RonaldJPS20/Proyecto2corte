from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--log-level=3") 

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

driver.find_element(By.ID, "alertButton").click()
time.sleep(1)
driver.switch_to.alert.accept()

driver.find_element(By.ID, "timerAlertButton").click()
time.sleep(6)
driver.switch_to.alert.accept()

driver.find_element(By.ID, "confirmButton").click()
time.sleep(1)
driver.switch_to.alert.dismiss()

driver.find_element(By.ID, "promtButton").click()
time.sleep(1)
alert = driver.switch_to.alert
alert.send_keys("se logrooooooooo")
alert.accept()

time.sleep(3)
driver.quit()
