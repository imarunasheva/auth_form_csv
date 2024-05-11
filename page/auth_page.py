from .base_page import BasePage
from .locators import AuthLocators
import time


class AuthPage(BasePage):

   def __init__(self, driver, timeout=15):
       super().__init__(driver, timeout)
       driver.get("https://b2c.passport.rt.ru/")
       time.sleep(10)
       driver.find_element(*AuthLocators.auth_register).click()

       # создаем необходимые элементы
       self.first_name = driver.find_element(*AuthLocators.auth_first_name)
       self.last_name = driver.find_element(*AuthLocators.auth_last_name)
       self.auth_address = driver.find_element(*AuthLocators.auth_address)
       self.auth_password = driver.find_element(*AuthLocators.auth_password)
       self.auth_password_confirm = driver.find_element(*AuthLocators.auth_password_confirm)
       self.auth_button = driver.find_element(*AuthLocators.auth_button)


   def enter_first_name(self, value):
       self.first_name.send_keys(value)

   def enter_last_name(self, value):
       self.last_name.send_keys(value)

   def enter_auth_address(self, value):
       self.auth_address.send_keys(value)

   def enter_auth_password(self, value):
       self.auth_password.send_keys(value)

   def enter_auth_password_confirm(self, value):
       self.auth_password_confirm.send_keys(value)

   def enter_auth_button(self):
       self.auth_button.click()
