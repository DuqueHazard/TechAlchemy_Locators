# Incluir acá los test cases para el módulo específico.
# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait

import time

class Test_Login:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        time.sleep(4)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_rol_name_recep(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys("rodrigomita1234@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys("Qwerty.23#")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//div[@class = 'sidebar-toggle']").click()
        time.sleep(10)
        actual = self.driver.find_element(By.XPATH, " //strong[text() = 'Recepcionista']").text
        print(f"+++++++++++++",actual)
        esperado = "Recepcionista"

        assert actual == esperado
        time.sleep(3)

       # self.driver.execute_script("document.body.style.zoom='50%'")
       
              
       
