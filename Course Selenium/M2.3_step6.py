from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button.click()
    window1 = browser.window_handles[1]#задаем переменную второй вкладке через массив
    browser.switch_to.window(window1)#переключаемся на вторую вкладку
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    time.sleep(15)
    browser.quit()
