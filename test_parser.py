from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

# команда ниже верне ошибку: '_pytest.config.exceptions.UsageError: --browser_name should be chrome or firefox',
# если в конфгурационном файле default=None
# pytest -s -v test_parser.py

# команда ниже запустит браузер chrome
# pytest -s -v --browser_name=chrome test_parser.py


# команда ниже запустит браузер firefox
# pytest -s -v --browser_name=firefox test_parser.py