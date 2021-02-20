import importlib
# from urllib3.exceptions import MaxRetryError

import polling2
import requests
from requests.exceptions import ConnectionError
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
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

        # poll server connection
        try:
            url = grid.replace('/wd/hub', '')
            polling2.poll(
                lambda: requests.get(url).status_code == 200,
                ignore_exceptions=(ConnectionError,),
                step=1,
                timeout=10
            )
        except polling2.TimeoutException:
            raise ConnectionError("Could not connect to Selenium server")

        # poll driver initialization
        try:
            output = polling2.poll(
                lambda: webdriver.Remote(
                    command_executor=grid,
                    desired_capabilities=DesiredCapabilities.CHROME,
                    options=options
                ),
                ignore_exceptions=(WebDriverException,),
                step=1,
                timeout=10
            )
        except polling2.TimeoutException:
            raise WebDriverException("Could not start new Driver session")
        # output = webdriver.Remote(
        #     command_executor=grid, desired_capabilities=DesiredCapabilities.CHROME, options=options
        # )

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
