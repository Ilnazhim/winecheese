import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from pages.data import DataPage
#import allure
from base.base_class import BaseClass


class MerchPage(BaseClass):

    # Locators
    ask_merch_forma = "//span[@class='PageFooter_footer__link__2yvLx']"
    order_shorts = "//img[@src='https://backapiwinecheese.ru/uploads/attachments/gallery-images/8/original/639ac87241c73154.jpg']"

    name_fio = "//input[@name='fio']"
    phone = "//input[@name='phone']"
    telegram = "//input[@name='social']"
    whatsapp = "//span[@class='SocialsInput_socials__block_item__BxyrR SocialsInput_socials__block_item_active__YXHIy']"
    button_send_form = "//button[@class='Button_button__RNIJo']"
    close = "//button[@class='FormModal_modal__header_button__-X7yr']"

    # Getters
    def get_ask_merch_forma(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ask_merch_forma)))

    def get_order_shorts(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_shorts)))

    def get_name_fio(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_fio)))

    def get_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_telegram(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.telegram)))

    def get_send_form(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_send_form)))

    # Actions

    def click_ask_merch_forma(self):
        self.get_ask_merch_forma().click()
        print("Click ask_espresso_forma")

    def click_order_shorts_forma(self):
        self.get_order_shorts().click()
        print("Click order_shorts")

    def input_name_fio_ask(self):
        self.get_name_fio().send_keys(*DataPage.fio_ask_merch)
        print("input name")

    def input_name_fio_order_shorts(self):
        self.get_name_fio().send_keys(*DataPage.fio_merch_order_shorts)
        print("input merch_order_shorts")

    def input_phone(self):
        self.get_phone().send_keys(*DataPage.phone)
        print("input phone")

    def input_telegram(self):
        self.get_telegram().send_keys(*DataPage.telegram)
        print("input telegram")

    def click_button_send_form(self):
        self.get_send_form().click()
        print("Click button_send_form")

    # Metods
    def fill_ask_merch_forma(self):
        """Fill ask merch forma"""
        # with allure.step("select_products_1"):
        Logger.add_start_step(method="merch ask forma")

        self.get_current_url()
        self.click_ask_merch_forma()
        self.input_name_fio_ask()
        self.input_phone()
        self.input_telegram()
        self.click_button_send_form()
        Logger.add_end_step(url=self.browser.current_url, method="merch ask forma")

    def fill_order_shorts_form(self):
        """Fill order_shorts forma"""
        # with allure.step("select_products_1"):
        Logger.add_start_step(method="order_shorts forma")

        self.get_current_url()
        self.click_order_shorts_forma()
        self.input_name_fio_order_shorts()
        self.input_phone()
        self.input_telegram()
        self.click_button_send_form()

        time.sleep(3)
        assert self.is_not_element_present(By.XPATH, self.close)
        Logger.add_end_step(url=self.browser.current_url, method="order_shorts forma")
