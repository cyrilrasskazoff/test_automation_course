from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

url = "http://suninjuly.github.io/registration1.html"

url_1 = 'http://suninjuly.github.io/registration2.html'


class TestWelcomeText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_search_element_1(self):
        driver = webdriver.Chrome()
        driver.get(url)

        input1 = driver.find_element(By.XPATH, '//form/div[1]/div[1]/input')
        input1.send_keys("FirstName")
        input2 = driver.find_element(By.XPATH, '//form/div[1]/div[2]/input')
        input2.send_keys("LasttName")
        input3 = driver.find_element(By.XPATH, '//form/div[1]/div[3]/input')
        input3.send_keys("test@te.st")

        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = driver.find_element(By.TAG_NAME, "h1")
        text = welcome_text.text
        self.assertEqual(text, "Congratulations! You have successfully registered!", "Welcome text error!")
        time.sleep(5)
        driver.quit()

    def test_search_element_2(self):
        driver = webdriver.Chrome()
        driver.get(url_1)

        input1 = driver.find_element(By.XPATH, '//form/div[1]/div[1]/input')
        input1.send_keys("FirstName")
        input2 = driver.find_element(By.XPATH, '//form/div[1]/div[2]/input')
        input2.send_keys("LasttName")
        input3 = driver.find_element(By.XPATH, '//form/div[1]/div[3]/input')
        input3.send_keys("test@te.st")

        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = driver.find_element(By.TAG_NAME, "h1")
        text = welcome_text.text
        self.assertEqual(text, "Congratulations! You have successfully registered!", "Welcome text error!")
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
