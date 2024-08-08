from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    sign_in_button = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"] span')
    SIGNIN_SIDENAV_BTN = (By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"] span')
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_signin(self):
        self.click(*self.sign_in_button)
        #self.find_element(*self.sign_in_button).click()

    def click_signin_sidenav(self):
        self.click(*self.SIGNIN_SIDENAV_BTN)

