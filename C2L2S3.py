import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    result = str(int(num1) + int(num2))

    select_list = Select(browser.find_element(By.ID, 'dropdown'))
    select_list.select_by_value(result)

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
