# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
from pyats import aetest

from oct.tests import test_run
from oct.tests import return_page_test, shopping_cart_test, login_page_test, search_page_test


class ScriptCommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def start(self, session):
        session.connect()
        session.start_services()


class EmailValidationTest(return_page_test.EmailValidationTest):
    """..."""


class GiftCertificateBonusTest(shopping_cart_test.GiftCertificateBonusTest):
    """..."""


class SearchInTitlesTest(search_page_test.SearchInTitlesTest):
    """..."""


class SearchSortingTest(search_page_test.SearchSortingTest):
    """..."""


class LoginTest(login_page_test.LoginPageTest):
    """..."""


class ScriptCommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def stop(self, session):
        session.stop_services()
        session.disconnect()


if __name__ == "__main__":
    # run aetest from CLI:
    #    python -m oct.tests.test_script -datafile="./oct/tests/datafile/common_data.yaml"
    # you can run separate testcase(s) by specifying uid parameter:
    #    python -m oct.tests.test_script -datafile="./oct/tests/datafile/common_data.yaml"
    #    -uids="Or('tc_name')"
    test_run()
