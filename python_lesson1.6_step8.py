# Поиск по XPath
# фильтрация:
# по любому атрибуту, будь то id, class, title (или любой другой). //img[@id='bullet']
# по порядковому номеру. //div[@class="row"]/div[2]
# по полному совпадению текста. //p[text()="<text>"]. Такой селектор вернет элемент, только если текст полностью совпадет.
# по частичному совпадению текста или атрибута. //p[contains(text(), "<text>")]
# по содержимому - //button[contains(@class, 'btn')]
# по нескольким атрибутам - //input[@type='email' and @role='login']
# булевы операции (and, or, not) и некоторые простые арифметические выражения //img[@name='bullet-cat' and @data-type='animal']
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]') #<button type="submit" class="btn"
    # disabled="disabled">Submit</button>
    button.click()

finally:
    time.sleep(15)
    browser.quit()

# не забываем оставить пустую строку в конце файла!