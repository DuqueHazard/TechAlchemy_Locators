from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Test_Reporte:
   
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        time.sleep(4)
 
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")
 
    def test_rol_name_report_mensual(self):
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys('rodrigomita1234@gmail.com')
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys('Qwerty.23#')
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(10)
 
        time.sleep(5)
        self.driver.execute_script("document.body.style.zoom='33%'")
       
        time.sleep(5)
        self.driver.execute_script("document.body.style.zoom='100%'")
       
 