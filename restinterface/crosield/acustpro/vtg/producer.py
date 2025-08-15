import asyncio
from typing import List

async def produce_work(
    batch: List[dict], work_queue: asyncio.Queue, producer_completed: asyncio.Event
):
    for data in batch:
        await work_queue.put(data)

    producer_completed.set()
