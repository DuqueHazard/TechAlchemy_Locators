# utils.py
from selenium.webdriver.common.by import By
import time

def login(driver, email, password):
    """
    Función para hacer login en la aplicación usando el email y la contraseña.
    """
    driver.find_element(By.XPATH,"//input[@type = 'email']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div//input[@type='email']").send_keys(email)
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@type = 'password']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div//input[@type='password']").send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
