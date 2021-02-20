from pyats.aetest import Testcase, test, setup, cleanup, loop

from pages.models.login_page import LoginPage
from oct.pages.base.base import Accessory
from . import test_run


class LoginInalid(Testcase):

    @setup
    def open(self, host: str):
        self.page = LoginPage()
        self.page.load(host)
        loop.mark(self.valid_data, testdata=self.parameters["valid_data"])
        self.AP = Accessory(url='account')

    @test
    def test_submit(self):
        self.page.button.click()
        # self.page.form.fill_out(
        #     email='person1@gmail.com',
        #     password='qwe132'
        # )
        # self.page.form.submit()
        #
        # assert self.AP.is_available
        # assert "Warning: No match for E-Mail Address and/or Password." in self.page.get_alerts()

    @cleanup
    def close(self):
        self.page.close()


if __name__ == "__main__":
    test_run()
