from config import *
import cv2
import asyncio



class Video():
    def __init__(self):
        self.video_path = VIDEO_PATH
        self.finished = False
        cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    async def play(self, filename):
        cap = cv2.VideoCapture(self.video_path + filename)

        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                cap.release()
                break

            cv2.imshow('Video', frame)

            if (cv2.waitKey(25) & 0xFF == ord('q')):
                cap.release()
                break
        
            await asyncio.sleep(1/240)


    async def spin(self, filename):
        await self.play(filename)
        self.finished=True


    async def idle(self):
        self.idle_task = asyncio.create_task(self.play('idle.mp4'))
        while True:
            if self.idle_task.done() or self.idle_task.cancelled():
                self.idle_task = asyncio.create_task(self.play('idle.mp4'))
            await asyncio.run(self.idle_task)