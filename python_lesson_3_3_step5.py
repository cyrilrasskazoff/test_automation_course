# PyTest: правила запуска тестов.
#1. если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории

#2. как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например:
    # pytest scripts/selenium_scripts
    # найти все тесты в директории scripts/selenium_scripts

    # pytest test_user_interface.py
    # найти и выполнить все тесты в файле

    # pytest scripts/drafts.py::test_register_new_user_parametrized
    # найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить

#3. дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории

#4. во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или *_test.py
# (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)

#5. внутри всех этих файлов находит тестовые функции по следующему правилу:
    # все тесты (ф-ции), название которых начинается с test, которые находятся вне классов
    # все тесты (ф-ции), название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)

# PyTest — отчёты
# Если запустить PyTest с параметром -v (verbose, то есть подробный),
# то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения: pytest -v <test-file directory>

# ************
# PyTest — проверка ожидаемого результата (assert) + exceptions (с использованием конструкции with)
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()



# В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException, которую ожидает контекстный менеджер
# pytest.raises, не возникнет, и тест упадёт.
