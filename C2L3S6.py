import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.XPATH, '//button').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    result = str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(result)

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(1)

finally:
    time.sleep(10)
    # browser.quit()
