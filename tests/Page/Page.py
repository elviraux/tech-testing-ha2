__author__ = 'Elvira'

import urlparse
from tests.Page.Component import TopMenu, BaseSettingsElement, LoginForm, BannerElement, WhereElement, WhomElement, SubmitButtonForm, Company, EditForm


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class LoginPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return LoginForm(self.driver)

class CurrentPage(Page):
    PATH = 'ads/campaigns/'

    @property
    def company(self):
        return Company(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class CreateCompanyPage(Page):
    PATH = 'ads/create/'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def base_form(self):
        return BaseSettingsElement(self.driver)

    @property
    def banner_form(self):
        return BannerElement(self.driver)

    @property
    def whom_form(self):
        return WhomElement(self.driver)

    @property
    def where_form(self):
        return WhereElement(self.driver)

    @property
    def submit_form(self):
        return SubmitButtonForm(self.driver)


class EditPage(Page):

    @property
    def edit_form(self):
        return EditForm(self.driver)


