# Автоиспользование фикстур
# При описании фикстуры можно указать дополнительный параметр autouse=True,
# который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# для каждого теста фикстура подготовки данных выполнилась без явного вызова.
# Нужно быть аккуратнее с этим параметром, потому что фикстура выполняется для всех тестов.
# Без явной необходимости автоиспользованием фикстур лучше не пользоваться.