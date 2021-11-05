import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(a: str):
    return str(math.log(abs(12*math.sin(int(a)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
