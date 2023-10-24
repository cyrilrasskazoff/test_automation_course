# использование скриптов: execute_script
# https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    # приведенный ниже код вернет ошибку, т.к. кнопка перекрыта другим элементом страницы
    # button = browser.find_element(By.TAG_NAME, "button")
    # time.sleep(5)
    # button.click()
    # browser.quit()

    # используем скрипт для прокрутки страницы
    button = browser.find_element(By.TAG_NAME, "button")
    time.sleep(5)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(5)
    button.click()

finally:
    browser.quit()

    # не забываем оставить пустую строку в конце файла!