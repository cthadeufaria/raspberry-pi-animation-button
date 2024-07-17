from statemachine import StateMachine, State
import random
import asyncio
import sys

from video import Video
from button import Button



class PrizeWheel(StateMachine):
    idle = State('Idle', initial=True)
    playing = State('Playing')

    cycle = (
        idle.to(playing, cond="button_pressed")
        | playing.to(idle, cond="video_finished")
    )


    def __init__(self, prizes):
        super().__init__()
        self.prizes = prizes
        self.button = Button(debug=True)
        self.video = Video()

    
    async def button_pressed(self):
        return self.button.is_pressed
    

    async def video_finished(self):
        return self.video.finished
    

    async def on_enter_playing(self):
        self.video.idle_task.cancel()
        await self.video.spin(random.choice(self.prizes))


    async def on_enter_idle(self):
        await self.video.idle()