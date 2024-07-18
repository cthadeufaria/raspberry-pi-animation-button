from statemachine import StateMachine, State
import random
import asyncio

from video import Video
from button import Button



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
        self.idle_task = None

    
    async def button_pressed(self):
        return self.button.is_pressed
    

    async def video_finished(self):
        return self.video.finished
    

    async def on_enter_playing(self):
        self.idle_task.cancel()
        await self.video.play(random.choice(self.prizes))


    async def on_enter_idle(self):
        if self.idle_task is not None:
            self.idle_task.cancel()
        self.idle_task = asyncio.create_task(self.video.play('idle.mp4'))
        await asyncio.run(self.idle_task)