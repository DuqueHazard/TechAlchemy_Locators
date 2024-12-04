# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página
 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# log.py
import sys
import os
# Modificar el PYTHONPATH para incluir el directorio raíz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Ahora puedes importar los módulos
from page_elements.nombre_de_la_pagina.utils import login

import random

# Maximizar la ventana del navegador
class TestAtt:
    def setup_method(self):
        self.driver=webdriver.Chrome()
       
        self.driver.get('http://localhost:3000/')
        self.driver.maximize_window()
        login(self.driver, "genzo24j@gmail.com", "Qwerty.23#")


        time.sleep(3)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
    def test_crear_cliente(self):
     
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH,"//button[text()='Crear Cliente']").click()
        time.sleep(1)
        ci_aleatorio = random.randint(10**6, 10**8 - 1)
        self.driver.find_element(By.XPATH,"//input[@name='ci']").send_keys(ci_aleatorio)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").send_keys('prueba')
        time.sleep(1)
        tel_aleatorio = random.randint(10**7, 10**8 - 1)
        self.driver.find_element(By.XPATH,"//input[@name='telefono']").send_keys(tel_aleatorio)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='correoElectronico']").send_keys('prueba',tel_aleatorio,'@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='direccion']").send_keys('Calle ',tel_aleatorio)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@name='idMembresia']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//option[@value='3']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@type='button']").click()
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

        time.sleep(10)
        esperado='Pago creado con éxito'
        actual=self.driver.find_element(By.XPATH,"//div[text()='Pago creado con éxito']").text
        time.sleep(2)

        self.driver.find_element(By.XPATH,"(//a[@class='ps-menu-button'])[9]").click()
        time.sleep(2)
        time.sleep(5)

        assert esperado==actual
    
    def test_editar_cliente(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Editar'])[2]").click()
        time.sleep(10)
        numero_al = random.randint(10**6, 10**8 - 1)
        esperado=f"{numero_al}"
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").send_keys(numero_al)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Actualizar Cliente']").click()
        time.sleep(6)

        actual=self.driver.find_element(By.XPATH,"((//table[@class='shadow-sm table table-striped table-bordered table-hover']//tbody//tr)[2]//td)[2]").text
        time.sleep(2)

        self.driver.find_element(By.XPATH,"(//a[@class='ps-menu-button'])[9]").click()
        time.sleep(10)

        assert esperado==actual
    def test_cliente_renovar_membresia(self):
        time.sleep(4)
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
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//a[@class='ps-menu-button'])[9]").click()
        time.sleep(2)

        assert esperado==actual
    def test_cliente_con_historial(self):
        time.sleep(4)
        esperado='Nombre Membresía'
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Ver Historial'])[1]").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH,"//th[text()='Nombre Membresía']").text
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Cerrar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//a[@class='ps-menu-button'])[9]").click()
        time.sleep(10)
        assert esperado==actual

    def test_cliente_sin_historial(self):
        time.sleep(4)
        esperado='No hay registros'
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Ver Historial'])[3]").click()
        time.sleep(2)
        actual=self.driver.find_element(By.XPATH,"//p[text()='No hay registros de membresía para este cliente.']").text
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Cerrar']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,"(//a[@class='ps-menu-button'])[9]").click()
        time.sleep(2)
        assert esperado in actual   
   
    def test_cliente_eliminar(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Eliminar'])[4]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='modal-footer']//button[text()='Eliminar']").click()
        time.sleep(4)

        esperado="Cliente con ID"
        actual=self.driver.find_element(By.XPATH,"//div[contains(text(),'Cliente')]").text
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//a[@class='ps-menu-button'])[9]").click()
        time.sleep(2)

        assert esperado in actual
    
        
       


        