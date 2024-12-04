 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
import time
 
# Maximizar la ventana del navegador
class TestInicio:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys("genzo24j@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys("Qwerty.23#")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(10)
     
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
   
    def test_crear_cliente(self):
       
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//select[@class='sc-ghWlax etIzGG'])[1]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,"//option[@value='Mensual']").click()
        time.sleep(2)

        esperado="Mensual"
        actual=self.driver.find_element(By.XPATH,"(//select[@class='sc-ghWlax etIzGG'])[1]").text
        time.sleep(2)

        assert esperado in actual
        


       