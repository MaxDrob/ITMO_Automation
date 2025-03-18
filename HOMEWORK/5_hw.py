from selenium import webdriver
from selenium.webdriver.common.by import By

def element_check():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    if driver.find_element(By.ID, "user-name") and driver.find_element(By.ID, "password") and driver.find_element(By.ID, "login-button"):
        print("Element found")
    else:
        print('Element missing')

element_check()