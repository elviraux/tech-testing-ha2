__author__ = 'Elvira'

import unittest
from selenium.webdriver import  DesiredCapabilities, Remote
import os
#from selenium.webdriver.support.ui import Select, WebDriverWait
from tests.Page.Page import CreateCompanyPage, CurrentPage, LoginPage
from tests.Page.Component import WhereElement, WhomElement




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

    def test_create(self):
        COMPANY_NAME ="Sunny"

        create_page = CreateCompanyPage(self.driver)
        create_page.open()
        base_settings = create_page.base_form()
        base_settings.set_name(COMPANY_NAME)
        base_settings.choose_company_type()
        base_settings.choose_platform()

        whom_settings = create_page.whom_form()
        whom_settings.choose_restrict()


   # def test_restrict(self):


"""
    #def test(self):


        COMPANY_NAME ="Sunny"
        HEADER = "Header"
        DESCRIPTION = "Description"
        TARGET = "http://www.odnoklassniki.ru/target"
        IMG1 = 'tests/source/1.jpg'
        IMG2 = 'tests/source/2.jpg'


        current_page = CurrentPage(self.driver)
        create_page = CreateCompanyPage(self.driver)
        email = create_page.top_menu.get_email()

        create_form = create_page.create_form()
        create_form.create()
        create_form.set_name(COMPANY_NAME)
        create_form.choose_company_type()
        create_form.choose_platform()


      #  create_form.set_title(HEADER)
        #create_form.set_description(DESCRIPTION)
       # create_form.set_target(TARGET)
        #create_form.upload_min_img(IMG1)
        #create_form.upload_max_img(IMG2)
        create_form.choose_restrict()
       # create_form.choose_place()
        place_list  = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector('[data_name=where]')
        )








    #def test_create(self):
        #create_page = CreateCompanyPage(self.driver)

"""

if __name__ == "__main__":
    unittest.main()









