import imp
from behave import *
from pythonBDD.configuration.Utilities.customlogger import LogGen
from pythonBDD.configuration.Utilities.readproperty import ReadConfig
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


baseURL = ReadConfig.getURL()

mylogger =LogGen.loggen()


@given(u'Launch the browser')
def step_impl(context):
    context.driver =webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("******Driver Initialised****")
    context.driver.get(baseURL)
    mylogger.info("****Browser launched*")


@then(u'verify the page title')
def step_impl(context):
    actual_title =context.driver.title
    expected_title ="Home Page"

    if actual_title ==expected_title:
        assert True
        mylogger.inf("******Title matched***")

    else:
        mylogger.info("****Title not matched**")
        assert False

@then(u'close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info("*****Browser Closed******")
