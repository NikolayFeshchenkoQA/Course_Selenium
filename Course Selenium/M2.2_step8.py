import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Oh")
    input2 = browser.find_element(By.CSS_SELECTOR,'[name="lastname"]')
    input2.send_keys("this")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("again@gmail.com")
    current_dir = os.path.abspath(os.path.dirname("M2.2_step8.py"))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')    # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

finally:
    time.sleep(20)
    browser.quit()

