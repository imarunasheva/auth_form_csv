from selenium.webdriver.common.by import By


class AuthLocators:
   #локаторы поиска полей ввода регистрационных данных
   auth_register = (By.ID, 'kc-register')
   auth_first_name = (By.XPATH, '//input[@name="firstName"]')
   auth_last_name = (By.XPATH, '//input[@name="lastName"]')
   auth_address = (By.XPATH, '//input[@id="address"]')
   auth_password = (By.XPATH, '//input[@id="password"]')
   auth_password_confirm = (By.XPATH, '//input[@id="password-confirm"]')
   auth_button = (By.XPATH, '//button[@name="register"]')

   # локаторы поиска результатов регистрации, ошибок полей ввода, учетная запись существует
   msg_result_positive = (By.XPATH, '//*[contains(text(), "Kод подтверждения отправлен на адрес ")\
                   or @class="card-modal__title"]')
   msg_result_negative = (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]')
