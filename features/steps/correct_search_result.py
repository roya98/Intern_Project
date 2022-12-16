from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#CURE_RESULT = (By.XPATH, "//span[@id='ProductCountDesktop' and contains(text(), '23')]")

@given('Open Search Result for Cure')
def open_cure_page(context):
    context.app.cure_page.open_url('/search?q=cure')





#$x("//span[@id='ProductCountDesktop' and contains(text(), '23')]")

@then('Verify 23 results')
def verify_cure_results(context):
    context.app.cure_page.verify_cure_results()



