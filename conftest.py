import pytest
from selenium import webdriver



# !!! Ранее мы добавили фикстуру browser, которая создает нам экземпляр браузера для тестов в данном файле.
# Когда файлов с тестами становится больше одного, приходится в каждом файле
# с тестами описывать данную фикстуру. Это очень неудобно. Для хранения часто употребимых фикстур
# и хранения глобальных настроек нужно использовать конфигурационный файл conftest.py, который должен лежать в
# директории верхнего уровня в вашем проекте с тестами. Можно создавать дополнительные файлы conftest.py
# в других директориях, но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     driver = webdriver.Chrome()
#     yield driver
#     print("\nquit browser..")
#     driver.quit()


# передача параметров в командной строке
# можно настраивать тестовые окружения с помощью передачи параметров через командную строку.
# Это делается с помощью встроенной функции pytest_addoption и фикстуры request.
# Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption,
# затем напишем фикстуру, которая будет обрабатывать переданные в опции данные.

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
# можно задать дефолтный браузер, например default="chrome" (вместо default=None),
# тогда при запуске теста без укзания параметра '--browser_name' автоматически запустится chrome.
# в противном случае нужно явно указать '--browser_name': pytest -s -v --browser_name=chrome <test_file_path>


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

