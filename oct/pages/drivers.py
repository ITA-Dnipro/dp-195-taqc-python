import importlib
from enum import Enum

from selenium import webdriver
from selenium.webdriver import Remote
from webdriver_manager.manager import DriverManager
from webdriver_manager.utils import ChromeType


class Browser(Enum):
    CHROME = "chrome"
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    OPERA = "opera"
    EDGE = "edge"


def get_driver(browser: Enum = Browser.CHROME) -> Remote:

    manager: DriverManager = None
    output = None

    if browser.value == "chrome":
        manager = importlib.import_module(name="webdriver_manager.chrome")
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        output = webdriver.Chrome(manager.ChromeDriverManager().install(), options=options)

    elif browser.value == "chromium":
        manager = importlib.import_module(name="webdriver_manager.chrome")
        output = webdriver.Chrome(
            manager.ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        )

    elif browser.value == "firefox":
        manager = importlib.import_module(name="webdriver_manager.firefox")
        output = webdriver.Firefox(executable_path=manager.GeckoDriverManager().install())

    elif browser.value == "edge":
        manager = importlib.import_module(name="webdriver_manager.microsoft")
        output = webdriver.Edge(manager.EdgeChromiumDriverManager().install())

    elif browser.value == "opera":
        manager = importlib.import_module(name="webdriver_manager.opera")
        output = webdriver.Opera(executable_path=manager.OperaDriverManager().install())

    return output


driver = get_driver()
