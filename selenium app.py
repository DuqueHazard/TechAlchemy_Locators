"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la libreria necesaria

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración automática del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir url en el navegador
#driver.get('https://www.multicine.com.bo/register')
time.sleep(1)
driver.get('https://www.multicine.com.bo')
time.sleep(1)

driver.find_element(By.XPATH, "//button//span[text()='Cancelar']").click()
time.sleep(1)

driver.get('https://www.multicine.com.bo/register')
time.sleep(1)

#registro
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("el lomaso")
driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("casimiro de las lomas")
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("69926300")
driver.find_element(By.XPATH, "//input[@name='address']").send_keys("av Baltica")

driver.find_element(By.XPATH, "//ion-select[@name='mySelect']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[text()='La Paz ']//ancestor::button").click()
driver.find_element(By.XPATH, "//span[text()='Aceptar']//ancestor::button").click()
time.sleep(1)


driver.find_element(By.XPATH, "//input[@name='docextend']").send_keys("Juno hqesw")
driver.find_element(By.XPATH, "//input[@name='docid']").send_keys("16324322")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("vosexe6108@hraifi.com")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='emailConfirm']").send_keys("vosexe6108@hraifi.com")

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwerty123$")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='passwordConfirm']").send_keys("Qwerty123$")

#seleccionar mess
driver.find_element(By.XPATH, "//ion-checkbox").click()

driver.get('https://www.multicine.com.bo/terms')


time.sleep(1)
driver.find_element(By.XPATH, "//ion-back-button").click()


driver.quit()

print("Prueba visual completada")
