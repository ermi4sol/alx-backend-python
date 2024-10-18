#!/usr/bin/env python3
"""Module for concurrent tasks using asyncio"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    This function creates n tasks using task_wait_random, runs them
    concurrently, and returns a list of the delay times in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for each task_wait_random call.

    Returns:
        List[float]: List of all the delays, sorted in ascending order.
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = await asyncio.gather(*tasks)
    return sorted(delays)