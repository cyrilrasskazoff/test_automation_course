# работа с выпадающими списками:
# browser.find_element(By.{choose a necessary selector}, "{}").click() - находим выпадающий список и кликаем по нему
# browser.find_element(By.{choose a necessary selector}, "{}").click() - находим нужный вариант в списке и кликаем по нему

# **************
# класс Select - позволяет избегать повторное использоване метода click():
# from selenium.webdriver.support.ui import Select
# dropdown = Select(browser.find_element(By.TAG_NAME, "select")) - инициализируем новый объект списка, передав в него WebElement с тегом select
# dropdown.select_by_value("value") OR dropdown.select_by_visible_text("text") OR dropdown.select_by_index(index) - находим любой вариант из списка
# с помощью метода select_by_

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
    return str(int(x) + int(y))


try:

    url = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    result = calc(x, y)

    # решение с помощью Select в следующтх 2 строках кода
    # dropdown = Select(browser.find_element(By.TAG_NAME, "select"))
    # dropdown.select_by_value(result)

    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{result}"]').click() # чтобы передать переменную в значение селектора нужно использовать f-строку!!

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла!