__author__ = 'Elvira'

import unittest
from selenium.webdriver import  DesiredCapabilities, Remote
from locators import locators

class ResultPage(object):
    def __init__(self, driver):
        self.driver = driver

    def result(self):
        return self.driver.find_element_by_class_name('campaign-title__name').text


class CreateGroupPage(object):
    CREATE = "toolbar__main-button"
    COMPANY_NAME = "base-setting__campaign-name__input"
    COMPANY_TYPE = "product-type-5212"
    PLATFORM = "pad-mobile_odkl_feed_abstract"
    TITLE = "//ul[@class_name='banner-form__list']/li[2]/input[1]"
    DESCRIPTION = "//ul[@class_name='banner-form__list']/li[3]/textarea[1]"
    TARGET = "//ul[@class_name='banner-form__list']/li[4]/span[2]/input[1]]"

    IMAGE1 = ".banner-form__img-file"

    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        btn_create_company = self.driver.find_element_by_class_name(self.CREATE)
        btn_create_company.click()

        set_name = self.driver.find_element_by_class_name(self.COMPANY_NAME)
        set_name.send_keys(locators['group_name'])

        btn_choose_company_type = self.driver.find_element_by_id(self.COMPANY_TYPE)
        btn_choose_company_type.click()

        btn_choose_platform = self.driver.find_element_by_id(self.PLATFORM)
        btn_choose_platform.click()

        set_title = self.driver.find_element_by_xpath(self.TITLE)
        set_title.send_keys("Header")

        set_description = self.driver.find_element_by_xpath(self.DESCRIPTION)
        set_description.send_keys("Text description blablabla")

        set_target = self.driver.find_element_by_xpath(self.TARGET)
        set_target.send_keys("http://www.odnoklassniki.ru/target")

        upload_min_img = self.driver.find_elements_by_class_name(self.IMAGE1)
        upload_min_img.send_keys('tests/source/1.jpg')

        upload_max_img = self.driver.find_element_by_xpath("//ul[@class_name='banner-form__list']/li[9]/form[1]/div[1]/input[1]")
        upload_max_img.send_keys('tests/source/2.jpg')

        btn_push = self.driver.find_element_by_xpath("//div[@class_name='banner-form__footer']/input[1]")
        btn_push.click()
    
        btn_choose_frame_age = self.driver.find_element_by_id("restrict-0+")
        btn_choose_frame_age.click()

        btn_choose_place = self.driver.find_element_by_xpath("ul[@id='campaign-setting__preset-list]/li[1]")
        btn_choose_place.click()

        btn_done_all = self.driver.find_element_by_class_name("main-button-new")
        btn_done_all.click()

        return ResultPage(self.driver).result()


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self, login, domain, password):
        self.driver.find_element_by_id("PH_authLink").click()
        self.driver.find_element_by_id("id_Login").send_keys(login)
        self.driver.find_element_by_id("id_Domain").send_keys(domain)
        self.driver.find_element_by_id("id_Password").send_keys(password)
        self.driver.find_element_by_xpath("//p[@id='gogogo']/input[1]").click()
        return CreateGroupPage(self.driver)

class CreateGroup(object):
    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        loginPage = LoginPage(self.driver)
        MakeGroupPage = loginPage.login(locators['login'], locators['domain'], locators['password'])
        result = MakeGroupPage.get_result()
        return result


class TestTarget(unittest.TestCase):

    def setUp(self):
        self.driver = Remote(
            desired_capabilities = DesiredCapabilities.CHROME.copy()
        )
        self.driver.get("https://target.mail.ru")
        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.close()

    def test_create_group(self):
        home = CreateGroup(self.driver)
        result = home.get_result()
        assert locators['group_name'] in result




if __name__ == "__main__":
    unittest.main()









