from pages.base.page import BasePage
from pages.base.elements import Block, Clickable


class AddressBookEntries(Block):
    contains = {
        "edit_button": {"locator": ("XPATH", "//a[@class='btn btn-info']"), "class": Clickable},
        "delete_button": {"locator": ("XPATH", "//a[@class='btn btn-danger']"), "class": Clickable}
    }


class NewAddressButton(Clickable):
    contains = {
        "btn": {"locator": ("XPATH", "//*[@id='content']/div[2]/div[2]/a"), "class": Clickable}
    }