Тесты выполняют тестирование формы регистрации, проверяют поля формы на предмет ввода допустимых/необходимых данных пользователя при регистрации профиля на сайте Ростелеком, соответствие вводимых символов требованиям, отраженным в брифе от заказчика.

Тесты используют на ввод тестовые данные из cvs-файлов (values_negative.csv, values_positive.csv), сгруппированных по ожидаемому результату (положительному/отрицательному).

В директории /page находятся файлы сценария страницы авторизации, базовой страницы, локаторы.

В директории /tests находятся тесты и csv-файлы с тестовыми данными.

Для запуска тестов требуется предварительная инсталляция:
-	 Pytest == 6.2.5
-	Selenium == 4.9.0
-	Pytest-selenium == 4.0.0
-	Webdriver-manager

Команды для запуска тестов:

python -m pytest tests/test_auth_form.py

python -m pytest tests/test_auth_form.py::TestAuthForm::test_auth_form_positive

python -m pytest tests/test_auth_form.py::TestAuthForm::test_auth_form_negative
