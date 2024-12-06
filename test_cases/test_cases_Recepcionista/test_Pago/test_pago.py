# Incluir acá los test cases para el módulo específico.
# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
# Modificar el PYTHONPATH para incluir el directorio raíz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Ahora puedes importar los módulos
from page_elements.test_Funciones.test_login import login

class Test_Notifiacion:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        time.sleep(4)
        login(self.driver,"rodrigomita1234@gmail.com","Qwerty.23#")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class = 'sidebar-toggle']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[text() = 'Pagos']").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
        print(" Prueba visual completada")
    
    def test_CrearPago(self):
        self.driver.find_element(By.XPATH,"//a [@class = 'btn btn-success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'id_cliente']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'id_cliente']").send_keys("1234567")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'monto']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'monto']").send_keys("60000")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@name = 'metodo_pago']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//option[text() = 'Efectivo']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'detalle']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//option[text() = 'Alquiler de Casillero']").click()
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(3)
        WebDriverWait(self.driver, 35).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Toastify__toast-icon Toastify--animate-icon Toastify__zoom-enter']//following-sibling::div")))
        actual = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-icon Toastify--animate-icon Toastify__zoom-enter']//following-sibling::div"))).text
        print(f"+++++++++++++ {actual}")
        esperado = "Pago creado exitosamente"
        assert actual == esperado, f"Error: Texto actual '{actual}' no coincide con el esperado '{esperado}'"
        time.sleep(2)
        

    
    def test_VerHisto(self):
        self.driver.find_element(By.XPATH,"(//a [@class = 'btn btn-secondary m-1'])[1]").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH, "//p[text() = 'Casillero']").text
        print(f"+++++++++++++",actual)
        esperado = "Detalle: Casillero"
        assert actual in esperado
        time.sleep(3)

    def test_Eliminar(self):
        self.driver.find_element(By.XPATH,"(//a [@class = 'btn btn-secondary m-1'])[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//button[text() = 'Eliminar'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='modal-content']//button[text()='Eliminar']").click()
        WebDriverWait(self.driver, 35).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Toastify__toast-icon Toastify--animate-icon Toastify__zoom-enter']//following-sibling::div")))
        actual = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-icon Toastify--animate-icon Toastify__zoom-enter']//following-sibling::div"))).text
        print(f"+++++++++++++ {actual}")
        esperado = "Pago eliminado con éxito."
        assert actual == esperado, f"Error: Texto actual '{actual}' no coincide con el esperado '{esperado}'"
        time.sleep(2)

        
        

        

       
        

        
        
        
            
    

    