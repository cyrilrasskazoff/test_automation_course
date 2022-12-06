# Метод get_attribute
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x_element = browser.find_element(By.ID, 'treasure') # <img src="images/chest.png" height="40" width="40" id="treasure" valuex="117">
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)



finally:
    time.sleep(10)
    browser.quit()