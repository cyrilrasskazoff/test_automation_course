# CSS селекторы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.TAG_NAME, 'input') #<input type="text" name="first_name" class="form-control"
    # required="" maxlength="32">
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name') #<input type="text" name="last_name" class="form-control"
    # required="" maxlength="32">
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city') #<input type="text" name="firstname"
    # class="form-control city" required="" maxlength="32">
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country') #<input type="text" name="firstname" class="form-control"
    # id="country" required="" maxlength="32">
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn') #<button id="submit_button" type="submit"
    # class="btn btn-default">Submit</button>
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла!