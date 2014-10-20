__author__ = 'Elvira'

import unittest
from selenium.webdriver import  DesiredCapabilities, Remote
import os
#from selenium.webdriver.support.ui import Select, WebDriverWait
from tests.Page.Page import CreateCompanyPage, CurrentPage, LoginPage




class TestTarget(unittest.TestCase):

    def setUp(self):
        LOGIN = 'tech-testing-ha2-9'
        DOMAIN ='@bk.ru'
        PASSWORD = os.environ.get('TTHA2PASSWORD')

        self.driver = Remote(
            desired_capabilities = DesiredCapabilities.FIREFOX.copy()
        )
        self.driver.get("https://target.mail.ru")
        self.driver.implicitly_wait(30)
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form()
        auth_form.set_login(LOGIN)
        auth_form.set_domain(DOMAIN)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

   #def tearDown(self):
        #self.driver.close()
    """
    def test_login(self):
        LOGIN = 'tech-testing-ha2-9'
        DOMAIN ='@bk.ru'
        EMAIL = LOGIN + DOMAIN
        curr_page = CurrentPage(self.driver)
        curr_page.open()
        top_email = curr_page.top_menu()
        email = top_email.get_email().text
        assert EMAIL in email
    """
    """
    def test_create(self):
        COMPANY_NAME ="Sunny"

        create_page = CreateCompanyPage(self.driver)
        create_page.open()
        base_settings = create_page.base_form()
        base_settings.set_name(COMPANY_NAME)
        base_settings.choose_company_type()
        base_settings.choose_platform()

        whom_settings = create_page.whom_form
        whom_settings.choose_restrict()

        where_settings = create_page.where_form
        where_settings.choose_place()


    """

    def test(self):


        create_page = CreateCompanyPage(self.driver)
        create_page.open()
        create_form = create_page.base_form()
        create_form.choose_company_type()
        create_form.choose_platform()
        create_form = create_page.banner_form()
        create_form.create_banner()










    #def test_create(self):
        #create_page = CreateCompanyPage(self.driver)



if __name__ == "__main__":
    unittest.main()









