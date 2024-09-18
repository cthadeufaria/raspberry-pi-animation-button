from statemachine import StateMachine, State
import random
import asyncio
import json

from video import Video
from button import Button
from led import Led
from config import NO_PRIZE_PROB, PRIZES_FILE



class PrizeWheel(StateMachine):
    idle = State('Idle', initial=True)
    playing = State('Playing')

    cycle = (
        idle.to(playing, cond="button_pressed")
        | playing.to(idle, cond="video_finished")
        | idle.to(idle, cond="video_finished")
    )


    def __init__(self, prizes):
        super().__init__()
        self.prizes = prizes
        self.button = Button(debug=False)
        self.video = Video()
        self.led = Led()
        self.idle_task = None

    
    async def button_pressed(self):
        return self.button.is_pressed
    

    async def video_finished(self):
        return self.video.finished
    

    async def on_enter_playing(self):
        self.led.off()
        self.led.blink(0.2)
        self.idle_task.cancel()
        weights = [v for k, v in self.prizes.items() if k != "NO_PRIZE.mp4"]
        self.prizes["NO_PRIZE.mp4"] = max(1, int(sum(weights) * NO_PRIZE_PROB / (1 - NO_PRIZE_PROB)))
        keys = list(self.prizes.keys())
        weights = list(self.prizes.values())
        prize = random.choices(keys, weights=weights, k=1)[0]
        self.prizes[prize] -= 1
        with open(PRIZES_FILE, 'w') as f:
            json.dump(self.prizes, f, indent=4)
        await self.video.play(prize)


    async def on_enter_idle(self):
        self.led.off()
        self.led.blink(1)
        if self.idle_task is not None:
            self.idle_task.cancel()
        self.idle_task = asyncio.create_task(self.video.play('idle.mp4'))
        await asyncio.run(self.idle_task)