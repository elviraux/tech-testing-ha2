__author__ = 'Elvira'
from Page import CurrentPage, CreateCompanyPage

def delete_company(driver):
    deletep = CurrentPage(driver)
    deletep.open()
    delete = deletep.company
    delete.delete()

def create_company(driver):
    COMPANY_NAME = "Sunny"

    create_page = CreateCompanyPage(driver)
    create_page.open()
    create_form = create_page.base_form
    create_form.set_name(COMPANY_NAME)
    create_form.choose_company_type()
    create_form.choose_platform()
    create_form = create_page.banner_form
    create_form.create_banner()
    whom_settings = create_page.whom_form
    whom_settings.choose_restrict()
    where_settings = create_page.where_form
    where_settings.choose_place()
    submit_form = create_page.submit_form
    submit_form.submit_create_company()

