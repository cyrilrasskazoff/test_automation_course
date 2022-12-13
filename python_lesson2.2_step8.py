# send a file - метод .send_keys(file_path)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

file_path = 'D:\\python_work\\Test_automation_pyton\\text_file.txt'
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
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла!