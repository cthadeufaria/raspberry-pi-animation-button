import gpiozero
from time import sleep



class Button:
    def __init__(self, pin=23):
        self.is_pressed = False
        self.button = gpiozero.Button(pin, bounce_time=0.05)
        self.button.when_pressed = self.press
        self.button.when_released = self.release

    def press(self):
        self.is_pressed = True
        print("Button pressed")

    def release(self):
        self.is_pressed = False
        print("Button released")


if __name__ == "__main__":
    button = Button()
    while True:
        sleep(1)