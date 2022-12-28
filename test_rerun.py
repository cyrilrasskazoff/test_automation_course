from selenium.webdriver.common.by import By
# Плагины и перезапуск тестов
# плагин pytest-rerunfailures - автоматически перезапускает Flaky-тесты или "мигающие" авто-тесты,
# т.е. такие тесты, которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов,
# могут иногда падать

# 1. установим плагин: pip install pytest-rerunfailures
# 2. указажем количество перезапусков для каждого из упавших тестов: нужно добавить в командную строку параметр:
# "--reruns n", где n — это количество перезапусков. Если при повторных запусках тесты пройдут успешно,
# то и прогон тестов будет считаться успешным. Количество перезапусков отображается в отчёте, благодаря чему можно
# позже анализировать проблемные тесты
# * Дополнительно укажем параметр "--tb=line", чтобы сократить лог с результатами теста

# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")