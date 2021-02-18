from oct.pages.base.elements import (
    RadioButton,
    Block,
    InputField,
    Clickable,
    CheckBox,
    DropDown,
    RadioButtonGroup,
)
from oct.pages.base.page import BasePage


class CheckoutOptions(RadioButtonGroup):
    contains = {
        "register_account": {
            "locator": (
                "XPATH",
                '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[1]/label/input',
            ),
            "class": RadioButton,
        },
        "guest_checkout": {
            "locator": (
                "XPATH",
                '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input',
            ),
            "class": RadioButton,
        },
    }


class CheckoutContinueButton(Clickable):
    contains = {"continue_button": {"locator": ("ID", "button-account"), "class": Clickable}}


class ReturningCustomer(Block):
    contains = {
        "email": {"locator": ("ID", "input-email"), "class": InputField},
        "password": {"locator": ("ID", "input-password"), "class": InputField},
        "login_button": {"locator": ("ID", "button-login"), "class": Clickable},
    }

    def fill_out(self, **kwargs):
        self.email.fill(kwargs.get("email"))
        self.password.fill(kwargs.get("password"))
        self.login_button.click()


class BillingDetails(Block):
    contains = {
        "first_name": {"locator": ("ID", "input-payment-firstname"), "class": InputField},
        "last_name": {"locator": ("ID", "input-payment-lastname"), "class": InputField},
        "email": {"locator": ("ID", "input-payment-email"), "class": InputField},
        "telephone": {"locator": ("ID", "input-payment-telephone"), "class": InputField},
        "company": {"locator": ("ID", "input-payment-company"), "class": InputField},
        "address_1": {"locator": ("ID", "input-payment-address-1"), "class": InputField},
        "address_2": {"locator": ("ID", "input-payment-address-2"), "class": InputField},
        "city": {"locator": ("ID", "input-payment-city"), "class": InputField},
        "post_code": {"locator": ("ID", "input-payment-postcode"), "class": InputField},
        "country": {"locator": ("ID", "input-payment-country"), "class": DropDown},
        "region_state": {"locator": ("ID", "input-payment-zone"), "class": DropDown},
        "my_delivery_and_billing_addresses": {
            "locator": ("XPATH", "//*[@id='collapse-payment-address']/div/div[2]/label/input"),
            "class": CheckBox,
        },
        "continue_button": {"locator": ("ID", "button-guest"), "class": Clickable},
    }

    def fill_out(self, **kwargs):
        self.first_name.fill(kwargs.get("first_name"))
        self.last_name.fill(kwargs.get("last_name"))
        self.email.fill(kwargs.get("email"))
        self.telephone.fill(kwargs.get("telephone"))
        self.company.fill(kwargs.get("company"))
        self.address_1.fill(kwargs.get("address_1"))
        self.address_2.fill(kwargs.get("address_2"))
        self.city.fill(kwargs.get("city"))
        self.post_code.fill(kwargs.get("post_code"))
        self.country.select(kwargs.get("country"))
        self.region_state.select(kwargs.get("region_state"))
        self.continue_button.click()


class DeliveryDetails(Block):
    contains = {
        "first_name": {"locator": ("ID", "input-shipping-firstname"), "class": InputField},
        "last_name": {"locator": ("ID", "input-shipping-lastname"), "class": InputField},
        "company": {"locator": ("ID", "input-shipping-company"), "class": InputField},
        "address_1": {"locator": ("ID", "input-shipping-address-1"), "class": InputField},
        "address_2": {"locator": ("ID", "input-shipping-address-2"), "class": InputField},
        "city": {"locator": ("ID", "input-shipping-city"), "class": InputField},
        "post_code": {"locator": ("ID", "input-shipping-postcode"), "class": InputField},
        "country": {"locator": ("ID", "input-shipping-country"), "class": DropDown},
        "region_state": {"locator": ("ID", "input-shipping-zone"), "class": DropDown},
        "continue_button": {"locator": ("ID", "button-guest-shipping"), "class": Clickable},
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


class DeliveryMethod(Block):
    contains = {
        "flat_shipping_rate": {
            "locator": ("XPATH", "//*[@ id='collapse-shipping-method']/div/div[1]/label/input"),
            "class": RadioButton,
        },
        "add_comments": {
            "locator": ("XPATH", "//*[@id='collapse-shipping-method']/div/p[4]/textarea"),
            "class": InputField,
        },
        "continue_button": {"locator": ("ID", "button-shipping-method"), "class": Clickable},
    }


class PaymentMethod(Block):
    contains = {
        "cash_on_delivery": {
            "locator": ("XPATH", "//*[@id='collapse-payment-method']/div/div[1]/label/input"),
            "class": RadioButton,
        },
        "add_comments": {
            "locator": ("XPATH", "//*[@id='collapse-payment-method']/div/p[3]/textarea"),
            "class": InputField,
        },
        "terms_and_conditions": {
            "locator": ("XPATH", "//*[@id='collapse-payment-method']/div/div[2]/div/input[1]"),
            "class": CheckBox,
        },
        "continue_button": {"locator": ("ID", "button-payment-method"), "class": Clickable},
    }


class ConfirmOrderButton(Clickable):
    contains = {"confirm_order_button": {"locator": ("ID", "button-confirm")}}


class CheckoutPage(BasePage):

    url = "index.php?route=checkout/checkout"

    contains = {
        "checkout_options": {
            "locator": ("XPATH", "//*[@id='collapse-checkout-option']/div/div/div[1]"),
            "class": CheckoutOptions,
        },
        "checkout_continue_button": {
            "locator": ("XPATH", "//*[@id='button-account']"),
            "class": CheckoutContinueButton,
        },
        "returning_customer": {
            "locator": ("XPATH", "//*[@id='collapse-checkout-option']/div/div/div[2]"),
            "class": ReturningCustomer,
        },
        "billing_form": {
            "locator": ("XPATH", "//*[@id='collapse-payment-address']/div"),
            "class": BillingDetails,
        },
        "delivery_form": {
            "locator": ("XPATH", "//*[@id='collapse-shipping-address']/div"),
            "class": DeliveryDetails,
        },
        "delivery_method": {
            "locator": ("XPATH", "//*[@id='collapse-shipping-method']/div"),
            "class": DeliveryMethod,
        },
        "payment_metod": {
            "locator": ("XPATH", "//*[@id='collapse-payment-method']/div"),
            "class": PaymentMethod,
        },
        "confirm_order": {
            "locator": ("XPATH", "//*[@id='collapse-checkout-confirm']/div"),
            "class": ConfirmOrderButton,
        },
    }
