#!/usr/bin/env python3
"""Module to measure the runtime of async_comprehension executed in parallel."""
import asyncio
import time
from typing import Coroutine
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel and measure the total runtime.
    Returns:
        The total runtime in seconds.
    """
    start = time.perf_counter()  # Start the timer

    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end = time.perf_counter()  # End the timer
    return end - start
