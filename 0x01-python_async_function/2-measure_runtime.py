#!/usr/bin/env python3
"""
Module: 2-measure_runtime
------------------------

This module contains three asynchronous coroutines:
wait_random, wait_n and measure_time.

"""

import asyncio
import time
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds (inclusive)
    and returns it.

    Args:
        max_delay (int): the maximum delay time in seconds (default 10)

    Returns:
        float: a random delay time between 0 and max_delay seconds (inclusive)
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns n instances of
    the wait_random coroutine with the specified max_delay
    and returns a list of all the resulting delays in ascending order.

    Args:
        n (int): the number of times to spawn wait_random
        max_delay (int): the maximum delay time in seconds
        to pass to each instance of wait_random

    Returns:
        List[float]: a list of delays in ascending order
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): the number of times to spawn wait_random
        max_delay (int): the maximum delay time in seconds
        to pass to each instance of wait_random

    Returns:
        float: the average time taken for each execution of wait_random
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
