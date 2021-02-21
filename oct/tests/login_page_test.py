from pyats.aetest import Testcase, test, setup, cleanup, loop

from oct.drivers import get_driver
from oct.pages import LoginPage, Accessory


class LoginPageTest(Testcase):
    @setup
    def start(self, browser, grid) -> None:
        self.driver = get_driver(browser, grid)
        self.page = LoginPage(self.driver)
        self.account = Accessory(self.driver, url="account")
        loop.mark(self.valid_data, testdata=self.parameters["valid_data"])
        loop.mark(self.invalid_data, testdata=self.parameters["invalid_data"])

    @test
    def invalid_data(self, steps, protocol, host, testdata, message) -> None:

        with steps.start("open page"):
            self.page.load(protocol, host)

        with steps.start("fill data"):
            self.page.form.fill_out(email=testdata["email"],
                                    password=testdata["password"])

        with steps.start("submit"):
            self.page.form.submit()

        with steps.start("check result"):
            if message in self.page.get_alerts():
                self.passed()
            else:
                self.failed(reason="Email and password are valid")

    @test
    def valid_data(self, steps, protocol, host, testdata) -> None:

        with steps.start("open page"):
            self.page.load(protocol, host)

        with steps.start("fill data"):
            self.page.form.fill_out(email=testdata["email"],
                                    password=testdata["password"])

        with steps.start("submit"):
            self.page.form.submit()

        with steps.start("check result"):
            if self.account.is_available:
                self.passed()
            else:
                self.failed(reason="Email or password is invalid")


    @cleanup
    def close(self) -> None:
        self.page.close()
