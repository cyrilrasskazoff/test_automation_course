# Область видимости scope
# Для фикстур можно задавать область покрытия фикстур. Допустимые значения:
# “function”: - фикстура будет вызываться один раз для тестового метода,
# “class”: - фикстура будет вызываться один раз для тестового класса,
# “module”: - фикстура будет вызываться один раз для модуля,
# “session”: - фикстура будет вызываться один раз для тестовой сессии.

# Запустим все наши тесты из класса TestMainPage1 в одном браузере для экономии времени, задав scope="class" в фикстуре browser:
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

# в данном примере браузер открылся один раз и тесты последовательно выполнились в этом браузере.
# Pекомендуем всё же запускать отдельный экземпляр браузера для каждого теста, чтобы повысить стабильность тестов.
# Фикстуры, которые занимают много времени для запуска и ресурсов (обычно это работа с базами данных), можно вызывать и один раз за сессию запуска тестов.