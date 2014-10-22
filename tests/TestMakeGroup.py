# -*- coding: utf-8 -*-

__author__ = 'Elvira'

import unittest
from selenium.webdriver import DesiredCapabilities, Remote
import os
from tests.Page import create_company, delete_company
from tests.Page.Page import CreateCompanyPage, CurrentPage, LoginPage, EditPage


class TestTarget(unittest.TestCase):
    LOGIN = 'tech-testing-ha2-9'
    DOMAIN = '@bk.ru'
    PASSWORD = os.environ.get('TTHA2PASSWORD')

    def setUp(self):
        self.created = False
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(30)
        auth_page = LoginPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.LOGIN)
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    def tearDown(self):
        if self.created:
            delete_company(self.driver)
        self.driver.quit()


    def test_login(self):
        EMAIL = self.LOGIN + self.DOMAIN

        top_email = CreateCompanyPage(self.driver).top_menu
        email = top_email.get_email
        assert EMAIL in email

    def test_place_select(self):
        RUS = u'Россия'

        create_page = CreateCompanyPage(self.driver)
        create_page.open()
        where_settings = create_page.where_form
        where_settings.choose_place()
        assert RUS in where_settings.get_chosen()


    def test_place_without_one(self):
        RUS = u'Россия (81 из 82)'

        create_page = CreateCompanyPage(self.driver)
        create_page.open()
        where_settings = create_page.where_form
        where_settings.choose_place()
        where_settings.choose_place_without_one_region()
        assert RUS in where_settings.get_chosen()


    def test_restrict(self):
        RESTRICT = u'12+'
        create_page = CreateCompanyPage(self.driver)
        create_page.open()
        whom_settings = create_page.whom_form
        whom_settings.choose_restrict()
        restrict = whom_settings.get_restrict()
        self.assertEquals(RESTRICT, restrict)

    def test_create(self):
        COMPANY_NAME = "Sunny"

        create_company(self.driver)
        self.created = True
        current_page = CurrentPage(self.driver)
        current_form = current_page.company
        assert COMPANY_NAME in current_form.get_title()


    def test_restrict_final(self):
        RESTRICT = u'12+'

        create_company(self.driver)
        self.created = True
        current = CurrentPage(self.driver)
        current_form = current.company
        current_form.edit()
        edit_form = EditPage(self.driver).edit_form
        restrict = edit_form.get_restrict()
        self.assertEquals(RESTRICT, restrict)


if __name__ == "__main__":
    unittest.main()









