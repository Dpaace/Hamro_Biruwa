import imp
from turtle import home
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pythonBDD.configuration.Pages.HomePage import HomePage
from pythonBDD.configuration.Utilities.customlogger import LogGen
from pythonBDD.configuration.Utilities.readproperty import ReadConfig
import time

baseURL =ReadConfig.getURL()
mylogger = LogGen.loggen()

@given(u'Launch the App')
def step_imp(context):
    mylogger.info("**Passing credentials")
    global loginpage
    global homepage 

    homepage=HomePage(context.driver)
    homepage.clickOnLogin()
    
    loginpage =LoginPage(context.driver)
    user =ReadConfig.getUserName()
    pwd =ReadConfig.getPassword()
    time.sleep(3)
    loginpage.setusername(user)
    loginpage.setpassword(pwd)
    mylogger.info("***Entered Credentials***")


@then(u'click login')
def step_impl(context):
    loginpage.clickOnLogin()
    mylogger.info("***Login button click")

    
@then(u'close the App')
def step_impl(context):
    context.driver.close()

