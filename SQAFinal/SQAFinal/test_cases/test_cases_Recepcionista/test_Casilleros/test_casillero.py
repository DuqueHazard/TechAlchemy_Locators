# Incluir acá los test cases para el módulo específico.
# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class Test_Casillero:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
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
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class = 'sidebar-toggle']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[text() = 'Casilleros']").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

        
    
    def test_Asignar(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text() = 'Asignar'])[3]").click() # Depende de que casillero este vacio / en este caso es el 3
        self.driver.find_element(By.XPATH,"//input[@placeholder = 'Ingrese el ID o nombre del cliente']").click()
        self.driver.find_element(By.XPATH,"//input[@placeholder = 'Ingrese el ID o nombre del cliente']").send_keys("712345678")
        time.sleep(3)
      #  self.driver.find_element(By.XPATH,"(//button[@class = 'list-group-item list-group-item-action'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"(//button[@class = 'btn btn-outline-primary'])[8]").click()
        self.driver.find_element(By.XPATH,"//button[@class = 'btn btn-primary']").click()
        time.sleep(15)
        actual = self.driver.find_element(By.XPATH, "(//strong[text() ='Ocupado'])[3]").text    # igual depende de que casillero ya esta ocupado / en este caso es el 3
        print(f"+++++++++++++",actual)
        esperado = "Ocupado"

        assert actual == esperado
        time.sleep(3)
        
       # self.driver.execute_script("document.body.style.zoom='50%'")
    
    def test_ver(self):
        time.sleep(2)
        #self.driver.execute_script("document.body.style.zoom='67%'")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//button[text()= 'Ver'])[3]").click()
        time.sleep(3)
        
        
    
    def test_editar(self):
        time.sleep(2)
        #self.driver.execute_script("document.body.style.zoom='67%'")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//button[text()= 'Editar'])[3]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input [@name = 'id_cliente']").click()
        self.driver.find_element(By.XPATH,"//input [@name = 'id_cliente']").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input [@name = 'id_cliente']").send_keys("1234567")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input [@name = 'fecha_devolucion']").click()
        self.driver.find_element(By.XPATH,"//input [@name = 'fecha_devolucion']").send_keys("25122024")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button [@class = 'btn btn-primary']").click()
        time.sleep(3)
    
    def test_eliminar(self):
        time.sleep(2)
        #self.driver.execute_script("document.body.style.zoom='67%'")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//button[text()= 'Eliminar'])[3]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div [@class = 'modal-footer']//child::button[text() = 'Eliminar']").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH, "(//strong [text()= 'Disponible'])[1]").text   
        print(f"+++++++++++++",actual)
        esperado = "Disponible"
        assert actual == esperado
        time.sleep(3)

        
        
        
        

        



              
       