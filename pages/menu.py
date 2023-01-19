import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from pages.data import DataPage
#import allure
from base.base_class import BaseClass


class MenuPage(BaseClass):

    # Locators
    button_menu = "//div[@class='Header_header__burger__T1wec Header_burger__cuGf3']"
    menu_cafe = "//a[@href='https://backapiwinecheese.ru/backend/uploads/menu.pdf']"


    # Getters
    def get_button_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_menu)))

    def get_menu_cafe(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_cafe)))


    # Actions
    def click_button_menu(self):
        self.get_button_menu().click()
        print("Click button_menu")

    def click_menu_cafe(self):
        self.get_menu_cafe().click()
        print("Click menu_cafe")



    # Metods

    def seen_menu_cafe(self):
        self.click_button_menu()
        self.click_menu_cafe()
        new_window = self.browser.window_handles[2]
        self.browser.switch_to.window(new_window)
        url = self.browser.current_url
        print(url)
        time.sleep(4)
        assert url == "https://backapiwinecheese.ru/backend/uploads/menu.pdf"

