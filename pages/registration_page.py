from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self,driver):
        self.driver = driver
        self.firstname_txt  = (By.ID,'input-firstname')
        self.lastname_txt = (By.ID,'input-lastname')
        self.email_txt = (By.ID,'input-email')
        self.telephone_txt = (By.ID,'input-telephone')
        self.password_txt = (By.ID,'input-password')
        self.confirm_password_txt = (By.ID,'input-confirm')
        self.yes_newsletter_radio = (By.XPATH,"//input[@name='newsletter' and @value='1']")
        self.no_newsletter_radio = (By.XPATH,"//input[@name='newsletter' and @value='0']")

    def type_firstname(self,firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)

    def type_lastname(self,lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)

    def type_email(self,email):
        self.driver.find_element(*self.email).send_keys(email)

    def type_telephone(self,telephone):
        self.driver.find_element(*self.telephone).send_keys(telephone)

    def type_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def type_confirm_password(self,confirm):
        self.driver.find_element(*self.confirm_password).send_keys(confirm)


    def click_yes_subscribe(self):
        self.driver.find_element(*self.yes_newsletter_radio).click()

    def click_no_subscrive(self):
        self.driver.find_element(*self.no_newsletter_radio).click()
