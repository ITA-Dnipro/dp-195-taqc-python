from pyats import aetest
from pyats.topology import loader

from settings import email, customer_password


def test_run(data_file) -> None:
    testbed = loader.load("testbed.yaml")
    device = testbed.devices["opencart-testing-vm"]
    device.connect()
    aetest.main(
        datafile=data_file, host=device.connections.main.ip, email=email, password=customer_password
    )
