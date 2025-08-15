import multiprocessing as mp
import asyncio
import concurrent.futures
import aiohttp

def create_proccesses(separate_loop_creator, coro):
    proccesses = []
    for n in range(2):
        proc = mp.Process(target=separate_loop_creator, args=(coro,))
        proc.start()
        proccesses.append(proc)
    for p in proccesses:
        p.join()

def separate_loop_creator(coro):
    sep_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(sep_loop)

    # tasks = [ asyncio.async(coro(sep_loop)) for _ in range(100) ]

    # coros = [ self.shebang(butt, intf, hostName[i], count = 1) for i in range(len(hostName)) ]
    # await asyncio.gather(*coros, return_exceptions = True)
    tasks = [ coro() for _ in range(100) ]
    try:
        sep_loop.run_until_complete(asyncio.wait(tasks))
        sep_loop.close()
    except Exception as err:
        print(err)
        for task in tasks:
            task.cancel()
        sep_loop.close()


# @asyncio.coroutine
def manager(exe, loop):
    # some calculations and start coros in several processes
    loop.run_in_executor(
        exe,
        create_proccesses,
        separate_loop_creator,
        some_coro
    )

# @asyncio.coroutine
def some_work_in_mainloop():
    while True:
        print('Some server dealing with connections here...')
        # yield from asyncio.sleep(1)
        # await asyncio.sleep(1)

# @asyncio.coroutine
async def some_coro(loop):
    with aiohttp.ClientSession(loop=loop) as session:
        # response = yield from session.get('https://www.baidu.com')
        # yield from asyncio.sleep(2)
        response = await session.get('https://www.baidu.com')
        await asyncio.sleep(2)
        print(response.status)

if __name__ == '__main__':
    mainloop = asyncio.get_event_loop()
    executor = concurrent.futures.ProcessPoolExecutor(5)
    # asyncio.async(some_work_in_mainloop())
    some_work_in_mainloop()
    # asyncio.async(manager(executor, mainloop))
    manager(executor, mainloop)
    try:
        mainloop.run_forever()
    finally:
        mainloop.close()