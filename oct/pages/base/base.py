from abc import ABC

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from drivers import driver


class Base(ABC):
    """Blueprint for Page and Element classes"""

    def __init__(self, refference):
        self._reff = refference

    contains = dict()
    """
    contains = {
        elementName: {
            "locator": (by, value),
            "class": Element
        },
    }
    """

    def _setup(self):
        """Create obj atributes from self.contains"""

        if self.contains:
            for key, val in self.contains.items():
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

        element = self._reff.find_element(by, value)
        return elcls(element)


class Page(Base):
    """Generic Page class"""

    def __init__(self, refference: WebDriver = driver):
        super().__init__(refference)

    url = ''

    @property
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

        self._driver.close()


class Success(Base):
    """Success Page class, do not inherit"""

    def __init__(self, refference: WebDriver = driver):
        super().__init__(refference)

    url = 'success'

    @property
    def is_available(self):
        return self.url in self._reff.current_url


class Element(Base):
    """Generic Element class"""

    def __init__(self, refference: WebElement):
        super().__init__(refference)
        self._setup()
