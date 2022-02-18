class HomePage:
    link_login_xpath ='//*[@id="navbarSupportedContent"]/ul/li[8]/a/i'

    def __init__(self, driver):
        self.driver = driver

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.link_login_xpath).click()  
