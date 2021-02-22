# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
import logging

from pyats import log
from pyats.aetest import Testcase, test, setup, cleanup, loop
from oct.drivers import get_driver
from oct.pages import ReturnPage

from settings import log_level, logger


class EmailValidationTest(Testcase):
    @setup
    def start(self, browser, grid) -> None:
        log.managed_handlers["tasklog"] = logging.FileHandler(
            "oct/tests/log/EmailValidationTest.log", mode="w", delay=True
        )
        log.managed_handlers.tasklog.setLevel(log_level)
        logger.addHandler(log.managed_handlers.tasklog)
        self.driver = get_driver(browser, grid)
        self.page = ReturnPage(self.driver)
        loop.mark(self.valid_data, testdata=self.parameters["valid_data"])
        loop.mark(self.invalid_data, testdata=self.parameters["invalid_data"])

    @test
    def valid_data(self, steps, protocol, host, testdata, message) -> None:

        with steps.start("open page"):
            self.page.load(protocol, host)

        with steps.start("fill data"):
            self.page.form.fill_out(email=testdata)

        with steps.start("submit"):
            self.page.form.submit()

        with steps.start("check result"):
            if message not in self.page.get_alerts():
                self.passed()
            else:
                logger.error(
                    "You can find screenshot of this error here: oct/tests/screenshot/%s.png",
                    self.page.get_screenshot(),
                )
                self.failed(reason="Email is invalid")

    @test
    def invalid_data(self, steps, protocol, host, testdata, message) -> None:

        with steps.start("open page"):
            self.page.load(protocol, host)

        with steps.start("fill data"):
            self.page.form.fill_out(email=testdata)

        with steps.start("submit"):
            self.page.form.submit()

        with steps.start("check result"):
            if message in self.page.get_alerts():
                self.passed()
            else:
                logger.error(
                    "You can find screenshot of this error here: oct/tests/screenshot/%s.png",
                    self.page.get_screenshot(),
                )
                self.failed(reason="Email is valid")

    @cleanup
    def close(self) -> None:
        logger.removeHandler(log.managed_handlers.tasklog)
        self.page.close()
