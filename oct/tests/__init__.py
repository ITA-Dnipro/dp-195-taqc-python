import os

from pyats import aetest
from pyats.topology import loader, Testbed

from oct.device_connection import NewSession
from settings import email, customer_password, browser, protocol


testbed_file = "testbed.yaml"
datafile = os.path.join(os.path.dirname(__file__), 'datafile', 'common_data.yaml')


def test_run(testbed_file: str = testbed_file, datafile: str = datafile) -> None:

    testbed = loader.load(testbed_file)

    aetest.main(**mandatory_test_arguments(testbed, datafile),
                email=email, password=customer_password)


def mandatory_test_arguments(
        testbed: Testbed,
        datafile: str,
        browser: str = browser,
        protocol: str = protocol,
) -> dict:

    device = testbed.devices["opencart-testing-vm"]
    host = device.connections.main.ip
    selenium_grid = testbed.custom["selenium-grid"]
    session = NewSession(device)

    return {
        "session": session,
        "browser": browser,
        "grid": selenium_grid,
        "protocol": protocol,
        "host": host,
        "datafile": datafile
    }
