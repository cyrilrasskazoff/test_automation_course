# Переключение на новую вкладку.
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# Это делается с помощью команды switch_to.window: browser.switch_to.window(window_name)

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает
# массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку: new_window = browser.window_handles[1]

# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться: first_window = browser.window_handles[0]

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(url)

    button_1 = browser.find_element(By.XPATH, '//button')
    browser.execute_script(
        "document.getElementsByTagName('button')[0].classList.remove('trollface');")  # это скрипт для удаления класса, с помощью которого кнопка перемещается
    button_1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button_2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_2.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла!
