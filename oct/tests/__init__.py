from pyats import aetest


def test_run(host: str = '127.0.0.1'):
    aetest.main(host=host)
