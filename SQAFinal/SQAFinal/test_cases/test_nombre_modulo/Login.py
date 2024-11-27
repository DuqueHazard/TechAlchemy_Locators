# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()
class TestAtt:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        
        self.driver.get('http://localhost:3000/')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
    def test_verify_imei(self):
        self.driver.find_element(By.XPATH,"//div//input[@type='email']").send_keys("genzo24j@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div//input[@type='password']").send_keys("Qwerty.23#")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div//button").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//div[@class='sidebar-toggle']").click()
        time.sleep(39)
        actual=self.driver.find_element(By.XPATH,"//h2[text()='ANDRES SEBASTIAN GUARACHI MAMANI']").text
        print("++++++++++",actual)
        esperado="ANDRES SEBASTIAN GUARACHI MAMANI"
        assert actual==esperado
    

