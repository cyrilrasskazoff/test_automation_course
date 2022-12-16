# Explicit Waits (WebDriverWait и expected_conditions) - позволяют задать специальное ожидание для конкретного элемента
# В модуле expected_conditions есть много правил, которые позволяют реализовать необходимые ожидания:
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
# подробнее тут: https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
# код ниже упадет с ошибкой no such element: Unable to locate element: {"method":"css selector","selector":"[id="verify_message"]"},
# т.к. кнопка с id="verify" была неактивна в момент нажатия (браузер нашел ее и кликнул)
# try:
#
#     browser = webdriver.Chrome()
#     # говорим WebDriver ждать все элементы в течение 5 секунд
#     browser.implicitly_wait(5)
#
#     browser.get("http://suninjuly.github.io/wait2.html")
#
#     button = browser.find_element(By.ID, "verify")
#     button.click()
#     message = browser.find_element(By.ID, "verify_message")
#
#     assert "successful" in message.text
# finally:
#     browser.quit()

# применим WebDriverWait и expected_conditions:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait2.html")
    # говорим Selenium ждать в течение 5 секунд пока кнопка станет активной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))) # element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()

# Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))

# не забываем оставить пустую строку в конце файла!