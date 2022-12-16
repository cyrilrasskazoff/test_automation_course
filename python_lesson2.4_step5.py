# Способы избежать ложного падения тестов из-за асинхронной работы скриптов или задержек от сервера.
# Selenium Waits (Implicit Waits) имлицитное ожидание:
# метод implicitly_wait({time in seconds}) - позволяет избежать метода time.wait(), который нужно вызывать при каждой необходимости ожидания
# метод implicitly_wait() вызывается 1 раз и применяется ко всему файлу
from selenium import webdriver
from selenium.webdriver.common.by import By

# код ниже завершится ошибкой NoSuchElementException, т.к. элемент button подгружвется с задержкой
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/wait1.html")
#     button = browser.find_element(By.ID, "verify")
#     button.click()
#     message = browser.find_element(By.ID, "verify_message")
#
#     assert "successful" in message.text
# finally:
#     browser.quit()

# то же самое с использовнием метода implicitly_wait()
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text # конструкция assert "text" in argument.text == argument содержит текст
finally:
    browser.quit()

# не забываем оставить пустую строку в конце файла!