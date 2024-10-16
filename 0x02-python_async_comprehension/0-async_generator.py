#!/usr/bin/env python3
"""
    The coroutine will loop 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10.
    Use the random module.
"""
from typing import List
import asyncio
import random


async def async_generator() -> List[float]:
    n = 10
    while (n > 0):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
        n -= 1
