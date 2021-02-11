import re

from oct.pages.base.elements import Block, Element, Link, Clickable
from oct.pages.base.page import BasePage


class ButtonGroup(Block):

    contains = {
        "reorder": {"locator": ("CLASS_NAME", "btn-primary"), "class": Clickable},
        "return_product": {"locator": ("CLASS_NAME", "btn-danger"), "class": Link},
    }


class OrderTableRow(Block):

    contains = {
        "product_name": {"locator": ("CSS_SELECTOR", "td:nth-child(1)"), "class": Element},
        "model": {"locator": ("CSS_SELECTOR", "td:nth-child(2)"), "class": Element},
        "quantity": {"locator": ("CSS_SELECTOR", "td:nth-child(3)"), "class": Element},
        "price": {"locator": ("CSS_SELECTOR", "td:nth-child(4)"), "class": Element},
        "total": {"locator": ("CSS_SELECTOR", "td:nth-child(5)"), "class": Element},
        "actions": {"locator": ("CSS_SELECTOR", "td:nth-child(6)"), "class": ButtonGroup},
    }


class OrderTable(Block):

    contains = {
        "rows": {
            "locator": ("XPATH", '//*[@id="content"]/div[1]/table/tbody'),
            "class": OrderTableRow,
            "is_loaded": True,
        }
    }


class Summary(Block):

    contains = {
        "subtotal": {
            "locator": ("CSS_SELECTOR", "tr:nth-child(1) > td:nth-child(3)"),
            "class": Element,
        },
        "flat_shipping_rate": {
            "locator": ("CSS_SELECTOR", "tr:nth-child(2) > td:nth-child(3)"),
            "class": Element,
        },
        "total": {
            "locator": ("CSS_SELECTOR", "tr:nth-child(3) > td:nth-child(3)"),
            "class": Element,
        },
    }


class OrderHistory(Block):

    contains = {
        "date_added": {"locator": ("CSS_SELECTOR", "td:nth-child(1)"), "class": Element},
        "status": {"locator": ("CSS_SELECTOR", "td:nth-child(2)"), "class": Element},
        "comment": {"locator": ("CSS_SELECTOR", "td:nth-child(3)"), "class": Element},
    }


class OrderInfoPage(BasePage):

    url = "index.php?route=account/order/info&order_id="

    def __init__(self, order_id: int):
        super().__init__()
        self.url = f"{self.url}{order_id}"

    contains = {
        "order_details": {
            "locator": ("XPATH", '//*[@id="content"]/table[1]/tbody'),
            "class": Block,
        },
        "payment_address": {
            "locator": ("XPATH", '//*[@id="content"]/table[2]/tbody/tr/td[1]'),
            "class": Block,
        },
        "shipping_address": {
            "locator": ("XPATH", '//*[@id="content"]/table[2]/tbody/tr/td[2]'),
            "class": Block,
        },
        "orders": {
            "locator": ("XPATH", '//*[@id="content"]/div[1]/table/tbody'),
            "class": OrderTable,
        },
        "summary": {
            "locator": ("XPATH", '//*[@id="content"]/div[1]/table/tfoot'),
            "class": Summary,
        },
        "order_history": {
            "locator": ("XPATH", '//*[@id="content"]/table[3]/tbody'),
            "class": OrderHistory,
        },
        "continue_btn": {"locator": ("XPATH", '//*[@id="content"]/div[2]/div/a'), "class": Link},
    }

    def get_order_details(self) -> dict:

        raw = re.sub("\n", " ", self.order_details.text)
        reg_ex = re.compile(
            r"Order ID: (.*) Date Added: (.*) Payment Method: (.*) Shipping Method: (.*)"
        )
        match = [i for i in reg_ex.search(raw).groups()]

        return {
            "order_id": match[0],
            "date_added": match[1],
            "payment_method": match[2],
            "shipping_method": match[3],
        }

    def get_payment_address_details(self) -> list:
        return self.payment_address.text.split("\n")

    def get_shipping_address_details(self) -> list:
        return self.shipping_address.text.split("\n")
