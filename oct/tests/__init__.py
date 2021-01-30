from pyats import aetest


def test_run(host: str = "127.0.0.1") -> None:
    aetest.main(host=host)
