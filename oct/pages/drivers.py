import importlib
from selenium import webdriver

from enum import Enum


class Browser(Enum):
    CHROME = 'chrome'
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'
    OPERA = 'opera'
    EDGE = 'edge'


def get_driver(browser=Browser.CHROME):

    if browser.value == 'chrome':
        manager = importlib.import_module(
            name='webdriver_manager.chrome')
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        return webdriver.Chrome(manager.ChromeDriverManager().install(), options=options)

    if browser.value == 'chromium':
        manager = importlib.import_module(
            name='webdriver_manager.chrome')
        option = importlib.import_module(
            name='webdriver_manager.utils')
        return webdriver.Chrome(
            manager.ChromeDriverManager(
                chrome_type=option.ChromeType.CHROMIUM).install()
        )

    if browser.value == 'firefox':
        manager = importlib.import_module(
            name='webdriver_manager.firefox')
        return webdriver.Firefox(executable_path=manager.GeckoDriverManager().install())

    if browser.value == 'edge':
        manager = importlib.import_module(
            name='webdriver_manager.microsoft')
        return webdriver.Edge(manager.EdgeChromiumDriverManager().install())

    if browser.value == 'opera':
        manager = importlib.import_module(
            name='webdriver_manager.opera')
        return webdriver.Opera(executable_path=manager.OperaDriverManager().install())


driver = get_driver(Browser.CHROME)
