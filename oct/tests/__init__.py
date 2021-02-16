from pyats import aetest
from pyats.topology import loader

from oct.drivers import get_driver
from settings import email, customer_password, browser, protocol


def test_run(data_file) -> None:
    testbed = loader.load("./../testbed.yaml")
    device = testbed.devices["opencart-testing-vm"]
    selenium_grid = testbed.custom["selenium-grid"]
    driver = get_driver(browser=browser, grid=selenium_grid)
    aetest.main(
        driver=driver,
        protocol=protocol,
        host=device.connections.main.ip,
        datafile=data_file,
        email=email,
        password=customer_password,
    )
