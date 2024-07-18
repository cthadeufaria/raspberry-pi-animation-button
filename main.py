import asyncio
import json

from prize_wheel import PrizeWheel
from config import PRIZES_FILE



async def main():
    with open(PRIZES_FILE, 'r') as f:
        prizes = json.load(f)

    sm = PrizeWheel(prizes=prizes)

    while True:
        try:
            await sm.send("cycle")

        except Exception as e:
            print(e)



if __name__ == "__main__": 
    asyncio.run(main())
