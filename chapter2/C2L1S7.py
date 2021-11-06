import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(a: str):
    return str(math.log(abs(12*math.sin(int(a)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_elem = browser.find_element(By.ID, 'treasure')
    x = x_elem.get_attribute("valuex")

    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
