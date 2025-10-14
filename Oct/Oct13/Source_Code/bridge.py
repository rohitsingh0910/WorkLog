from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_volume(self, volume):
        pass


class TV(Device):
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")

    def set_volume(self, volume):
        print(f"TV volume set to {volume}")


class Radio(Device):
    def turn_on(self):
        print("Radio is now ON")

    def turn_off(self):
        print("Radio is now OFF")

    def set_volume(self, volume):
        print(f"Radio volume set to {volume}")


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_volume(self, volume):
        self.device.set_volume(volume)


tv = TV()
remote = RemoteControl(tv)
remote.turn_on()
remote.set_volume(10)

radio = Radio()
radio_remote = RemoteControl(radio)
radio_remote.turn_on()
radio_remote.set_volume(5)
