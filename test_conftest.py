# применние конфигурационного файла conftest.py
# перед использованием, зайти в conftest.py и выбрать тип используемой фикстуры. От этого будте зависеть, каким образом
# запускать тест: с помощью переачи параметров в командной строке (при использовании функции pytest_addoption и
# фикстуры request) или дефолтно
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")