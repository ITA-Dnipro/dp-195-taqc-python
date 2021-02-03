from pages.base.page import BasePage
from pages.base.elements import RadioButton, Form, InputField, RadioButtonGroup, DropDown


class DefaultAddress(RadioButtonGroup):
    contains = {
        "yes": {
            "locator": ("XPATH", '//*[@id="content"]/form/fieldset/div[10]/div/label[1]/input'),
            "class": RadioButton,
        },
        "no": {
            "locator": ("XPATH", '//*[@id="content"]/form/fieldset/div[10]/div/label[2]/input'),
            "class": RadioButton,
        },
    }


class AddAddressForm(Form):
    contains = {
        "first_name": {"locator": ("ID", "input-firstname"), "class": InputField},
        "last_name": {"locator": ("ID", "input-lastname"), "class": InputField},
        "company": {"locator": ("ID", "input-company"), "class": InputField},
        "address_1": {"locator": ("ID", "input-address-1"), "class": InputField},
        "address_2": {"locator": ("ID", "input-address-2"), "class": InputField},
        "city": {"locator": ("ID", "input-city"), "class": InputField},
        "post_code": {"locator": ("ID", "input-postcode"), "class": InputField},
        "country": {"locator": ("ID", "input-country"), "class": DropDown},
        "region_state": {"locator": ("ID", "input-zone"), "class": DropDown},
        "default_address": {
            "locator": ("XPATH", '//*[@id="content"]/form/fieldset/div[10]/div'),
            "class": DefaultAddress,
        },
    }

    def fill_out(self, **kwargs):
        self.first_name.fill(kwargs.get("first_name"))
        self.last_name.fill(kwargs.get("last_name"))
        self.company.fill(kwargs.get("company"))
        self.address_1.fill(kwargs.get("address_1"))
        self.address_2.fill(kwargs.get("address_2"))
        self.city.fill(kwargs.get("city"))
        self.post_code.fill(kwargs.get("post_code"))
        self.country.select(kwargs.get("country"))
        self.region_state.select(kwargs.get("region_state"))
        self.default_address.select_option(kwargs.get("region_state"))


class AddAddressPage(BasePage):
    url = "index.php?route=account/address/add"

    contains = {
        "form": {"locator": ("CLASS_NAME", "form-horizontal"), "class": AddAddressForm},
    }
