import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//input[@required and @class="form-control first"]').send_keys("first name")
    browser.find_element(By.XPATH, '//input[@required and @class="form-control second"]').send_keys("last name")
    browser.find_element(By.XPATH, '//input[@required and @class="form-control third"]').send_keys("email@email.email")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
