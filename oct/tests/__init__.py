import logging
import os
from oct.device_connection import NewSession
from pyats import aetest
from pyats import log
from pyats.topology import loader, Testbed

from settings import email, customer_password, browser, protocol, log_level

TESTBED = "testbed.yaml"


def test_run(testbed_file: str = TESTBED) -> None:
    testbed = loader.load(testbed_file)

    aetest.main(
        **mandatory_test_arguments(testbed),
        email=email,
        password=customer_password,
        logger=create_log(),
    )


def mandatory_test_arguments(
    testbed: Testbed,
    test_browser: str = browser,
    app_protocol: str = protocol,
) -> dict:
    device = testbed.devices["opencart-testing-vm"]
    host = device.connections.main.ip
    selenium_grid = testbed.custom["selenium-grid"]
    session = NewSession(device)

    return {
        "session": session,
        "browser": test_browser,
        "grid": selenium_grid,
        "protocol": app_protocol,
        "host": host,
    }


def create_log():
    logger = logging.getLogger()
    logger.addHandler(log.managed_handlers.tasklog)
    logger.setLevel(log_level)
    log.managed_handlers.tasklog.setLevel(log_level)
    log.managed_handlers.tasklog.changeFile(
        os.path.join(os.path.dirname(__file__), f"log/start.log")
    )
    return log.managed_handlers.tasklog
