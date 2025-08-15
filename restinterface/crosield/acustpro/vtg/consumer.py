import asyncio
from random import random
from time import perf_counter
from functools import wraps


def worker(func):
    @wraps(func)
    async def wrapper(work_queue: asyncio.Queue, result_queue: asyncio.Queue):
        while True:
            task_data = await work_queue.get()

            task_id = task_data["task_id"]
            number = task_data["number"]

            start = perf_counter()
            await asyncio.sleep(random() * 2)


            result = func(number)


            end = perf_counter()

            await result_queue.put(
                {
                    "task_id": task_id,
                    "result": result,
                    "time_secs": end - start
                }
            )
            work_queue.task_done()
    return wrapper


def compute_square(number):
    return number * number

@worker
async def do_work(number):
    return compute_square(number)