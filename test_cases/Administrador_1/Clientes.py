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

        time.sleep(3)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
        
    def test_verificar_redireccion_clientes(self):
        login(self.driver, "genzo24j@gmail.com", "Qwerty.23#")
        time.sleep(2)

        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(7)

        actual=self.driver.find_element(By.XPATH,"//h1[@class='text-center mb-4']").text
        time.sleep(1)
        
        esperado="Lista de Clientes"

        print("Actual: ",actual," Esperado: ",esperado)
        assert actual==esperado

    def test_crear_cliente(self):
        login(self.driver, "genzo24j@gmail.com", "Qwerty.23#")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Crear Cliente']").click()
        time.sleep(2)
        num = random.randint(10**6, 10**8 - 1)
        self.driver.find_element(By.XPATH, "//input[@name='ci']").send_keys(num)
        time.sleep(10)



        