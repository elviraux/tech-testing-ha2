__author__ = 'Elvira'

from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def wait(self, DRIVER, selector):
        return WebDriverWait(DRIVER, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(selector)
        )

    def wait_id(self, selector):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(selector)
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
        return self.wait(self.driver, self.EMAIL)

class BannerElement(Component):

    TITLE = '.banner-form__input[data_name=title]'
    DESCRIPTION = '.banner-form__input_text-area[data-name=text]'
    TARGET = 'input.banner-form__input-no-utm'
    IMAGE1 = '.banner-form__img-file'
    IMAGE2 = '.banner-form__img-file[data-name=promo_image]'
    SAVE = '.banner-form__save-button'

    @staticmethod
    def waiting(driver):
        IMG = '.banner-preview__img'
        banners = driver.find_elements_by_css_selector(IMG)
        for banner in banners:
            if banner.value_of_css_property("display") == 'block':
                return banner

    def banner(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.banner-form')
        )

    def set_title(self, header):

        banner_title = WebDriverWait(self.banner(), 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('input[data-name=title]')
        )
        banner_title.send_keys('TITLE OLOLOLO')

    def set_description(self, description):
        element = self.wait(self.banner(), self.DESCRIPTION)
        element.send_keys(description)

    def set_target(self, url):
        elements = WebDriverWait(self.banner(), 30, 0.1).until(
            lambda d: d.find_elements_by_css_selector(self.TARGET)
        )
        target = None
        for e in elements:
            if e.is_displayed():
                target = e
                break
        if target is None:
            raise Exception("Couldn't find element")

        target.send_keys(url)

    def upload_min_img(self, img):
        BANNER_PREVIEW ='.banner-preview__middleleft'
        CROPPER = '.image-cropper__save'

        element = self.wait(self.banner(), self.IMAGE1)
        element.send_keys(img)
        self.wait(self.driver, CROPPER).click()
        img1 = self.banner().find_element_by_css_selector(BANNER_PREVIEW)
        WebDriverWait(img1, 30, 0.1).until(
            self.waiting
        )

    def upload_max_img(self, img):
        BANNER_PREVIEW = '.banner-preview__bottom'
        CROPPER = '.image-cropper__save'

        element = self.wait(self.banner(), self.IMAGE2)
        element.send_keys(img)
        self.wait(self.driver, CROPPER).click()

        img2 = self.banner().find_element_by_css_selector(BANNER_PREVIEW)
        WebDriverWait(img2, 30, 0.1).until(
            self.waiting
        )



    def save_banner(self):
        elements = WebDriverWait(self.driver, 30, 0.1).until(
            lambda p: p.find_elements_by_css_selector(self.SAVE)
        )
        button = None
        for e in elements:
            if e.is_displayed():
                button = e
                break
        if button is None:
            raise Exception("Couldn't find element")
        button.click()


    def create_banner(self):
        HEADER = "Header"
        DESCRIPTION = "Description"
        TARGET = "http://www.odnoklassniki.ru/target"
        IMG1 = 'tests/source/1.jpg'
        IMG2 = 'tests/source/2.jpg'

        self.set_title(HEADER)
        self.set_description(DESCRIPTION)
        self.set_target(TARGET)
        self.upload_min_img(IMG1)
        self.upload_max_img(IMG2)
        self.save_banner()




class BaseSettingsElement(Component):
    CREATE = "toolbar__main-button"
    COMPANY_NAME = ".base-setting__campaign-name__input"
    COMPANY_TYPE = "#product-type-5212"
    PLATFORM = "pad-mobile_odkl_feed_abstract"

    def create(self):
        self.wait(self.driver, self.CREATE).click()

    def set_name(self, company_name):
        element = self.driver.find_element_by_css_selector(self.COMPANY_NAME)
        element.clear()
        element.send_keys(company_name)

    def choose_company_type(self):
        self.driver.find_element_by_css_selector(self.COMPANY_TYPE).click()

    def choose_platform(self):
        self.driver.find_element_by_id(self.PLATFORM).click()



class WhomElement(Component):
    RESTRICT = '.campaign-setting__wrapper_restrict'
    SHOW_RESTRICT = '[data-node-id=restrict]'
    RESTRICT12 = 'restrict-12+'

    def choose_restrict(self):
        restrict = self.wait(self.RESTRICT)
        restrict.find_element_by_css_selector(self.SHOW_RESTRICT).click()
        restrict_btn =  self.wait_id(self.RESTRICT12)
        restrict_btn.click()


class WhereElement(Component):
    PLACE_LIST = '.campaign-setting__preset-list'
    PLACE = 'li.campaign-setting__preset[data-value=188]'
    def choose_place(self):


        place_list = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.campaign-setting__preset-list')
        )
        place_element = WebDriverWait(place_list, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('[data-name=russia]')
        )

        place_wrapper  =  WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.campaign-setting__wrapper_regions')
        )
        place_rus = WebDriverWait(place_wrapper, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.tree__node[id=regions188]')
        )
        place_rus_btn = WebDriverWait(place_rus, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.tree__node__input')
        )
        if not place_rus_btn.is_selected():
            place_rus_btn.click()
            place_rus_btn.get_attribute('checked')




