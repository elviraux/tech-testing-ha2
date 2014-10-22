__author__ = 'Elvira'

from selenium.webdriver.support.ui import WebDriverWait

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

class Company(Component):
    COMPANYNAME = '.campaign-title__name'
    PLACE = '.campaign-title__settings.js-campaign-title-settings'
    EDIT = '.control__link_edit'
    RESTRICTION = '[data-node-id="restrict"]'
    DELETE = '.control__preset_delete'

    def get_title(self):
        return self.driver.find_element_by_css_selector(self.COMPANYNAME).text

    def get_place(self):
        return self.driver.find_element_by_css_selector(self.PLACE)

    def edit(self):

        self.driver.find_element_by_css_selector(self.EDIT).click()

    def get_restrictions(self):
        restrict = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.RESTRICTION)
        )
        return restrict.text

    def delete(self):
        self.driver.find_element_by_css_selector(self.DELETE).click()


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
        return self.wait(self.driver, self.EMAIL).text

class BannerElement(Component):
    TITLE = 'input[data-name=title]'
    DESCRIPTION = '.banner-form__input_text-area[data-name=text]'
    TARGET = 'input.banner-form__input-no-utm'
    IMAGE1 = '.banner-form__img-file'
    IMAGE2 = '.banner-form__img-file[data-name=promo_image]'
    SAVE = '.banner-form__save-button'
    BANNER_PREVIEW ='.banner-preview__middleleft'
    CROPPER = '.image-cropper__save'

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
            lambda d: d.find_element_by_css_selector(self.TITLE)
        )
        banner_title.send_keys(header)

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
        element = self.wait(self.banner(), self.IMAGE1)
        element.send_keys(img)
        self.wait(self.driver, self.CROPPER).click()
        img1 = self.banner().find_element_by_css_selector(self.BANNER_PREVIEW)
        WebDriverWait(img1, 30, 0.1).until(
            self.waiting
        )

    def upload_max_img(self, img):
        BANNER_PREVIEW = '.banner-preview__bottom'

        element = self.wait(self.banner(), self.IMAGE2)
        element.send_keys(img)
        self.wait(self.driver, self.CROPPER).click()

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
        HEADER = "TITLE OLOLOLO"
        DESCRIPTION = "Description blablablablablablabla"
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
        restrict = self.wait(self.driver, self.RESTRICT)
        restrict.find_element_by_css_selector(self.SHOW_RESTRICT).click()
        self.wait_id(self.RESTRICT12).click()


    def get_restrict(self):
        restrict = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.SHOW_RESTRICT)
        )
        return restrict.text


class WhereElement(Component):
    PLACE_WRAPPER = '.campaign-setting__wrapper_regions'
    PLACE_LIST = '.campaign-setting__preset-list'
    PLACE_RUS = '.tree__node[id=regions188]'
    PLACE_ICON = '.tree__node__collapse-icon'
    AMUR = 'li[id = regions10]'
    CHECKBOX ='.tree__node__input'
    CHOSENWRAPPER = '.projection__wrapper'
    ITEM = '.projection__geography-targeting__text'


    def choose_place(self):
        place_wrapper  =  WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PLACE_WRAPPER)
        )
        place_rus = WebDriverWait(place_wrapper, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PLACE_RUS)
        )
        place_rus_btn = WebDriverWait(place_rus, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CHECKBOX)
        )
        if not place_rus_btn.is_selected():
            place_rus_btn.click()
            place_rus_btn.get_attribute('checked')


    def choose_place_without_one_region(self):
        place_wrapper  =  WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PLACE_WRAPPER)
        )
        place_rus = WebDriverWait(place_wrapper, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PLACE_RUS)
        )
        place_rus.find_element_by_css_selector(self.PLACE_ICON).click()
        wrapper = place_rus.find_element_by_css_selector(self.AMUR)
        place_amur = WebDriverWait(wrapper, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CHECKBOX)
        )
        if place_amur.is_selected():
            place_amur.click()


    def get_chosen(self):
        place_wrapper  =  self.wait(self.driver, self.CHOSENWRAPPER)
        return self.wait(place_wrapper, self.ITEM).text


class SubmitButtonForm(Component):
    BUTTON = '.main-button-new'

    def submit_create_company(self):
        self.driver.find_element_by_css_selector(self.BUTTON).click()


class EditForm(Component):
    RESTRICTION = '[data-node-id="restrict"]'

    def get_restrict(self):
        restrict = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.RESTRICTION)
        )
        return restrict.text