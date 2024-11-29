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
        time.sleep(2)
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
        time.sleep(29)
        actual="Usuario creado con éxito."
        esperado=self.driver.find_element(By.XPATH,"//div[text()='Usuario creado con éxito.']").text()
        assert actual==esperado
    

