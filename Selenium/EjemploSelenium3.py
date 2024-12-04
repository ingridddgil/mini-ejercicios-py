from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.pino.mx/ti/lista.php")
lista = []
for i in range(1, 47):
    campo = f"m_{i}"
    lista.append(WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, campo))).get_dom_attribute("value"))

driver2 = driver.Chrome()

driver2.get("http://www.pino.mx/ti/codigo01.php")
