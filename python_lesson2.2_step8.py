# send a file - метод .send_keys(file_path)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# простой способ: прямо объявить путь к файлу. недостаток - придется переписывать каждый раз для нового окружения
# (например, другая ОС, другой компьютер)
# file_path = 'D:\\python_work\\Automation_Testing_Sel\\text_file.txt'
# file_path = '/Users/kirillrasskazov/Documents/AutomationSelenium/text_file.txt'

#  ****************
# оптимальный способ: Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с
# операционной системой — os. В этом случае ваш код не будет зависеть от операционной системы, которую вы используете.
import os
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'text_file.txt')    # добавляем к этому пути имя файла

try:
    url = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(url)


    input1 = browser.find_element(By.XPATH, '//div/input[1]')
    input1.send_keys("Name")
    input2 = browser.find_element(By.XPATH, '//div/input[2]')
    input2.send_keys("LastName")
    input3 = browser.find_element(By.XPATH, '//div/input[3]')
    input3.send_keys("test@test.com")
    input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла!