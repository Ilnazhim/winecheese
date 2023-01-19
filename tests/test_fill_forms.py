import time
import allure
from pages.cafe import CafePage
from pages.career import CareerPage
from pages.contact import ContactPage
from pages.espresso import EspressoPage
from pages.gastro_lavka import GastroPage
from pages.haltura import HalturaPage
from pages.menu import MenuPage
from pages.merch import MerchPage
from pages.restaurant import RestaurantPage
from pages.wine_shop import WineShopPage


#@allure.description("Test select product 1")
def test_fill_restaurant_forms(browser):

    link = "https://winecheese.ru/restaurant"
    print("\nStart Restaurant forma")
    browser.maximize_window()
    rp = RestaurantPage(browser, link)
    rp.open()
    rp.fill_restaurant_forma()
    rp.open()
    rp.fill_ask_restaurant_forma()


def test_fill_cafe_forms(browser):
    link = "https://winecheese.ru/cafe"
    print("\nStart Cafe forma")
    browser.maximize_window()
    cp = CafePage(browser, link)
    cp.open()
    cp.fill_cafe_forma()
    cp.open()
    cp.fill_ask_cafe_forma()


def test_fill_espresso_forms(browser):
    link = "https://winecheese.ru/espresso_bar"
    print("\nStart espresso forma")
    browser.maximize_window()
    ep = EspressoPage(browser, link)
    ep.open()
    ep.fill_ask_espresso_forma()


def test_fill_merch_forms(browser):
    link = "https://winecheese.ru/merch"
    print("\nStart merch forma")
    browser.maximize_window()
    mp = MerchPage(browser, link)
    mp.open()
    mp.fill_ask_merch_forma()
    mp.open()
    mp.fill_order_shorts_form()


def test_fill_wine_shop_forms(browser):
    link = "https://winecheese.ru/vine_shop"
    print("\nStart wine shop forma")
    browser.maximize_window()
    wp = WineShopPage(browser, link)
    wp.open()
    wp.fill_ask_wine_shop_forma()
    # wp.open()
    # wp.fill_ask_wine_forma()


def test_fill_gastro_forms(browser):
    link = "https://winecheese.ru/gastronomic_shop"
    print("\nStart gastro shop forma")
    browser.maximize_window()
    gp = GastroPage(browser, link)
    gp.open()
    gp.fill_ask_gastro_forma()


def test_career_forms(browser):
    link = "https://winecheese.ru/career"
    print("\nStart career forma")
    browser.maximize_window()
    crp = CareerPage(browser, link)
    crp.open()
    crp.fill_career_form()


def test_fill_haltura_forms(browser):
    link = "https://winecheese.ru/hackwork"
    print("\nStart haltura forma")
    browser.maximize_window()
    hp = HalturaPage(browser, link)
    hp.open()
    hp.fill_haltura_form()


def test_contact_form(browser):
    link = "https://winecheese.ru/contacts"
    print("\nStart contact form")
    browser.maximize_window()
    conp = ContactPage(browser, link)
    conp.open()
    conp.fill_contact_form()


def test_see_menus(browser):
    link = "https://winecheese.ru/restaurant"
    print("\nStart see menus")
    browser.maximize_window()
    rp = RestaurantPage(browser, link)
    rp.open()
    rp.seen_menu_rest()
    link = "https://winecheese.ru/"
    mp = MenuPage(browser, link)
    mp.open()
    mp.seen_menu_cafe()


    print("Finish Tests")
    time.sleep(1)
