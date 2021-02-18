# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=attribute-defined-outside-init # pyATS-related exclusion
# from pyats.aetest import Testcase, test, setup, cleanup, loop

# from oct.pages import SearchPage


# class SearchPageTest(Testcase):

#     @setup
#     def start(self, driver) -> None:
#         self.page = SearchPage(driver)
#         loop.mark(self.test_search, request=self.parameters["search_request"])

#     @test
#     def test_search(self, steps, protocol, host, request):

#         with steps.start("open page"):
#             self.page.load(protocol, host)

#         with steps.start("searching"):
#             page.search(keywords=request)
