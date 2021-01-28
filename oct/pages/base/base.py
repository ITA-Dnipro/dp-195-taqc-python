from abc import ABC
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.drivers import driver


def timeout(timesec: int):
    def deco(func):
        def wrapper(self):
            countdown = time.time()
            while (time.time() - countdown) < timesec:
                result = func(self)
                if result is True:
                    return result
            return func(self)
        return wrapper
    return deco


WAIT = 5


class Base(ABC):
    """Blueprint for Page and Element classes"""

    def __init__(self, base):
        self._base = base

    contains = dict()
    """
    contains class attribute contains page's webelements. Webelements set
    is the page specific.
    Example:
    contains = {
        elementName: {
            "locator": (by, value),
            "class": Element
        },
        ...
    }

    For pages with dynamically generated content (Search Page, Category Page)
    specify loadable webelement (such ProductThumb) by adding "is_loaded"
    parameter to the element's dict as such:
    contains = {
        ...
        elementName: {
            "locator": (by, value),
            "class": ProductThumb,
            "is_loaded": True
        },
        ...
    }
    """

    def _setup(self):
        """Create obj atributes from self.contains"""

        if self.contains:
            for key, val in self.contains.items():

                if val.get('is_loaded') is True:
                    """Add laoded webelements to the object"""

                    setattr(self, 'elements_loaded', 0)
                    locator_name, locator_value = val.get('locator')
                    element_class = self._check_class(val.get('class'))
                    find_by = getattr(By, locator_name.upper())

                    elements = self._base.find_elements(find_by, locator_value)

                    for index, element in enumerate(elements):
                        attr = f"{element_class.__name__.lower()}_{index}"
                        setattr(self, attr, element_class(element))
                        self.elements_loaded += 1

                else:
                    """Add static webelements to the object"""

                    locator_name, locator_value = val.get('locator')
                    element_class = self._check_class(val.get('class'))
                    find_by = getattr(By, locator_name.upper())
                    setattr(self, key,
                            self._get_instance(
                                by=find_by, value=locator_value, elcls=element_class)
                            )

    def _check_class(self, elcls):
        """Check class of a contained object"""

        if issubclass(elcls, Element):
            return elcls

        raise TypeError(
            'Contained object has to be an instance of the Element class!')

    def _get_instance(self, by, value, elcls):
        """Create instance of Element class"""

        element = self._base.find_element(by, value)
        return elcls(element)


class Page(Base):
    """Generic Page class"""

    def __init__(self, base: WebDriver = driver):
        super().__init__(base)

    url = ''

    @property
    @timeout(WAIT)
    def is_available(self):
        """Check if this page is currently open in the browser"""

        return self.url in self._base.current_url

    def get_alerts(self):
        """Get all alert pop-ups from the page, used for testing"""

        warn_texts = [
            el.text for el in self._base.find_elements_by_class_name('text-danger')
        ]
        alerts = [
            el.text for el in self._base.find_elements_by_class_name('alert')
        ]
        return warn_texts + alerts

    def load(self, host):
        """Load page"""

        self._base.get(f'https://{host}/{self.url}')
        self._base.maximize_window()
        self._setup()

    def close(self):
        """Close Page"""

        self._base.close()


class Success(Base):
    """Success Page class, do not inherit"""

    def __init__(self, base: WebDriver = driver):
        super().__init__(base)

    url = 'success'

    @property
    @timeout(WAIT)
    def is_available(self):
        return self.url in self._base.current_url


class Element(Base):
    """Generic Element class"""

    def __init__(self, base: WebElement):
        super().__init__(base)
        self._setup()

    @property
    def text(self):
        return self._base.text
