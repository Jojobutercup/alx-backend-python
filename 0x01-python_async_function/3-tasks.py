#!/usr/bin/env python3
"""
Module: 3-tasks
------------------------

This module contains two asynchronous coroutines:
wait_random and task_wait_random

"""

from typing import Optional
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds (included)
    and eventually returns it.

    Args:
    - max_delay (int): maximum delay in seconds (default 10)

    Returns:
    - float: random delay between 0 and max_delay seconds (included)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A regular function that creates an asyncio.Task for
    the wait_random coroutine with the specified max_delay.

    Args:
        max_delay (int): the maximum delay time in seconds to pass to
        wait_random

    Returns:
        asyncio.Task: a task object that will run the
        wait_random coroutine with the specified max_delay
    """
    return asyncio.create_task(wait_random(max_delay))
