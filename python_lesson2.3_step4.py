# Alerts - работа с модальными oкнами.
# 1 тип Alert: модальное окно с кнопкой 'OK':
# alert = browser.switch_to.alert - (переключение на модальное окно)
# alert.accept() - принимаем Alert (= нажать на OK)

# если нужно получить текст из alert, используйте свойство text объекта alert:
# 1. alert = browser.switch_to.alert
# 2. alert_text = alert.text


# 2 тип Confirm: модальное окно с кнопками 'OK' и 'Cancel' - предлагает либо согласиться либо отказаться от сообщения:
# confirm = browser.switch_to.alert
# confirm.accept() - соглашаемся
# confirm.dismiss() - не соглашаемся


# 3 тип Prompt - имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys()
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept() OR prompt.dismiss()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    url = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(url)

    button_1 = browser.find_element(By.XPATH, '//button')
    button_1.click()
    alert = browser.switch_to.alert
    alert.accept()

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
