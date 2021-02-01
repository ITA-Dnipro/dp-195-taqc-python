from pages.base.page import BasePage
from pages.base.elements import RadioButton, RadioButtonGroup, Block, InputField, Clickable


class AddToCart(Block):

    contains = {
        "qty": {"locator": ("ID", "input-quantity"), "class": InputField},
        "btn": {"locator": ("TAG_NAME", "button"), "class": Clickable},
    }

    def add(self, amount: int = 1) -> None:

        self.qty.fill(amount)
        self.btn.click()


class Rate(RadioButtonGroup):

    contains = {
        "1": {
            "locator": ("XPATH", '//*[@id="form-review"]/div[4]/div/input[1]'),
            "class": RadioButton,
        },
        "2": {
            "locator": ("XPATH", '//*[@id="form-review"]/div[4]/div/input[2]'),
            "class": RadioButton,
        },
        "3": {
            "locator": ("XPATH", '//*[@id="form-review"]/div[4]/div/input[3]'),
            "class": RadioButton,
        },
        "4": {
            "locator": ("XPATH", '//*[@id="form-review"]/div[4]/div/input[4]'),
            "class": RadioButton,
        },
        "5": {
            "locator": ("XPATH", '//*[@id="form-review"]/div[4]/div/input[5]'),
            "class": RadioButton,
        },
    }


class Review(Block):

    contains = {
        "name": {"locator": ("TAG_NAME", "input"), "class": InputField},
        "body": {"locator": ("TAG_NAME", "textarea"), "class": InputField},
        "rating": {"locator": ("XPATH", '//*[@id="form-review"]/div[4]'), "class": Rate},
        "btn": {"locator": ("TAG_NAME", "button"), "class": Clickable},
    }

    def fill_out(self, **kwargs: str) -> None:

        self.name.fill(kwargs.get("name"))
        self.body.fill(kwargs.get("body"))
        self.rating.select_option(kwargs.get("rating"))

    def send(self) -> None:

        self.btn.click()


class ProductPage(BasePage):

    url = "/index.php?route=product/product&product_id=41"

    contains = {
        "add_to_wishlist": {
            "locator": ("XPATH", '//*[@id="content"]/div/div[2]/div[1]/button[1]'),
            "class": Clickable,
        },
        "cart": {"locator": ("ID", "product"), "class": AddToCart},
        "review_link": {
            "locator": ("XPATH", '//*[@id="content"]/div/div[2]/div[3]/p/a[2]'),
            "class": Clickable,
        },
        "review_tab": {
            "locator": ("XPATH", '//*[@id="content"]/div/div[2]/div[3]/p/a[2]'),
            "class": Clickable,
        },
        "review": {"locator": ("XPATH", '//*[@id="form-review"]'), "class": Review},
    }
