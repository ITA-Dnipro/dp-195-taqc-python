# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
from pyats.aetest import Testcase, test, setup, cleanup

from oct.pages import ReturnPage
from oct.tests import test_run, from_file


class EmailValidationTest(Testcase):

    parameters = {"warning_message": "E-Mail Address does not appear to be valid!"}

    @setup
    def create(self, host: str) -> None:
        self.page = ReturnPage()
        self.host = host

    @test.loop(testdata=from_file("testdata/valid_email.json"))
    def test_valid_data(self, testdata) -> None:
        self.page.load(self.host)
        self.page.form.fill_out(email=testdata)
        self.page.form.submit()
        assert self.parameters["warning_message"] not in self.page.get_alerts()

    @test.loop(testdata=from_file("testdata/invalid_email.json"))
    def test_invalid_data(self, testdata) -> None:
        self.page.load(self.host)
        self.page.form.fill_out(email=testdata)
        self.page.form.submit()
        assert self.parameters["warning_message"] in self.page.get_alerts()

    @cleanup
    def close(self) -> None:
        self.page.close()


if __name__ == "__main__":
    test_run()
