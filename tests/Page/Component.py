__author__ = 'Elvira'

from selenium.webdriver.support.ui import WebDriverWait

class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def wait(self, selector):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(selector)
        )



class LoginForm(Component):

    SUBMIT = "#gogogo>input"
    PASSWORD = "id_Password"
    LOGIN = "id_Login"
    DOMAIN = "id_Domain"

    def set_login(self, login):
        self.driver.find_element_by_id(self.LOGIN).send_keys(login)

    def set_domain(self, domain):
        self.driver.find_element_by_id(self.DOMAIN).send_keys(domain)

    def set_password(self, password):
        self.driver.find_element_by_id(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

class TopMenu(Component):
    EMAIL = '#PH_user-email'

    @property
    def get_email(self):
        return self.wait(self.EMAIL)

class BannerElement(Component):

    def get_form(self):
        return self.driver.find_element_by_class_name('banner-form')


class BaseSettingsElement(Component):
    CREATE = "toolbar__main-button"
    COMPANY_NAME = ".base-setting__campaign-name__input"
    COMPANY_TYPE = "#product-type-5212"
    PLATFORM = "pad-mobile_odkl_feed_abstract"

    def create(self):
        self.wait(self.CREATE).click()

    def set_name(self, company_name):
        element = self.driver.find_element_by_css_selector(self.COMPANY_NAME)
        element.clear()
        element.send_keys(company_name)

    def choose_company_type(self):
        self.driver.find_element_by_css_selector(self.COMPANY_TYPE).click()

    def choose_platform(self):
        self.driver.find_element_by_id(self.PLATFORM).click()


class BannerElement(Component):

    TITLE = '.banner-form__input[data_name=title]'
    DESCRIPTION = '.banner-form__input_text-area[data-name=text]'
    TARGET = '.banner-form__input[data-name=url]'

    IMAGE1 = '.banner-form__img-file'
    IMAGE2 = '.banner-form__img-file[data-name=promo_image]'
    AGE = "restrict-0+"
    PLACE_LIST = 'campaign-setting__preset-list'
    PLACE = '[data-name=russia]'

    #def get_banner(self):
        #return BannerElement(self.driver).get_form()

    def set_title(self, header):
        element = wait(self.TITLE)
        element.send_keys(header)

    def set_description(self, description):
        element = wait(self.DESCRIPTION)
        element.send_keys(description)

    def set_target(self, target):
        element = wait(self.TARGET)
        element.send_keys(target)

    def upload_min_img(self, img):
        element = wait(self.IMAGE1)
        element.send_keys(img)

    def upload_max_img(self, img):
        element = wait(self.IMAGE2)
        element.send_keys(img)


class WhomElement(Component):
    RESTRICT = 'campaign-setting__wrapper_restrict'
    SHOW_RESTRICT = '[data-node-id=restrict]'
    RESTRICT12 = 'restrict-12+'

    def choose_restrict(self):
        restrict = wait(self.RESTRICT)
        restrict.find_element_by_css_selector(self.SHOW_RESTRICT).click()
        restrict_btn =  wait(self.RESTRICT12)
        restrict_btn.click()


class WhereElement(Component):
    def choose_place(self):
        place_list  = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_class_name(self.PLACE_LIST)
        )

