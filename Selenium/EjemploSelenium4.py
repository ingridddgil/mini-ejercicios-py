from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
nombres = []
apellidos = []

driver.get("http://www.pino.mx/act25/lista.php")

for i in range(1, 17):
    codigo_nombre = f"nom_{i}"
    codigo_apellido = f"ap_{i}"
    nombres.append(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, codigo_nombre))).get_dom_attribute("value"))
    apellidos.append(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, codigo_apellido))).get_dom_attribute("value"))

for nombre, apellido in zip(nombres, apellidos):
    driver.get("http://www.pino.mx/act25/registro01.php")
    campo_nombre = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nombre")))
    campo_nombre.send_keys(nombre)
    
    campo_apellido = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "apellidos")))
    campo_apellido.send_keys(apellido)
    campo_apellido.send_keys(Keys.ENTER)

    confirmacion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmacion"))).get_dom_attribute("value")

    print(nombre, apellido, confirmacion,"\n")