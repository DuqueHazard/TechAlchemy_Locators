# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Maximizar la ventana del navegador

class TestAtt:
   
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        time.sleep(3)
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
        self.driver.find_element(By.XPATH,"//div[@class = 'sidebar-toggle']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//span[text() = 'Empleados']").click()
        time.sleep(7)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")

  
      
    def test_Crear(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text()='Crear Empleado']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div//label[text()='Nombre Completo']//following-sibling::input").send_keys("Ambersint serbio Nuismd")
        
        time.sleep(2)

        self.driver.find_element(By.XPATH,"//select").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,"//select//option[@value='Administrador']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div//label[text()='Salario']//following-sibling::input").send_keys(1000)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button").click()
        time.sleep(8)
        

        actual = self.driver.find_element(By.XPATH, "//td[text()='Ambersint serbio Nuismd']").text
        esperado = "Ambersint serbio Nuismd"
        assert actual==esperado

    def test_Editar(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//table//tr//td[text()='Ambersint serbio Nuismd']//following-sibling::td//button[text()='Editar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div//label[text()='Nombre Completo']//following-sibling::input").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div//label[text()='Nombre Completo']//following-sibling::input").send_keys("Pablo segundo hybg")
        time.sleep(2)
    
        
        self.driver.find_element(By.XPATH,"//button").click()
        time.sleep(7)
        

        actual = self.driver.find_element(By.XPATH, "//td[text()='Pablo segundo hybg']").text
        esperado = "Pablo segundo hybg"
        time.sleep(20)
        assert actual==esperado

    def test_Eliminar(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//table//tr//td[text()='Pablo segundo hybg']//following-sibling::td//button[text()='Eliminar']").click()
        time.sleep(2)    
        self.driver.find_element(By.XPATH,"//div[@class='modal-dialog']//button[text()='Eliminar']").click()
        time.sleep(10)
        actual = self.driver.find_element(By.XPATH, "//tr").text
        esperado = ""
        assert actual != esperado
     

    

