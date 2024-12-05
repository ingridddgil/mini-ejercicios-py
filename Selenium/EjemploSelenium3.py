from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.pino.mx/ti/lista.php")

matriculas = []

for i in range(1, 47):
    campo = f"m_{i}"
    matriculas.append(WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, campo))).get_dom_attribute("value"))

sum = 1
   
for matricula in matriculas:
    driver.get("http://www.pino.mx/ti/codigo01.php")

    campo_matricula = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, "matricula")))
    campo_matricula.send_keys(matricula)
    campo_matricula.send_keys(Keys.ENTER)

    codigo = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, "codigo"))).get_dom_attribute("value")

    driver.get("http://www.pino.mx/ti/acceso01.php")

    campo_matricula = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, "matricula")))
    campo_matricula.send_keys(matricula)

    campo_codigo = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, "codigo")))
    campo_codigo.send_keys(codigo)
    campo_codigo.send_keys(Keys.ENTER)

    id = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID, "confirmacion"))).get_dom_attribute("value")

    print(f"{sum} Matricula: {matricula}\nCodigo: {codigo}\nID de cofirmación: {id}")
    sum += 1

    
