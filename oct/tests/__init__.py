from pyats import aetest
from pyats.topology import loader

from oct.drivers import Browser, get_driver
from settings import email, customer_password


def test_run(data_file) -> None:
    testbed = loader.load("./../testbed.yaml")
    device = testbed.devices["opencart-testing-vm"]
    selenium_grid = testbed.custom["selenium-grid"]
    driver = get_driver(browser=Browser.CHROME, grid=selenium_grid)
    aetest.main(
        datafile=data_file,
        host=device.connections.main.ip,
        driver=driver,
        email=email,
        password=customer_password,
    )
