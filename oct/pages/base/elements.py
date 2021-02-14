"""Module contains basic webelements of the page object."""

from selenium.common.exceptions import NoSuchElementException

from oct.pages.base.base import Element


class InputField(Element):
    """Any type of a writable input."""

    def fill(self, text: str) -> None:
        if text not in ["", None]:
            self._base.clear()
            self._base.send_keys(text)


class Clickable(Element):
    """Any type of a clickable element."""

    def click(self) -> None:
        self._base.click()


class Selectable(Element):
    """Any type of a selectable element."""

    def is_selected(self) -> None:
        return self._base.is_selected()


class RadioButton(Selectable, Clickable):
    """General radiobutton, which can be selected by clicking on it."""


class CheckBox(Selectable, Clickable):
    """General checkbox, which can be selected by clicking on it."""


class Block(Element):
    """Dumb container."""


class RadioButtonGroup(Element):
    """Provide selecting functionality for radiobuttons."""

    def select_option(self, name: str) -> None:
        """Select by option name."""

        if name is None:
            return

        if not self.contains or name not in self.contains.keys():
            raise NoSuchElementException

        attr = getattr(self, name)
        if not attr.is_selected():
            attr.click()

    def select_any(self) -> None:
        """Select firs possible option."""

        if not self.contains:
            raise NoSuchElementException

        option = list(self.contains.keys())[0]
        attr = getattr(self, option)
        if not attr.is_selected():
            attr.click()


class Form(Element):
    """Generic form class."""

    def submit(self) -> None:
        self._base.submit()


class ProductThumb(Element):
    """Product thumb block."""

    contains = {
        "title": {
            "locator": ("CSS_SELECTOR", "div:nth-child(2) > div.caption > h4"),
            "class": Element,
        },
        "description": {
            "locator": ("CSS_SELECTOR", "div:nth-child(2) > div.caption > p:nth-child(2)"),
            "class": Element,
        },
        "price": {
            "locator": ("CSS_SELECTOR", "div:nth-child(2) > div.caption > p.price"),
            "class": Element,
        },
        "link": {"locator": ("TAG_NAME", "a"), "class": Clickable},
        "cart": {"locator": ("CLASS_NAME", "fa-shopping-cart"), "class": Clickable},
        "wish": {"locator": ("CLASS_NAME", "fa-heart"), "class": Clickable},
        "compare": {"locator": ("CLASS_NAME", "fa-exchange"), "class": Clickable},
    }

    def click(self) -> None:
        self.link.click()


class Link(Element):
    """Redirection link."""

    @property
    def href(self):
        link = self._base.get_attribute("href")
        if link is None:
            link = self._base.get_attribute("value")
        return link


class DropDown(Element):
    def select(self, name):
        """Click it."""
        if name:
            self._base.find_element_by_xpath(f'//option[text()="{name}"]').click()

    def get_value(self, name) -> str:
        option = self._base.find_element_by_xpath(f'//option[text()="{name}"]')
        return option.get_attribute("value")


class Paginator(Block):
    """Pagination bar."""

    contains = {"tabs": {"locator": ("TAG_NAME", "li"), "class": Link, "is_loaded": True}}

    @property
    def number_of_pages(self) -> int:
        pages = 1
        if len(self.tabs) != 0:
            digits = map(lambda x: int(x.text), filter(lambda y: y.text.isdigit(), self.tabs))
            pages = max(digits)

        return pages

    @property
    def current_page_num(self) -> int:
        active = None
        if self.number_of_pages != 1:
            page = list(
                filter(
                    lambda x: x._base.get_attribute("class") == "active",  # pylint: disable=W0212
                    self.tabs,
                )
            )
            active = int(page[0].text)

        else:
            active = 1
        return active

    @property
    def next_page_num(self) -> int:
        nexp = None
        if self.number_of_pages - self.current_page_num > 0:
            nexp = self.current_page_num + 1
        else:
            nexp = self.current_page_num
        return nexp

    @property
    def prev_page_num(self) -> int:
        prep = None
        if self.current_page_num != 1:
            prep = self.current_page_num - 1
        else:
            prep = self.current_page_num
        return prep
