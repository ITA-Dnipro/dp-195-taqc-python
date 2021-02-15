from oct.pages.base.page import BasePage
from oct.pages.base.elements import Block, Clickable


class AddressBookEntries(Block):
    contains = {
        "edit_button": {"locator": ("CSS_SELECTOR", "a.btn.btn-info"), "class": Clickable},
        "delete_button": {"locator": ("CSS_SELECTOR", "a.btn.btn-danger"), "class": Clickable},
    }


class ButtonsClearfix(Clickable):
    contains = {
        "back_button": {"locator": ("CSS_SELECTOR", "a.btn.btn-default"), "class": Clickable},
        "new_address_button": {
            "locator": ("CSS_SELECTOR", "a.btn.btn-primary"),
            "class": Clickable,
        },
    }


class AddressBookPage(BasePage):
    url = "index.php?route=account/address"

    contains = {
        "edit_delete_buttons": {
            "locator": (
                "XPATH",
                "//*[@id='content']/div[1]/table/tbody/tr/td[2]",
            ),
            "class": AddressBookEntries,
        },
        "new_address_and_back": {
            "locator": (
                "XPATH",
                "//*[@id='content']/div[2]",
            ),
            "class": ButtonsClearfix,
        },
    }
