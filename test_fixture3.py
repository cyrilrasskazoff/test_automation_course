# Финализаторы в фикстурах - закрываем браузер
# чтобы оперативная память не закончилась быстро, надо явно закрывать браузеры после каждого теста.
# Для этого мы можем воспользоваться финализаторами. Один из вариантов финализатора — использование ключевого слова Python: yield.
# После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, следующей за строкой со словом yield:
# Aльтернативный способ вызова teardown кода с помощью встроенной фикстуры request и ее метода addfinalizer: \
# https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser_object = webdriver.Chrome()
    yield browser_object
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser_object.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")