from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('click on add cart button')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[id*='addToCartButtonOrTextIdFor89231945']").click()
    sleep(10)


# def open_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[class='sc-9306beff-0 sc-e6042511-0 dfqbQr ibmrHV']").click()


@when('user is on product page')
def product_page(context):
    context.driver.get('https://www.target.com/p/A-54551690')


@then('user can select colors')
def select_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(By.CSS_SELECTOR, '[aria-label="Carousel"] ul li')
    for color in colors[0:4]:
        color.click()
        sleep(3)
        selected_color = context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] div').text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'








