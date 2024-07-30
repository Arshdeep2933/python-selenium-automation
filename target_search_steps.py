from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    context.app.main_page.open()


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-9d95d074-3 kYwmqK']").click()
    sleep(6)
    context.app.header.search_product()


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_text, f'Expected {product} not in actual {actual_text}'
    context.app.search_results_page.verify_text()


