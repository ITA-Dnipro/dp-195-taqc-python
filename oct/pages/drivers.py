from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from enum import Enum


class Browser(Enum):
    CHROME = 'chrome'
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'
    OPERA = 'opera'
    EDGE = 'edge'


def get_driver(browser=Browser.CHROME):

    if browser == 'chrome':
        return webdriver.Chrome(ChromeDriverManager().install())
    if browser == 'chromium':
        return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    if browser == 'firefox':
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if browser == 'opera':
        return webdriver.Edge(EdgeChromiumDriverManager().install())
    if browser == 'edge':
        return webdriver.Opera(executable_path=OperaDriverManager().install())


driver = get_driver(Browser.CHROME)
