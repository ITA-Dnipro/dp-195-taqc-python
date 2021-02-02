import os

from pyats import aetest


def test_run(
    host: str = "127.0.0.1",
    email=os.environ.get("CUSTOMER_EMAIL"),
    password=os.environ.get("CUSTOMER_PASSWORD"),
) -> None:
    aetest.main(host=host, email=email, password=password)
