# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
from pyats.aetest import Testcase, test, setup, cleanup, loop
from oct.drivers import get_driver
from oct.pages import ReturnPage

from settings import logger, log_error_message, log_change_file_handler


class EmailValidationTest(Testcase):
    @setup
    def start(self, browser, grid) -> None:
        self.tasklog = log_change_file_handler("EmailValidationTest")
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
                log_error_message(
                    cls_refer=self,
                    test_name="EmailValidationTest",
                    failed_message="Email is invalid"
                )

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
                log_error_message(
                    cls_refer=self,
                    test_name="EmailValidationTest",
                    failed_message="Email is valid"
                )

    @cleanup
    def close(self) -> None:
        logger.removeHandler(self.tasklog)
        self.page.close()
