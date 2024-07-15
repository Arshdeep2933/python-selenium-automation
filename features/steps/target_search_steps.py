from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for Product')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-9d95d074-3 kYwmqK']").click()
    sleep(6)

@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'
