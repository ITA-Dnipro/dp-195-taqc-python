from oct.pages.base.page import BasePage
from oct.pages.base.elements import CheckBox, RadioButton, RadioButtonGroup, Form, Block, InputField


class NewsLetter(RadioButtonGroup):
    contains = {
        "yes": {"locator": ("XPATH", '//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input'),
                "class": RadioButton},
        "no": {"locator": ("XPATH", '//*[@id="content"]/form/fieldset[3]/div/div/label[2]/input'),
               "class": RadioButton}
    }


class YourPassword(Block):
    contains = {
        "password": {"locator": ("ID", "input-password"), "class": InputField},
        "confirm": {"locator": ("ID", "input-confirm"), "class": InputField}
    }


class PersonalDetails(Block):
    contains = {
        "first_name": {"locator": ("ID", "input-firstname"), "class": InputField},
        "last_name": {"locator": ("ID", "input-lastname"), "class": InputField},
        "email": {"locator": ("ID", "input-email"), "class": InputField},
        "telephone": {"locator": ("ID", "input-telephone"), "class": InputField}
    }


class RegistrationForm(Form):
    contains = {
        "personal": {"locator": ("XPATH", '//*[@id="account"]'), "class": PersonalDetails},
        "password": {"locator": ("XPATH", '//*[@id="content"]/form/fieldset[2]'), "class": YourPassword},
        "newsletter": {"locator": ("XPATH", '//*[@id="content"]/form/fieldset[3]'), "class": NewsLetter},
        'policy': {"locator": ("XPATH", '//*[@id="content"]/form/div/div/input[1]'), "class": CheckBox}
    }

    def fill_out(self, **kwargs):
        self.personal.first_name.fill(kwargs.get("first_name"))
        self.personal.last_name.fill(kwargs.get("last_name"))
        self.personal.email.fill(kwargs.get("email"))
        self.personal.telephone.fill(kwargs.get("telephone"))
        self.password.password.fill(kwargs.get("password"))
        self.password.confirm.fill(kwargs.get("password"))
        self.newsletter.select_option(kwargs.get("reason"))
        self.policy.click()


class RegistrationPage(BasePage):
    url = "index.php?route=account/register"

    contains = {
        "form": {"locator": ("CLASS_NAME", "form-horizontal"), "class": RegistrationForm},
    }
