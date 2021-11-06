import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
# browser.implicitly_wait(5)

try:
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    result = str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(result)

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()
