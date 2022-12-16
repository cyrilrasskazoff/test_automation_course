# checkboxes and radio buttons
# атрибут .text
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(url)

# Для этой задачи понадобится использовать атрибут .text для найденного элемента.
# Обратите внимание, что скобки здесь не нужны:
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value') # <span class="nowrap" id="input_value">559</span>
    x = x_element.text
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

# не забываем оставить пустую строку в конце файла!