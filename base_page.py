from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def get_current_window(self):
        window = self.driver.current_window_handle
        print('Current window:', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        print(f'All windows {windows}')
        self.driver.switch_to.window(windows[1])
        print(f'Switched to window => {windows[1]}')

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print(f'Switched to window => {window_id}')

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self , text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_partial_url(self, url):
        self.verify_partial_url(url)

    def close(self):
        self.driver.close()