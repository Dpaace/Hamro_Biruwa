from msilib.schema import ControlEvent
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




@given(u'Launch Google Chrome')
def open_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
   
@when(u'Open HamroBiruwa Homepage')
def openHome(context):
    context.driver.get("http://127.0.0.1:8000/")
    
@then(u'Verify that the logo is present on webpage')
def verifying(context):
    status =context.driver.find_element_by_xpath("/html/body/nav/div/a/img").is_displayed()
    assert status is True
   

@then(u'Close Browser')
def closeBrowser(context):
    context.driver.close()
    