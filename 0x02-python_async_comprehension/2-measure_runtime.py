#!/usr/bin/env python3
"""
    measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        Args:
        Returns: returns total time
    """
    start = time.time()
    await asyncio.gather(*(map(lambda _: async_comprehension(), range(4))))
    stop = time.time()
    return stop - start
