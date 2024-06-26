from config import PRIZES

import asyncio

from prize_wheel import PrizeWheel



async def main():
    state_machine = PrizeWheel(prizes=PRIZES)

    while True:
        try:
            await state_machine.send("cycle")
            asyncio.sleep(1/30)

        except Exception as e:
            print(e)



if __name__ == "__main__": 
    asyncio.run(main())