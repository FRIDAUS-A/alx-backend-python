#!/usr/bin/env python3
"""
    The coroutine will loop 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10.
    Use the random module.
"""
from typing import List, Generator
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
        Args:
        Returns: returns a list of random numbers
    """
    return [i async for i in async_generator()]
