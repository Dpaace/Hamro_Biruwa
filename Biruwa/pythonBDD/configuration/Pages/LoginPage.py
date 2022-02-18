class LoginPage:

    txt_username_id ="userName"
    txt_password_id="passWord"
    btn_login_xpath = '//*[@id="btn_login"]'


    def __init__(self, driver):
       self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)   

    def setpassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)   
    
    def clickOnLogin(self):
        self.driver.find_element_by_id(self.btn_login_xpath).click()