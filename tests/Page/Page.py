__author__ = 'Elvira'

import urlparse
from tests.Page.Component import TopMenu, BaseSettingsElement, LoginForm, BannerElement, WhereElement, WhomElement


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

    def form(self):
        return LoginForm(self.driver)

class CurrentPage(Page):
    PATH = 'ads/campaigns/'


    def top_menu(self):
        return TopMenu(self.driver)


class CreateCompanyPage(Page):
    PATH = 'ads/create/'


    def top_menu(self):
        return TopMenu(self.driver)


    def base_form(self):
        return BaseSettingsElement(self.driver)


    def banner_form(self):
        return BannerElement(self.driver)

    @property
    def whom_form(self):
        return WhomElement(self.driver)

    @property
    def where_form(self):
        return WhereElement(self.driver)