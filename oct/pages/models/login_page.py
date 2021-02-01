from pages.base.page import BasePage
from pages.base.elements import Form, Block, InputField


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


class LoginPage(BasePage):
    url = "index.php?route=account/login"

    contains = {
        "form": {"locator": ("XPATH", "//*[@id=\"content\"]/div/div[2]/div/form"), "class": LoginForm},
    }
