"""Module contains BasePage class with the common layout of the Opencart webpage."""

from selenium.webdriver.common.by import By

from oct.pages.base.base import Page
from oct.pages.base.elements import Block, Clickable, InputField


class AccountDropDown(Clickable):

    contains = {
        "register": {
            "locator": ("XPATH", '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'),
            "class": Clickable,
        },
        "login": {
            "locator": ("XPATH", '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a'),
            "class": Clickable,
        },
    }


class Header(Block):

    contains = {
        "account": {"locator": ("CLASS_NAME", "dropdown"), "class": AccountDropDown},
        "wishlist": {"locator": ("ID", "wishlist-total"), "class": Clickable},
        "shopping_cart": {"locator": ("CLASS_NAME", "fa-shopping-cart"), "class": Clickable},
        "checkout": {"locator": ("CLASS_NAME", "fa-share"), "class": Clickable},
    }


class SearchBar(Block):

    contains = {
        "field": {"locator": ("TAG_NAME", "input"), "class": InputField},
        "go": {"locator": ("TAG_NAME", "button"), "class": Clickable},
    }

    def find_article(self, name: str) -> None:
        self.field.fill(name)
        self.go.click()


class Desktop(Clickable):

    contains = {
        "pc": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            "class": Clickable,
        },
        "mac": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            "class": Clickable,
        },
        "all": {"locator": ("CLASS_NAME", "see-all"), "class": Clickable},
    }


class Laptops(Clickable):

    contains = {
        "windows": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            "class": Clickable,
        },
        "mac": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            "class": Clickable,
        },
        "all": {"locator": ("CLASS_NAME", "see-all"), "class": Clickable},
    }


class Components(Clickable):

    contains = {
        "mice": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[1]/a'),
            "class": Clickable,
        },
        "trackballs": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[2]/a'),
            "class": Clickable,
        },
        "printers": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[3]/a'),
            "class": Clickable,
        },
        "scanners": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[4]/a'),
            "class": Clickable,
        },
        "webcams": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[5]/a'),
            "class": Clickable,
        },
        "all": {"locator": ("CLASS_NAME", "see-all"), "class": Clickable},
    }


class NavBar(Block):

    contains = {
        "pc": {"locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[1]'), "class": Desktop},
        "laptop": {"locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[2]'), "class": Laptops},
        "components": {
            "locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[3]'),
            "class": Components,
        },
        "tablets": {"locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[4]'), "class": Clickable},
        "soft": {"locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[5]'), "class": Clickable},
        "phones": {"locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[6]'), "class": Clickable},
        "cameras": {"locator": ("XPATH", '//*[@id="menu"]/div[2]/ul/li[7]'), "class": Clickable},
    }


class Footer(Block):

    contains = {
        "about": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[1]/ul/li[1]/a"),
            "class": Clickable,
        },
        "delivery": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[1]/ul/li[2]/a"),
            "class": Clickable,
        },
        "policy": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[1]/ul/li[3]/a"),
            "class": Clickable,
        },
        "terms": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[1]/ul/li[4]/a"),
            "class": Clickable,
        },
        "contact": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[2]/ul/li[1]/a"),
            "class": Clickable,
        },
        "return": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[2]/ul/li[2]/a"),
            "class": Clickable,
        },
        "map": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[2]/ul/li[3]/a"),
            "class": Clickable,
        },
        "brands": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[3]/ul/li[1]/a"),
            "class": Clickable,
        },
        "certificates": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[3]/ul/li[2]/a"),
            "class": Clickable,
        },
        "affilate": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[3]/ul/li[3]/a"),
            "class": Clickable,
        },
        "specials": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[3]/ul/li[4]/a"),
            "class": Clickable,
        },
        "account": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[4]/ul/li[1]/a"),
            "class": Clickable,
        },
        "orders": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[4]/ul/li[2]/a"),
            "class": Clickable,
        },
        "wish": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[4]/ul/li[3]/a"),
            "class": Clickable,
        },
        "news": {
            "locator": ("XPATH", "/html/body/footer/div/div/div[4]/ul/li[4]/a"),
            "class": Clickable,
        },
    }


class BasePage(Page):
    @property
    def header(self) -> Header:
        element = self._base.find_element(By.ID, "top")
        return Header(element)

    @property
    def cart_status(self) -> Clickable:
        element = self._base.find_element(By.ID, "cart")
        return Clickable(element)

    @property
    def search(self) -> SearchBar:
        element = self._base.find_element(By.ID, "search")
        return SearchBar(element)

    @property
    def navbar(self) -> NavBar:
        element = self._base.find_element(By.ID, "menu")
        return NavBar(element)

    @property
    def footer(self) -> Footer:
        element = self._base.find_element(By.TAG_NAME, "footer")
        return Footer(element)
