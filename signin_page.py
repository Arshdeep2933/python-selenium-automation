from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(Page):
    SIGNIN_HEADER = (By.CSS_SELECTOR, 'h1 span')
    TERMS_CONDITIONS = (By.CSS_SELECTOR, "[aria-label = 'terms & conditions - opens in a new window']")



    def verify_signin_page_opened(self):
        sleep(15)
        expected_text = 'Sign into your Target account'
        actual_text = self.find_element(*self.SIGNIN_HEADER).text
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

    def open_signin_page(self):
        self.open_url('https://www.target.com/login')
    def click_term_cond(self):
        self.click(*self.TERMS_CONDITIONS)

    def terms_and_cond_page_opened(self):
       self.verify_partial_url()


