# Incluir acá los test cases para el módulo específico.
# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class Test_Notifiacion:
    
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
        self.driver.find_element(By.XPATH,"//span[text() = 'Notificaciones']").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

        
    
    def test_Asignar(self):
        email = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "element_css"))).get_attribute("value")
        actual = self.driver.find_element(By.XPATH, "//div[text() = 'Hay 12 membresías que ya vencieron.']").text    # igual depende de que casillero ya esta ocupado / en este caso es el 3
        print(f"+++++++++++++",actual)
        esperado = "Hay 12 membresías que ya vencieron."

        assert actual == esperado
        time.sleep(3)
        
       # self.driver.execute_script("document.body.style.zoom='50%'")
    
        
        
        
        

        



              
       