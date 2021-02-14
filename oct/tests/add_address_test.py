# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
from oct.pages import AddAddressPage
from pyats.aetest import Testcase, test, setup, cleanup, loop
from oct.tests import test_run


class AddAddressTest(Testcase):
    @setup
    def open(self, host: str, email: str, password: str) -> None:
        self.page = AddAddressPage()
        self.page.add_logged_in_cookie_session(host, email, password)
        self.page.load(host)
        loop.mark(self.valid_data, testdata=self.parameters["valid_data"])
        loop.mark(self.invalid_data, testdata=self.parameters["invalid_data"])

    @test
    def valid_data(self, steps, testdata, host) -> None:
        print(testdata)
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
            assert testdata["excpected_valid_data"] in self.page.get_alerts()
        with steps.start("forth step", description="Click button Create new address"):
            self.page.load(host)

    @test
    def invalid_data(self, steps, testdata, host) -> None:
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
            assert testdata["excpected_valid_data"] not in self.page.get_alerts()
        with steps.start("forth step", description="Click button Create new address"):
            self.page.load(host)

    @cleanup
    def close(self) -> None:
        self.page.close()


if __name__ == "__main__":
    test_run("datafile/add_address_data.yaml")
