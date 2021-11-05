import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('111')
    browser.find_element(By.NAME, 'lastname').send_keys('222')
    browser.find_element(By.NAME, 'email').send_keys('333@444.555')

    file_path = os.path.join(os.getcwd(), 'blank.txt')

    browser.find_element(By.NAME, 'file').send_keys(file_path)

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
