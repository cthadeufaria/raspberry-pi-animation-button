from config import *
import cv2
import asyncio



class Video:
    def __init__(self):
        self.video_path = VIDEO_PATH
        self.finished = False
        cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    async def play(self, filename):
        while not self.finished:
            self.cap = cv2.VideoCapture(self.video_path + filename)

            if not self.cap.isOpened():
                print("Error: Could not open video.")
                exit()

            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    self.cap.release()
                    if filename != 'idle.mp4':
                        self.finished = True
                    break

                cv2.imshow('Video', frame)

                if (cv2.waitKey(25) & 0xFF == ord('q')):
                    self.cap.release()
                    if filename != 'idle.mp4':
                        self.finished = True
                    break
            
                await asyncio.sleep(1/30)


    async def spin(self, filename):
        await self.play(filename)
        await asyncio.sleep(1)


    async def idle_video(self):
        self.finished = False
        while True:
            await self.play('idle.mp4')
            await asyncio.sleep(1)