import time

from pyats.topology import Device


class NewSession:
    """Class provides interfaces to interact with the device."""

    def __init__(self, device: Device):
        self._device = device

    def connect(self) -> None:
        self._device.connect()

    def disconnect(self) -> None:
        self._device.disconnect()

    def start_services(self) -> None:
        self._device.execute("docker-compose -f docker-compose-webapp.yaml start")
        self._device.execute("docker-compose -f docker-compose-selenium.yaml start")
        # time.sleep(5)

    def stop_services(self) -> None:
        self._device.execute("docker-compose -f docker-compose-webapp.yaml stop")
        self._device.execute("docker-compose -f docker-compose-selenium.yaml stop")
