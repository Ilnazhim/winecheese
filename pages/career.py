import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser
from utilities.logger import Logger
from pages.data import DataPage
#import allure
from base.base_class import BaseClass


class CareerPage(BaseClass):

    # Locators
    career_form = "//h4[@class='JobsBlock_content__title__-m5XF']"

    name_fio = "//input[@name='fio']"
    phone = "//input[@name='phone']"
    telegram = "//input[@name='social']"
    whatsapp = "//span[@class='SocialsInput_socials__block_item__BxyrR SocialsInput_socials__block_item_active__YXHIy']"
    link_field = "//input[@name='link_resume']"
    message = "//textarea[@name='text']"
    button_send_form = "//button[@class='Button_button__RNIJo']"
    close = "//button[@class='FormModal_modal__header_button__-X7yr']"

    # Getters

    def get_career_form(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.career_form)))

    def get_name_fio(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_fio)))

    def get_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_telegram(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.telegram)))

    def get_link_field(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_field)))

    def get_message(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.message)))

    def get_send_form(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_send_form)))

    # Actions

    def click_career_form(self):
        self.get_career_form().click()
        print("Click career_form")

    def input_name_fio_career_form(self):
        self.get_name_fio().send_keys(*DataPage.fio_career_form)
        print("input name_fio_career_form")

    def input_phone(self):
        self.get_phone().send_keys(*DataPage.phone)
        print("input phone")

    def input_telegram(self):
        self.get_telegram().send_keys(*DataPage.telegram)
        print("input telegram")

    def input_link_field(self):
        self.get_link_field().send_keys(*DataPage.link_field)
        print("input link_field")

    def input_message(self):
        self.get_message().send_keys(*DataPage.message)
        print("input message")

    def click_button_send_form(self):
        self.get_send_form().click()
        print("Click button_send_form")


    # Metods
    def fill_career_form(self):
        """Fill career_form"""
        # with allure.step("select_products_1"):
        Logger.add_start_step(method="career_form")

        self.get_current_url()
        self.click_career_form()
        self.input_name_fio_career_form()
        self.input_phone()
        self.input_telegram()
        self.input_link_field()
        self.input_message()
        time.sleep(3)
        self.click_button_send_form()

        time.sleep(3)
        assert self.is_not_element_present(By.XPATH, self.close)
        Logger.add_end_step(url=self.browser.current_url, method="career_form")
