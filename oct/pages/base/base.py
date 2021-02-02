"""Module contains base classes for page objects and webelements."""

import time
from abc import ABC
from typing import Any, Union, Type, List, Optional

import requests
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.drivers import driver


def timeout(timesec: int):
    """Page loading timeout decorator."""

    def deco(func):
        def wrapper(self) -> bool:
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
    """Blueprint for Page and Element classes."""

    def __init__(self, base: Any) -> None:
        self._base = base

    contains: Optional[dict] = None
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

    def _setup(self) -> None:
        """Create obj atributes from self.contains."""

        if self.contains:
            for key, val in self.contains.items():

                if val.get("is_loaded") is True:
                    # Add loaded webelements to the object

                    locator_name, locator_value = val.get("locator")
                    elcls = self.check_class(val.get("class"))
                    find_by = getattr(By, locator_name.upper())

                    elements = self._base.find_elements(find_by, locator_value)
                    attr = key
                    setattr(self, attr, [elcls(element) for element in elements])
                    setattr(self, f"{attr}_loaded", len(elements))

                else:
                    # Add static webelements to the object

                    locator_name, locator_value = val.get("locator")
                    elcls = self.check_class(val.get("class"))
                    find_by = getattr(By, locator_name.upper())
                    setattr(self, key, self.get_instance(find_by, locator_value, elcls))

    @staticmethod
    def check_class(elcls: Type["Element"]) -> Union[Type["Element"], None]:
        """Check class of a contained object."""

        if issubclass(elcls, Element):
            return elcls

        raise TypeError("Contained object has to be an instance of the Element class!")

    def get_instance(self, find_by: str, value: str, elcls: Type["Element"]) -> WebElement:
        """Create instance of Element class."""

        element = self._base.find_element(find_by, value)
        return elcls(element)


class Page(Base):
    """Basic page class."""

    def __init__(self, base: WebDriver = driver):
        super().__init__(base)

    url = ""

    @property
    @timeout(WAIT)
    def is_available(self) -> bool:
        """Check if this page is currently open in the browser."""

        return self.url in self._base.current_url

    def get_alerts(self) -> List[str]:
        """Get all alert pop-ups from the page, used for testing."""

        warn_texts = [el.text for el in self._base.find_elements_by_class_name("text-danger")]
        alerts = [el.text for el in self._base.find_elements_by_class_name("alert")]
        return warn_texts + alerts

    def load(self, host: str) -> None:
        """Load page."""

        self._base.get(f"https://{host}/{self.url}")
        self._base.maximize_window()
        self._setup()

    def add_logged_in_cookie_session(self, host: str, email: str, password: str) -> None:
        """Add logged in cookie session"""

        data = {"email": email, "password": password}
        url = f"https://{host}/index.php?route=account/login"
        request = requests.Request(method="POST", url=url, data=data)
        session = requests.Session()
        session.send(request.prepare(), verify=False)
        self._base.add_cookie({"name": "OCSESSID", "value": session.cookies["OCSESSID"]})

    def close(self) -> None:
        """Close Page."""

        self._base.close()


class Success(Base):
    """Success page class, do not inherit."""

    def __init__(self, base: WebDriver = driver):
        super().__init__(base)

    url = "success"

    @property
    @timeout(WAIT)
    def is_available(self) -> bool:
        return self.url in self._base.current_url


class Element(Base):
    """Basic weblement class."""

    def __init__(self, base: WebElement):
        super().__init__(base)
        self._setup()

    @property
    def text(self) -> str:
        return self._base.text

    @property
    @timeout(WAIT)
    def is_displayed(self) -> bool:
        return self._base.is_displayed()
