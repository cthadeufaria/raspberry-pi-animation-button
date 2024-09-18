import gpiozero



class Led:
    def __init__(self):
        self.led = gpiozero.LED(25)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def blink(self, period):
        self.led.blink(on_time=period, off_time=period, background=True)