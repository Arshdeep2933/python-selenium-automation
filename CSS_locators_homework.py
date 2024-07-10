from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, "[class='a-icon a-icon-logo']")

# CREATE ACCOUNT BUTTON
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")

# your name
driver.find_element(By.CSS_SELECTOR, "[type='text']")

# Email
driver.find_element(By.CSS_SELECTOR, "[type='email']")

# password
driver.find_element(By.CSS_SELECTOR, "[aria-describedby='passwordHelp_ap_password']")

# password confirm
driver.find_element(By.CSS_SELECTOR, "[class='a-input-text a-span12 auth-required-field auth-require-fields-match']")

# Continue button
driver.find_element(By.CSS_SELECTOR, "#auth-continue-announce")

# CONTNUE OF USE
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?']")

# privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Sign in
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")