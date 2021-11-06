import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_link1(self):
        self.check_required_fields("http://suninjuly.github.io/registration1.html")

    def test_link2(self):
        self.check_required_fields("http://suninjuly.github.io/registration2.html")

    def check_required_fields(self, link):
        self.browser.get(link)

        self.browser.find_element(By.XPATH, '//input[@required and @class="form-control first"]').send_keys("firstname")
        self.browser.find_element(By.XPATH, '//input[@required and @class="form-control second"]').send_keys("lastname")
        self.browser.find_element(By.XPATH, '//input[@required and @class="form-control third"]').send_keys("email")

        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
