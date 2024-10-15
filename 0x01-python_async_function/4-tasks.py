#!/usr/bin/env python3
"""
    Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random
    is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Args:
            n: number of times to spawn
            max_delay: max delay
        Return:
            returns a list of float
    """
    result_list = await asyncio.gather(*(
                        map(lambda _: task_wait_random(max_delay), range(n))))
    return sorted(result_list)
