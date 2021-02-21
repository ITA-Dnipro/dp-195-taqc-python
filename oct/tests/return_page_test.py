# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
import os

from pyats.aetest import Testcase, test, setup, cleanup, loop

from oct.drivers import get_driver
from oct.pages import ReturnPage
from settings import log_managed


class EmailValidationTest(Testcase):
    @setup
    def start(self, browser, grid) -> None:
        self.driver = get_driver(browser, grid)
        self.page = ReturnPage(self.driver)
        loop.mark(self.valid_data, testdata=self.parameters["valid_data"])
        loop.mark(self.invalid_data, testdata=self.parameters["invalid_data"])

    @test
    def valid_data(self, steps, protocol, host, testdata, message) -> None:
        log_managed["handler"].changeFile(
            os.path.join(os.path.dirname(__file__), "log/return_page_valid_data.log")
        )
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
                self.failed(reason="Email is invalid")

    @test
    def invalid_data(self, steps, protocol, host, testdata, message) -> None:
        log_managed["handler"].changeFile(
            os.path.join(os.path.dirname(__file__), "log/return_page_invalid_data.log")
        )
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
                self.failed(reason="Email is valid")

    @cleanup
    def close(self) -> None:
        self.page.close()
