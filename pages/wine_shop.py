import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser
from utilities.logger import Logger
from pages.data import DataPage
#import allure
from base.base_class import BaseClass


class WineShopPage(BaseClass):

    # Locators
    button_yes_18_old = "//button[@class='CheckAge_page__btn__w0129']"
    ask_wine_shop_forma = "//span[@class='PageFooter_footer__link__2yvLx']"
    menu = "//h2"
    menu_2 = "//div[@class='AdvBlock_content__q7QRV undefined']"

    label = ActionChains(browser)

    ask_wine_forma = "//p[@class='ProductCard_card__info__wgxIR']"
    ask_wine_forma_cart = "//div[@class='Modal_content__link__+sw8X']"

    name_fio = "//input[@name='fio']"
    phone = "//input[@name='phone']"
    telegram = "//input[@name='social']"
    whatsapp = "//span[@class='SocialsInput_socials__block_item__BxyrR SocialsInput_socials__block_item_active__YXHIy']"
    button_send_form = "//button[@class='Button_button__RNIJo']"
    close = "//button[@class='FormModal_modal__header_button__-X7yr']"



    # Getters
    def get_button_yes_18_old(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_yes_18_old)))

    def get_ask_wine_shop_forma(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ask_wine_shop_forma)))

    def get_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_menu_2(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_2)))

    def get_ask_wine_forma(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ask_wine_forma)))

    def get_ask_wine_forma_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ask_wine_forma_cart)))

    def get_name_fio(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_fio)))

    def get_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_telegram(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.telegram)))

    def get_send_form(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_send_form)))

    # Actions
    def click_button_yes_18_old(self):
        self.get_button_yes_18_old().click()
        print("Click button_yes_18_old")

    def click_ask_wine_shop_forma(self):
        self.get_ask_wine_shop_forma().click()
        print("Click ask_wine_shop_forma")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_menu_2(self):
        self.get_menu_2().click()
        print("Click menu 2")

    def input_key(self):
        self.label.send_keys(Keys.TAB)
        print("input_key")

    def click_ask_wine_forma_cart(self):
        self.get_ask_wine_forma_cart().click()
        print("Click ask_wine_forma_cart")

    def click_ask_wine_forma(self):
        self.get_ask_wine_forma().click()
        print("Click wine_forma")

    def input_name_fio_ask_wine_shop(self):
        self.get_name_fio().send_keys(*DataPage.fio_ask_wine_shop)
        print("input name_fio_ask_wine_shop")

    def input_name_fio_ask_wine_forma(self):
        self.get_name_fio().send_keys(*DataPage.fio_ask_wine)
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
    def fill_ask_wine_shop_forma(self):
        """Fill ask_wine_shop_forma"""
        # with allure.step("select_products_1"):
        Logger.add_start_step(method="wine_shop ask forma")

        self.get_current_url()
        self.click_button_yes_18_old()
        self.click_ask_wine_shop_forma()
        self.input_name_fio_ask_wine_shop()
        self.input_phone()
        self.input_telegram()
        self.click_button_send_form()
        Logger.add_end_step(url=self.browser.current_url, method="wine_shop ask forma")

    def fill_ask_wine_forma(self):
        """Fill ask_wine_forma"""
        # with allure.step("select_products_1"):
        Logger.add_start_step(method="ask_wine_forma")
        self.browser.maximize_window()
        self.get_current_url()
        self.click_button_yes_18_old()
        time.sleep(1)
        self.click_menu()
        self.input_key()
        self.browser.execute_script("window.scrollBy(0,1000);")
        self.click_menu_2()
        # self.input_key()
        time.sleep(5)
        # action = ActionChains(browser)
        # scrollto = self.browser.find_element(By.XPATH, "//span[@class='PageFooter_footer__link__2yvLx']")
        # action.move_to_element(scrollto).perform()

        self.click_ask_wine_forma()
        self.click_ask_wine_forma_cart()
        self.input_name_fio_ask_wine_forma()
        self.input_phone()
        self.input_telegram()
        # self.click_button_send_form()

        time.sleep(3)
        assert self.is_not_element_present(By.XPATH, self.close), "Should be not close button"
        Logger.add_end_step(url=self.browser.current_url, method="ask_wine_forma")
