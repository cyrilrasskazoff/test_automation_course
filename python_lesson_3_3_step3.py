import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration1.html"

url_1 = 'http://suninjuly.github.io/registration2.html'


def test_search_element_1():
    try:
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

        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text = driver.find_element(By.TAG_NAME, "h1")
        text = welcome_text.text
        assert text == "Congratulations! You have successfully registered!", "Welcome text error!"
        time.sleep(5)
    finally:
        driver.quit()


def test_search_element_2():
    try:
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
        assert text == "Congratulations! You have successfully registered!", "Welcome text error!"
        time.sleep(5)
    finally:
        driver.quit()

