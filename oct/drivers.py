import importlib
from enum import Enum

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.utils import ChromeType


class Browser(Enum):
    CHROME_REMOTE = "chrome_remote"
    CHROME = "chrome"
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    OPERA = "opera"
    EDGE = "edge"


def get_driver(browser: str, grid: str) -> WebDriver:

    output = None

    # run tests on remoute server
    if browser.value == "chrome_remote":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--remote-debugging-port=9222")
        options.headless = True
        output = webdriver.Remote(
            command_executor=grid, desired_capabilities=DesiredCapabilities.CHROME, options=options
        )

    # run tests locally
    elif browser.value == "chrome":
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
