from selenium.common.exceptions import NoSuchElementException

from pages.base.page import BasePage
from pages.base.elements import Clickable, Block, Link, ProductThumb


class DropDownSelector(Clickable):
    """Dropdown menu."""

    def select_option(self, name: str) -> str:
        if not self.contains or name not in self.contains.keys():
            raise NoSuchElementException

        attr = getattr(self, name)
        return attr.href


class SortBy(DropDownSelector):
    """Sort by dropdown menu."""

    contains = {
        "default": {"locator": ("XPATH", '//*[@id="input-sort"]/option[1]'), "class": Link},
        "name_a_z": {"locator": ("XPATH", '//*[@id="input-sort"]/option[2]'), "class": Link},
        "name_z_a": {"locator": ("XPATH", '//*[@id="input-sort"]/option[3]'), "class": Link},
        "price_low_high": {
            "locator": ("XPATH", '//*[@id="input-sort"]/option[4]'),
            "class": Link,
        },
        "price_high_low": {
            "locator": ("XPATH", '//*[@id="input-sort"]/option[5]'),
            "class": Link,
        },
        "rating_high": {
            "locator": ("XPATH", '//*[@id="input-sort"]/option[6]'),
            "class": Link,
        },
        "rating_low": {"locator": ("XPATH", '//*[@id="input-sort"]/option[7]'), "class": Link},
        "model_a_z": {"locator": ("XPATH", '//*[@id="input-sort"]/option[8]'), "class": Link},
        "model_z_a": {"locator": ("XPATH", '//*[@id="input-sort"]/option[9]'), "class": Link},
    }

    def select_option(self, name: str = "default"):
        return super().select_option(name)


class Show(DropDownSelector):
    """Items per page dropdown menu."""

    contains = {
        "15": {"locator": ("XPATH", '//*[@id="input-limit"]/option[1]'), "class": Link},
        "25": {"locator": ("XPATH", '//*[@id="input-limit"]/option[2]'), "class": Link},
        "50": {"locator": ("XPATH", '//*[@id="input-limit"]/option[3]'), "class": Link},
        "75": {"locator": ("XPATH", '//*[@id="input-limit"]/option[4]'), "class": Link},
        "100": {"locator": ("XPATH", '//*[@id="input-limit"]/option[5]'), "class": Link},
    }

    def select_option(self, name: str = "15"):
        return super().select_option(name)


class Paginator(Clickable):
    """Pagination bar."""

    contains = {"page": {"locator": ("TAG_NAME", "li"), "class": Link, "is_loaded": True}}


class SideBar(Block):

    contains = {"category": {"locator": ("TAG_NAME", "a"), "class": Link, "is_loaded": True}}


class CategoryPage(BasePage):
    def __init__(self, path: str = ""):
        super().__init__()
        self.url = f"{self.url}&{path}"

    url = "index.php?route=product/category"

    contains = {
        "sidebar": {"locator": ("ID", "column-left"), "class": SideBar},
        "sort": {"locator": ("ID", "input-sort"), "class": SortBy},
        "show": {"locator": ("ID", "input-limit"), "class": Show},
        "paginator": {"locator": ("CLASS_NAME", "pagination"), "class": Paginator},
        "products": {
            "locator": ("CLASS_NAME", "product-thumb"),
            "class": ProductThumb,
            "is_loaded": True,
        },
    }
