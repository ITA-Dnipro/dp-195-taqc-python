import re

from oct.pages.base.page import BasePage
from oct.pages.base.elements import (
    InputField,
    DropDown,
    CheckBox,
    ProductThumb,
    Paginator,
    Block,
    Element,
)


def reload_page(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.load(self._host)
        return

    return wrapper


class SearchBlock(Block):

    contains = {
        "search_field": {"locator": ("ID", "input-search"), "class": InputField},
        "categories": {"locator": ("NAME", "category_id"), "class": DropDown},
        "search_in_subcat": {"locator": ("NAME", "sub_category"), "class": CheckBox},
        "search_in_descrp": {"locator": ("NAME", "description"), "class": CheckBox},
    }

    def search(
        self,
        keywords: str,
        category: str = "All Categories",
        subcat: bool = False,
        descr: bool = False,
    ) -> str:

        query = ""

        if keywords:
            self.search_field.fill(keywords)
            q_kw = keywords.replace(" ", "%20")
            query += f"&search={q_kw}"

        if subcat is True and not self.search_in_subcat.is_selected():
            query += "&sub_category=true"
            self.search_in_subcat.click()
        elif subcat is False and self.search_in_subcat.is_selected():
            self.search_in_subcat.click()

        if descr is True and not self.search_in_descrp.is_selected():
            query += "&description=true"
            self.search_in_descrp.click()
        elif descr is False and self.search_in_descrp.is_selected():
            self.search_in_descrp.click()

        if category != "All Categories":
            q_opt = self.categories.get_value(category)
            query += f"&category_id={q_opt}"

        return query


class SortingBlock(Block):

    contains = {
        "sort_by_drop": {"locator": ("ID", "input-sort"), "class": DropDown},
        "show_drop": {"locator": ("ID", "input-limit"), "class": DropDown},
    }

    def sort_by(self, name: str = "Default"):

        query = ""

        if name != "Default":
            raw_value = self.sort_by_drop.get_value(name).split("&")
            sort_query = list(filter(lambda x: "sort=" in x, raw_value))[0]
            query = sort_query

        return query

    def show(self, param: str = "15"):

        query = ""

        if param != "15":
            raw_value = self.show_drop.get_value(param).split("&")
            show_query = list(filter(lambda x: "limit=" in x, raw_value))[0]
            query = show_query

        return query


class SearchPage(BasePage):

    url = "index.php?route=product/search"

    contains = {
        "search_block": {"locator": ("ID", "content"), "class": SearchBlock},
        "sort_block": {"locator": ("ID", "content"), "class": SortingBlock},
        "products": {
            "locator": ("CLASS_NAME", "product-thumb"),
            "class": ProductThumb,
            "is_loaded": True,
        },
        "paginator": {"locator": ("CLASS_NAME", "pagination"), "class": Paginator},
        "pages": {"locator": ("XPATH", '//*[@id="content"]/div[4]/div[2]'), "class": Element},
    }

    def load(self, host: str):
        super().load(host)
        self._host = host

    def _sub_query_parameter(self, query: str):
        param, val = query.split("=")
        param_present = False
        url_parts = self.url.split("&")
        for index, part in enumerate(url_parts):
            if param in part:
                param_present = True
                url_parts[index] = f"{param}={val}"

        if param_present is True:
            self.url = "&".join(url_parts)
        else:
            self.url += f"&{param}={val}"

    @reload_page
    def search(
        self,
        keywords: str,
        category: str = "All Categories",
        subcat: bool = False,
        descr: bool = False,
    ):
        query = self.search_block.search(keywords, category, subcat, descr)
        self.url = SearchPage.url + query

    @reload_page
    def sort_by(self, name: str = "Default"):
        query = self.sort_block.sort_by(name)
        self._sub_query_parameter(query)

    @reload_page
    def show(self, param: str = "15"):
        query = self.sort_block.show(param)
        self._sub_query_parameter(query)

    @reload_page
    def next_page(self):
        if self.paginator is not None:
            nexp = f"page={self.paginator.next_page}"
            self._sub_query_parameter(nexp)

    @reload_page
    def prev_page(self):
        if self.paginator is not None:
            prev = f"page={self.paginator.prev_page}"
            self._sub_query_parameter(prev)

    @reload_page
    def go_to_page(self, page: int):
        if page >= 1 and page <= self.check_pagination["pages"]:
            goto = f"page={page}"
            self._sub_query_parameter(goto)

    def get_products(self) -> list:
        result = []
        for product in self.products:
            result.append(
                {
                    "title": product.title.text,
                    "description": product.description.text,
                    "price": product.price.text,
                }
            )
        return result

    def get_pagination(self) -> dict:
        reg_ex = re.compile(r"Showing (.*) to (.*) of (.*) \((.*) Pages\)")
        match = list(map(int, reg_ex.search(self.pages.text).groups()))
        return {
            "products_on_page": match[1] - match[0] + 1,
            "overall_products": match[2],
            "pages": match[3],
        }


if __name__ == "__main__":

    from oct.pages.drivers import DRIVER

    host = "127.0.0.1"

    page = SearchPage(DRIVER)
    page.load(host)
