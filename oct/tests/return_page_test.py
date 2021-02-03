# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
# pylint:disable=duplicate-code

from pyats.aetest import Testcase, test, setup, cleanup

from oct.pages import ReturnPage, Success
from oct.tests import test_run


class LoggedInValid(Testcase):
    @setup
    def open(self, host: str) -> None:
        self.page = ReturnPage()
        self.page.load(host)

    @test
    def test_submit(self) -> None:
        self.page.form.fill_out(
            first_name="John",
            last_name="Doe",
            email="kek@gmail.com",
            telephone="2212211",
            order_id="5",
            product_name="iphone",
            product_code="i5",
            reason="wrong",
            is_opened="yes",
            details="asdsdsadasdsddwwscscew",
        )
        self.page.form.submit()
        assert Success().is_available

    @cleanup
    def close(self) -> None:
        self.page.close()


if __name__ == "__main__":
    test_run()
