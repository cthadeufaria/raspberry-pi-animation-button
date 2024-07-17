import asyncio

from prize_wheel import PrizeWheel
from config import PRIZES



async def main():
    sm = PrizeWheel(prizes=PRIZES)

    while True:
        try:
            await sm.send("cycle")

        except Exception as e:
            print(e)



if __name__ == "__main__": 
    asyncio.run(main())
