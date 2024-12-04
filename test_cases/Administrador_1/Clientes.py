 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
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
        self.driver.find_element(By.XPATH,"//span[text() = 'Clientes']").click()
        time.sleep(10)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completa")
   
    def test_crear_cliente(self):
       
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//button[text()='Crear Cliente']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='ci']").send_keys(12387297)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").send_keys("Juniatio Budsw Nummbertin")
        time.sleep(2)
     
        self.driver.find_element(By.XPATH,"//input[@name='telefono']").send_keys(78392212)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='correoElectronico']").send_keys("pruebdsfs@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='direccion']").send_keys("Calle 2")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@name='idMembresia']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//option[@value='3']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@type='button']").click()
        time.sleep(10)
 
        self.driver.find_element(By.XPATH,"//input[@placeholder='Monto']").send_keys(150)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@class='form-select']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value='Efectivo']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[text()='Seleccione un detalle']//ancestor::select").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[text()='Membresía']").click()
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
        time.sleep(8)
 
        esperado= "Miguel el muerde almohadas"
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name='nombreCompleto']").send_keys("Miguel el muerde almohadas")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Actualizar Cliente']").click()
        time.sleep(6)
 
        actual=self.driver.find_element(By.XPATH,"//tr//td[text()='Miguel el muerde almohadas']").text
        assert esperado==actual
     
 
    def test_cliente_con_historial(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Ver Historial'])[1]").click()
        time.sleep(5)
        actual=self.driver.find_element(By.XPATH,"//th[text()='Nombre Membresía']").text
        esperado='Nombre Membresía'
        assert esperado==actual
        time.sleep(2)
   
 
     
    def test_cliente_sin_historial(self):
        time.sleep(4)
        esperado='No hay registros de membresía para este cliente.'
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Ver Historial'])[3]").click()
        time.sleep(5)
        actual=self.driver.find_element(By.XPATH,"//p[text()='No hay registros de membresía para este cliente.']").text
        assert esperado==actual  
   
    def test_cliente_renovar_membresia(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,"(//span[@class='ps-menu-icon css-wx7wi4'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//button[text()='Renovar Membresía'])[1]").click()
        time.sleep(8)
        self.driver.find_element(By.XPATH,"//select[@name='idMembresia']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value='3']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button").click()
 
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Monto']").send_keys(140)
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
        esperado='Pago creado con éxito'
        WebDriverWait(self.driver, 35).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Pago creado con éxito']")))
        actual = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Pago creado con éxito']"))).text
        print(f"+++++++++++++ {actual}")
        assert actual == esperado, f"Error: Texto actual '{actual}' no coincide con el esperado '{esperado}'"
        time.sleep(2)    
   
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
    
        
       


        