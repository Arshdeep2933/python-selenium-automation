from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignInPage(Page):
    SIGNIN_HEADER = (By.CSS_SELECTOR, 'h1 span')

    def verify_signin_page_opened(self):
        sleep(15)
        expected_text = 'Sign into your Target account'
        actual_text = self.find_element(*self.SIGNIN_HEADER).text
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'