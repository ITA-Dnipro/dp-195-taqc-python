from pages.base.page import BasePage
from pages.base.elements import RadioButton, RadioButtonGroup, Block, InputField, Clickable, Form, CheckBox


class NewCustomer(RadioButtonGroup):
    contains = {
        "register_account": {
            "locator": (
                "XPATH",
                '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[1]/label/input'
            ),
            "class": RadioButton,
        },
        "guest_checkout": {
            "locator": (
                "XPATH",
                '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input'
            ),
            "class": RadioButton,
        },
        "continue_button": {
            "locator": (
                "XPATH",
                "//*[@id='button-account']"
            ),
            "class": Clickable
        }
    }


class ReturningCustomer(Form):
    contains = {
        "email": {
            "locator": (
                "XPATH",
                "//*[@id='input-email']"
            ),
            "class": InputField
        },
        "password": {
            "locator": (
                "XPATH",
                "//*[@id='input-password']"
            ),
            "class": InputField
        },
        "login_button": {
            "locator": (
                "XPATH",
                "//*[@ id='button-login']"
            )
        }
    }
    def fill_out(self, **kwargs):
        self.test.email.fill(kwargs.get("email"))
        self.test.password.fill(kwargs.get("password"))


class YourPersonalDetails(Block):
    contains = {
        "first_name": {"locator": ("XPATH", "//*[@id='input-payment-firstname']"), "class": InputField},
        "last_name": {"locator": ("XPATH", "//*[@id='input-payment-lastname']"), "class": InputField},
        "email": {"locator": ("XPATH", "//*[@id='input-payment-email']"), "class": InputField},
        "telephone": {"locator": ("XPATH", "//*[@id='input-payment-telephone']"), "class": InputField},
    }


class YourAddress(Block):
    contains = {
        "company": {"locator": ("XPATH", "//*[@id='input-payment-company']"), "class": InputField},
        "address_1": {"locator": ("XPATH", "//*[@id='input-payment-address-1']"), "class": InputField},
        "address_2": {"locator": ("XPATH", "//*[@id='input-payment-address-2']"), "class": InputField},
        "city": {"locator": ("XPATH", "//*[@id='input-payment-city']"), "class": InputField},
        "post_code": {"locator": ("XPATH", "//*[@id='input-payment-postcode']"), "class": InputField},
        "country": {"locator": ("XPATH", "//*[@id='input-payment-country']"), "class": Dropdown},
        "region_state": {"locator": ("XPATH", "//*[@id='input-payment-zone']"), "class": Dropdown},
    }


class DeliveryMethod(Block):
    contains = {
        "flat_shipping_rate": {
            "locator": (
                "XPATH",
                "//*[@ id='collapse-shipping-method']/div/div[1]/label/input"
            )
        },
        "add_comments": {
            "locator": (
                "XPATH",
                "//*[@id='collapse-shipping-method']/div/p[4]/textarea"
            ), "class": InputField
        },
        "continue_button": {
            "locator": (
                "XPATH",
                "//*[@id='button-shipping-method']"
            ), "class": Clickable
        }
    }


class PaymentMethod(Block):
    contains = {
        "cash_on_delivery": {
            "locator": (
                "XPATH",
                "//*[@id='collapse-payment-method']/div/div[1]/label/input"
            )
        },
        "add_comments": {
            "locator": (
                "XPATH",
                "//*[@id='collapse-payment-method']/div/p[3]/textarea"
            ), "class": InputField
        },
        "terms_and_conditions": {
          "locator": (
              "XPATH",
              "//*[@id='collapse-payment-method']/div/div[2]/div/input[1]"
          ), "class": CheckBox
        },
        "continue_button": {
            "locator": (
                "XPATH",
                "//*[@id='button-payment-method']"
            ), "class": Clickable
        }
    }


class ConfirmOrder(Block):
    contains = {
        "confirm_order_button": {
            "locator": (
                "XPATH",
                "//*[@id='button-confirm']"
            ), "class": Clickable
        }
    }
