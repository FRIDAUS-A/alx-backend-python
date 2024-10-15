#!/usr/bin/env python3
"""
    Import wait_random from the previous python file that you’ve written and
    write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Args:
            n: spawn n times with spcified delay
            max_delay: delay
    """
    result_list = []
    while (n > 0):
        result_list.append(await wait_random(max_delay))
        n -= 1

    return sorted(result_list)
