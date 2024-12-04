# Incluir acá los test cases para el módulo específico.
# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
# Modificar el PYTHONPATH para incluir el directorio raíz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Ahora puedes importar los módulos
from page_elements.test_Funciones.test_login import login


import time

class Test_Casillero:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        time.sleep(4)
      
        login(self.driver,"rodrigomita1234@gmail.com","Qwerty.23#")
        time.sleep(2)
        
        self.driver.find_element(By.XPATH,"//div[@class = 'sidebar-toggle']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[text() = 'Cerrar Sesión']").click()
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

        
    
    def test_cerrar(self):

        actual = self.driver.find_element(By.XPATH, "//h2[text() = 'Inicio de sesión']").text    # igual depende de que casillero ya esta ocupado / en este caso es el 3
        print(f"+++++++++++++",actual)
        esperado = "Inicio de sesión"

        assert actual == esperado
        time.sleep(3)
        
       # self.driver.execute_script("document.body.style.zoom='50%'")
   