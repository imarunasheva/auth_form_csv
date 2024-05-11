import csv
import pytest
from page.auth_page import AuthPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.locators import AuthLocators

@pytest.fixture(autouse=True)
def driver():
   options = webdriver.ChromeOptions()
   options.add_experimental_option('excludeSwitches', ['enable-logging'])
   options.add_argument('--log-level=3')
   service = ChromeService(executable_path=ChromeDriverManager().install())
   driver = webdriver.Chrome(service=service, options=options)
   yield driver
   driver.quit()


def data_for_test_positive():
    """Данные для тестов с ожидаемыми положительными результатами"""
    test_data_positive = []
    with open('tests/values_positive.csv', newline='', encoding='utf-8') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        next(data)  # skip header row
        for row in data:
            test_data_positive.append(row)
    return test_data_positive

def data_for_test_negative():
    """Данные для тестов с ожидаемыми отрицательными результатами"""
    test_data_negative = []
    with open('tests/values_negative.csv', newline='', encoding='utf-8') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        next(data)  # skip header row
        for row in data:
            test_data_negative.append(row)
    return test_data_negative


class TestAuthForm:
    @pytest.mark.parametrize('name_test, firstname, lastname, address, password, password_confirm', data_for_test_positive())
    def test_auth_form_positive(self, selenium, driver, name_test, firstname, lastname, address, password, password_confirm):
        # Ожидаемые положительные тесты
        page = AuthPage(selenium)
        page.enter_first_name(firstname)
        page.enter_last_name(lastname)
        page.enter_auth_address(address)
        page.enter_auth_password(password)
        page.enter_auth_password_confirm(password_confirm)
        page.enter_auth_button()

        result = driver.find_element(*AuthLocators.msg_result_positive)

        assert result

        print(f'-Тест "{name_test}" выполнен: {result.text}')

    @pytest.mark.parametrize('name_test, firstname, lastname, address, password, password_confirm', data_for_test_negative())
    def test_auth_form_negative(self, selenium, driver, name_test, firstname, lastname, address, password, password_confirm):
        # Ожидаемые отрицательные тесты
        page = AuthPage(selenium)
        page.enter_first_name(firstname)
        page.enter_last_name(lastname)
        page.enter_auth_address(address)
        page.enter_auth_password(password)
        page.enter_auth_password_confirm(password_confirm)
        page.enter_auth_button()

        result = driver.find_element(*AuthLocators.msg_result_negative)

        assert result

        print(f'-Тест "{name_test}" выполнен: {result.text}')
