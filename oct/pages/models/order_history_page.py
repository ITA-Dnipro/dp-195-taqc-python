from oct.pages.base.elements import Block, Element, Link
from oct.pages.base.page import BasePage


class OrderTableRow(Block):

    contains = {
        "id": {"locator": ("CSS_SELECTOR", "td:nth-child(1)"), "class": Element},
        "customer": {"locator": ("CSS_SELECTOR", "td:nth-child(2)"), "class": Element},
        "num_of_products": {"locator": ("CSS_SELECTOR", "td:nth-child(3)"), "class": Element},
        "status": {"locator": ("CSS_SELECTOR", "td:nth-child(4)"), "class": Element},
        "total": {"locator": ("CSS_SELECTOR", "td:nth-child(5)"), "class": Element},
        "date_added": {"locator": ("CSS_SELECTOR", "td:nth-child(6)"), "class": Element},
        "view": {"locator": ("CSS_SELECTOR", "td:nth-child(7) > a"), "class": Link},
    }


class OrderTable(Block):

    contains = {"rows": {"locator": ("TAG_NAME", "tr"), "class": OrderTableRow, "is_loaded": True}}


class OrderHistoryPage(BasePage):

    url = "index.php?route=account/order"

    contains = {
        "table": {"locator": ("XPATH", '//*[@id="content"]/div[1]/table'), "class": OrderTable},
        "continue_btn": {"locator": ("XPATH", '//*[@id="content"]/div[3]/div/a'), "class": Link},
    }
