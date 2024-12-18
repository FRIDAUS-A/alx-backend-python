#!/usr/bin/env python3
"""
    Create a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Args:
            n: number of time to spawn
            max_delay: max amount of delay
        Returns:
            returns the average time per courotine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    return (stop - start) / n
