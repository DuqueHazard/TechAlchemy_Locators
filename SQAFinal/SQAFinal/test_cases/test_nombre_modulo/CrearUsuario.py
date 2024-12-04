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
      
        self.driver.find_element(By.XPATH,"//div[@class = 'sidebar-toggle']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[text() = 'Usuarios']").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")

    def test_Crear(self):
        self.driver.find_element(By.XPATH,"//button[text()='Crear Usuario']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Ingrese el nombre del usuario']").send_keys("Juanito de la cruz")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Ingrese el correo electrónico']").send_keys("jun@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select//option[text()='Adminstrador']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Ingrese una contraseña segura']").send_keys("Qwerty.232#")
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//button").click()
        time.sleep(9)
        actual=self.driver.find_element(By.XPATH,"//table//td[text()='Juanito de la cruz']").text
        esperado = "Juanito de la cruz"
        assert actual==esperado
      
    def test_Editar(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//table//tr//td[text()='Juanito de la cruz']//following-sibling::td//button[text()='Editar']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Ingrese el nombre del usuario']").clear()
        
        self.driver.find_element(By.XPATH,"//input[@placeholder='Ingrese el nombre del usuario']").send_keys("Juaz")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button").click()
        time.sleep(5)
        actual=self.driver.find_element(By.XPATH,"//table//td[text()='Juaz']").text
        time.sleep(2)

        esperado = "Juaz"
        assert esperado==actual
       
    def test_Eliminar(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//table//tr//td[text()='Juaz']//following-sibling::td//button[text()='Eliminar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='modal-dialog']//button[text()='Eliminar']").click()
        time.sleep(10)

        actual= self.driver.find_element(By.XPATH,"//table//tr").text
        time.sleep(2)

        esperado = ""
        assert esperado!=actual

    

    

