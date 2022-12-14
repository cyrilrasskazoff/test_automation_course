# уникальность селекторов + assert
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    url = "http://suninjuly.github.io/registration1.html"
    # url = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.XPATH, '//form/div[1]/div[1]/input')
    input1.send_keys("FirstName")
    input2 = browser.find_element(By.XPATH, '//form/div[1]/div[2]/input')
    input2.send_keys("LasttName")
    input3 = browser.find_element(By.XPATH, '//form/div[1]/div[3]/input')
    input3.send_keys("test@te.st")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text = browser.find_element(By.TAG_NAME, "h1")
    text = welcome_text.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла!