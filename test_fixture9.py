# XFail: помечать тест как ожидаемо падающий
# добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":
#
# def test_guest_should_see_search_button_on_the_main_page(self, browser):
#      browser.get(link)
#      browser.find_element(By.CSS_SELECTOR, "button.favorite")
# Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала.
# Пока разработчики исправляют баг, мы хотим, чтобы результат прогона всех наших тестов был успешен, но падающий тест помечался соответствующим образом,
# чтобы про него не забыть. Добавим маркировку @pytest.mark.xfail для падающего теста

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

# Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как XPASS (“unexpectedly passing” — неожиданно проходит).
# После этого маркировку xfail для теста можно удалить. Кстати, к маркировке xfail можно добавлять параметр reason.
# Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx
# !!! перед прогоном не забыть раскоментить код ниже и закоментить 4 строки кода выше
#     @pytest.mark.xfail(reason="fixing this bug right now")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")

