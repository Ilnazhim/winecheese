import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from pages.data import DataPage
#import allure
from base.base_class import BaseClass


class CafePage(BaseClass):

    # Locators
    cafe_forma = "//span[@class='PageFooter_footer__link__2yvLx PageFooter_footer__link_black__tTQLE']"
    ask_cafe_forma = "//span[@class='PageFooter_footer__link__2yvLx']"
    name_fio = "//input[@name='fio']"
    phone = "//input[@name='phone']"
    guest = "//input[@name='guests']"
    time = "//input[@name='time']"
    date = "//input[@name='date']"
    telegram = "//input[@name='social']"
    whatsapp = "//span[@class='SocialsInput_socials__block_item__BxyrR SocialsInput_socials__block_item_disabled__ohsYS']"
    button_send_form = "//button[@class='Button_button__RNIJo']"
    close = "//button[@class='FormModal_modal__header_button__-X7yr']"


    # Getters
    def get_cafe_forma(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.cafe_forma)))

    def get_ask_cafe_forma(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ask_cafe_forma)))

    def get_name_fio(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_fio)))

    def get_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_guest(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.guest)))

    def get_time(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.time)))

    def get_date(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.date)))

    def get_whatsapp(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.whatsapp)))

    def get_telegram(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.telegram)))

    def get_send_form(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_send_form)))

    # Actions
    def click_cafe_forma(self):
        self.get_cafe_forma().click()
        print("Click cafe_forma")

    def click_ask_cafe_forma(self):
        self.get_ask_cafe_forma().click()
        print("Click cafe_forma")

    def input_name_fio(self):
        self.get_name_fio().send_keys(*DataPage.fio_cafe)
        print("input name")

    def input_ask_name_fio(self):
        self.get_name_fio().send_keys(*DataPage.fio_ask_cafe)
        print("input name")

    def input_phone(self):
        self.get_phone().send_keys(*DataPage.phone)
        print("input phone")

    def input_guest(self):
        self.get_guest().send_keys(*DataPage.guest)
        print("input guest")

    def input_time(self):
        self.get_time().send_keys(*DataPage.time)
        print("input time")

    def input_date(self):
        self.get_date().send_keys(*DataPage.date)
        print("input date")

    def input_telegram(self):
        self.get_telegram().send_keys(*DataPage.telegram)
        print("input telegram")

    def click_whatsapp(self):
        self.get_whatsapp().click()
        print("click_whatsapp")

    def click_button_send_form(self):
        self.get_send_form().click()
        print("Click button_send_form")


    # Metods
    def fill_cafe_forma(self):
        """Fill cafe forma"""
        #with allure.step("select_products_1"):
        Logger.add_start_step(method="cafe forma")

        self.get_current_url()
        self.click_cafe_forma()
        self.input_name_fio()
        self.input_phone()
        self.input_guest()
        self.input_time()
        self.input_date()
        self.click_whatsapp()
        self.click_button_send_form()
        Logger.add_end_step(url=self.browser.current_url, method="cafe forma")

    def fill_ask_cafe_forma(self):
        """Fill ask cafe forma"""
        #with allure.step("select_products_1"):
        Logger.add_start_step(method="cafe forma")

        self.get_current_url()
        self.click_ask_cafe_forma()
        self.input_ask_name_fio()
        self.input_phone()
        self.click_whatsapp()
        self.click_button_send_form()

        time.sleep(3)
        assert self.is_not_element_present(By.XPATH, self.close)
        Logger.add_end_step(url=self.browser.current_url, method="cafe forma")
