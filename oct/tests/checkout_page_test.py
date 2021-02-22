from pyats.aetest import Testcase, test, setup, cleanup

from oct.drivers import get_driver
from oct.pages import ProductPage, CheckoutPage


class GuestCheckoutTest(Testcase):
    @setup
    def start(self, browser, grid) -> None:
        self.driver = get_driver(browser, grid)
        product_page = ProductPage(self.driver)
        product_page.load("http", "34.107.116.227")
        product_page.cart.add()
        self.page = CheckoutPage(self.driver)

    @test
    def valid_guest_checkout(self, steps, valid_data) -> None:
        with steps.start("first step", description="Select guest checkout options"):
            self.page.load("http", "34.107.116.227")
            self.page.checkout_options.guest_checkout.click()
            self.page.checkout_options.continue_button.click()
        with steps.start("second step", description="Fill Billing Details Form"):
            if self.page.billing_details.is_displayed:
                self.page.billing_details.fill_out(
                    country=valid_data.get("country", ""),
                    first_name=valid_data["first_name"],
                    last_name=valid_data["last_name"],
                    email=valid_data["email"],
                    telephone=valid_data["telephone"],
                    address_1=valid_data["address_1"],
                    city=valid_data["city"],
                    post_code=valid_data["post_code"],
                    region_state=valid_data.get("region_state", ""),
                )
            page.billing_form.continue_button.click()