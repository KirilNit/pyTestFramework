from driver import WebDriver

class LoggingPage:
    def __init__(self, invoke):
        self.driver = WebDriver(driver=invoke)
        self.logo = "//div[@class='content__title']"
        self.sign_in = "//ul[contains(@class, 'header__nav--ltr')]/descendant::a[contains(text(), 'Sign in') ]"
        self.password_field = "//div[@role='presentation']/descendant::input[@type='{}']"
        self.next_button = "//div[@id='{}']"
        self.email_or_phone = "//div[@role='presentation']/descendant::input[@aria-label='Email or phone']"



    def go_to_logging_page(self):
        self.driver.go_to_url('https://www.google.com/gmail/about/#')
        self.driver.wait_for_visibility_of_web_element(self.logo)
        self.driver.wait_for_visibility_of_web_element(self.sign_in)

    def do_login(self, email, password):
        self.driver.wait_for_web_element_to_be_located(self.sign_in)
        self.driver.click_web_element(self.sign_in)
        self.driver.wait_for_web_element_to_be_located(self.password_field.format('email'))
        self.driver.set_web_element_text(self.password_field.format('email'), email)
        self.driver.click_web_element(self.next_button.format('identifierNext'))
        self.driver.set_web_element_text(self.password_field.format('password'), password)
        self.driver.click_web_element(self.next_button.format('passwordNext'))
