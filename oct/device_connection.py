import time

from pyats.topology import Device


class ServiceError(BaseException):
    pass


class NewSession:
    """Class provides interfaces to interact with the device."""

    def __init__(self, device: Device):
        self._device = device

    def connect(self) -> None:
        self._device.connect()

    def disconnect(self) -> None:
        self._device.disconnect()

    def start_services(self) -> None:
        # self._device.execute('selenium start')
        # time.sleep(15)
        # self._device.execute('\n')
        pass

    def stop_services(self) -> None:
        self._device.execute('selenium stop')
