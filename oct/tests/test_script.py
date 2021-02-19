# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
from pyats import aetest

from oct.tests import test_run
from oct.tests import return_page_test, shopping_cart_test


class ScriptCommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def start(self, session):
        session.connect()
        session.start_services()


class EmailValidationTest(return_page_test.EmailValidationTest):
    """..."""


class ShoppingCartTest(shopping_cart_test.ShoppingCartTest):
    """..."""


class ScriptCommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def stop(self, session):
        session.stop_services()
        session.disconnect()


if __name__ == "__main__":
    test_run()
