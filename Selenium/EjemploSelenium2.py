from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

matricula = input("Ingresa tu matricula: ")

driver = webdriver.Chrome()
driver.get("http://www.pino.mx/ti/codigo01.php")

campo_matricula = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, "matricula")))
campo_matricula.send_keys(matricula)
campo_matricula.send_keys(Keys.ENTER)

campo_codigo = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "codigo")))
codigo_valor = campo_codigo.get_dom_attribute("value")


driver2 = webdriver.Chrome()
driver2.get("http://www.pino.mx/ti/acceso01.php")

campo_matricula = WebDriverWait(driver2, 5).until(EC.presence_of_element_located((By.ID, "matricula")))
campo_matricula.send_keys(matricula)
campo_codigo = WebDriverWait(driver2, 5).until(EC.presence_of_element_located((By.ID, "codigo")))
campo_codigo.send_keys(codigo_valor)
campo_codigo.send_keys(Keys.ENTER)

campo_confirmacion = WebDriverWait(driver2, 5).until(EC.presence_of_element_located((By.ID, "confirmacion")))
confirmacion_valor =campo_confirmacion.get_dom_attribute("value")

time.sleep(6)

print(f"Matricula: {matricula}\nCódigo: {codigo_valor}\nID de confirmación: {confirmacion_valor}")