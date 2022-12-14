# Важной составляющей в использовании PyTest является концепция фикстур.
# Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.
#
# setup_ & teardown_ методы в фикстурах
# Исходя из комментариев и документации https://docs.pytest.org/en/latest/how-to/xunit_setup.html:
#
# префиксы setup_*, teardown_* отвечают за порядок исполнения фикстур: до чего-то, после чего-то.
# постфиксы *_class, *_method и другие отвечают за уровень применения фикстур: ко всему классу, к каждому методу в классе и тд.
# Исходя их логики выше:
#
# setup_class выполняется один раз перед запуском всех тестовых методов в классе
# teardown_class выполянется один раз после всех тестовых методов в классе
# setup_method выполняется перед запуском каждого тестового метода в классе
# teardown_method выполняется каждый раз после тестового метода в классе
# Про декоратор:
#
# @classmethod декоратор, использованный для удобства чтения кода. Так мы дополнительно размечаем в коде, что метод ниже (в нашем примере с *_class) применяется ко всему классу.

# *************************
# в качестве тест-свитов будем использовать классы
# !!! Важно!!! чтобы увидеть текст, который выводится командой print(), нужно использовать переметр -s: pytest -s
from selenium import webdriver
from selenium.webdriver.common.by import By
url = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1(): # тест-свит, в котором браузер запустится 1 раз для всех тестов

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2(): # тест-свит, в котором браузер запустится отдельно для каждого теста

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# P.S. Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на результаты выполнения следующего теста,
# поэтому лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее.
# К тому же если вдруг браузер зависнет в одном тесте, то другие тесты не пострадают, если они запускаются каждый в собственном браузере.