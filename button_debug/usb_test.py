import evdev
from evdev import InputDevice, categorize, ecodes

class Button:

    def __init__(self):
        # List all input devices
        self.devices = [InputDevice(path) for path in evdev.list_devices()]
        for device in self.devices:
            print(device)

        # Replace '/dev/input/eventX' with your device path
        self.button = InputDevice('/dev/input/eventX')

        print(f"Listening to {self.button}")

    def listen(self):
        for event in self.button.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                print(categorize(event))
                if event.value == 1:  # Key pressed
                    print("Button pressed!")
                elif event.value == 0:  # Key released
                    print("Button released!")
