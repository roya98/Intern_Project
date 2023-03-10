from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# $x("//a[@class='header__heading-link link link--text focus-inset']")
# $$("#healthytext")



@given('Open Search Result for Cure')
def open_cure_page(context):
    context.app.cure_page.open_url('/search?q=cure')


@when('Click on CureSkin logo in the header')
def click_on_logo(context):
    context.app.cure_page.click_on_logo()




#$x("//span[@id='ProductCountDesktop' and contains(text(), '23')]")

@then('Verify 23 results')
def verify_cure_results(context):
    context.app.cure_page.verify_cure_results()



@then('Verify first results have name, image, and price')
def verify_infor_img(context):
    context.app.cure_page.verify_infor_img()









