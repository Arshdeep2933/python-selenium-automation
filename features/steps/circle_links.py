from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then

@given('user is on target circle')
def open_target(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')



@then('make sure there are 10 links')
def num_links(context):
    links = context.driver.find_elements(By.XPATH, "//div[@class='cell-item-content']")
    assert len(links) == 10, f'expected 10 but got {len(links)}'