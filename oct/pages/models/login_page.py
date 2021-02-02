from pages.base.page import BasePage
from pages.base.elements import Form, Block, InputField, Clickable


class NewCustomerButton(Block):
    contains = {
        "button": {"locator":("XPATH", "//*[@id=\"content\"]/div/div[1]/div/a"), "class": Clickable}
    }


class ReturningCustomer(Block):
    contains = {
        "email": {"locator": ("ID", "input-email"), "class": InputField},
        "password": {"locator": ("ID", "input-password"), "class": InputField},
    }


class LoginForm(Form):
    contains = {
        "personal": {"locator": ("XPATH", "//*[@id=\"content\"]/div/div[2]/div/form"), "class": ReturningCustomer},
    }

    def fill_out(self, **kwargs):
        self.personal.email.fill(kwargs.get("email"))
        self.personal.password.fill(kwargs.get("password"))


class NewCustomer(Block):
    contains = {
        'action': {"locator": ("CLASS_NAME", "btn-primary"), "class": NewCustomerButton}
    }

    def click_button(self):
        self.action.button.click()


class LoginPage(BasePage):
    url = "index.php?route=account/login"

    contains = {
        "form": {"locator": ("XPATH", "//*[@id=\"content\"]/div/div[2]/div/form"), "class": LoginForm},
        "action": {"locator": ("XPATH", "//*[@id=\"content\"]/div/div[1]/div"), "class": NewCustomer}
    }
