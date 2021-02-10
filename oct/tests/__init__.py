import json
from settings import host, email, customer_password
from pyats import aetest


def from_file(filename: str):
    """Load test data from json file."""
    with open(filename, "r") as data:
        return json.loads(data.read())


def test_run() -> None:
    aetest.main(host=host, email=email, password=customer_password)
