# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
import logging

from oct.drivers import get_driver
from oct.pages import ProductPage, ShoppingCartPage
from pyats import log
from pyats.aetest import Testcase, test, setup, cleanup

from settings import log_level, logger


class GiftCertificateBonusTest(Testcase):
    @setup
    def precondition(self, browser, grid, protocol, host, email, password) -> None:
        log.managed_handlers["tasklog"] = logging.FileHandler("oct/tests/log/GiftCertificateBonus.log", mode="w", delay=True)
        log.managed_handlers.tasklog.setLevel(log_level)
        logger.addHandler(log.managed_handlers.tasklog)
        self.driver = get_driver(browser, grid)
        self.page = ProductPage(self.driver)
        self.page.load(protocol, host)
        self.page.add_logged_in_cookie_session(protocol, host, email, password)
        self.page.cart.add()
        self.page = ShoppingCartPage(self.driver)

    @test
    def test_submit(self, steps, protocol, host, gift_certificate) -> None:

        with steps.start("open page"):
            self.page.load(protocol, host)

        with steps.start("apply certificate"):
            self.page.apply_gift_certificate(gift_certificate)

        with steps.start("check result"):
            actual_result = self.page.sub_total + self.page.discount(gift_certificate)
            expected_result = self.page.total
            if actual_result == expected_result:
                self.passed()
            else:
                self.failed(reason="Incorrect result")

    @cleanup
    def close(self) -> None:
        logger.removeHandler(log.managed_handlers.tasklog)
        self.page.close()
