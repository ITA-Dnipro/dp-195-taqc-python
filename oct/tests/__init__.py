import json
from pyats import aetest


def from_file(filename: str):
    """Load test data from json file."""
    with open(filename, "r") as data:
        return json.loads(data.read())


def test_run(host: str = "127.0.0.1") -> None:
    aetest.main(host=host)
