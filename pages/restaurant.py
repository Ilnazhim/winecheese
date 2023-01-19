import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from pages.data import DataPage
#import allure
from base.base_class import BaseClass


class RestaurantPage(BaseClass):

    # Locators
    restaurant_forma = "//span[@class='PageFooter_footer__link__2yvLx PageFooter_footer__link_red__aPzDU']"
    ask_restaurant_forma = "//span[@class='PageFooter_footer__link__2yvLx']"
    name_fio = "//input[@name='fio']"
    phone = "//input[@name='phone']"
    guest = "//input[@name='guests']"
    time = "//input[@name='time']"
    date = "//input[@name='date']"
    telegram = "//input[@name='social']"
    whatsapp = "//span[@class='SocialsInput_socials__block_item__BxyrR SocialsInput_socials__block_item_active__YXHIy']"
    button_send_form = "//button[@class='Button_button__RNIJo']"
    close = "//button[@class='FormModal_modal__header_button__-X7yr']"

    about_rest = "//h2[@class='TitleBlock_page_title__-dRZO AboutBlock_about__title__tAmOG']"
    menu_rest = "//a[@href='https://backapiwinecheese.ru/backend/uploads/menu-1.pdf']"


    # Getters
    def get_restaurant_forma(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.restaurant_forma)))

    def get_ask_restaurant_forma(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ask_restaurant_forma)))
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

    def get_telegram(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.telegram)))

    def get_send_form(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_send_form)))

    def get_menu_rest(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_rest)))

    def get_about_rest(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_rest)))

    # Actions
    def click_restaurant_forma(self):
        self.get_restaurant_forma().click()
        print("Click restaurant_forma")

    def input_name_fio(self):
        self.get_name_fio().send_keys(*DataPage.fio_rest)
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

    def click_button_send_form(self):
        self.get_send_form().click()
        print("Click button_send_form")

    def click_ask_restaurant_forma(self):
        self.get_ask_restaurant_forma().click()
        print("Click restaurant_forma")

    def input_name_fio_ask(self):
        self.get_name_fio().send_keys(*DataPage.fio_ask_rest)
        print("input name")

    def click_about_rest(self):
        self.get_about_rest().click()
        print("Click about_rest")

    def click_menu_rest(self):
        self.get_menu_rest().click()
        print("Click menu_rest")


    # Metods
    def fill_restaurant_forma(self):
        """Fill restaurant forma"""
        #with allure.step("select_products_1"):
        Logger.add_start_step(method="restaurant forma")

        self.get_current_url()
        self.click_restaurant_forma()
        self.input_name_fio()
        self.input_phone()
        self.input_guest()
        self.input_time()
        self.input_date()
        self.input_telegram()
        self.click_button_send_form()
        Logger.add_end_step(url=self.browser.current_url, method="restaurant forma")

    def fill_ask_restaurant_forma(self):
        """Fill ask restaurant forma"""
        # with allure.step("select_products_1"):
        Logger.add_start_step(method="restaurant ask forma")

        self.get_current_url()
        self.click_ask_restaurant_forma()
        self.input_name_fio_ask()
        self.input_phone()
        self.input_telegram()
        self.click_button_send_form()

        time.sleep(3)
        assert self.is_not_element_present(By.XPATH, self.close)
        Logger.add_end_step(url=self.browser.current_url, method="restaurant ask forma")


    def seen_menu_rest(self):

        self.click_about_rest()
        self.click_menu_rest()
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        url = self.browser.current_url
        print(url)
        time.sleep(4)
        assert url == "https://backapiwinecheese.ru/backend/uploads/menu-1.pdf"

