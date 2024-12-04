# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait

import time

class Test_Reporte:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        time.sleep(4)
        time.sleep(4)
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
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")


    def test_rol_name_report_mensual(self):
        time.sleep(8)
        self.driver.execute_script("document.body.style.zoom='33%'")
        time.sleep(5)
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//div[@class = 'sidebar-toggle']").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, " //strong[text() = 'Recepcionista']").text
        print(f"+++++++++++++",actual)
        esperado = "Recepcionista"
        assert actual == esperado
        time.sleep(3)
    
    #def test_descarga(self):


       