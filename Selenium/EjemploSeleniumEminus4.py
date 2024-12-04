from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://eminus.uv.mx/eminus4/")

# Esperar hasta que el campo de usuario sea visible
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("S22017036")

# Esperar hasta que el campo de contraseña sea visible
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("Gatosconguantes/2")
password_field.send_keys(Keys.ENTER)

time.sleep(10)
