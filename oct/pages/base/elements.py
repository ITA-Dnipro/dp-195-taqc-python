"""Module contains basic webelements of the page object."""

from selenium.common.exceptions import NoSuchElementException

from .base import Element


class InputField(Element):
    """Any type of a writable input."""

    def fill(self, text: str) -> None:
        if text is not None:
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
        "caption": {"locator": ("CLASS_NAME", "caption"), "class": Element},
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
        """Click it"""
        self._base.find_element_by_xpath(f'//*[@id="input-zone"]/option[text()="{name}"]').click()
