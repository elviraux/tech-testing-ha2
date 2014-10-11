__author__ = 'Elvira'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.get('https://target.mail.ru/')

browser.implicitly_wait(30)


#Login
browser.find_element_by_id("PH_authLink").click()
browser.find_element_by_id("id_Login").send_keys("tech-testing-ha2-9")
browser.find_element_by_id("id_Domain").send_keys("@bk.ru")
browser.find_element_by_id("id_Password").send_keys("Pa$$w0rD-9")
browser.find_element_by_xpath("//p[@id='gogogo']/input[1]").click()


#create company
browser.find_element_by_class_name("toolbar__main-button").click()
browser.find_element_by_class_name("base-setting__campaign-name__input").send_keys("My company")
browser.find_element_by_id("product-type-5212").click()
browser.find_element_by_id("pad-mobile_odkl_feed_abstract").click()
browser.find_element_by_xpath("//ul[@class_name='banner-form__list']/li[2]/input[1]").send_keys("Header")
browser.find_element_by_xpath("//ul[@class_name='banner-form__list']/li[3]/textarea[1]").send_keys("Text description blablabla")
browser.find_element_by_xpath("//ul[@class_name='banner-form__list']/li[4]/span[2]/input[1]]").send_keys("http://www.odnoklassniki.ru/target")
# zdes' upload photo
# zdes' toje
browser.find_element_by_xpath("//div[@class_name='banner-form__footer']/input[1]").click()

browser.find_element_by_id("restrict-0+").click()
browser.find_element_by_xpath("ul[@id='campaign-setting__preset-list]/li[1]").click()
browser.find_element_by_class_name("main-button-new").click()








