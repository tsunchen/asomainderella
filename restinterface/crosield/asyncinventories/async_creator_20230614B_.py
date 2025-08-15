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
    tasks = [ coro(sep_loop) for _ in range(2) ]
    try:
        sep_loop.run_until_complete(asyncio.wait(tasks))
        sep_loop.close()
    except Exception as err:
        print(err)
        for task in tasks:
            task.cancel()
        sep_loop.close()


def manager(exe, loop):
    # some calculations and start coros in several processes
    loop.run_in_executor(
        exe,
        create_proccesses,
        separate_loop_creator,
        some_coro
    )


async def some_work_in_mainloop():
    while True:
        print('Some server dealing with connections here...')
        await asyncio.sleep(1)


async def some_coro(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        response = await session.get('https://www.baidu.com')
        await asyncio.sleep(2)
        print(response.status)


if __name__=='__main__':
    # asyncio.run(main())
    ## asyncio.set_event_loop(asyncio.new_event_loop())
    ## asyncio.get_event_loop().run_until_complete(main())
    mainloop = asyncio.get_event_loop()
    executor = concurrent.futures.ProcessPoolExecutor(5)
    manager(executor, mainloop)
    try:
        mainloop.run_forever()
    finally:
        mainloop.close()