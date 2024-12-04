from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.pino.mx/ti/codigo01.php")
campo_matricula = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "matricula")))
    
campo_matricula.send_keys("S22017036")
campo_matricula.send_keys(Keys.ENTER)
    

campo_codigo = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "codigo")))

matricula = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "matricula"))).get_dom_attribute("value")
codigo = campo_codigo.get_dom_attribute("value")
    
    
time.sleep(5)
    

print(f"Matricula: {matricula}\nCódigo: {codigo}")