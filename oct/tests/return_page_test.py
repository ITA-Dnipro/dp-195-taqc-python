from pyats.aetest import TestCase, test, setup, cleanup, main

from pages import ReturnPage


class LoggedInValid(TestCase):

    @setup
    def login(self):
        pass

    @setup
    def make_order(self, **kwargs):
        pass

    @test
    def test_submit(self, **kwargs):
        pass

    @cleanup
    def close(self):
        pass


if __name__ == "__main__":
    main()
