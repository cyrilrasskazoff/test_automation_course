import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

# Ранее мы добавили фикстуру browser, которая создает нам экземпляр браузера для тестов в данном файле.
# Когда файлов с тестами становится больше одного, приходится в каждом файле
# с тестами описывать данную фикстуру. Это очень неудобно. Для хранения часто употребимых фикстур
# и хранения глобальных настроек нужно использовать файл conftest.py, который должен лежать в
# директории верхнего уровня в вашем проекте с тестами. Можно создавать дополнительные файлы conftest.py
# в других директориях, но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.