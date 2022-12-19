from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# $x("//*[@class='modal__toggle-open icon icon-search']")


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_url()


@when('From page footer, click Search')
def click_search(context):
    context.app.main_page.click_search()


@then('Verify search page opened')
def verify_open_search(context):
    context.app.main_page.verify_open_search()




