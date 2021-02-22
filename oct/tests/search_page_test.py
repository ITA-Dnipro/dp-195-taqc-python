# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
# pylint: disable=not-callable # pyATS-related exclusion
import logging

from pyats import log
from pyats.aetest import Testcase, test, setup, cleanup
from oct.drivers import get_driver
from oct.pages import SearchPage

from settings import log_level, logger


class SearchInTitlesTest(Testcase):
    @setup
    def start(self, browser, grid) -> None:
        log.managed_handlers["tasklog"] = logging.FileHandler(
            "oct/tests/log/SearchInTitles.log", mode="w", delay=True
        )
        log.managed_handlers.tasklog.setLevel(log_level)
        logger.addHandler(log.managed_handlers.tasklog)
        self.driver = get_driver(browser, grid)
        self.page = SearchPage(self.driver)

    @test
    def test_search(self, steps, protocol, host, keyword) -> None:

        with steps.start("open page"):
            self.page.load(protocol, host)

        with steps.start("enter search keyword"):
            self.page.search(keywords=keyword)

        with steps.start("check search result"):
            search_result = self.page.get_products()
            product_titles = (product["title"] for product in search_result)
            for title in product_titles:
                if keyword.lower() not in title.lower():
                    logger.error(
                        "You can find screenshot of this error here:" "oct/tests/screenshot/%s.png",
                        self.page.get_screenshot(),
                    )
                    self.failed("Product title does not match the search entry!")

    @cleanup
    def close(self) -> None:
        logger.removeHandler(log.managed_handlers.tasklog)
        self.page.close()


class SearchSortingTest(Testcase):
    @setup
    def start(self, browser, grid) -> None:
        log.managed_handlers["tasklog"] = logging.FileHandler(
            "oct/tests/log/SearchSorting.log", mode="w", delay=True
        )
        log.managed_handlers.tasklog.setLevel(log_level)
        logger.addHandler(log.managed_handlers.tasklog)
        self.driver = get_driver(browser, grid)
        self.page = SearchPage(self.driver)

    @test
    def search_all(self, protocol, host):
        self.page.load(protocol, host)
        self.page.search(keywords="  ")

    @test
    def alphabetic_ascending(self):
        self.page.sort_by("Name (A - Z)")
        sort_result = self.page.get_products()
        product_titles = [product["title"].lower() for product in sort_result]
        expected_order = sorted(product_titles)
        if product_titles != expected_order:
            logger.error(
                "You can find screenshot of this error here: oct/tests/screenshot/%s.png",
                self.page.get_screenshot(),
            )
            self.failed("Product title shoud be sorted in alphabetical order!")

    @test
    def alphabetic_descending(self):
        self.page.sort_by("Name (Z - A)")
        sort_result = self.page.get_products()
        product_titles = [product["title"].lower() for product in sort_result]
        expected_order = sorted(product_titles, reverse=True)
        if product_titles != expected_order:
            logger.error(
                "You can find screenshot of this error here: oct/tests/screenshot/%s.png",
                self.page.get_screenshot(),
            )
            self.failed("Product title shoud be sorted in reverse alphabetical order!")

    @test
    def price_ascending(self):
        self.page.sort_by("Price (Low > High)")
        sort_result = self.page.get_products()
        product_prices = [product["price"] for product in sort_result]
        expected_order = sorted(product_prices)
        if product_prices != expected_order:
            logger.error(
                "You can find screenshot of this error here: oct/tests/screenshot/%s.png",
                self.page.get_screenshot(),
            )
            self.failed("Product prices shoud be sorted in ascending order!")

    @test
    def price_descending(self):
        self.page.sort_by("Price (High > Low)")
        sort_result = self.page.get_products()
        product_prices = [product["price"] for product in sort_result]
        expected_order = sorted(product_prices, reverse=True)
        if product_prices != expected_order:
            logger.error(
                "You can find screenshot of this error here: oct/tests/screenshot/%s.png",
                self.page.get_screenshot(),
            )
            self.failed("Product prices shoud be sorted in descending order!")

    @cleanup
    def close(self) -> None:
        logger.removeHandler(log.managed_handlers.tasklog)
        self.page.close()