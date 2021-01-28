"""Basic elements"""


from selenium.common.exceptions import NoSuchElementException

from .base import Element


class InputField(Element):
    """Any type of a writable input"""

    def fill(self, text):
        """Write something"""
        if text is not None:
            self._reff.clear()
            self._reff.send_keys(text)


class Clickable(Element):
    """Any type of a clickable element"""

    def click(self):
        """Click it"""
        self._reff.click()


class Selectable(Element):
    """Any type of a selectable element"""

    def is_selected(self):
        """Check if selected"""
        return self._reff.is_selected()


class RadioButton(Selectable, Clickable):
    """General radiobutton, which can be selected by clicking on it"""
    pass


class CheckBox(Selectable, Clickable):
    """General checkbox, which can be selected by clicking on it"""
    pass


class DropDown(Clickable):
    """This is basically a clickable container"""
    pass


class Block(Element):
    """Dumb container"""
    pass


class RadioButtonGroup(Element):
    """Provide selecting functionality for radiobuttons"""

    def select_option(self, name):
        """Select by option name"""

        if not self.contains or (name not in self.contains.keys() and name is not None):
            raise NoSuchElementException

        if name is not None:
            attr = getattr(self, name)
            if not attr.is_selected():
                attr.click()

    def select_any(self):
        """Select firs possible option"""

        if not self.contains:
            raise NoSuchElementException

        option = list(self.contains.keys())[0]
        attr = getattr(self, option)

        if not attr.is_selected():
            attr.click()


class Form(Element):
    """Generic form"""

    def submit(self):
        self._reff.submit()


class ProductThumb(Element):
    """Product thumb block"""

    contains = {
        'caption': {
            'locator': ("CLASS_NAME", "caption"),
            'class': Element
        },
        'link': {
            'locator': ("TAG_NAME", "a"),
            'class': Clickable
        },
        'cart': {
            'locator': ("CLASS_NAME", "fa-shopping-cart"),
            'class': Clickable
        },
        'wish': {
            'locator': ("CLASS_NAME", "fa-heart"),
            'class': Clickable
        },
        'compare': {
            'locator': ("CLASS_NAME", "fa-exchange"),
            'class': Clickable
        },
    }

    def click(self):
        self.link.click()
