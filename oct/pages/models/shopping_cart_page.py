from oct.pages.base.elements import Form, InputField, Clickable, Block
from oct.pages.base.page import BasePage
from oct.pages import Success


class InfoTableRow(Block):
    contains = {
        "name": {"locator": ("CSS_SELECTOR", "td:first-child > strong"), "class": Block},
        "value": {"locator": ("CSS_SELECTOR", "td:last-child"), "class": Block},
    }

    @property
    def name_text(self):
        return self.name.text.strip(":")

    @property
    def value_text(self):
        return float(self.value.text.strip("$").replace(",", ""))


class InfoTable(Block):
    contains = {"rows": {"locator": ("TAG_NAME", "tr"), "class": InfoTableRow, "is_loaded": True}}


class CertificateForm(Block):
    contains = {
        "gift_certificate": {"locator": ("NAME", "voucher"), "class": InputField},
        "apply_gift_certificate": {"locator": ("ID", "button-voucher"), "class": Clickable},
    }

    def fill_out(self, **kwargs: str) -> None:
        self.gift_certificate.fill(kwargs.get("gift_certificate"))

    def send(self) -> None:
        self.apply_gift_certificate.click()


class CouponForm(Block):
    contains = {
        "coupon": {"locator": ("NAME", "coupon"), "class": InputField},
        "apply_coupon": {"locator": ("ID", "button-coupon"), "class": Clickable},
    }

    def fill_out(self, **kwargs: str) -> None:
        self.coupon.fill(kwargs.get("coupon"))

    def send(self) -> None:
        self.apply_coupon.click()


class QuantityForm(Form):
    contains = {
        "quantity": {"locator": ("CSS_SELECTOR", "[type='text']"), "class": InputField},
        "button_remove": {
            "locator": ("CSS_SELECTOR", ".btn-danger[type='button']"),
            "class": Clickable,
        },
    }


class ShoppingCartPage(BasePage):
    url = "index.php?route=checkout/cart"
    contains = {
        "quantity_form": {
            "locator": ("XPATH", '//*[@id="content"]/form/div/table/tbody/tr/td[4]'),
            "class": QuantityForm,
        },
        "use_coupon_code_dropdown": {
            "locator": ("PARTIAL_LINK_TEXT", "Use Coupon Code"),
            "class": Clickable,
        },
        "coupon_form": {"locator": ("ID", "collapse-coupon"), "class": CouponForm},
        "use_gift_certificate_dropdown": {
            "locator": ("PARTIAL_LINK_TEXT", "Use Gift Certificate"),
            "class": Clickable,
        },
        "certificate_form": {"locator": ("ID", "collapse-voucher"), "class": CertificateForm},
        "info_table": {
            "locator": ("XPATH", '//*[@id="content"]/div[2]/div/table'),
            "class": InfoTable,
        },
        "checkout_button": {"locator": ("PARTIAL_LINK_TEXT", "Checkout"), "class": Clickable},
    }

    @property
    def sub_total(self) -> float:
        return self.info_table_results["Sub-Total"]

    def discount(self, gift_certificate) -> float:
        return self.info_table_results[f"Gift Certificate ({gift_certificate})"]

    @property
    def total(self) -> float:
        return self.info_table_results["Total"]

    def apply_gift_certificate(self, gift_certificate):
        self.use_gift_certificate_dropdown.click()
        self.certificate_form.is_displayed
        self.certificate_form.fill_out(gift_certificate=gift_certificate)
        self.certificate_form.send()
        Success.is_available
        self._setup()

    @property
    def info_table_results(self) -> dict:
        return {row.name_text: row.value_text for row in self.info_table.rows}
