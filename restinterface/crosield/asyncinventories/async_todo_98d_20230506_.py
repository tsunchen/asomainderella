import time
import asyncio
import random
from pprint import pprint

async def do_work(s: str, delay_s: float = 1.0):
    print(f"{s} started")
    await asyncio.sleep(delay_s)
    print(f"{s} done, cost {delay_s}")


async def main():
    start = time.perf_counter()

    todo = ['get package', 'laundry', 'bake cake']

    coros = [ do_work(item, random.randint(1, 5)) for item in todo ]

    results = await asyncio.gather(*coros, return_exceptions = True)

    for r in results:
        pprint(r)

    end = time.perf_counter()
    print(f"it took: {end - start:.2f}s")


if __name__=='__main__':
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
