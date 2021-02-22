# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
from pyats.aetest import Testcase, test, setup, cleanup, loop

from oct.drivers import get_driver
from oct.pages import AddAddressPage


class AddAddressTest(Testcase):
    @setup
    def open(self, browser, grid, protocol, host, email, password) -> None:
        self.driver = get_driver(browser, grid)
        self.page = AddAddressPage(self.driver)
        self.page.add_logged_in_cookie_session(protocol, host, email, password)
        loop.mark(self.valid_data, testdata=self.parameters["valid_data"])
        loop.mark(self.invalid_data, testdata=self.parameters["invalid_data"])

    @test
    def valid_data(self, steps, testdata, protocol, host) -> None:
        with steps.start("open page"):
            self.page.load(protocol, host)
        with steps.start("first step", description="Fill AddAddress Form"):
            self.page.form.fill_out(
                first_name=testdata["first_name"],
                last_name=testdata["last_name"],
                company=testdata["company"],
                address_1=testdata["address_1"],
                address_2=testdata["address_2"],
                city=testdata["city"],
                post_code=testdata["post_code"],
                country=testdata["country"],
                region_state=testdata["region_state"],
                default_address=testdata["default_address"],
            )
        with steps.start("second step", description="Click Submit button Form"):
            self.page.form.submit()
        with steps.start("third step", description="Success alert appears"):
            if testdata["excpected_valid_data"] in self.page.get_alerts():
                self.passed()
            else:
                self.failed()

    @test
    def invalid_data(self, steps, testdata, protocol, host) -> None:
        with steps.start("open page"):
            self.page.load(protocol, host)
        with steps.start("first step", description="Fill AddAddress Form"):
            self.page.form.fill_out(
                first_name=testdata["first_name"],
                last_name=testdata["last_name"],
                company=testdata["company"],
                address_1=testdata["address_1"],
                address_2=testdata["address_2"],
                city=testdata["city"],
                post_code=testdata["post_code"],
                country=testdata.get("country", ""),
                region_state=testdata.get("region_state", ""),
                default_address=testdata["default_address"],
            )
        with steps.start("second step", description="Click Submit button Form"):
            self.page.form.submit()
        with steps.start("third step", description="Success alert appears"):
            if testdata["excpected_valid_data"] not in self.page.get_alerts():
                self.passed()
            else:
                self.failed()

    @cleanup
    def close(self) -> None:
        self.page.close()
