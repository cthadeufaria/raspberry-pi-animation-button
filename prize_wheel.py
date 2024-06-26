from statemachine import StateMachine, State
import random

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
        self.video = Video()
        self.button = Button()

    
    def button_pressed(self):
        return self.button.is_pressed
    

    def video_finished(self):
        return self.video.finished
    

    async def on_enter_playing(self):
        await self.video.spin(random.choice(self.prizes))
    

    async def on_enter_idle(self):
        await self.video.idle_video()