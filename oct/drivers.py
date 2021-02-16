import importlib

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.utils import ChromeType


def get_driver(browser: str, grid: str) -> WebDriver:

    output = None

    # run tests on remoute server
    if browser == "chrome_remote":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--remote-debugging-port=9222")
        options.headless = True
        output = webdriver.Remote(
            command_executor=grid, desired_capabilities=DesiredCapabilities.CHROME, options=options
        )

    # run tests locally
    elif browser == "chrome":
        manager = importlib.import_module(name="webdriver_manager.chrome")
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        output = webdriver.Chrome(manager.ChromeDriverManager().install(), options=options)

    elif browser == "chromium":
        manager = importlib.import_module(name="webdriver_manager.chrome")
        output = webdriver.Chrome(
            manager.ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        )

    elif browser == "firefox":
        manager = importlib.import_module(name="webdriver_manager.firefox")
        output = webdriver.Firefox(executable_path=manager.GeckoDriverManager().install())

    elif browser == "edge":
        manager = importlib.import_module(name="webdriver_manager.microsoft")
        output = webdriver.Edge(manager.EdgeChromiumDriverManager().install())

    elif browser == "opera":
        manager = importlib.import_module(name="webdriver_manager.opera")
        output = webdriver.Opera(executable_path=manager.OperaDriverManager().install())

    return output
