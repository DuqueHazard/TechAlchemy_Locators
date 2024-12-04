# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# log.py
import sys
import os
# Modificar el PYTHONPATH para incluir el directorio raíz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
 
# Ahora puedes importar los módulos
from page_elements.test_Funciones.test_login import login
 
import random
 
# Maximizar la ventana del navegador
class TestAtt:
    def setup_method(self):
        self.driver=webdriver.Chrome()
       
        self.driver.get('http://localhost:3000/')
        self.driver.maximize_window()
        login(self.driver,"rodrigomita1234@gmail.com","Qwerty.23#")
 
        time.sleep(3)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
    
    def test_crear_cliente(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH,"//button[text()='Crear Cliente']").click()
        time.sleep(2)
        ci_aleatorio = random.randint(10**6, 10**8 - 1)
        self.driver.find_element(By.XPATH,"//input[@name='ci']").send_keys(ci_aleatorio)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").send_keys('prueba')
        time.sleep(2)
        tel_aleatorio = random.randint(10**7, 10**8 - 1)
        self.driver.find_element(By.XPATH,"//input[@name='telefono']").send_keys(tel_aleatorio)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='correoElectronico']").send_keys('prueba',tel_aleatorio,'@gmail.com')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='direccion']").send_keys('Calle ',tel_aleatorio)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@name='idMembresia']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//option[@value='3']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@type='button']").click()
        time.sleep(10)

        self.driver.find_element(By.XPATH,"//input[@placeholder='Monto']").send_keys('71')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@class='form-select']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value='Efectivo']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[text()='Seleccione un detalle']//ancestor::select").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[text()='Alquiler Casillero']").click()
        time.sleep(2)
 
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
        WebDriverWait(self.driver, 35).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Pago creado con éxito']")))
        actual = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Pago creado con éxito']"))).text
        print(f"+++++++++++++ {actual}")
        esperado='Pago creado con éxito'
        assert actual == esperado, f"Error: Texto actual '{actual}' no coincide con el esperado '{esperado}'"
        time.sleep(1)
    
    
    def test_editar_cliente(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//button[text()='Editar'])[2]").click()
        time.sleep(5)
        numero_al = random.randint(10**6, 10**8 - 1)
        esperado=f"{numero_al}"
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").send_keys(numero_al)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Actualizar Cliente']").click()
        time.sleep(6)
 
        actual=self.driver.find_element(By.XPATH,"((//table[@class='shadow-sm table table-striped table-bordered table-hover']//tbody//tr)[2]//td)[2]").text
        assert esperado==actual
     
    
    def test_cliente_con_historial(self):
        time.sleep(4)
        esperado='Nombre Membresía'
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Ver Historial'])[1]").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH,"//th[text()='Nombre Membresía']").text
        assert esperado==actual
    
    
    def test_cliente_sin_historial(self):
        time.sleep(4)
        esperado='No hay registros de membresía para este cliente.'
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Ver Historial'])[3]").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH,"//p[text()='No hay registros de membresía para este cliente.']").text
        assert esperado==actual  
    
    
    def test_cliente_sin_historial(self):
        time.sleep(4)
        esperado='No hay registros de membresía para este cliente.'
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Renovar Membresía'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@name='idMembresia']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value='3']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button").click()
 
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Monto']").send_keys('71')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@class='form-select']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value='Efectivo']").click()
       
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[text()='Seleccione un detalle']//ancestor::select").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[text()='Alquiler Casillero']").click()
        time.sleep(2)
 
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
 
        time.sleep(2)
        esperado='Pago creado con éxito'
        actual=self.driver.find_element(By.XPATH,"//div[text()='Pago creado con éxito']").text
        assert esperado==actual
    
    
    def test_cliente_eliminar(self):
        time.sleep(4)
        esperado='No hay registros de membresía para este cliente.'
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Eliminar'])[5]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='modal-footer']//button[text()='Eliminar']").click()
        time.sleep(3)
 
        esperado="Cliente con ID"
        actual=self.driver.find_element(By.XPATH,"//div[contains(text(),'Cliente')]").text
        assert esperado in actual
    
     
       
       
 
 
       
 