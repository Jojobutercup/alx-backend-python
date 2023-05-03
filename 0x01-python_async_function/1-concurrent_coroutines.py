#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a
    random delay between 0 and max_delay seconds (included)
    and eventually returns it.

    Args:
    - max_delay (int): maximum delay in seconds (default 10)

    Returns:
    - float: random delay between 0 and max_delay seconds (included)
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns
    n instances of the wait_random coroutine with the specified max_delay
    and returns a list of all the resulting delays in ascending order.

    Args:
    - n (int): number of times to spawn wait_random
    - max_delay (int): maximum delay
    in seconds to pass to each instance of wait_random

    Returns:
    - List[float]: list of delays in ascending order
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)
