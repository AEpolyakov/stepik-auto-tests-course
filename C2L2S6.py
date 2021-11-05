import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    result = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(result)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    radio = browser.find_element(By.ID, 'robotsRule')
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')

    browser.execute_script('return arguments[0].scrollIntoView(true);', button)

    checkbox.click()
    radio.click()
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
