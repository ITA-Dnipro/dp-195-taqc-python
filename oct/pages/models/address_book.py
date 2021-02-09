from pages.base.elements import Block, Clickable


class AddressBookEntries(Block):
    contains = {
        "edit_button": {"locator": ("CSS_SELECTOR", "a.btn.btn-info"), "class": Clickable},
        "delete_button": {"locator": ("CSS_SELECTOR", "a.btn.btn-danger"), "class": Clickable},
    }


class ButtonsClearfix(Clickable):
    contains = {
        "back_button": {"locator": ("CSS_SELECTOR", "a.btn.btn-default"), "class": Clickable},
        "delete_button": {"locator": ("CSS_SELECTOR", "a.btn.btn-primary"), "class": Clickable},
    }
