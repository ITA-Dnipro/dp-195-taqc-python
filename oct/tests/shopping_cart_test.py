# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion

from pyats.aetest import Testcase, test, setup, cleanup

from oct.pages import ProductPage, ShoppingCartPage
from oct.tests import test_run


class ShoppingCartTest(Testcase):
    @setup
    def open(self, host, driver, email, password) -> None:
        self.page = ProductPage(driver)
        self.page.load(host)
        self.page.add_logged_in_cookie_session(host, email, password)
        self.page.cart.add()

    @test
    def test_submit(self, host, driver, gift_certificate: str = "100dollars") -> None:
        self.page = ShoppingCartPage(driver)
        self.page.load(host)
        self.page.apply_gift_certificate(gift_certificate)
        actual_result = self.page.sub_total + self.page.discount(gift_certificate)
        expected_result = self.page.total
        assert actual_result == expected_result

    @cleanup
    def close(self) -> None:
        self.page.close()


if __name__ == "__main__":
    test_run(data_file=None)
