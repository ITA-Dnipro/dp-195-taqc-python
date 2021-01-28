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
                if func(self) is True:
                    return func(self)
            return func(self)
        return wrapper
    return deco


WAIT = 5


class Base(ABC):
    """Blueprint for Page and Element classes"""

    def __init__(self, refference):
        self._reff = refference

    contains = dict()
    """
    contains class attribute contains page's static webelements. Webelements set
    is the page specific.
    Example:
    contains = {
        elementName: {
            "locator": (by, value),
            "class": Element
        },
    }
    """
    loads = dict()
    """
    load class attribute contains page's dynamically generated webelements (if any).
    Use for pages where dynamically generated content is the subject of testing.
    Example:
    loads = {
        "group locator": (),
        "class": Element
    }
    """

    def _setup(self):
        """Create obj atributes from self.contains and self.loads"""

        if self.contains:
            for key, val in self.contains.items():
                locator_name, locator_value = val.get('locator')
                element_class = self._check_class(val.get('class'))
                find_by = getattr(By, locator_name.upper())

                setattr(self, key,
                        self._get_instance(
                            by=find_by, value=locator_value, elcls=element_class)
                        )

        if self.loads:
            setattr(self, 'elements_loaded', 0)

            locator_name, locator_value = self.loads.get('group locator')
            element_class = self._check_class(self.loads.get('class'))
            find_by = getattr(By, locator_name.upper())

            elements = self._reff.find_elements(find_by, locator_value)
            for index, element in enumerate(elements):
                attr = ("%s_%d" % (element_class.__name__.lower(), index))

                setattr(self, attr, element_class(element))
                self.elements_loaded += 1

    def _check_class(self, elcls):
        """Check class of a contained object"""

        if issubclass(elcls, Element):
            return elcls

        raise TypeError(
            'Contained object has to be an instance of the Element class!')

    def _get_instance(self, by, value, elcls):
        """Create instance of Element class"""

        element = self._reff.find_element(by, value)
        return elcls(element)


class Page(Base):
    """Generic Page class"""

    def __init__(self, refference: WebDriver = driver):
        super().__init__(refference)

    url = ''

    @property
    @timeout(WAIT)
    def is_available(self):
        """Check if this page is currently open in the browser"""

        return self.url in self._reff.current_url

    def get_alerts(self):
        """Get all alert pop-ups from the page, used for testing"""

        warn_texts = [
            el.text for el in self._reff.find_elements_by_class_name('text-danger')
        ]
        alerts = [
            el.text for el in self._reff.find_elements_by_class_name('alert')
        ]
        return warn_texts + alerts

    def load(self, host):
        """Load page"""

        self._reff.get(f'https://{host}/{self.url}')
        self._reff.maximize_window()
        self._setup()

    def close(self):
        """Close Page"""

        self._reff.close()


class Success(Base):
    """Success Page class, do not inherit"""

    def __init__(self, refference: WebDriver = driver):
        super().__init__(refference)

    url = 'success'

    @property
    @timeout(WAIT)
    def is_available(self):
        return self.url in self._reff.current_url


class Element(Base):
    """Generic Element class"""

    def __init__(self, refference: WebElement):
        super().__init__(refference)
        self._setup()

    @property
    def text(self):
        return self._reff.text
