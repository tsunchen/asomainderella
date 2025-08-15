import asyncio
from time import perf_counter
from typing import Callable, List

import vtg.consumer as consumer
import vtg.producer as producer
import vtg.resulthandler as resulthandler

NUM_WORKERS = 5
WORK_QUEUE_MAX_SIZE = 20

NUM_RESULT_HANDLERS = 5
RESULT_QUEUE_MAX_SIZE = 20

async def _controller(
    batch: List[dict], task_completed_callback: Callable, job_completed_callback: Callable
) -> None:
    start = perf_counter()
    work_queue = asyncio.Queue(maxsize = WORK_QUEUE_MAX_SIZE)
    result_queue = asyncio.Queue(maxsize = RESULT_QUEUE_MAX_SIZE)

    tasks = []
    producer_completed = asyncio.Event()
    producer_completed.clear()
    tasks.append(
        asyncio.create_task(producer.produce_work(batch, work_queue, producer_completed))
    )

    for _ in range(NUM_WORKERS):
        tasks.append(
            asyncio.create_task(consumer.do_work(work_queue, result_queue))
    )

    for _ in range(NUM_RESULT_HANDLERS):
        tasks.append(
            asyncio.create_task(resulthandler.handle_task_result(result_queue, task_completed_callback))
    )

    await producer_completed.wait()
    await work_queue.join()
    await result_queue.join()

    for task in tasks:
        task.cancel()

    end = perf_counter()
    job_completed_callback({"elapsed_secs": end - start })


def run_job(batch: List[dict], task_completed_callback: Callable, job_completed_callback: Callable
) -> None:
    asyncio.run(_controller(batch ,task_completed_callback, job_completed_callback))
